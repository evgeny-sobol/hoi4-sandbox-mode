#!/usr/bin/env python3
"""Guard: every elif/else in HSL must attach to an if/elif at its indent.

Deleting a branch can orphan the else below it (the pick function lost its
pin ifs and kept the else, which broke scenario selection with a game-parser
error the HSL compiler does not catch). The check scans back from each
elif/else past deeper body lines; the first line at the same or lower indent
must open or continue the chain. Lines with unbalanced braces on either side
are skipped instead of flagged.
"""
from __future__ import annotations

import pathlib
import re

MODS = [
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]
CHAIN_OPEN = re.compile(r"^(if|elif)\b.*:$")
CHAIN_ELSE = re.compile(r"^else\s*:$")


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip())


def problems_in(path: pathlib.Path) -> list[str]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    out = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        is_elif = bool(re.match(r"^elif\b", stripped))
        is_else = bool(CHAIN_ELSE.match(stripped))
        if not (is_elif or is_else):
            continue
        level = indent_of(line)
        found = None
        for j in range(i - 1, -1, -1):
            prev = lines[j]
            if not prev.strip() or prev.strip().startswith("#"):
                continue
            if "{" in prev or "}" in prev or "{" in line or "}" in line:
                found = "braces"
                break
            if indent_of(prev) > level:
                continue
            found = prev.strip()
            break
        if found is None:
            out.append(f"{path.name}:{i + 1}: {stripped[:60]} has no anchor above")
        elif found == "braces":
            continue
        elif is_elif and not re.match(r"^(if|elif)\b.*:$", found):
            out.append(f"{path.name}:{i + 1}: elif without an if/elif above (found {found[:50]!r})")
        elif is_else and not re.match(r"^(if|elif)\b.*:$", found):
            out.append(f"{path.name}:{i + 1}: else without an if/elif above (found {found[:50]!r})")
    return out


def main() -> int:
    problems = 0
    for mod in MODS:
        for path in sorted((mod / "common").rglob("*.hsl")):
            for msg in problems_in(path):
                problems += 1
                print(f"{mod.name}: {msg}")
        for path in sorted((mod / "events").glob("*.hsl")):
            for msg in problems_in(path):
                problems += 1
                print(f"{mod.name}: {msg}")
    print("problems:", problems)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
