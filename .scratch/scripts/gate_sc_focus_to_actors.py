#!/usr/bin/env python3
"""Gate sc_focus telemetry to scenario actors only.

`sc_focus` fired for every country completing any boosted focus, so a Japanese
or American line showed up in an Italian session. Replace the call with a
dedicated macro that first checks the completing country is the aggressor or a
declared target of the live arc.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NF = ROOT / "common" / "national_focus"
TRIG = ROOT / "common" / "scripted_triggers" / "99_sandbox_scenario_triggers.hsl"
MACROS = ROOT / "common" / "macros.hml"

OLD = "$sandbox_log_sc(sc_focus, "
NEW = "$sandbox_log_sc_focus("

TRIGGER = '''
# ROOT is a live actor of the current arc: the aggressor, or one of the
# declared targets. Gates per-actor telemetry (focus completions) so unrelated
# countries do not pollute an arc's log.
is_scenario_actor:
  is_sandbox_mode_on()
  global.sandbox_scenario > 0
  global.sandbox_scenario_phase < 3
  OR:
    is_live_scenario_aggressor
    THIS in global.sandbox_targets[]
'''

MACRO = '''
# Scenario-actor focus telemetry. Only the aggressor and the declared targets
# are logged; the factors for other countries are noise in a session log.
macro sandbox_log_sc_focus(_id_):
  if is_sandbox_mode_on() and has_global_flag(sandbox_log_scenarios):
    if is_scenario_actor():
      log("#sandbox [GetDateText] [THIS.GetTag] sc_focus _id_ sc=[?global.sandbox_scenario|.0] phase=[?global.sandbox_scenario_phase|.0] pin=[?global.sandbox_scenario_pin|.0] t=[?months_elapsed]")
'''


def main() -> None:
    # 1. trigger
    trig = TRIG.read_text(encoding="utf-8").rstrip("\n")
    if "is_scenario_actor:" in trig:
        print("trigger already present")
    else:
        TRIG.write_text(trig + "\n" + TRIGGER, encoding="utf-8")
        print("trigger added")

    # 2. macro
    mac = MACROS.read_text(encoding="utf-8").rstrip("\n")
    if "macro sandbox_log_sc_focus(" in mac:
        print("macro already present")
    else:
        MACROS.write_text(mac + "\n" + MACRO, encoding="utf-8")
        print("macro added")

    # 3. swap call sites
    total = 0
    for p in sorted(NF.glob("*.include")):
        t = p.read_text(encoding="utf-8")
        n = t.count(OLD)
        if n:
            p.write_text(t.replace(OLD, NEW), encoding="utf-8")
            total += n
        print(f"  {p.name}: {n} swapped")
    print(f"total swapped: {total}")


if __name__ == "__main__":
    main()
