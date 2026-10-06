#!/usr/bin/env python3
"""Guard: the pick must offer an arc only when its aggressor passes the arc's
gate (issue 21). Reads the derail gate per arc and checks that the pick's
`eligible[].add(N)` for that arc sits behind the matching government test.
"""
from __future__ import annotations

import pathlib
import re

MODS = [
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    pathlib.Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]
CATALOG = pathlib.Path("common/scripted_effects/99_sandbox_scenarios.hsl")
FUNC = re.compile(r"^([A-Za-z_0-9]+)\(\):$")
SCEN = re.compile(r"sandbox_scenario == (\d+)")
ADD = re.compile(r"^(\s*)eligible\[\]\.add\((\d+)\)$")


def gates(lines: list[str]) -> dict[int, tuple[str, set[str]]]:
    """arc -> (aggressor, {governments the arm requires or excludes})."""
    funcs: dict[str, list[str]] = {}
    cur = None
    for line in lines:
        m = FUNC.match(line.strip())
        if m:
            cur = m.group(1)
            funcs[cur] = []
        elif cur:
            funcs[cur].append(line)
    disp = funcs["sandbox_scenario_check_derail"]
    arc_body: dict[int, str] = {}
    cur_arc = None
    for line in disp:
        m = SCEN.search(line)
        if m and line.strip().startswith(("if", "elif")):
            cur_arc = int(m.group(1))
            arc_body[cur_arc] = ""
        elif cur_arc is not None:
            arc_body[cur_arc] += line + "\n"
    out: dict[int, tuple[str, set[str]]] = {}
    for arc, body in arc_body.items():
        helper = re.search(r"(sandbox_scenario_check_\w+_derail|gen_\w+_derail)\(\)", body)
        src = "\n".join(funcs.get(helper.group(1), [])) if helper else body
        gov = re.findall(r"(\w+)->has_government\((\w+)\)", src)
        if gov:
            out[arc] = (gov[0][0], {g[1] for g in gov})
    return out


def main() -> int:
    problems = 0
    for mod in MODS:
        lines = (mod / CATALOG).read_text(encoding="utf-8", errors="replace").splitlines()
        need = gates(lines)
        start = next(i for i, l in enumerate(lines) if l.strip() == "sandbox_pick_scenario():")
        end = next(i for i in range(start + 1, len(lines)) if FUNC.match(lines[i].strip()))
        body = lines[start:end]
        for arc, (agg, govs) in sorted(need.items()):
            hits = [i for i, l in enumerate(body) if f"eligible[].add({arc})" in l]
            if not hits:
                continue
            for i in hits:
                window = "\n".join(body[max(0, i - 4) : i])
                if not any(f"{agg}->has_government({g})" in window for g in govs):
                    problems += 1
                    print(f"{mod.name}: arc {arc} eligible add without the {agg} gate")
    print("problems:", problems)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
