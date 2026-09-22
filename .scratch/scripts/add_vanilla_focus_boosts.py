#!/usr/bin/env python3
"""Splice $ai_scenario_focus_boost() into the arc war-focus branches.

Mirrors the Rt56 overlay, mapped to vanilla ids. The boost sits on the war
focuses and on their branch roots (the s10/s11 lesson: a boost behind an
unboosted fork is dead).
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NF = ROOT / "common" / "national_focus"

SPLICES = {
    "germany.include": [
        # war focuses
        "GER_danzig_or_war", "GER_demand_sudetenland", "GER_war_with_france", "GER_around_maginot",
        # branch roots
        "GER_remilitarize_the_rhineland", "GER_anschluss",
    ],
    "soviet.include": [
        "SOV_preemptive_invasion_of_iran",
    ],
    "japan.include": [
        "JAP_reinforce_the_beijing_garrison", "JAP_strike_the_southern_road",
        "JAP_revisit_the_thirteen_demands", "JAP_occupy_siam",
    ],
    "italy.include": [
        "ITA_italys_destiny", "ITA_war_with_greece",
        "ITA_foreign_affairs", "ITA_ratify_the_stresa_front",
    ],
    "uk.include": [
        "ENG_war_with_ussr", "ENG_embargo_ussr",
        "ENG_steady_as_she_goes",
    ],
    "usa.include": [
        "USA_war_plan_orange", "USA_war_plan_black",
        "USA_defense_of_the_pacific", "USA_intervention_in_europe",
    ],
}


def add_boosts(path: Path, focuses: list[str]) -> int:
    raw = path.read_text(encoding="utf-8")
    added = 0
    for fc in focuses:
        start = raw.find(f"focus[id = {fc}]:")
        if start < 0:
            print(f"  miss in {path.name}: {fc}")
            continue
        nxt = raw.find("\n  focus[id = ", start + 5)
        if nxt < 0:
            nxt = len(raw)
        block = raw[start:nxt]
        if "$ai_scenario_focus_boost()" in block:
            continue
        anchor = raw.find("      $ai_sandbox_modifier()", start)
        if anchor < 0 or anchor > nxt:
            print(f"  no sandbox-modifier anchor in {path.name}: {fc}")
            continue
        line_end = raw.find("\n", anchor) + 1
        ins = "      +modifier:\n        $ai_scenario_focus_boost()\n"
        raw = raw[:line_end] + ins + raw[line_end:]
        added += 1
    path.write_text(raw, encoding="utf-8")
    return added


def main() -> None:
    total = 0
    for name, focuses in SPLICES.items():
        n = add_boosts(NF / name, focuses)
        total += n
        print(f"{name}: +{n}")
    print(f"total boosts added: {total}")


if __name__ == "__main__":
    main()
