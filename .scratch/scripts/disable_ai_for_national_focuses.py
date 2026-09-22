#!/usr/bin/env python3
"""
Generate .include files that append a sandbox-mode modifier to every focus's
ai_will_do in a HoI4 national_focus directory.

For each focus:
  * ai_will_do EXISTS  -> navigate into it and CREATE a new modifier:
        ai_will_do:
          +modifier:
            is_sandbox_mode_on()
            base(1.0)
  * ai_will_do MISSING -> CREATE the whole block:
        +ai_will_do:
          modifier:
            is_sandbox_mode_on()
            base(1.0)

Usage:
    python disable_ai_for_national_focuses.py -in <national_focus_dir> -out <output_dir>
"""

import argparse
import os

# ---------------------------------------------------------------------------
# Brace-aware scanning (ported from the HSL project: includes.py /
# extract_ai_will_do.py). Handles strings and # comments so braces inside them
# don't throw off depth counting.
# ---------------------------------------------------------------------------

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
# .include generation
# ---------------------------------------------------------------------------

INDENT = "  "  # two-space indent, matching the HSL/.include convention


def build_include(text):
    """Return the .include text for one focus-tree file, or None if it has no
    focuses to override."""
    lines = []

    # focus blocks live inside focus_tree = { ... }; handle multiple trees.
    tree_ranges = list(_iter_named_blocks(text, "focus_tree", 0, len(text)))
    if not tree_ranges:
        return None

    emitted_any = False

    for tree_open, tree_close in tree_ranges:
        tree_id = _read_direct_scalar(text, tree_open, tree_close, "id")
        if tree_id is None:
            # Cannot address a tree without an id; skip it.
            continue

        focus_lines = []
        for f_open, f_close in _iter_named_blocks(text, "focus", tree_open, tree_close):
            focus_id = _read_direct_scalar(text, f_open, f_close, "id")
            if focus_id is None:
                continue  # malformed focus without id

            has_awd = _has_direct_block(text, f_open, f_close, "ai_will_do")

            focus_lines.append("")  # blank line before each focus block
            focus_lines.append(f"{INDENT}focus[id = {focus_id}]:")
            if has_awd:
                # Navigate into existing ai_will_do, create a new modifier.
                focus_lines.append(f"{INDENT*2}ai_will_do:")
                focus_lines.append(f"{INDENT*3}+modifier:")
                focus_lines.append(f"{INDENT*4}is_sandbox_mode_on()")
                focus_lines.append(f"{INDENT*4}base(1.0)")
            else:
                # Create the whole ai_will_do block.
                focus_lines.append(f"{INDENT*2}+ai_will_do:")
                focus_lines.append(f"{INDENT*3}modifier:")
                focus_lines.append(f"{INDENT*4}is_sandbox_mode_on()")
                focus_lines.append(f"{INDENT*4}base(1.0)")

        if focus_lines:
            lines.append(f"focus_tree[id = {tree_id}]:")
            lines.extend(focus_lines)
            emitted_any = True

    if not emitted_any:
        return None
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(
        description="Generate ai_will_do override .include files for HoI4 focus trees."
    )
    ap.add_argument("-in", dest="in_dir", required=True,
                    help="Path to common/national_focus/ (scanned recursively).")
    ap.add_argument("-out", dest="out_dir", required=True,
                    help="Output directory for generated .include files.")
    args = ap.parse_args()

    in_dir = args.in_dir
    out_dir = args.out_dir

    if not os.path.isdir(in_dir):
        raise SystemExit(f"Input directory does not exist: {in_dir}")

    generated = 0
    skipped = 0

    for root, _dirs, files in os.walk(in_dir):
        for fn in files:
            if not fn.endswith(".txt"):
                continue
            src_path = os.path.join(root, fn)
            with open(src_path, "r", encoding="utf-8-sig") as f:
                text = f.read()

            include_text = build_include(text)
            if include_text is None:
                skipped += 1
                continue

            # Mirror the input's relative layout under out_dir.
            rel = os.path.relpath(src_path, in_dir)
            rel_include = os.path.splitext(rel)[0] + ".include"
            dst_path = os.path.join(out_dir, rel_include)
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)

            with open(dst_path, "w", encoding="utf-8") as f:
                f.write(include_text)

            print(f"  {rel} -> {rel_include}")
            generated += 1

    print("-" * 50)
    print(f"Generated: {generated} .include file(s); skipped (no focus tree): {skipped}")


if __name__ == "__main__":
    main()
