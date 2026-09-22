#!/usr/bin/env python3
"""Add a peak-timeout derail arm to the vanilla and Rt56 scenario engines.

An arc that reaches peak and does not ignite within PEAK_MONTHS derails with
reason `peak_timeout`; the existing derail dispatcher then repicks on random or
goes quiet when pinned. This closes the "hung arc" hole seen in observer
sessions (Italy sat at peak for six years; Japan for a full year).

Three edits per repo:
1. macros.hml: `sandbox_check_peak_timeout()` bumps the counter while the arc is
   at peak and derails past the threshold.
2. Derail dispatcher: call the new arm next to the civil-war check.
3. pick/repick: reset `sandbox_scenario_peak_months` with the existing counters.
"""
from __future__ import annotations

import re
from pathlib import Path

PEAK_MONTHS = 12

REPOS = [
    Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox"),
    Path(r"C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56"),
]

MACRO = f'''
# docs/gdd/Scenarios.md "Lifecycle": an arc that reaches peak and does not
# ignite within {PEAK_MONTHS} months is dead: the ladder holds at peak forever
# otherwise (an observer session sat there for six years). Derails with reason
# `peak_timeout`; the dispatcher then repicks on random or goes quiet when
# pinned. Counter resets at pick/repick.
macro sandbox_check_peak_timeout():
  if global.sandbox_scenario_phase == 2:
    global.&sandbox_scenario_peak_months += 1
    if global.sandbox_scenario_peak_months >= {PEAK_MONTHS}:
      global.&sandbox_scenario_phase = 3
      $sandbox_log_sc(sc_derail, peak_timeout)
      $sandbox_log_sc(sc_end, peak_timeout)
  else:
    global.&sandbox_scenario_peak_months = 0
'''


def patch_macros(root: Path) -> None:
    p = root / "common" / "macros.hml"
    t = p.read_text(encoding="utf-8")
    if "sandbox_check_peak_timeout" in t:
        print("    macros: already present")
        return
    anchor = "macro sandbox_check_aggressor_civil_war():"
    if anchor not in t:
        raise SystemExit("ABORT: civil-war macro anchor not found")
    t = t.replace(anchor, MACRO.strip() + "\n\n" + anchor, 1)
    p.write_text(t, encoding="utf-8")
    print("    macros: peak-timeout arm added")


def patch_derail(root: Path) -> None:
    p = root / "common" / "scripted_effects" / "99_sandbox_scenarios.hsl"
    t = p.read_text(encoding="utf-8")
    if "sandbox_check_peak_timeout()" in t:
        print("    derail: already wired")
        return
    anchor = "  sandbox_scenario_check_civil_war_derail()"
    if anchor not in t:
        raise SystemExit("ABORT: derail dispatcher anchor not found")
    t = t.replace(anchor, anchor + "\n  sandbox_check_peak_timeout()", 1)
    p.write_text(t, encoding="utf-8")
    print("    derail: wired")


def patch_resets(root: Path) -> None:
    p = root / "common" / "scripted_effects" / "99_sandbox_scenarios.hsl"
    t = p.read_text(encoding="utf-8")
    if "sandbox_scenario_peak_months = 0" in t:
        print("    resets: already present")
        return
    pat = re.compile(r"(?m)^([ \t]*)global\.&sandbox_scenario_civil_war_months = 0[ \t]*$")
    hits = pat.findall(t)
    if not hits:
        raise SystemExit("ABORT: no counter reset sites found")
    t = pat.sub(
        lambda m: f"{m.group(1)}global.&sandbox_scenario_civil_war_months = 0\n"
                  f"{m.group(1)}global.&sandbox_scenario_peak_months = 0",
        t,
    )
    p.write_text(t, encoding="utf-8")
    print(f"    resets: {len(hits)} site(s) patched")


def main() -> None:
    for root in REPOS:
        print(f"== {root.name} ==")
        if not (root / "common" / "macros.hml").exists():
            print("    SKIP: not a mod repo")
            continue
        patch_macros(root)
        patch_derail(root)
        patch_resets(root)


if __name__ == "__main__":
    main()
