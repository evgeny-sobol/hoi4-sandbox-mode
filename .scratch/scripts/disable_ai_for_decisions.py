#!/usr/bin/env python3
"""
Generate .include delta files that inject a sandbox-mode modifier into every
`ai_will_do` block found in the `common/decisions` .txt files.

For each input .txt that contains at least one `ai_will_do` section, an
identically named .include is written to the output directory. Each .include
navigates to every `ai_will_do` block (via its `<category> -> <decision>` path)
and creates:

    +modifier:
      factor(0)
      add(1)
      is_sandbox_mode_on()

which the HSL compiler turns into:

    modifier = {
        factor = 0
        add = 1
        is_sandbox_mode_on = yes
    }

Decision files are structured as top-level category blocks, each holding
decision entries, each of which may hold an `ai_will_do` block:

    <category> = {
        <decision> = {
            ...
            ai_will_do = { ... }
        }
    }

Note there is no outer wrapper block (unlike common/ideas, which nests
everything under `ideas = { }`); categories sit at file top level.

Files without any ai_will_do section are skipped (no .include produced).

Usage:
    python gen_decisions_includes.py <in_dir> <out_dir>

Defaults, if omitted:
    in_dir  = "Hearts of Iron IV/common/decisions"
    out_dir = "out"
"""

import os
import sys


# ---------------------------------------------------------------------------
# Brace-aware scanning primitives (same approach as includes.py in the project)
# ---------------------------------------------------------------------------

_WORD_CHARS = set(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
)


def _is_word_char(text, i):
    return 0 <= i < len(text) and text[i] in _WORD_CHARS


def _skip_string(text, i):
    # i points at the opening quote; return index just past the closing quote.
    # Clausewitz strings do NOT use backslash escaping — a backslash is a literal
    # path separator (e.g. "gfx\interface\x.dds"), so a string ending in \" still
    # closes at that quote. Treating \" as an escaped quote here would swallow the
    # closing quote, run the "string" to end-of-file, and unbalance every brace
    # after it.
    i += 1
    n = len(text)
    while i < n:
        if text[i] == '"':
            return i + 1
        i += 1
    return i


def _skip_comment(text, i):
    n = len(text)
    while i < n and text[i] != '\n':
        i += 1
    return i


def _match_closing_brace(text, open_pos):
    """open_pos is just AFTER a '{'. Return index of the matching '}'."""
    depth = 1
    i = open_pos
    n = len(text)
    while i < n:
        c = text[i]
        if c == '#':
            i = _skip_comment(text, i)
        elif c == '"':
            i = _skip_string(text, i)
        elif c == '{':
            depth += 1
            i += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i
            i += 1
        else:
            i += 1
    line = text.count('\n', 0, open_pos) + 1
    raise ValueError(
        f"Unbalanced braces: no matching '}}' for '{{' opened near line {line}")


def _iter_named_blocks(text, start, end):
    """Yield (name, open_pos, close_pos) for every direct-child block
    `name = { ... }` at brace depth 0 within text[start:end]."""
    i = start
    depth = 0
    while i < end:
        c = text[i]
        if c == '#':
            i = _skip_comment(text, i)
            continue
        if c == '"':
            i = _skip_string(text, i)
            continue
        if c == '{':
            depth += 1
            i += 1
            continue
        if c == '}':
            depth -= 1
            i += 1
            continue

        if depth == 0 and (c in _WORD_CHARS) and not _is_word_char(text, i - 1):
            j = i
            while j < end and text[j] in _WORD_CHARS:
                j += 1
            k = j
            while k < end and text[k] in ' \t\r\n':
                k += 1
            if k < end and text[k] == '=':
                k += 1
                while k < end and text[k] in ' \t\r\n':
                    k += 1
                if k < end and text[k] == '{':
                    open_pos = k + 1
                    close_pos = _match_closing_brace(text, open_pos)
                    yield (text[i:j], open_pos, close_pos)
                    i = close_pos + 1
                    continue
            i = j
            continue
        i += 1


def _has_direct_child(text, start, end, name):
    for cname, _, _ in _iter_named_blocks(text, start, end):
        if cname == name:
            return True
    return False


def _brace_balance_ok(text):
    """Return the net brace balance ignoring comments and strings.

    > 0  => that many '{' never closed (missing closers at EOF)
    == 0 => balanced
    < 0  => an extra '}' appeared (structural defect, not EOF-fixable)

    Also returns whether any point in the scan went to negative depth, which
    signals a stray/misplaced '}' rather than a simple unterminated tail.
    """
    i = 0
    n = len(text)
    depth = 0
    went_negative = False
    while i < n:
        c = text[i]
        if c == '#':
            i = _skip_comment(text, i)
            continue
        if c == '"':
            i = _skip_string(text, i)
            continue
        if c == '{':
            depth += 1
            i += 1
            continue
        if c == '}':
            depth -= 1
            if depth < 0:
                went_negative = True
            i += 1
            continue
        i += 1
    return depth, went_negative


