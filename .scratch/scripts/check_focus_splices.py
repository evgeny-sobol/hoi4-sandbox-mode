#!/usr/bin/env python3
"""Guard the scenario focus splices in both mods.

Three rules, all mechanical and cheap:

1. A `+completion_reward` splice must sit at the focus-body indent, never at
   the tree level. A tree-level splice lands outside its focus and the engine
   rejects it (issue 17).
2. Focus telemetry must go through the gated wrapper
   `$sandbox_log_sc_focus(<id>)`. The ungated base writer lets an unrelated
   country's focus land in an arc's log (issue 18).
3. In a spec-driven mod every boosted focus carries exactly one `sc_focus`
   block for its own id, and no focus carries a log without a boost (issue 31).
   `_sandbox-r56` is not spec-driven yet (issue 28), so rule 3 is scoped to
   `_sandbox`.

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
# Rule 3 applies only where the builder owns the boost plan.
PARITY_MODS = {MODS[0].name}
TREE_LEVEL = re.compile(r"^  \+completion_reward:\s*$")
UNGATED = "$sandbox_log_sc(sc_focus"
FOCUS_HEAD = re.compile(r"^  focus\[id = ([A-Za-z0-9_]+)\]:", re.M)
BOOST_MARKER = "$ai_scenario_focus_boost"
LOG_MARKER = "$sandbox_log_sc_focus"
LOG_ID_RE = re.compile(r"\$sandbox_log_sc_focus\(([A-Za-z0-9_]+)\)")


def focus_blocks(text: str) -> list[tuple[str, str]]:
    heads = [(m.group(1), m.start()) for m in FOCUS_HEAD.finditer(text)]
    out = []
    for i, (fid, start) in enumerate(heads):
        end = heads[i + 1][1] if i + 1 < len(heads) else len(text)
        out.append((fid, text[start:end]))
    return out


def main() -> int:
    offenders = 0
    for mod in MODS:
        parity = mod.name in PARITY_MODS
        for path in sorted((mod / "common" / "national_focus").glob("*.include")):
            rel = path.relative_to(mod)
            text = path.read_text(encoding="utf-8", errors="replace")
            for i, line in enumerate(text.splitlines(), 1):
                if TREE_LEVEL.match(line):
                    offenders += 1
                    print(f"{rel}:{i}: tree-level +completion_reward")
                if UNGATED in line:
                    offenders += 1
                    print(f"{rel}:{i}: ungated sc_focus call")
            if not parity:
                continue
            for fid, block in focus_blocks(text):
                boosted = BOOST_MARKER in block
                ids = LOG_ID_RE.findall(block)
                if boosted and ids != [fid]:
                    offenders += 1
                    print(f"{rel}: {fid}: boosted focus needs exactly one sc_focus({fid}), has {ids}")
                elif ids and not boosted:
                    offenders += 1
                    print(f"{rel}: {fid}: sc_focus without a boost")
    print(f"offenders: {offenders}")
    return 1 if offenders else 0


if __name__ == "__main__":
    raise SystemExit(main())
