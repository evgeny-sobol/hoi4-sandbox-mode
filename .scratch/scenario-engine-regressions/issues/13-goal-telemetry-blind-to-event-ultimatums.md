# 13 - Goal telemetry is blind to event-driven ultimatums

Status: needs-triage
Type: bug
Blocked by: none

## Problem

`sc_goal` and `sc_justify` sample the wargoal path: `has_wargoal_against(TARGET)` in the monthly
s7 telemetry, and the justify pulse hook for `sc_justify`. But the historical arcs do not use
wargoals. Their war focuses send a `country_event` ultimatum instead, and the war follows from the
event options.

Evidence from the third `_sandbox` session (942 lines, 1936.1 - 1942.6), where the `axis` arc
ignited successfully:

```
1939.4  GER sc_focus GER_reassert_eastern_claims  sc=1 phase=2
1939.6  GER sc_focus GER_demand_sudetenland       sc=1 phase=2
1939.8  GER sc_focus GER_danzig_or_war            sc=1 phase=2
1939.8  GER sc_ignite axis_war + sc_success + sc_end
```

`sc_goal` = 0, `sc_justify` = 0, `sc_goal_end` = 0 for the whole session, while the arc went from
peak to ignition through the event path.

The focus that does the work carries no wargoal:

- `GER_danzig_or_war`: `will_lead_to_war_with = POL`, then a `completion_reward` that sends
  `POL = { country_event = { id = germany.86 } }`. No `create_wargoal`.
- `GER_demand_sudetenland`: same shape, `will_lead_to_war_with` plus an event.
- `GER_war_with_france` is the exception: it does call `create_wargoal` twice.

`germany.86` offers the target two options; the war follows from whichever it picks (the AI takes
the war option most of the time).

## Why it matters

The acceptance checklist reads `sc_goal` / `sc_justify` / `sc_goal_end` as the proof that the arc
is pressing its targets. On every arc that wars through an ultimatum event, those lines are silent
even when the arc is working perfectly, so the telemetry cannot distinguish "the arc is applying
pressure" from "the arc is inert". This is what made issue 08 look like an AI failure.

## Open question

What should the goal telemetry sample so it covers both paths? Candidates:

1. Sample the arc's own pressure instead of the wargoal: the `sc_crisis` ultimatum events already
   log which option the target picked, so a per-target "ultimatum issued / submitted / defied"
   rollup may be enough.
2. Keep `sc_goal` as the wargoal probe and add a second probe for the event path (e.g. a flag set
   by the ultimatum event, sampled monthly).
3. Treat this as documentation only: state in the GDD that `sc_goal` covers the wargoal path and
   the `sc_crisis` lines cover the ultimatum path.

Needs a maintainer decision before an agent picks it up.

## Related

- Issue 08 was rescoped into this ticket; its "peak never converts" claim did not reproduce.
- `docs/gdd/Scenarios.md` "Hooks and telemetry" describes the s7 package without noting that
  `sc_goal` is wargoal-only.

## Comments
