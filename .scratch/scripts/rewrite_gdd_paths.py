#!/usr/bin/env python3
"""Rewrite `gdd/` path references to `docs/gdd/` after moving the GDD folder.

Covers source comments/logmacros (.hsl/.hml/.include), markdown cross-links,
and any other text file that names the old top-level `gdd/` path. Idempotent:
`docs/gdd/` is left untouched (the negative lookbehind skips it).
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# `gdd/` not already preceded by `docs/` (and not part of a longer word).
PATTERN = re.compile(r"(?<!docs/)(?<![\w/])gdd/")
EXTS = {".hsl", ".hml", ".include", ".md", ".ps1", ".yml", ".txt", ".mdc"}


def main() -> None:
    changed = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in EXTS:
            continue
        # Keep the tooling itself and any vendored/git internals out.
        rel = path.relative_to(ROOT)
        if rel.parts[:1] == (".git",) or ".scratch" in rel.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new = PATTERN.sub("docs/gdd/", text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed.append(str(rel))

    print(f"rewrote {len(changed)} files")
    for c in sorted(changed):
        print(f"  {c}")


if __name__ == "__main__":
    main()
