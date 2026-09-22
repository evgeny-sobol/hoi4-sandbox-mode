#!/usr/bin/env python3
"""Extend the arc focus boosts to the full ancestor closure of each key focus.

The vanilla port boosted only the war leafs and one or two roots, so almost
every leaf sat behind an unboosted fork (a mutually-exclusive ideological gate
for Japan, an Africa path for Italy, and so on). The AI never commits to the
fork, so the leaf never becomes available and the boost does nothing (the
documented s10 lesson).

This widens the splice set: for each key focus it walks `prerequisite` blocks
transitively (AND groups plus OR alternatives, union of both) and boosts every
ancestor too. Idempotent: focuses already carrying the boost are skipped.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NF = ROOT / "common" / "national_focus"
GAME_NF = Path(r"C:\Games\Steam\steamapps\common\Hearts of Iron IV\common\national_focus")

# arc key focuses (the leaves the arcs actually rely on)
KEYS = {
    "germany": ["GER_remilitarize_the_rhineland", "GER_anschluss", "GER_demand_sudetenland",
                "GER_danzig_or_war", "GER_around_maginot", "GER_war_with_france"],
    "soviet": ["SOV_preemptive_invasion_of_iran"],
    "japan": ["JAP_reinforce_the_beijing_garrison", "JAP_strike_the_southern_road",
              "JAP_revisit_the_thirteen_demands", "JAP_occupy_siam"],
    "italy": ["ITA_italys_destiny", "ITA_war_with_greece",
              "ITA_foreign_affairs", "ITA_ratify_the_stresa_front"],
    "uk": ["ENG_war_with_ussr", "ENG_embargo_ussr", "ENG_steady_as_she_goes"],
    "usa": ["USA_war_plan_orange", "USA_war_plan_black",
            "USA_defense_of_the_pacific", "USA_intervention_in_europe"],
}

ID_RE = re.compile(r"id\s*=\s*([A-Za-z0-9_]+)")
FOCUSREF_RE = re.compile(r"focus\s*=\s*([A-Za-z0-9_]+)")


def focus_blocks(text: str):
    for m in re.finditer(r"(?m)^\t?focus\s*=\s*\{", text):
        i = text.index("{", m.start())
        depth, j = 0, i
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        yield text[i:j + 1]


def section(body: str, name: str) -> str:
    m = re.search(rf"(?m)^\s*{name}\s*=\s*\{{", body)
    if not m:
        return ""
    i = body.index("{", m.start())
    depth, j = 0, i
    while j < len(body):
        if body[j] == "{":
            depth += 1
        elif body[j] == "}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    return body[i:j + 1]


def parse(paths) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for p in paths:
        text = p.read_text(encoding="utf-8", errors="ignore")
        for b in focus_blocks(text):
            m = ID_RE.search(b)
            if m:
                graph[m.group(1)] = FOCUSREF_RE.findall(section(b, "prerequisite"))
    return graph


def closure(seeds: list[str], graph: dict[str, list[str]]) -> set[str]:
    seen: set[str] = set()
    frontier = list(seeds)
    while frontier:
        f = frontier.pop()
        if f in seen or f not in graph:
            continue
        seen.add(f)
        frontier += graph[f]
    return seen


def has_boost(block: str) -> bool:
    return "$ai_scenario_focus_boost()" in block


def add_boost(raw: str, fc: str) -> tuple[str, str]:
    start = raw.find(f"focus[id = {fc}]:")
    if start < 0:
        return raw, "miss"
    nxt = raw.find("\n  focus[id = ", start + 5)
    if nxt < 0:
        nxt = len(raw)
    block = raw[start:nxt]
    if has_boost(block):
        return raw, "have"
    anchor = raw.find("      $ai_sandbox_modifier()", start)
    if anchor < 0 or anchor > nxt:
        return raw, "noanchor"
    line_end = raw.find("\n", anchor) + 1
    ins = "      +modifier:\n        $ai_scenario_focus_boost()\n"
    return raw[:line_end] + ins + raw[line_end:], "added"


def main() -> None:
    for country, seeds in KEYS.items():
        graph = parse(GAME_NF.glob(f"{country}*.txt"))
        need = sorted(closure(seeds, graph))
        path = NF / f"{country}.include"
        if not path.exists():
            print(f"== {country}: no include at {path.name}")
            continue
        raw = path.read_text(encoding="utf-8")
        stats = {"added": 0, "have": 0, "miss": 0, "noanchor": 0}
        for fc in need:
            raw, st = add_boost(raw, fc)
            stats[st] += 1
        path.write_text(raw, encoding="utf-8")
        print(f"== {country}: closure={len(need)} added={stats['added']} "
              f"already={stats['have']} miss={stats['miss']} noanchor={stats['noanchor']}")


if __name__ == "__main__":
    main()
