#!/usr/bin/env python3
"""Guard the derail dispatcher: every arc must park on a dead aggressor.

Two accepted shapes per branch: a generated/helper call (the helper owns the
arms) or inline `country_exists` + `has_capitulated()`. Covers both mods and
any arc count the catalog carries.
"""
from __future__ import annotations

import pathlib
import re

MODS = [
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]
CATALOG = pathlib.Path("common") / "scripted_effects" / "99_sandbox_scenarios.hsl"
FUNC = re.compile(r"^[A-Za-z_0-9]+\(\):$")
BRANCH = re.compile(r"^  (?:if|elif) global\.sandbox_scenario_phase < 3 and global\.sandbox_scenario == (\d+):$")
ARM_CALL = re.compile(r"(sandbox_scenario_check_\w+_derail|gen_\w+_derail)\(\)")


def check(mod: pathlib.Path) -> list[str]:
    lines = (mod / CATALOG).read_text(encoding="utf-8", errors="replace").splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip() == "sandbox_scenario_check_derail():")
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if FUNC.match(lines[i].strip()):
            end = i
            break

    cur = None
    branches: dict[int, list[str]] = {}
    for line in lines[start + 1 : end]:
        m = BRANCH.match(line)
        if m:
            cur = int(m.group(1))
            branches[cur] = []
        elif cur is not None and line.startswith("  "):
            branches[cur].append(line)

    problems: list[str] = []
    for arc in sorted(branches):
        body = "\n".join(branches[arc])
        if ARM_CALL.search(body):
            continue
        if "country_exists(" in body and "has_capitulated()" in body:
            continue
        problems.append(f"{mod.name}: arc {arc} has no gone/capitulated arm")
    return problems


def main() -> int:
    problems: list[str] = []
    for mod in MODS:
        found = check(mod)
        problems.extend(found)
        print(f"{mod.name}: problems {len(found)}")
    for p in problems:
        print(p)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