def repair_eof_braces(text):
    """Auto-fix the single safe case: a file missing exactly its trailing
    top-level closing brace(s), which HoI4's engine tolerates by auto-closing
    at EOF.

    Returns (repaired_text, n_added). Only acts when:
      * the net balance is positive (unclosed '{' remain), AND
      * depth never went negative anywhere (no stray/misplaced '}').

    Both conditions together mean the structure is well-formed right up to EOF
    and only the outermost block(s) lack their closing brace — exactly the
    persia/SOV/switzerland pattern. Any other imbalance (extra '}', a '}' at
    the wrong place) fails the negative-depth check and is left untouched so it
    still surfaces as a real error.
    """
    balance, went_negative = _brace_balance_ok(text)
    if balance <= 0 or went_negative:
        return text, 0
    # Append exactly `balance` closing braces, each on its own line.
    suffix = '\n' + '\n'.join('}' for _ in range(balance)) + '\n'
    return text + suffix, balance


def diagnose_brace_balance(text):
    """Best-effort locator for a source-level brace defect.

    HoI4's engine tolerates a missing closing brace at end of file (it auto-
    closes), so some vanilla/mod idea files ship with one extra '{' in real
    code. A strict matcher can't recover from that. This returns a short
    human-readable hint about the first line where nesting diverges from
    indentation, or None if nothing obvious is found.

    Heuristic only: it assumes the file is tab-indented one level per brace
    (true for vanilla ideas). It reports the first `name = {` opener or bare
    `}` whose resulting depth doesn't match its indentation.
    """
    lines = text.splitlines()

    # End-of-line brace depth for each line (code-only).
    i = 0
    n = len(text)
    depth = 0
    cur = 1
    eol_depth = {}
    while i < n:
        c = text[i]
        if c == '\n':
            eol_depth[cur] = depth
            cur += 1
            i += 1
            continue
        if c == '#':
            i = _skip_comment(text, i)
            continue
        if c == '"':
            i = _skip_string(text, i)
            continue
        if c == '{':
            depth += 1
            i += 1
            continue
        if c == '}':
            depth -= 1
            i += 1
            continue
        i += 1
    eol_depth[cur] = depth

    def tabs(s):
        return len(s) - len(s.lstrip('\t'))

    for ln in range(1, len(lines) + 1):
        s = lines[ln - 1]
        st = s.strip()
        if not st or st.startswith('#'):
            continue
        d = eol_depth.get(ln, 0)
        tb = tabs(s)
        if st.endswith('= {') or st.endswith('={'):
            if d != tb + 1:
                return (f"structure diverges near line {ln}: '{st[:50]}' "
                        f"nests at depth {d}, expected {tb + 1} "
                        f"(likely a stray '{{' or missing '}}' above)")
        elif st == '}':
            if d != tb:
                return (f"structure diverges near line {ln}: closing '}}' "
                        f"leaves depth {d}, expected {tb} "
                        f"(likely a stray '{{' or missing '}}' above)")
    return None


# ---------------------------------------------------------------------------
# Path discovery: ideas -> <category> -> <idea> that owns an ai_will_do block
# ---------------------------------------------------------------------------

def find_ai_will_do_paths(text):
    """
    For every decision entry with a direct `ai_will_do` block, return a tuple:

        (cat_name, cat_index, dec_name, dec_index)

    where `cat_index` is the 0-based position of the category among *all*
    top-level blocks sharing its name (or None if that name is unique at top
    level), and `dec_index` is the analogous position of the decision among all
    same-named blocks inside its category (or None if unique there).

    The indices exist because block names are not guaranteed unique: some files
    have two top-level blocks with the same name (e.g. a debug category and the
    real one). A bare-name include selector always resolves to the *first* such
    block, so when a name repeats we must address the intended block by
    position instead. The engine's [N] selector counts among same-named
    siblings, which is exactly what these indices measure.

    Structure assumed (vanilla common/decisions):
        <category> = {
            <decision> = {
                ...
                ai_will_do = { ... }
            }
        }

    Categories sit at file top level; there is no outer wrapper block.
    """
    # Count top-level blocks per name so we know which names are ambiguous.
    top_blocks = list(_iter_named_blocks(text, 0, len(text)))
    top_name_counts = {}
    for name, _, _ in top_blocks:
        top_name_counts[name] = top_name_counts.get(name, 0) + 1

    paths = []
    top_seen = {}  # running index per top-level name
    for cat_name, cat_o, cat_c in top_blocks:
        cat_pos = top_seen.get(cat_name, 0)
        top_seen[cat_name] = cat_pos + 1
        cat_index = cat_pos if top_name_counts[cat_name] > 1 else None

        # Decisions inside this category, with per-name index for ambiguity.
        dec_blocks = list(_iter_named_blocks(text, cat_o, cat_c))
        dec_name_counts = {}
        for name, _, _ in dec_blocks:
            dec_name_counts[name] = dec_name_counts.get(name, 0) + 1

        dec_seen = {}
        for dec_name, dec_o, dec_c in dec_blocks:
            dec_pos = dec_seen.get(dec_name, 0)
            dec_seen[dec_name] = dec_pos + 1
            if not _has_direct_child(text, dec_o, dec_c, "ai_will_do"):
                continue
            dec_index = dec_pos if dec_name_counts[dec_name] > 1 else None
            paths.append((cat_name, cat_index, dec_name, dec_index))

    return paths


