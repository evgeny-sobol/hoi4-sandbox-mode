#!/usr/bin/env python3
"""
Generate the base sandbox ai_will_do gate for a HoI4 national_focus directory.

WHAT THIS WRITES, AND WHAT IT DOES NOT
======================================
For every focus it emits exactly one structural decision, the same one for all:

    $ai_sandbox_modifier()          -> factor(0) + add(40) + is_sandbox_mode_on()

That is the floor described in ``docs/gdd/National Focuses.md`` section
"Basic modifiers". Every focus gets it; nothing else here is mechanical.

The following are DESIGN decisions and are deliberately NOT generated:

  * ``$root_modifier()`` on a focus with no ``prerequisite`` block. 1,000 of the
    1,000 artefacts carry it exactly when the focus is a root, but a reader who
    regenerates blindly would also lose the hand-authored cases.
  * ``$crossroad_modifier(N)`` on mutually exclusive forks. The gate is
    "mutually exclusive AND optional AND not already partitioned by party
    popularity / Tyranny / a ``has_government`` check / a political
    ``search_filters`` entry" (same section of the GDD). Mechanical detection of
    the first three predicates alone leaves 79 groups that a faithful
    regeneration must leave alone - optional MIC and doctrine forks that were
    deliberately kept at singleton weight (commit 08074b4).
  * Party-popularity shares, Tyranny tilts, diplomacy modifiers, the MIC and
    war-support modifiers, advisor slot gates.

So: generate into a scratch directory, then merge by hand. The tool is
additive by design; it never rewrites an existing include.

ORDER
=====
Rows come out in vanilla file order. Some shipped includes (``germany``) are
hand-grouped by their table-of-contents sections instead, so a diff against a
fresh generation there is expected and is not a defect.

ROW KIND
========
Vanilla carries focus blocks in two shapes, and the include has to mirror the
shape so the HSL compiler can find the block:

  * inside ``focus_tree = { }``   -> file header ``focus_tree[id = X]:``
    and rows ``focus[id = ...]`` / ``shared_focus[id = ...]``
  * at the top level of a file    -> rows ``shared_focus[id = ...]`` /
    ``joint_focus[id = ...]``, no tree header

A vanilla file is one or the other; no file mixes the two shapes, so the tree
decision is per file.

CREATING vs NAVIGATING ``ai_will_do``
=====================================
The ``+`` in ``+ai_will_do:`` means "create a block". Creating a second
``ai_will_do`` when vanilla already has one leaves the focus with two blocks
and the first one's weight is lost outside sandbox mode. 3,248 of the 3,252
rows are ``+ai_will_do`` because vanilla has no block; 6,973 are a plain
``ai_will_do:`` because it does. The form is a function of the vanilla file, so
it is generated, not assumed.

Usage
=====
    python disable_ai_for_national_focuses.py -in <vanilla_national_focus_dir> \
        -out <scratch_dir> [--check] [--verbose]

``--check`` regenerates in memory and diffs against the existing includes in
the same layout, reporting per focus: a missing row, a row on a focus vanilla
does not have, and any now-wrong create/navigate form. Use it after a game
patch: a patch that adds a focus or gives a focus an ``ai_will_do`` block shows
up as one report line instead of as a silently doubled block.

Output is plain ASCII, LF line endings, no BOM, matching the sibling scripts.
"""

import argparse
import os
import re
import sys

# ---------------------------------------------------------------------------
# Brace-aware scanning (ported from the HSL project: includes.py /
# extract_ai_will_do.py). Handles strings and # comments so braces inside them
# don't throw off depth counting.
# ---------------------------------------------------------------------------

_WORD_CHARS = set(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
)

# Focus-block row names, in the order a vanilla file may nest them.
FOCUS_KINDS = ("focus", "shared_focus", "joint_focus")


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
    raise ValueError("Unbalanced braces: no matching '}' found")


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


def _read_direct_scalar(text, open_pos, close_pos, key):
    """Return the scalar value of the first depth-0 `key = <scalar>` inside the
    block, or None. Block-valued keys are skipped."""
    i = open_pos
    depth = 0
    klen = len(key)
    while i < close_pos:
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
                and text.startswith(key, i) \
                and not _is_word_char(text, i + klen):
            j = i + klen
            while j < close_pos and text[j] in ' \t\r\n':
                j += 1
            if j < close_pos and text[j] == '=':
                j += 1
                while j < close_pos and text[j] in ' \t\r\n':
                    j += 1
                if j < close_pos and text[j] == '{':
                    i = _match_closing_brace(text, j + 1) + 1
                    continue
                if j < close_pos and text[j] == '"':
                    endq = _skip_string(text, j)
                    return text[j:endq].strip('"')
                k = j
                while k < close_pos and text[k] not in ' \t\r\n}#':
                    k += 1
                return text[j:k]
            i = i + klen
            continue
        i += 1
    return None


