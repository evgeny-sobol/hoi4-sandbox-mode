#!/usr/bin/env python3
"""
Generate .include files that disable AI strategies / strategy plans in sandbox
mode. For each top-level plan block, the sandbox trigger is injected into BOTH
gate blocks, because an ai_strategy that was already assigned stays assigned
until its `abort` fires:

  * enable : add  is_sandbox_mode_on(no)   -> plan won't (re)enable in sandbox
  * abort  : add  is_sandbox_mode_on(yes)  -> plan is dropped if already active

`abort` has three shapes, handled as follows:

  1. abort = { OR = { ... } }     -> navigate abort:/OR: and add the trigger.
  2. abort = { <flat triggers> }  -> the flat list is an implicit AND, so the
     trigger cannot be appended directly (that would AND it with the rest). The
     flat body is first NORMALIZED in memory into abort = { OR = { ... } }, then
     handled as case 1.
  3. abort absent                 -> create it: +abort with is_sandbox_mode_on(yes).

Pipeline per source .txt:
  1. Expand single-line enable/abort blocks and normalize flat aborts into OR
     form (in a temporary .txt; the real source is never modified).
  2. Build the .include from the normalized temporary text.
  3. Delete the temporary .txt.

Usage:
    python disable_ai_for_strategies.py -in <ai_strategy_dir> -out <output_dir>
"""

import argparse
import os
import re
import tempfile

# ===========================================================================
# Brace-aware scanning (ported from the HSL project).
# ===========================================================================

_WORD_CHARS = set(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
)


def _is_word_char(text, i):
    return 0 <= i < len(text) and text[i] in _WORD_CHARS


def _skip_string(text, i):
    i += 1
    n = len(text)
    while i < n:
        c = text[i]
        if c == '\\':
            i += 2
            continue
        if c == '"':
            return i + 1
        i += 1
    return i


def _skip_comment(text, i):
    n = len(text)
    while i < n and text[i] != '\n':
        i += 1
    return i


def _match_closing_brace(text, open_pos):
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
    raise ValueError("Unbalanced braces: no matching '}' found")


def _iter_top_level_blocks(text):
    """Yield (name, open_pos, close_pos) for every `NAME = { ... }` at depth 0."""
    i = 0
    n = len(text)
    depth = 0
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
            i += 1
            continue

        if depth == 0 and (c in _WORD_CHARS) and not _is_word_char(text, i - 1):
            j = i
            while j < n and text[j] in _WORD_CHARS:
                j += 1
            name = text[i:j]
            k = j
            while k < n and text[k] in ' \t\r\n':
                k += 1
            if k < n and text[k] == '=':
                k += 1
                while k < n and text[k] in ' \t\r\n':
                    k += 1
                if k < n and text[k] == '{':
                    open_pos = k + 1
                    close_pos = _match_closing_brace(text, open_pos)
                    yield (name, open_pos, close_pos)
                    i = close_pos + 1
                    continue
            i = j
            continue
        i += 1


def _iter_named_blocks(text, name, start, end):
    """Yield (open_pos, close_pos) for every direct-child `name = { ... }`
    at brace depth 0 within text[start:end]."""
    i = start
    depth = 0
    nlen = len(name)
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

        if depth == 0 and not _is_word_char(text, i - 1) \
                and text.startswith(name, i) \
                and not _is_word_char(text, i + nlen):
            j = i + nlen
            while j < end and text[j] in ' \t\r\n':
                j += 1
            if j < end and text[j] == '=':
                j += 1
                while j < end and text[j] in ' \t\r\n':
                    j += 1
                if j < end and text[j] == '{':
                    open_pos = j + 1
                    close_pos = _match_closing_brace(text, open_pos)
                    yield (open_pos, close_pos)
                    i = close_pos + 1
                    continue
            i = i + nlen
            continue
        i += 1


def _has_direct_block(text, open_pos, close_pos, key):
    for _ in _iter_named_blocks(text, key, open_pos, close_pos):
        return True
    return False


