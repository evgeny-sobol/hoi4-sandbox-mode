#!/usr/bin/env python3
"""Tighten the splice guard: only scenario sc_focus splices may not sit at
tree level; vanilla-authored top-level rewards are legitimate."""
from __future__ import annotations

import pathlib
import re
import sys

MODS = [
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]
TREE_LEVEL = re.compile(r"^  \+completion_reward:\s*$")


def main() -> int:
    offenders = 0
    for mod in MODS:
        for path in sorted((mod / "common" / "national_focus").glob("*.include")):
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            for i, line in enumerate(lines, 1):
                if TREE_LEVEL.match(line):
                    offenders += 1
                    print(f"{path.relative_to(mod)}:{i}: tree-level +completion_reward")
    print(f"offenders: {offenders}")
    return 1 if offenders else 0


if __name__ == "__main__":
    raise SystemExit(main())
