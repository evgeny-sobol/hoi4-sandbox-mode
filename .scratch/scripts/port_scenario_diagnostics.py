#!/usr/bin/env python3
"""Port scenario diagnostics from the Rt56 overlay into the vanilla mod.

Three edits, all mirroring the proven Rt56 forms:

1. F1: exempt declared scenario enemies from the betrayal weight penalty in
   `ai_betrayal_modifier_vs` (macros.hml).
2. sc_focus: splice `+ completion_reward` / sc_focus logging into every focus
   that already carries ai_scenario_focus_boost.
3. sc_justify + on_wargoal_expire: wire the wargoal hooks the vanilla mod was
   missing, using the vanilla arc/target table.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NF = ROOT / "common" / "national_focus"
MACROS = ROOT / "common" / "macros.hml"
ONACT = ROOT / "common" / "on_actions" / "99_sandbox_on_actions.hsl"

# focus id -> sc_focus label (label == focus id, as in Rt56)
FOCUS_IDS = {
    "germany.include": [
        "GER_remilitarize_the_rhineland", "GER_anschluss", "GER_demand_sudetenland",
        "GER_danzig_or_war", "GER_around_maginot", "GER_war_with_france",
    ],
    "italy.include": [
        "ITA_foreign_affairs", "ITA_ratify_the_stresa_front",
        "ITA_italys_destiny", "ITA_war_with_greece",
    ],
    "japan.include": [
        "JAP_occupy_siam", "JAP_strike_the_southern_road",
        "JAP_revisit_the_thirteen_demands", "JAP_reinforce_the_beijing_garrison",
    ],
    "soviet.include": ["SOV_preemptive_invasion_of_iran"],
    "uk.include": ["ENG_steady_as_she_goes", "ENG_embargo_ussr", "ENG_war_with_ussr"],
    "usa.include": [
        "USA_intervention_in_europe", "USA_war_plan_black",
        "USA_war_plan_orange", "USA_defense_of_the_pacific",
    ],
}

FOCUS_RE = re.compile(r"^  focus\[id\s*=\s*([A-Za-z0-9_]+)\]")


def add_sc_focus() -> None:
    for name, ids in FOCUS_IDS.items():
        path = NF / name
        lines = path.read_text(encoding="utf-8").split("\n")
        # block boundaries: header line index -> next header index
        starts: list[tuple[int, str]] = []
        for i, ln in enumerate(lines):
            m = FOCUS_RE.match(ln)
            if m:
                starts.append((i, m.group(1)))
        bounds = {fid: (i, starts[k + 1][0] if k + 1 < len(starts) else len(lines))
                  for k, (i, fid) in enumerate(starts)}
        inserts: list[tuple[int, str]] = []
        for fid in ids:
            if fid not in bounds:
                print(f"  WARN {name}: focus {fid} not found")
                continue
            _s, e = bounds[fid]
            # back up over trailing blank lines so the splice lands inside the block
            ins = e
            while ins > 0 and lines[ins - 1].strip() == "":
                ins -= 1
            if any("sc_focus" in ln for ln in lines[_s:e]):
                print(f"  skip {fid} (already spliced)")
                continue
            inserts.append((ins, fid))
        for ins, fid in sorted(inserts, reverse=True):
            lines[ins:ins] = [
                "    +completion_reward:",
                f"      $sandbox_log_sc(sc_focus, {fid})",
            ]
        path.write_text("\n".join(lines), encoding="utf-8")
        print(f"  {name}: sc_focus +{len(inserts)}")


def add_f1() -> None:
    text = MACROS.read_text(encoding="utf-8")
    old = (
        "macro ai_betrayal_modifier_vs(_tag_):\n"
        "  $ai_betrayal_modifier()\n"
        "  country_exists(_tag_)\n"
        "  _tag_->is_friend_of_PREV()\n"
    )
    new = (
        "macro ai_betrayal_modifier_vs(_tag_):\n"
        "  $ai_betrayal_modifier()\n"
        "  country_exists(_tag_)\n"
        "  _tag_->is_friend_of_PREV()\n"
        "  _tag_->is_scenario_enemy_of_PREV(no)\n"
    )
    if "_tag_->is_scenario_enemy_of_PREV(no)" in text:
        print("  macros.hml: F1 already present")
        return
    if old not in text:
        raise SystemExit("ABORT: ai_betrayal_modifier_vs anchor not found")
    MACROS.write_text(text.replace(old, new, 1), encoding="utf-8")
    print("  macros.hml: F1 exemption added")


# Vanilla arc table: (scenario id, aggressor, variant A targets, variant B targets)
ARCS = [
    (1, "GER", ["CZE", "POL"], ["FRA", "ENG"]),
    (2, "SOV", ["TUR", "IRQ", "PER"], ["PAK", "RAJ", "AFG"]),
    (3, "JAP", ["CHI", "PHI"], ["BRM", "INS", "MAL"]),
    (4, "ITA", ["YUG", "GRE"], ["FRA", "ENG"]),
    (5, "ENG", ["SOV"], ["SOV"]),
    (6, "USA", ["JAP"], ["ENG", "CAN"]),
]


def justify_block() -> str:
    out = [
        "        # s7 diagnostic (read-only): aggressor justifying on arc targets is",
        "        # otherwise silent (Honor drips only vs friends). Daily while active.",
    ]
    for sid, agg, ta, tb in ARCS:
        out.append(
            f"        if global.sandbox_scenario == {sid} and "
            f"global.sandbox_scenario_phase < 3 and tag({agg}):"
        )
        out.append("          if global.sandbox_target_variant == a:")
        for t in ta:
            out.append(f"            if FROM->tag({t}):")
            out.append(f"              $sandbox_log_sc(sc_justify, {agg.lower()}_on_{t.lower()})")
        out.append("          else:")
        for t in tb:
            out.append(f"            if FROM->tag({t}):")
            out.append(f"              $sandbox_log_sc(sc_justify, {agg.lower()}_on_{t.lower()})")
    return "\n".join(out)


def expire_block() -> str:
    out = [
        "  # s7 diagnostic (read-only): a held-then-unused wargoal is the last-step",
        "  # smoking gun. THIS-only: on_wargoal_expire scopes are undocumented.",
        "  on_wargoal_expire:",
        "    effect:",
        "      if global.sandbox_scenario_phase < 3:",
    ]
    for sid, agg, ta, tb in ARCS:
        out.append(f"        if global.sandbox_scenario == {sid}:")
        out.append("          if global.sandbox_target_variant == a:")
        out.append(f"            if tag({agg} | {' | '.join(ta)}):")
        out.append("              $sandbox_log_sc(sc_goal_end, goal_expired)")
        out.append("          else:")
        out.append(f"            if tag({agg} | {' | '.join(tb)}):")
        out.append("              $sandbox_log_sc(sc_goal_end, goal_expired)")
    return "\n".join(out)


def add_wargoal_hooks() -> None:
    text = ONACT.read_text(encoding="utf-8")
    changed = False

    if "sc_justify" not in text:
        anchor = (
            "  # ROOT = leaving country, FROM = faction leader\n"
            "  on_leave_faction:"
        )
        if anchor not in text:
            raise SystemExit("ABORT: on_leave_faction anchor not found")
        text = text.replace(
            anchor, justify_block() + "\n\n" + anchor, 1
        )
        print("  on_actions: sc_justify added")
        changed = True
    else:
        print("  on_actions: sc_justify already present")

    if "on_wargoal_expire" not in text:
        anchor = "  on_justifying_wargoal_pulse:"
        if anchor not in text:
            raise SystemExit("ABORT: on_justifying_wargoal_pulse anchor not found")
        text = text.replace(anchor, expire_block() + "\n\n" + anchor, 1)
        print("  on_actions: on_wargoal_expire added")
        changed = True
    else:
        print("  on_actions: on_wargoal_expire already present")

    if changed:
        ONACT.write_text(text, encoding="utf-8")


def main() -> None:
    print("sc_focus:")
    add_sc_focus()
    print("F1:")
    add_f1()
    print("wargoal hooks:")
    add_wargoal_hooks()


if __name__ == "__main__":
    main()