# ---------------------------------------------------------------------------
# Include emission
# ---------------------------------------------------------------------------

INDENT = "  "  # two spaces per level, matching the project's HSL rendering

# The modifier body injected into each ai_will_do block.
_MODIFIER_LINES = [
    "+modifier:",
    "  factor(0)",
    "  add(1)",
    "  is_sandbox_mode_on()",
]


def _header(name, index):
    """Header token for one path segment: bare `name` when unambiguous, or
    `name[index]` when the name repeats among its siblings."""
    return f"{name}[{index}]" if index is not None else name


def build_include(paths):
    """Render the .include source for a list of
    (cat_name, cat_index, dec_name, dec_index) tuples, grouping decisions under
    their shared category header.

    Decision categories are top-level, so there is no `ideas:` wrapper: the
    category header sits at column 0. A `[N]` selector is emitted for any name
    that is not unique among its siblings, so duplicated category or decision
    names still resolve to the intended block.
    """
    lines = []

    # Group decisions by category identity (name + positional index), preserving
    # first-seen order of both categories and decisions.
    grouped = {}
    order = []
    for cat_name, cat_index, dec_name, dec_index in paths:
        key = (cat_name, cat_index)
        if key not in grouped:
            grouped[key] = []
            order.append(key)
        grouped[key].append((dec_name, dec_index))

    for c, key in enumerate(order):
        cat_name, cat_index = key
        if c > 0:
            # Blank line between category blocks.
            lines.append("")
        lines.append(f"{_header(cat_name, cat_index)}:")
        for n, (dec_name, dec_index) in enumerate(grouped[key]):
            if n > 0:
                # Blank line between decision blocks (not before the first).
                lines.append("")
            lines.append(f"{INDENT}{_header(dec_name, dec_index)}:")
            lines.append(f"{INDENT * 2}ai_will_do:")
            for ml in _MODIFIER_LINES:
                lines.append(f"{INDENT * 3}{ml}")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def process_dir(in_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    written = 0
    skipped = 0
    errored = 0
    repaired = 0
    for fname in sorted(os.listdir(in_dir)):
        if not fname.endswith(".txt"):
            continue
        in_path = os.path.join(in_dir, fname)
        if not os.path.isfile(in_path):
            continue

        with open(in_path, "r", encoding="utf-8-sig") as f:
            text = f.read()

        # Auto-close a file that is missing only its trailing top-level brace(s),
        # mirroring the engine's EOF tolerance. Any other imbalance is left alone
        # so it still surfaces as a real parse error below.
        text, n_added = repair_eof_braces(text)
        repaired_note = ""
        if n_added:
            repaired += 1
            brace_word = "brace" if n_added == 1 else "braces"
            repaired_note = f" (auto-closed {n_added} missing top-level {brace_word})"

        try:
            paths = find_ai_will_do_paths(text)
        except ValueError as e:
            # Don't let one malformed/unparseable file abort the whole run;
            # report it (with a location hint if we can find one) and move on.
            hint = diagnose_brace_balance(text)
            detail = hint if hint else str(e)
            print(f"  !! {fname}: skipped ({detail})")
            errored += 1
            continue

        if not paths:
            skipped += 1
            continue

        out_name = fname[:-len(".txt")] + ".include"
        out_path = os.path.join(out_dir, out_name)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(build_include(paths))

        print(f"  {fname}: {len(paths)} ai_will_do -> {out_name}{repaired_note}")
        written += 1

    msg = (f"Done. {written} include file(s) written, "
           f"{skipped} file(s) skipped (no ai_will_do)")
    if repaired:
        msg += f", {repaired} file(s) auto-closed at EOF"
    if errored:
        msg += f", {errored} file(s) skipped (parse error)"
    print(msg + ".")


def main():
    in_dir = sys.argv[1] if len(sys.argv) > 1 else "Hearts of Iron IV/common/decisions"
    out_dir = sys.argv[2] if len(sys.argv) > 2 else "out"

    if not os.path.isdir(in_dir):
        print(f"Input directory not found: {in_dir}")
        sys.exit(1)

    process_dir(in_dir, out_dir)


if __name__ == "__main__":
    main()
