# 07 - Arc ladder is global-time based, so a repicked arc compresses to two months

Status: needs-triage
Type: bug
Blocked by: none

## Problem

The ladder rungs are gated on `months_elapsed >= 12` / `>= 24`, and `months_elapsed` is a
per-country counter that runs from session start - it is not reset when an arc is picked or
repicked. A repicked arc therefore enters at whatever rung the session clock already reached.

`docs/gdd/Scenarios.md:45-54` defines the ladder **per arc**:

| Rung | Fires at | Releases |
|---|---|---|
| smolder | month 0 | seed only |
| crises | month 12 | crisis events |
| peak | month 24 | ultimatums to targets, join offers |

## Session evidence (`_sandbox`, 1936.1 - 1942.1, 72 months)

First arc, picked at `t=0` - on schedule:

```
HAI sc_phase smolder sc=2 phase=0 t=0
HAI sc_phase crises  sc=2 phase=1 t=12
HAI sc_phase peak    sc=2 phase=2 t=24
```

Repicked arc (`sov_south` derailed at `t=36`, repicked to `axis`) - ladder collapses:

```
HAI sc_repick axis    sc=1 phase=0 t=36
HAI sc_pick   axis    sc=1 phase=0 t=36
HAI sc_phase  smolder sc=1 phase=0 t=36
HAI sc_phase  crises  sc=1 phase=1 t=36   # same month: 36 >= 12
HAI sc_phase  peak    sc=1 phase=2 t=37   # next month: 37 >= 24
```

Third arc (`japanese`, repicked at `t=49` after `axis` derailed) - same collapse:

```
HAI sc_repick japanese sc=3 phase=0 t=49
HAI sc_phase  crises   sc=3 phase=1 t=49
JAP sc_ignite japanese_war sc=3 phase=3 t=50
```

So both repicked arcs spent zero months in smolder and one month in crises, instead of the 12 + 12
the GDD prescribes. Their crisis/ultimatum content fires in the same tick the arc is chosen, and
the join lever fires before any of it can be answered - the `axis` arc reached peak and derailed
on `peak_timeout` 12 months later with `sc_goal`/`sc_justify` at zero for the whole arc.

## Cause

`common/scripted_effects/99_sandbox_scenarios.hsl`:

```hsl
 239: if global.sandbox_scenario == 1 and global.sandbox_scenario_phase == 0 and months_elapsed >= 12:
 243: elif global.sandbox_scenario == 1 and global.sandbox_scenario_phase == 1 and months_elapsed >= 24:
```

`months_elapsed` is `&months_elapsed += 1` in `on_monthly` (`core/common/on_actions/99_sandbox_core_on_actions.hsl:69`)
and is only zeroed at country init, not at `sandbox_pick_scenario` / `sandbox_scenario_maybe_repick`
(they reset `sandbox_scenario_phase`, `sandbox_scenario_civil_war_months` and
`sandbox_scenario_peak_months`, but not the ladder clock).

## Suggested fix (needs a decision)

Add an arc-relative counter (e.g. `global.&sandbox_scenario_arc_months`) reset to 0 in
`sandbox_pick_scenario` and `sandbox_scenario_maybe_repick` and incremented in
`sandbox_scenario_tick`, then gate the rungs on that instead of `months_elapsed`. Note the
telemetry `t=` field deliberately reports `months_elapsed`, so the new counter should be logged
separately if the arc age is needed for acceptance reads.

The `t=` field is read in `docs/gdd/Scenarios.md:113-117`, so the GDD may need a note that the
ladder clock is arc-relative while `t=` is session-relative.

## Comments
