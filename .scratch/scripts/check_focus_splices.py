#!/usr/bin/env python3
"""Guard the scenario focus splices in both mods.

Two rules, both mechanical and cheap:

1. A `+completion_reward` splice must sit at the focus-body indent, never at
   the tree level. A tree-level splice lands outside its focus and the engine
   rejects it (issue 17).
2. Focus telemetry must go through the gated wrapper
   `$sandbox_log_sc_focus(<id>)`. The ungated base writer lets an unrelated
   country's focus land in an arc's log (issue 18).

Run before a compile; the generator can still emit either shape, so the guard
is the gate, not a formality.
"""
from __future__ import annotations

import pathlib
import re

MODS = [
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]
TREE_LEVEL = re.compile(r"^  \+completion_reward:\s*$")
UNGATED = "$sandbox_log_sc(sc_focus"


def main() -> int:
    offenders = 0
    for mod in MODS:
        for path in sorted((mod / "common" / "national_focus").glob("*.include")):
            rel = path.relative_to(mod)
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
            for i, line in enumerate(lines, 1):
                if TREE_LEVEL.match(line):
                    offenders += 1
                    print(f"{rel}:{i}: tree-level +completion_reward")
                if UNGATED in line:
                    offenders += 1
                    print(f"{rel}:{i}: ungated sc_focus call")
    print(f"offenders: {offenders}")
    return 1 if offenders else 0


if __name__ == "__main__":
    raise SystemExit(main())
