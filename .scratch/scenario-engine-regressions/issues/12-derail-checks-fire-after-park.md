# 12 - Derail checks keep firing after an arc is already parked at phase 3

Status: needs-triage
Type: bug
Blocked by: none

## Problem

The derail dispatcher never guards its arity checks on the current phase. After `peak_timeout`
parks an arc at `phase = 3`, the next monthly ticks run the same check again and emit a second
`sc_derail` + `sc_end` every month, forever, even though the arc is already dead.

`common/scripted_effects/99_sandbox_scenarios.hsl`:

```hsl
978  sandbox_scenario_check_derail():
979    phase_before = global.sandbox_scenario_phase
980    sandbox_scenario_check_civil_war_derail()
981    $sandbox_check_peak_timeout()
982    if global.sandbox_scenario == 1:
983      if not country_exists(GER):
984        global.&sandbox_scenario_phase = 3
985        $sandbox_log_sc(sc_derail, ger_gone)
986        $sandbox_log_sc(sc_end, ger_gone)
...
993        $sandbox_check_targets_derail2(GER, CZE, POL)   # <- no phase guard
```

`$sandbox_check_peak_timeout` (macros.hml:637) is itself phase-aware (`if phase == 2 ...`), and
the target-derail macros are not. The tail reacts to *post-derail game state*: once the arc is
parked, the targets have usually been annexed or turned into subjects/faction members, so the
`elif` branch of `$sandbox_check_targets_derail*` is true on every subsequent tick.

Compare `sandbox_scenario_tick()` (line 233), which *does* guard the ladder rungs with
`global.sandbox_scenario_phase == 0` / `== 1`, and the flush at line 1066:

```hsl
1066    if phase_before < 3 and global.sandbox_scenario_phase == 3:
1067      sandbox_scenario_maybe_repick()
```

The `phase_before < 3` guard here is exactly the missing one, but it only protects the repick,
not the derail checks above it.

## Session evidence (`_sandbox`, 1936.1 - 1942.6)

The `axis` arc (sc=1, GER vs CZE/POL) ignited successfully on 1939.8 and logged its own end:

```
2:00, 31 August, 1939 GER sc_ignite axis_war sc=1 phase=3 pin=0 t=43
2:00, 31 August, 1939 GER sc_success axis_war sc=1 phase=3 pin=0 t=43
2:00, 31 August, 1939 GER sc_end axis_war sc=1 phase=3 pin=0 t=43
```

Almost three years later the host keeps re-derailing the same dead arc every month:

```
1:00, 1 May, 1942   HAI sc_derail targets_neutralized sc=1 phase=3 pin=0 t=76
1:00, 1 May, 1942   HAI sc_end   targets_neutralized sc=1 phase=3 pin=0 t=76
1:00, 1 June, 1942  HAI sc_derail targets_neutralized sc=1 phase=3 pin=0 t=76
1:00, 1 June, 1942  HAI sc_end   targets_neutralized sc=1 phase=3 pin=0 t=76
```

`sc_derail` / `sc_end` totals are 3 / 4 rather than the expected 1 / 1 for a single successful
arc: two of the four `sc_end` lines are this phantom repeat. The `sc_target` lines stop after
ignition (correct) but `sc_derail` does not.

## Why it matters

- Log noise: a parked arc keeps writing two lines a month forever, drowning the rest of the
  session and making "how did this arc end" unreadable.
- It is a symptom of the missing guard in every `elif`/`else` derail arm at
  `99_sandbox_scenarios.hsl:982-1065`; a future arm added there will inherit it.

## Fix sketch

Guard the whole dispatcher body on the pre-tick phase, matching the repick guard:

```hsl
  sandbox_scenario_check_derail():
    if global.sandbox_scenario_phase >= 3:
      return              # or wrap the body in `if ... < 3:`
    phase_before = global.sandbox_scenario_phase
    ...
```

or add `global.sandbox_scenario_phase < 3` to each per-arc `if`/`elif`, as
`sandbox_scenario_check_civil_war_derail()` already does at line 955.

This file is per-mod (`common/scripted_effects/99_sandbox_scenarios.hsl`), so the same fix must
be applied in `_sandbox` and `_sandbox-r56` (r56 line 3183).

## GDD anchors

- `docs/gdd/Scenarios.md:78-81` - "Derail parks a dead arc at phase 3 ... On random a derail
  repicks". One derail per arc, not one per month.

## Comments
