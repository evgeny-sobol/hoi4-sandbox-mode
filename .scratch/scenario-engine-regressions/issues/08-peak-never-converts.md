# 08 - Peak never converts: no wargoal, no justify, no boosted focus for the aggressor

Status: needs-triage
Type: bug
Blocked by: none

## Problem

Across the whole session (72 months, three arcs, two of them held at peak for a full year with a
x5-boosted war focus) the aggressor produced **zero** justify/goal activity:

```
sc_goal     0
sc_justify  0
sc_goal_end 0
```

`sc_power` fired 182 times in the same window, so `sandbox_scenario_s7_telemetry()` is running
and the missing `sc_goal` is a real absence of a wargoal, not dead telemetry.

`docs/gdd/Scenarios.md:108-117` (Acceptance checklist) expects `sc_goal`, `sc_justify` and
`sc_goal_end` lines when a scenario runs, and ignition when a war fires between declared enemies.

## Session evidence

Arc 2 (`sov_south`), aggressor SOV, at peak for the full 12 months:

```
HAI sc_phase peak sc=2 phase=2 t=24
SOV sc_actor gate=1 agg=1 tgt=0 enemies=6 sc=2 phase=2 t=25 .. t=35
HAI sc_derail peak_timeout sc=2 phase=3 t=36
```

Arc 1 (`axis`), aggressor GER, repicked at `t=36`, at peak from `t=37` to `t=49`:

```
GER sc_actor gate=1 agg=1 tgt=0 enemies=4 sc=1 phase=1 t=37
HAI sc_phase peak sc=1 phase=2 t=37
CZE sc_target open sc=1 phase=2 t=37
POL sc_target open sc=1 phase=2 t=37
CZE sc_crisis axis_ult_2_submit sc=1 phase=2 t=37
POL sc_crisis axis_ult_3_defy sc=1 phase=2 t=37
HAI sc_derail peak_timeout sc=1 phase=3 t=49
```

Both targets logged `sc_target open` (not `at_war`, not `in_faction`) for the whole year, so no
war was ever declared in either direction.

The one ignition in the session came from a war that already existed before the arc was picked,
not from the arc's own pressure:

```
JAP sc_seed t0=CHI t1=PHI sc=3 phase=0 t=49
JAP sc_ignite japanese_war sc=3 phase=3 t=50   # Sino-Japanese war already running
```

## Not a wiring gap

The levers the GDD names are compiled and live:

- `ai_scenario_focus_boost` (x5) is spliced onto 63 focuses and evaluates
  `is_live_scenario_aggressor = yes` - and the gate is now healthy (issue 04 fix; `agg=1`).
- The F1 betrayal exemption is compiled into the war focuses:
  `CZE = { is_scenario_enemy_of_PREV = no }` (44 occurrences in `germany.txt`).
- The aggressor is seeded as a 65-intensity national rival of each target.

So the boost applies, the exemption applies, and the AI still does not walk the war branch.

## Aggressor focus completions

`sc_focus` never fired for GER or SOV at all in 72 months - not one of the 16 GER / 5 SOV boosted
focuses completed. This is the long-standing "Japan completed zero war focuses" observation from
`docs/gdd/Scenarios.md:123-126`, still open after the boost was repaired.

## Open question for triage

At least one of the two failed aggressors was AI-controlled (arc 1 and arc 2 cannot both be the
player), so this is not explained by a human player ignoring the branch. But the log has no
player marker, so the exact player tag is unknown. Confirming it would remove the last
alternative explanation.

## Related

- `docs/gdd/Scenarios.md:123-126` already records this as an open item ("a peak that outlives
  the ladder is still undetected"). The new evidence is stronger: the peak is not merely
  undetected, the conversion never starts.
- Issue 09 (symmetric seeding) is adjacent but distinct: it would make a target-initiated war
  fail to ignite. Here no war was declared at all.

## Comments