# ===========================================================================
# STEP 1a: expand single-line `name = { ... }` blocks (enable / abort)
# ===========================================================================

_TOKEN = re.compile(r'"[^"]*"|[{}]|[^\s{}]+')


def _reflow_inner(inner, base_indent):
    toks = _TOKEN.findall(inner)
    if not toks:
        return None
    lines = []
    indent = 1
    cur = []

    def flush():
        if cur:
            lines.append(base_indent + ('\t' * indent) + ' '.join(cur))
            cur.clear()

    for t in toks:
        if t == '{':
            cur.append('{')
            flush()
            indent += 1
        elif t == '}':
            flush()
            indent -= 1
            lines.append(base_indent + ('\t' * indent) + '}')
        else:
            cur.append(t)
            if len(cur) == 3:
                flush()
    flush()
    return '\n'.join(lines)


def expand_single_line_blocks(text, name):
    """Rewrite every single-line `name = { ... }` (any depth) into multi-line."""
    out = []
    i = 0
    n = len(text)
    nlen = len(name)
    while i < n:
        c = text[i]
        if c == '#':
            j = _skip_comment(text, i)
            out.append(text[i:j]); i = j; continue
        if c == '"':
            j = _skip_string(text, i)
            out.append(text[i:j]); i = j; continue
        if not _is_word_char(text, i - 1) \
                and text.startswith(name, i) \
                and not _is_word_char(text, i + nlen):
            j = i + nlen
            k = j
            while k < n and text[k] in ' \t\r\n':
                k += 1
            if k < n and text[k] == '=':
                k += 1
                while k < n and text[k] in ' \t\r\n':
                    k += 1
                if k < n and text[k] == '{':
                    open_pos = k + 1
                    close_pos = _match_closing_brace(text, open_pos)
                    block_text = text[open_pos:close_pos]
                    if '\n' not in block_text:
                        line_start = text.rfind('\n', 0, i) + 1
                        base_indent = text[line_start:i]
                        body = _reflow_inner(block_text.strip(), base_indent)
                        if body is not None:
                            out.append(f"{name} = {{\n{body}\n{base_indent}}}")
                        else:
                            out.append(f"{name} = {{\n{base_indent}}}")
                        i = close_pos + 1
                        continue
            out.append(text[i:j]); i = j; continue
        out.append(c); i += 1
    return ''.join(out)


# ===========================================================================
# STEP 1b: normalize flat `abort = { ... }` into `abort = { OR = { ... } }`
# ===========================================================================

def normalize_flat_aborts(text):
    """For each top-level plan, if its `abort` is a flat trigger list (no direct
    OR child), wrap the body in an OR block. OR-form and missing aborts are left
    untouched. Applied bottom-up so offsets stay valid."""
    edits = []
    for name, o, c in _iter_top_level_blocks(text):
        ablocks = list(_iter_named_blocks(text, 'abort', o, c))
        if not ablocks:
            continue
        ao, ac = ablocks[0]
        if list(_iter_named_blocks(text, 'OR', ao, ac)):
            continue  # already OR-form

        inner = text[ao:ac]
        astart = text.rfind('abort', o, ao)
        line_start = text.rfind('\n', 0, astart) + 1
        base = text[line_start:astart]

        inner_lines = [l for l in inner.strip('\n').split('\n')]
        wrapped = '\n'.join(
            (base + '\t\t' + l.strip()) if l.strip() else ''
            for l in inner_lines
        )
        wrapped = wrapped.strip('\n')
        replacement = (
            f"abort = {{\n{base}\tOR = {{\n{wrapped}\n{base}\t}}\n{base}}}"
        )
        edits.append((astart, ac + 1, replacement))

    for s, e, r in sorted(edits, key=lambda t: t[0], reverse=True):
        text = text[:s] + r + text[e:]
    return text


