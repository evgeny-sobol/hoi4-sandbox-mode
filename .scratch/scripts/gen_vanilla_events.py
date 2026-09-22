#!/usr/bin/env python3
"""Generate the vanilla scenario event files (docs/gdd/Scenarios.md).

Six arcs, same anatomy as the Rt56 overlay: a crisis event `.1`, one
ultimatum per target slot (`.2`, `.3`, ...), and a peak join offer `.4`.
Ultimatum options use the reference anatomy: submit 30% (war support -0.10,
aggressor +0.05) and defy 70% (+0.10, aggressor +0.05 and rivalry vs PREV).
Because an event is shared by both variant targets, rivalry uses PREV.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EVENTS = ROOT / "events"

ARCS = {
    "axis": dict(agg="GER", A=["CZE", "POL"], B=["FRA", "ENG"]),
    "sov_south": dict(agg="SOV", A=["TUR", "IRQ", "PER"], B=["PAK", "RAJ", "AFG"]),
    "japanese": dict(agg="JAP", A=["CHI", "PHI"], B=["BRM", "INS", "MAL"]),
    "italian": dict(agg="ITA", A=["YUG", "GRE"], B=["FRA", "ENG"]),
    "eng_soviet": dict(agg="ENG", A=["SOV"], B=["SOV"]),
    "usa_warplan": dict(agg="USA", A=["JAP"], B=["ENG", "CAN"]),
}


def ultimatum(agg: str, ns: str, num: int, tags: list[str]) -> str:
    trig = " | ".join(tags)
    return "\n".join([
        f"# Ultimatum {num} ({trig}).",
        "country_event:",
        f"  id(sandbox_{ns}.{num})",
        f"  title(sandbox_{ns}_{num}_t)",
        f"  desc(sandbox_{ns}_{num}_d)",
        "  picture(GFX_news_event_005)",
        "  is_triggered_only(yes)",
        "  trigger:",
        f"    tag({trig})",
        "  option:",
        f"    name(sandbox_{ns}_{num}_a)",
        "    ai_chance:",
        "      factor(30)",
        "    add_war_support(-0.10)",
        f"    {agg}:",
        "      add_war_support(0.05)",
        f"    $sandbox_log_sc(sc_crisis, {ns}_ult_{num}_submit)",
        "  option:",
        f"    name(sandbox_{ns}_{num}_b)",
        "    ai_chance:",
        "      factor(70)",
        "    add_war_support(0.10)",
        f"    {agg}:",
        "      add_war_support(0.05)",
        "      $sandbox_add_rivalry_vs(PREV, 15)",
        f"    $sandbox_log_sc(sc_crisis, {ns}_ult_{num}_defy)",
    ])


def crisis(ns: str, agg: str, t0: str) -> str:
    return "\n".join([
        f"# Crisis: provocation lands on the aggressor's desk.",
        "country_event:",
        f"  id(sandbox_{ns}.1)",
        f"  title(sandbox_{ns}_1_t)",
        f"  desc(sandbox_{ns}_1_d)",
        "  picture(GFX_news_event_002)",
        "  is_triggered_only(yes)",
        "  trigger:",
        f"    tag({agg})",
        "  option:",
        f"    name(sandbox_{ns}_1_a)",
        "    ai_chance:",
        "      factor(85)",
        f"    $sandbox_log_sc(sc_crisis, {ns}_crisis)",
        f"    $sandbox_add_rivalry_vs({t0}, 10)",
        "    add_war_support(0.05)",
        "  option:",
        f"    name(sandbox_{ns}_1_b)",
        "    ai_chance:",
        "      factor(15)",
    ])


def join(ns: str, agg: str, bloc: str, num: int) -> str:
    # No faction is formed. Making the aggressor a faction leader would lock it
    # out of its own war focuses, several of which require `is_in_faction = no`
    # (ITA_pact_of_steel, ITA_italy_first, GER_integrate_czechoslovakia,
    # JAP_sea_pressure_siam). Joiners get opinion plus mutual military access.
    return "\n".join([
        "# Peak phase: a top-2 open-pool candidate is offered a place in the bloc.",
        "# The exit from any old faction is Honor-free (one-shot skip flag, like a",
        "# released nation). No faction is created: see the note above.",
        "country_event:",
        f"  id(sandbox_{ns}.{num})",
        f"  title(sandbox_{ns}_{num}_t)",
        f"  desc(sandbox_{ns}_{num}_d)",
        "  picture(GFX_news_event_004)",
        "  is_triggered_only(yes)",
        "  trigger:",
        "    is_ai(yes)",
        f"    not is_in_faction_with({agg})",
        "  option:",
        f"    name(sandbox_{ns}_{num}_a)",
        "    ai_chance:",
        "      factor(90)",
        "    if is_in_faction(yes):",
        "      set_country_flag(sandbox_honor_skip_leave_faction)",
        "      leave_faction(yes)",
        f"    give_military_access({agg})",
        f"    {agg}:",
        "      give_military_access(PREV)",
        f"    $add_opinion_modifier({agg}, scenario_ally)",
        f"    $sandbox_log_sc(sc_join, {bloc}_joined)",
        "  option:",
        f"    name(sandbox_{ns}_{num}_b)",
        "    ai_chance:",
        "      factor(10)",
    ])


def main() -> None:
    for ns, a in ARCS.items():
        agg = a["agg"]
        n = max(len(a["A"]), len(a["B"]))
        parts = [
            f"# docs/gdd/Scenarios Catalog.md: arc events for {ns}.",
            f"add_namespace(sandbox_{ns})",
            "",
            crisis(ns, agg, a["A"][0]),
        ]
        for i in range(n):
            tags = []
            if i < len(a["A"]):
                tags.append(a["A"][i])
            if i < len(a["B"]) and a["B"][i] not in tags:
                tags.append(a["B"][i])
            parts += ["", ultimatum(agg, ns, i + 2, tags)]
        parts += ["", join(ns, agg, ns, n + 2)]
        path = EVENTS / f"99_sandbox_scenario_{ns}.hsl"
        path.write_text("\n".join(parts) + "\n", encoding="utf-8")
        print(f"wrote {path.name}")


if __name__ == "__main__":
    main()
