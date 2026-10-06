# 16 - `sc_goal` stays silent while the aggressor actively justifies

Status: resolved
Type: bug
Blocked by: none

## What to build

`sc_goal` reports the aggressor's pressure on a target whenever it is actually
justifying, so a session where the arc presses a target through the wargoal path shows that in the
log instead of reading as inert.

## Problem

In the `_sandbox-r56` session the aggressor justified against Poland for two months and the arc
ignited, yet `sc_goal` produced nothing for the whole session:

```
1937.10.08 .. 1937.12.07   GER sc_justify ger_on_pol   x61
1938.2                     GER sc_ignite axis_war + sc_success + sc_end
1936.1 .. 1938.2           sc_goal = 0, sc_goal_end = 0
```

`sc_goal` samples `has_wargoal_against(<target>)` from the aggressor's scope once a month. The
aggressor here was *justifying* - the wargoal does not exist until the justification completes, and
the arc ignited before that happened. So the probe was silent precisely while the pressure was real.

This is a second, distinct cause of the same symptom issue 13 describes. Issue 13 covers arcs that
war through an event ultimatum and therefore never hold a wargoal at all; here the arc does use the
wargoal path, and the sample still misses it.

The blocking issue matters: in this session the declared second target's tag also drifted (Poland
became a civil-war fragment, logged as `D09`), so part of the silence may be `has_wargoal_against`
being asked about a tag that no longer resolves. Issue 14 settles the tag question first, after
which this ticket can tell a genuine sampling gap from a tag mismatch.

## Why it matters

`sc_goal` is one of the three lines the acceptance checklist reads to prove an arc is pressing its
targets. When it is silent through a successful ignition, the checklist cannot distinguish "the arc
applied no pressure" from "the sample missed the window", and the analyst has to reconstruct the
story from `sc_justify` alone.

## Acceptance

- [ ] A session where the aggressor justifies on a declared target produces `sc_goal` lines that
      cover the justification window, not only a completed wargoal.
- [ ] The line still means "the aggressor holds or is building a claim on this target"; a target
      the aggressor is not pressuring produces nothing.
- [ ] An arc that wars through an event ultimatum without any justification remains covered by
      whatever issue 13 settles; this ticket does not claim to cover that path.
- [ ] Both mods recompiled clean; no new `error.log` lines attributable to scenario files.

## Out of scope

- The event-ultimatum path, which is issue 13.
- The sampling cadence of the s7 package, which is issue 15.
- The tag-drift question, which issue 14 settles first.

## Verification: PASSED (static)

Code:
- Every s7 `sc_goal` guard now reads
  `has_wargoal_against(T) or is_justifying_wargoal_against(T)` (24 sites in
  `_sandbox`, 138 in `_sandbox-r56`); no plain `has_wargoal_against(T)` guard
  remains. A pair with neither a held wargoal nor an active justification still
  logs nothing, so the "no pressure -> no line" criterion holds by
  construction.
- `is_justifying_wargoal_against` is a vanilla country trigger (used in vanilla
  `common/ai_strategy/`), taken in the aggressor scope with the target tag as
  argument. The event-ultimatum path is untouched (issue 13).
- Issue 14's tag-drift code shipped alongside in the same files, so the block
  on it is cleared.

Compile: both mods recompile clean; generated `.txt` carry 24/138
`is_justifying_wargoal_against` occurrences.

Observer confirmation is deferred by maintainer decision: no `_sandbox` session
produced a justification, so the justification window could not be observed.
Accepted on code + compiler.