def preprocess(text):
    """Full in-memory normalization before .include generation."""
    text = expand_single_line_blocks(text, 'enable')
    text = expand_single_line_blocks(text, 'abort')
    text = normalize_flat_aborts(text)
    return text


# ===========================================================================
# STEP 2: build the .include
# ===========================================================================

INDENT = "  "  # two-space indent, matching the HSL/.include convention


def build_include(text):
    """Return the .include text for one (already preprocessed) file, or None if
    it has no top-level plan blocks."""
    lines = []
    emitted_any = False

    for name, open_pos, close_pos in _iter_top_level_blocks(text):
        has_enable = _has_direct_block(text, open_pos, close_pos, "enable")
        has_abort = _has_direct_block(text, open_pos, close_pos, "abort")

        if emitted_any:
            lines.append("")  # blank line between plans

        lines.append(f"{name}:")

        # enable: prevent (re)enabling in sandbox.
        if has_enable:
            lines.append(f"{INDENT}enable:")
            lines.append(f"{INDENT*2}is_sandbox_mode_on(no)")
        else:
            lines.append(f"{INDENT}+enable:")
            lines.append(f"{INDENT*2}is_sandbox_mode_on(no)")

        # abort: drop the strategy in sandbox. After preprocessing, an existing
        # abort is always in OR form, so we navigate abort:/OR: and add a branch.
        if has_abort:
            lines.append(f"{INDENT}abort:")
            lines.append(f"{INDENT*2}OR:")
            lines.append(f"{INDENT*3}is_sandbox_mode_on(yes)")
        else:
            lines.append(f"{INDENT}+abort:")
            lines.append(f"{INDENT*2}is_sandbox_mode_on(yes)")

        emitted_any = True

    if not emitted_any:
        return None
    return "\n".join(lines) + "\n"


# ===========================================================================
# PIPELINE
# ===========================================================================

def process_file(src_path, in_dir, out_dir, tmp_dir):
    with open(src_path, "r", encoding="utf-8-sig") as f:
        text = f.read()

    processed = preprocess(text)

    rel = os.path.relpath(src_path, in_dir)
    tmp_path = os.path.join(tmp_dir, rel)
    os.makedirs(os.path.dirname(tmp_path), exist_ok=True)
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(processed)

    try:
        with open(tmp_path, "r", encoding="utf-8-sig") as f:
            include_text = build_include(f.read())
    finally:
        try:
            os.remove(tmp_path)
        except OSError:
            pass

    if include_text is None:
        return 'skipped'

    rel_include = os.path.splitext(rel)[0] + ".include"
    dst_path = os.path.join(out_dir, rel_include)
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(include_text)
    return 'built'


def main():
    ap = argparse.ArgumentParser(
        description="Generate sandbox-disable .include files (enable + abort) for AI strategies."
    )
    ap.add_argument("-in", dest="in_dir", required=True,
                    help="Path to common/ai_strategy(_plans)/ (scanned recursively).")
    ap.add_argument("-out", dest="out_dir", required=True,
                    help="Output directory for generated .include files.")
    args = ap.parse_args()

    in_dir = args.in_dir
    out_dir = args.out_dir

    if not os.path.isdir(in_dir):
        raise SystemExit(f"Input directory does not exist: {in_dir}")

    generated = 0
    skipped = 0

    with tempfile.TemporaryDirectory(prefix="hsl_sandbox_") as tmp_dir:
        for root, _dirs, files in os.walk(in_dir):
            for fn in files:
                if not fn.endswith(".txt"):
                    continue
                src_path = os.path.join(root, fn)
                rel = os.path.relpath(src_path, in_dir)
                status = process_file(src_path, in_dir, out_dir, tmp_dir)
                if status == 'built':
                    print(f"  {rel} -> {os.path.splitext(rel)[0]}.include")
                    generated += 1
                else:
                    skipped += 1

    print("-" * 50)
    print(f"Generated: {generated} .include file(s); skipped (no plan blocks): {skipped}")


if __name__ == "__main__":
    main()