def _has_direct_block(text, open_pos, close_pos, key):
    """True if a direct (depth-0) `key = { ... }` block exists in the block."""
    for _ in _iter_named_blocks(text, key, open_pos, close_pos):
        return True
    return False


# ---------------------------------------------------------------------------
# Vanilla model
# ---------------------------------------------------------------------------

class Row:
    """One focus block found in a vanilla file."""

    __slots__ = ("kind", "focus_id", "has_ai_will_do", "is_root")

    def __init__(self, kind, focus_id, has_ai_will_do, is_root):
        self.kind = kind
        self.focus_id = focus_id
        self.has_ai_will_do = has_ai_will_do
        self.is_root = is_root


def read_vanilla(text):
    """Return (tree_id, [Row]) for one vanilla focus file.

    tree_id is None when the file holds top-level shared/joint focuses instead
    of a focus_tree. Vanilla files are one shape or the other; a file with both
    would need a header per shape and is rejected rather than guessed at."""
    rows = []

    trees = list(_iter_named_blocks(text, "focus_tree", 0, len(text)))
    top_rows = []
    for kind in FOCUS_KINDS:
        for open_pos, close_pos in _iter_named_blocks(text, kind, 0, len(text)):
            focus_id = _read_direct_scalar(text, open_pos, close_pos, "id")
            if focus_id is None:
                continue  # malformed block without an id
            top_rows.append(Row(
                kind,
                focus_id,
                _has_direct_block(text, open_pos, close_pos, "ai_will_do"),
                not _has_direct_block(text, open_pos, close_pos, "prerequisite"),
            ))

    if len(trees) > 1:
        raise ValueError("file holds more than one focus_tree; split it first")

    if trees:
        if top_rows:
            raise ValueError(
                "file mixes a focus_tree with top-level shared/joint focuses; "
                "the include layout cannot address both")
        tree_open, tree_close = trees[0]
        tree_id = _read_direct_scalar(text, tree_open, tree_close, "id")
        if tree_id is None:
            raise ValueError("focus_tree without an id")
        for kind in FOCUS_KINDS:
            for open_pos, close_pos in _iter_named_blocks(
                    text, kind, tree_open, tree_close):
                focus_id = _read_direct_scalar(text, open_pos, close_pos, "id")
                if focus_id is None:
                    continue
                rows.append(Row(
                    kind,
                    focus_id,
                    _has_direct_block(text, open_pos, close_pos, "ai_will_do"),
                    not _has_direct_block(
                        text, open_pos, close_pos, "prerequisite"),
                ))
        return tree_id, rows

    if not top_rows:
        return None, []
    return None, top_rows


# ---------------------------------------------------------------------------
# .include rendering
# ---------------------------------------------------------------------------

INDENT = "  "  # two-space indent, matching the HSL/.include convention


def render_row(row):
    """Render one row with only the base sandbox floor."""
    lines = [f"{INDENT}{row.kind}[id = {row.focus_id}]:"]
    if row.has_ai_will_do:
        # Navigate into the existing block and append a modifier.
        lines.append(f"{INDENT * 2}ai_will_do:")
        lines.append(f"{INDENT * 3}+modifier:")
    else:
        # Create the block; vanilla has none.
        lines.append(f"{INDENT * 2}+ai_will_do:")
        lines.append(f"{INDENT * 3}modifier:")
    lines.append(f"{INDENT * 4}$ai_sandbox_modifier()")
    return lines


def render_include(tree_id, rows):
    """Render the .include body for one vanilla file, or None if no rows."""
    if not rows:
        return None
    lines = []
    if tree_id is not None:
        lines.append(f"focus_tree[id = {tree_id}]:")
    for row in rows:
        # A tree header owns the first separator; a header-less file starts
        # straight with its first row.
        if lines:
            lines.append("")
        lines.extend(render_row(row))
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# --check: compare the vanilla model against the existing includes
# ---------------------------------------------------------------------------

def parse_include(text):
    """Map focus id -> (kind, creates_block) from an existing .include."""
    out = {}
    for m in re.finditer(
            r"(?m)^" + INDENT + r"(focus|shared_focus|joint_focus)"
            r"\[id = ([A-Za-z0-9_\-]+)\]:", text):
        kind, focus_id = m.group(1), m.group(2)
        out[focus_id] = (kind, _include_tail(text, m.end()))
    return out


def _include_tail(text, start):
    """True if this row CREATES ai_will_do, False if it navigates, None if it
    does not touch ai_will_do at all.

    Indexed selectors (``ai_will_do[0]:``) address one of several blocks in the
    same focus; they are a navigate, not a create."""
    end = len(text)
    m = re.search(r"(?m)^" + INDENT + r"(?:focus|shared_focus|joint_focus)"
                  r"\[id = ", text[start:])
    if m:
        end = start + m.start()
    body = text[start:end]
    selector = r"ai_will_do(?:\[[^\]]+\])?:"
    if re.search(r"(?m)^" + INDENT * 2 + r"\+" + selector, body):
        return True
    if re.search(r"(?m)^" + INDENT * 2 + selector, body):
        return False
    return None


