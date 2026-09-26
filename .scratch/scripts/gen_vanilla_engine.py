#!/usr/bin/env python3
"""Generate the vanilla (_sandbox) scenario engine from the arc table.

Six arcs (one per major; Habsburg excluded), all historical (no flip gates):
  1 GER Axis        A: CZE,POL        B: FRA,ENG
  2 SOV SovietSouth A: TUR,IRQ,PER    B: PAK,RAJ,AFG
  3 JAP Japanese    A: CHI,PHI        B: BRM,INS,MAL
  4 ITA Italian     A: YUG,GRE        B: FRA,ENG
  5 ENG Anti-Soviet A: SOV            B: (same)
  6 USA WarPlan     A: JAP            B: ENG,CAN
  7 gap (FRANCE excluded: not content-portable)

Same file paths/names as the Rt56 overlay; only ids and pool composition differ.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCEN = ROOT / "common" / "scripted_effects" / "99_sandbox_scenarios.hsl"

# id -> dict(agg, ns, label, A, B)
ARCS = {
    1: dict(agg="GER", ns="axis", label="axis_war", A=["CZE", "POL"], B=["FRA", "ENG"]),
    2: dict(agg="SOV", ns="sov_south", label="sov_south_war", A=["TUR", "IRQ", "PER"], B=["PAK", "RAJ", "AFG"]),
    3: dict(agg="JAP", ns="japanese", label="japanese_war", A=["CHI", "PHI"], B=["BRM", "INS", "MAL"]),
    4: dict(agg="ITA", ns="italian", label="italian_war", A=["YUG", "GRE"], B=["FRA", "ENG"]),
    5: dict(agg="ENG", ns="eng_soviet", label="eng_soviet_war", A=["SOV"], B=["SOV"]),
    6: dict(agg="USA", ns="usa_warplan", label="usa_warplan_war", A=["JAP"], B=["ENG", "CAN"]),
}


def set_targets() -> str:
    out = [
        "# Target variants for the active arc (docs/gdd/Scenarios Catalog.md). HSL",
        "# cannot hold tags in variables, so the chosen pair is written into the",
        "# persistent sandbox_targets[] array. Variant A is the historical default.",
        "sandbox_set_targets():",
        "  global.&sandbox_targets[].clear()",
    ]
    for sid, a in ARCS.items():
        out.append(f"  if global.sandbox_scenario == {sid}:")
        out.append("    if global.sandbox_target_variant == a:")
        for t in a["A"]:
            out.append(f"      global.&sandbox_targets[].add({t})")
        out.append("    else:")
        for t in a["B"]:
            out.append(f"      global.&sandbox_targets[].add({t})")
    return "\n".join(out)


def pick() -> str:
    out = ["sandbox_pick_scenario():"]
    pins = {1: "axis", 2: "sov_south", 3: "japanese", 4: "italian", 5: "eng_soviet", 6: "usa_warplan"}
    for sid, key in pins.items():
        out.append(f"  if sandbox_scenario_pin_is_{key}():")
        out.append("    global.&sandbox_scenario_pin = 1")
        out.append(f"    global.&sandbox_scenario = {sid}")
    out.append("  else:")
    out.append("    # Random pick (default): equal roll over eligible arcs (aggressor exists).")
    out.append("    global.&sandbox_scenario_pin = 0")
    out.append("    eligible[].clear()")
    for sid, a in ARCS.items():
        out.append(f"    if country_exists({a['agg']}):")
        out.append(f"      eligible[].add({sid})")
    out.append("    if eligible[].size() == 0:")
    out.append("      global.&sandbox_scenario = 0")
    out.append("    else:")
    out.append("      eligible_max = eligible[].size() - 1")
    out.append("      roll = randi(0, eligible_max)")
    out.append("      global.&sandbox_scenario = eligible[roll]")
    out.append("  global.&sandbox_scenario_phase = 0")
    out.append("  global.&sandbox_scenario_civil_war_months = 0")
    out.append("  global.&sandbox_scenario_peak_months = 0")
    out.append("  variant_roll = randi(0, 1)")
    out.append("  if variant_roll == 0:")
    out.append("    global.&sandbox_target_variant = a")
    out.append("  else:")
    out.append("    global.&sandbox_target_variant = b")
    out.append("  sandbox_set_targets()")
    out.append("  sandbox_seed_actors()")
    for sid, a in ARCS.items():
        out.append(f"  if global.sandbox_scenario == {sid}:")
        out.append(f"    $sandbox_log_sc(sc_pick, {a['ns']})")
    out.append("  $sandbox_log_sc(sc_phase, smolder)")
    out.append("  sandbox_scenario_log_variant()")
    return "\n".join(out)


def log_variant() -> str:
    return "\n".join([
        "# docs/gdd/Scenarios.md \"Hooks and telemetry\": the A/B roll is logged",
        "# as its own line so a session's target set reads without digging.",
        "sandbox_scenario_log_variant():",
        "  if global.sandbox_target_variant == a:",
        "    $sandbox_log_sc(sc_variant, a)",
        "  else:",
        "    $sandbox_log_sc(sc_variant, b)",
    ])


def repick() -> str:
    out = [
        "# docs/gdd/Scenarios.md \"Selection\": repick after a derail on random.",
        "sandbox_scenario_maybe_repick():",
        "  if global.sandbox_scenario_pin == 0:",
        "    global.&sandbox_derailed_arcs[].add(global.sandbox_scenario)",
        "    for every_country():",
        "      &scenario_enemies[].clear()",
        "    eligible[].clear()",
    ]
    for sid, a in ARCS.items():
        out.append(f"    if country_exists({a['agg']}) and {sid} not in global.sandbox_derailed_arcs[]:")
        out.append(f"      eligible[].add({sid})")
    out.append("    if eligible[].size() == 0:")
    out.append("      $sandbox_log_sc(sc_repick, none_eligible)")
    out.append("    else:")
    out.append("      global.&sandbox_scenario = eligible[0]")
    out.append("      global.&sandbox_scenario_phase = 0")
    out.append("      global.&sandbox_scenario_civil_war_months = 0")
    out.append("      global.&sandbox_scenario_peak_months = 0")
    out.append("      variant_roll = randi(0, 1)")
    out.append("      if variant_roll == 0:")
    out.append("        global.&sandbox_target_variant = a")
    out.append("      else:")
    out.append("        global.&sandbox_target_variant = b")
    out.append("      sandbox_set_targets()")
    out.append("      sandbox_seed_actors()")
    for sid, a in ARCS.items():
        out.append(f"      if global.sandbox_scenario == {sid}:")
        out.append(f"        $sandbox_log_sc(sc_repick, {a['ns']})")
        out.append(f"        $sandbox_log_sc(sc_pick, {a['ns']})")
    out.append("      $sandbox_log_sc(sc_phase, smolder)")
    out.append("      sandbox_scenario_log_variant()")
    return "\n".join(out)


def seed_actors() -> str:
    out = [
        "# Shared seed for the active arc (docs/gdd/Scenarios.md \"Levers\"). Seeds",
        "# the aggressor against its chosen sandbox_targets[] at 65 and records the",
        "# enemies symmetrically. THIS is the aggressor.",
        "sandbox_seed_actors():",
    ]
    for sid, a in ARCS.items():
        out.append(f"  if global.sandbox_scenario == {sid}:")
        out.append(f"    {a['agg']}:")
        out.append("      sandbox_seed_from_targets()")
    out.append("")
    out.append("# Runs in the aggressor's scope. Each live target slot is seeded as a")
    out.append("# rival and both sides record scenario_enemies[].")
    out.append("sandbox_seed_from_targets():")
    out.append("  add_war_support(0.10)")
    for i in range(3):
        out.append(f"  if sandbox_targets[{i}] != 0:")
        out.append(f"    var:sandbox_targets[{i}]:")
        out.append("      PREV:")
        out.append("        $sandbox_seed_rival(PREV, 65)")
        out.append("        &scenario_enemies[].add(PREV)")
    for i in range(3):
        out.append(f"  if sandbox_targets[{i}] != 0:")
        out.append(f"    var:sandbox_targets[{i}]:")
        out.append("      PREV:")
        out.append("        &scenario_enemies[].add(PREV)")
    out.append("  $sandbox_log_sc_seed()")
    return "\n".join(out)


def tick() -> str:
    out = [
        "# Monthly ladder tick (docs/gdd/Scenarios.md \"Lifecycle\"). Thresholds are",
        "# HAI months_elapsed: < 12 smolder, 12-23 crises, 24+ peak. A derail check",
        "# runs first; a parked arc goes quiet.",
        "sandbox_scenario_tick():",
        "  if global.sandbox_scenario == 0:",
        "    pass",
        "  else:",
        "    sandbox_scenario_check_ignite_by_war()",
        "    sandbox_scenario_check_derail()",
    ]
    for sid, a in ARCS.items():
        ns = a["ns"]
        out.append(f"  if global.sandbox_scenario == {sid} and global.sandbox_scenario_phase == 0 and months_elapsed >= 12:")
        out.append("    global.&sandbox_scenario_phase = 1")
        out.append("    $sandbox_log_sc(sc_phase, crises)")
        out.append(f"    sandbox_fire_{ns}_crises()")
        out.append(f"  elif global.sandbox_scenario == {sid} and global.sandbox_scenario_phase == 1 and months_elapsed >= 24:")
        out.append("    global.&sandbox_scenario_phase = 2")
        out.append("    $sandbox_log_sc(sc_phase, peak)")
        out.append(f"    sandbox_fire_{ns}_peak()")
    out.append("  sandbox_scenario_s7_telemetry()")
    return "\n".join(out)


def crises(a: dict) -> str:
    agg = a["agg"]
    ns = a["ns"]
    t0 = a["A"][0]
    return "\n".join([
        f"# Crises phase for {ns}: provocation lands on the aggressor's desk.",
        f"sandbox_fire_{ns}_crises():",
        f"  if global.sandbox_scenario == {next(k for k, v in ARCS.items() if v is a)} and global.sandbox_scenario_phase == 1:",
        f"    {agg}:",
        f"      if country_exists({t0}) and not {agg}->has_war_with({t0}):",
        f"        {agg}:",
        "          country_event:",
        f"            id(sandbox_{ns}.1)",
    ])


def peak(sid: int, a: dict) -> str:
    agg = a["agg"]
    ns = a["ns"]
    out = [
        f"# Peak phase for {ns}: ultimatums to the chosen targets, then join offers.",
        f"sandbox_fire_{ns}_peak():",
        f"  if global.sandbox_scenario == {sid} and global.sandbox_scenario_phase == 2:",
        "    if global.sandbox_target_variant == a:",
    ]

    def variant_block(tags: list[str], indent: str) -> list[str]:
        b = []
        for i, t in enumerate(tags):
            ev = i + 2
            b.append(f"{indent}if country_exists({t}):")
            b.append(f"{indent}  {t}:")
            b.append(f"{indent}    $sandbox_log_target_status({agg})")
            b.append(f"{indent}if country_exists({t}) and not {agg}->has_war_with({t}):")
            b.append(f"{indent}  {t}:")
            b.append(f"{indent}    country_event:")
            b.append(f"{indent}      id(sandbox_{ns}.{ev})")
        return b

    out += variant_block(a["A"], "      ")
    out.append("    else:")
    out += variant_block(a["B"], "      ")
    out.append(f"    {agg}:")
    out.append(f"      sandbox_select_{ns}_joiners()")
    return "\n".join(out)


def joiners(sid: int, a: dict) -> str:
    ns = a["ns"]
    num = max(len(a["A"]), len(a["B"])) + 2
    return "\n".join([
        f"# Join levers for {ns}: open-pool top-2 by scenario_join_scorer.",
        f"sandbox_select_{ns}_joiners():",
        "  sandbox_snapshot_join_industry()",
        "  get_sorted_scored_countries(scenario_join_scorer, scenario_join_candidates[], scenario_join_scores[])",
        "  if scenario_join_scores[0] > 0:",
        "    var:scenario_join_candidates[0]:",
        "      country_event:",
        f"        id(sandbox_{ns}.{num})",
        "      $sandbox_log_sc(sc_offer, invited)",
        "  if scenario_join_scores[1] > 0:",
        "    var:scenario_join_candidates[1]:",
        "      country_event:",
        f"        id(sandbox_{ns}.{num})",
        "      $sandbox_log_sc(sc_offer, invited)",
    ])


def join_helpers() -> str:
    return "\n".join([
        "# Shared join-2.0 helper: industry snapshot for the scorer.",
        "sandbox_snapshot_join_industry():",
        "  for every_country():",
        "    &scenario_join_industry = num_of_factories",
    ])


def s7() -> str:
    out = [
        "# s7 diagnostic (read-only): monthly strength + wargoal snapshot.",
        "sandbox_scenario_s7_telemetry():",
    ]
    for sid, a in ARCS.items():
        agg = a["agg"]
        out.append(f"  if global.sandbox_scenario == {sid} and global.sandbox_scenario_phase < 3:")
        out.append("    if global.sandbox_target_variant == a:")
        union = []
        for t in a["A"]:
            if t not in union:
                union.append(t)
        # aggressor power
        out.append("      " + agg + ":")
        out.append("        sc_div = num_divisions")
        out.append("        sc_fab = num_of_factories")
        out.append("        $sandbox_log_sc_power()")
        for t in union:
            out.append(f"      if country_exists({t}):")
            out.append(f"        {t}:")
            out.append("          sc_div = num_divisions")
            out.append("          sc_fab = num_of_factories")
            out.append("          $sandbox_log_sc_power()")
        out.append("      " + agg + ":")
        for t in union:
            out.append(f"        if has_wargoal_against({t}):")
            out.append(f"          $sandbox_log_sc(sc_goal, {agg.lower()}_on_{t.lower()})")
        out.append("    else:")
        unionB = []
        for t in a["B"]:
            if t not in unionB:
                unionB.append(t)
        out.append("      " + agg + ":")
        out.append("        sc_div = num_divisions")
        out.append("        sc_fab = num_of_factories")
        out.append("        $sandbox_log_sc_power()")
        for t in unionB:
            out.append(f"      if country_exists({t}):")
            out.append(f"        {t}:")
            out.append("          sc_div = num_divisions")
            out.append("          sc_fab = num_of_factories")
            out.append("          $sandbox_log_sc_power()")
        out.append("      " + agg + ":")
        for t in unionB:
            out.append(f"        if has_wargoal_against({t}):")
            out.append(f"          $sandbox_log_sc(sc_goal, {agg.lower()}_on_{t.lower()})")
    return "\n".join(out)


def success() -> str:
    out = ["sandbox_log_scenario_success():"]
    first = True
    for sid, a in ARCS.items():
        kw = "if" if first else "elif"
        first = False
        out.append(f"  {kw} global.sandbox_scenario == {sid}:")
        out.append(f"    $sandbox_log_sc(sc_ignite, {a['label']})")
        out.append(f"    $sandbox_log_sc(sc_success, {a['label']})")
        out.append(f"    $sandbox_log_sc(sc_end, {a['label']})")
    return "\n".join(out)


def ignite() -> str:
    return "\n".join([
        "# docs/gdd/Scenarios.md \"Lifecycle\": any war between declared scenario",
        "# enemies ignites the arc (symmetric). Two paths share the log table:",
        "# on_declare_war (direct) and the monthly ongoing-war sweep (indirect).",
        "sandbox_scenario_ignite():",
        "  if global.sandbox_scenario > 0 and global.sandbox_scenario_phase < 3 and FROM in &scenario_enemies[]:",
        "    global.&sandbox_scenario_phase = 3",
        "    sandbox_log_scenario_success()",
        "",
        "# Runs in the aggressor's scope (THIS = aggressor): fires when THIS is at",
        "# war with any chosen target.",
        "sandbox_ignite_if_at_war():",
    ] + sum([
        [
            f"  if global.sandbox_scenario_phase < 3 and sandbox_targets[{i}] != 0:",
            f"    var:sandbox_targets[{i}]:",
            "      PREV:",
            "        if has_war_with(PREV):",
            "          global.&sandbox_scenario_phase = 3",
            "          sandbox_log_scenario_success()",
        ]
        for i in range(4)
    ], []) + [
        "",
        "sandbox_scenario_check_ignite_by_war():",
        "  if global.sandbox_scenario > 0 and global.sandbox_scenario_phase < 3:",
    ] + sum([
        [
            ("    if" if i == 0 else "    elif") + f" global.sandbox_scenario == {sid}:",
            f"      {a['agg']}:",
            "        sandbox_ignite_if_at_war()",
        ]
        for i, (sid, a) in enumerate(ARCS.items())
    ], []))


def civil_war_derail() -> str:
    out = [
        "# docs/gdd/Scenarios.md \"Lifecycle\": an aggressor stuck in a civil war",
        "# cannot prosecute its arc, so the director derails after 12 months of it.",
        "sandbox_scenario_check_civil_war_derail():",
        "  if global.sandbox_scenario > 0 and global.sandbox_scenario_phase < 3:",
    ]
    for i, (sid, a) in enumerate(ARCS.items()):
        kw = "    if" if i == 0 else "    elif"
        out.append(f"{kw} global.sandbox_scenario == {sid}:")
        out.append(f"      {a['agg']}:")
        out.append("        $sandbox_check_aggressor_civil_war()")
    return "\n".join(out)


def derail() -> str:
    out = [
        "# docs/gdd/Scenarios.md \"Lifecycle\": derail dispatcher.",
        "sandbox_scenario_check_derail():",
        "  phase_before = global.sandbox_scenario_phase",
        "  sandbox_scenario_check_civil_war_derail()",
        "  $sandbox_check_peak_timeout()",
    ]
    for i, (sid, a) in enumerate(ARCS.items()):
        agg = a["agg"]
        na = len(a["A"])
        nb = len(a["B"])
        kw = "  if" if i == 0 else "  elif"
        out.append(f"{kw} global.sandbox_scenario == {sid}:")
        out.append(f"    if not country_exists({agg}):")
        out.append("      global.&sandbox_scenario_phase = 3")
        out.append(f"      $sandbox_log_sc(sc_derail, {agg.lower()}_gone)")
        out.append(f"      $sandbox_log_sc(sc_end, {agg.lower()}_gone)")
        out.append(f"    elif {agg}->has_capitulated():")
        out.append("      global.&sandbox_scenario_phase = 3")
        out.append(f"      $sandbox_log_sc(sc_derail, {agg.lower()}_capitulated)")
        out.append(f"      $sandbox_log_sc(sc_end, {agg.lower()}_capitulated)")
        out.append("    else:")
        out.append("      if global.sandbox_target_variant == a:")
        out.append(f"        $sandbox_check_targets_derail{na}({agg}, {', '.join(a['A'])})")
        out.append("      else:")
        out.append(f"        $sandbox_check_targets_derail{nb}({agg}, {', '.join(a['B'])})")
    out.append("  if phase_before < 3 and global.sandbox_scenario_phase == 3:")
    out.append("    sandbox_scenario_maybe_repick()")
    return "\n".join(out)


def header() -> str:
    return "\n".join([
        "# docs/gdd/Scenarios.md: director skeleton for the vanilla mod. Pick runs",
        "# once at on_startup in HAI scope; the ladder tick runs monthly.",
        "# State (globals, all 0 until picked):",
        "#   sandbox_scenario: 0 none, 1 axis, 2 sov_south, 3 japanese, 4 italian,",
        "#     5 eng_soviet, 6 usa_warplan (7 reserved: France is not content-portable)",
        "#   sandbox_scenario_phase: 0 smolder, 1 crises, 2 peak, 3 ended",
        "#   sandbox_scenario_pin: 0 random, 1 pinned to the picked arc",
        "#   sandbox_derailed_arcs[]: ids that derailed this session",
        "",
    ])


def main() -> None:
    parts = [
        header(),
        set_targets(), "",
        pick(), "",
        log_variant(), "",
        repick(), "",
        seed_actors(), "",
        tick(), "",
        join_helpers(), "",
    ]
    for sid, a in ARCS.items():
        parts += [crises(a), "", peak(sid, a), "", joiners(sid, a), ""]
    parts += [
        s7(), "",
        success(), "",
        ignite(), "",
        civil_war_derail(), "",
        derail(), "",
    ]
    SCEN.write_text("\n".join(parts), encoding="utf-8")
    lines = len(SCEN.read_text(encoding="utf-8").splitlines())
    print(f"wrote {SCEN.relative_to(ROOT)} ({lines} lines)")


if __name__ == "__main__":
    main()