def check_one(rel_include, vanilla_text, include_path):
    """Report drift between vanilla and the shipped include. Returns (errors,
    warnings)."""
    try:
        tree_id, rows = read_vanilla(vanilla_text)
    except ValueError as exc:
        return [f"{rel_include}: {exc}"], []
    errors = []
    if not rows:
        return errors, []

    if not os.path.isfile(include_path):
        errors.append(
            f"{rel_include}: missing include; vanilla has {len(rows)} focus "
            f"block(s) with no sandbox gate")
        return errors, []

    with open(include_path, "r", encoding="utf-8") as f:
        existing = parse_include(f.read())

    covered = set()
    for row in rows:
        if row.focus_id not in existing:
            errors.append(
                f"{rel_include}: {row.focus_id} has NO row in the include "
                f"(vanilla {'has' if row.has_ai_will_do else 'has no'} "
                f"ai_will_do)")
            continue
        covered.add(row.focus_id)
        kind, creates = existing[row.focus_id]
        if kind != row.kind:
            errors.append(
                f"{rel_include}: {row.focus_id} is a {row.kind} in vanilla "
                f"but a {kind} in the include")
        if creates is None:
            errors.append(
                f"{rel_include}: {row.focus_id} has a row with no "
                f"ai_will_do gate")
        elif creates and row.has_ai_will_do:
            errors.append(
                f"{rel_include}: {row.focus_id} CREATES ai_will_do but "
                f"vanilla already has one (two blocks, the vanilla weight is "
                f"lost outside sandbox mode)")

    vanilla_ids = {row.focus_id for row in rows}
    for focus_id in sorted(set(existing) - vanilla_ids):
        errors.append(
            f"{rel_include}: {focus_id} has a row but vanilla has no such "
            f"focus (removed by a patch or wrongly named)")
    return errors, []


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Generate the base sandbox ai_will_do gate for a HoI4 "
                    "national_focus directory.")
    ap.add_argument("-in", dest="in_dir", required=True,
                    help="Path to the vanilla common/national_focus/.")
    ap.add_argument("-out", dest="out_dir", required=True,
                    help="Output directory for generated .include files, or "
                         "the directory holding the shipped includes with "
                         "--check.")
    ap.add_argument("--check", action="store_true",
                    help="Do not write; compare the vanilla model against the "
                         "existing includes in -out and report drift.")
    ap.add_argument("--verbose", action="store_true",
                    help="Also list every focus written / verified.")
    args = ap.parse_args()

    if not os.path.isdir(args.in_dir):
        raise SystemExit(f"Input directory does not exist: {args.in_dir}")
    if not args.check:
        os.makedirs(args.out_dir, exist_ok=True)

    generated = 0
    skipped = 0
    rows_total = 0
    errors = []

    for root, _dirs, files in os.walk(args.in_dir):
        for fn in sorted(files):
            if not fn.endswith(".txt"):
                continue
            src_path = os.path.join(root, fn)
            with open(src_path, "r", encoding="utf-8-sig") as f:
                text = f.read()

            rel = os.path.relpath(src_path, args.in_dir)
            rel_include = os.path.splitext(rel)[0] + ".include"
            dst_path = os.path.join(args.out_dir, rel_include)

            if args.check:
                found, _ = check_one(rel_include, text, dst_path)
                errors.extend(found)
                if args.verbose and not found:
                    print(f"  ok: {rel_include}")
                continue

            try:
                tree_id, rows = read_vanilla(text)
            except ValueError as exc:
                errors.append(f"{rel_include}: {exc}")
                continue
            include_text = render_include(tree_id, rows)
            if include_text is None:
                skipped += 1
                continue

            os.makedirs(os.path.dirname(dst_path) or ".", exist_ok=True)
            with open(dst_path, "w", encoding="utf-8", newline="\n") as f:
                f.write(include_text)

            print(f"  {rel} -> {rel_include} ({len(rows)} row(s))")
            generated += 1
            rows_total += len(rows)

    print("-" * 50)
    if args.check:
        if errors:
            for line in errors:
                print(f"error: {line}")
            print(f"{len(errors)} problem(s)")
            return 1
        print("ok: includes match the vanilla focus model")
        return 0

    print(f"Generated: {generated} .include file(s), {rows_total} row(s); "
          f"skipped (no focus blocks): {skipped}")
    if errors:
        for line in errors:
            print(f"error: {line}")
        return 1
    print("Base gate only: add $root_modifier() to roots and "
          "$crossroad_modifier(N) to the forks the GDD marks optional, by hand.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
