# 18 - r56 focus telemetry bypasses the scenario-actor gate

Status: resolved
Type: bug
Blocked by: none

## What to build

Rt56 focus telemetry must go through the gated wrapper like every other mod,
so a completed focus logs `sc_focus` only for the aggressor and its declared
targets. Today it calls the base writer directly, so any country's completion
appears in an arc's log.

## Problem

`v0.2.1` Rt56 session, arc 11 (SOV aggressor against TUR/IRQ/PER):

```
1936.4  USA sc_focus USA_suspend_the_presecution      sc=11 phase=0
1936.8  JAP sc_focus JAP_reinforce_the_beijing_garrison sc=11 phase=0
1937.10 USA sc_focus USA_us_ussr_economic_cooperation sc=11 phase=1
```

None of the three is a scenario actor. An unrelated country's focus pollutes
the arc's log, which is exactly what the gate exists to prevent
(`docs/gdd/Scenarios.md`, "Hooks and telemetry": per-actor lines are gated on
`is_scenario_actor`).

Cause: the Rt56 includes call `$sandbox_log_sc(sc_focus, ...)` while the
vanilla call sites use the gated macro `$sandbox_log_sc_focus(...)`. Counts:
vanilla 63 gated, 0 ungated; Rt56 86 ungated, 0 gated. The gated macro is
already defined in the shared `macros.hml` and the trigger exists in the
shared engine triggers, so only the call sites differ.

## Why it matters

A polluted log hides the real signal: a reader cannot tell an arc's own war
branch from a bystander's politics, and the s10 lesson (a dead boost must be
visible) is defeated the moment an unrelated `sc_focus` line looks like
progress.

## Acceptance

- [x] Every Rt56 `sc_focus` log line goes through `$sandbox_log_sc_focus`.
- [ ] An observer session with a non-actor major completing focuses logs no
      `sc_focus` line for it (needs a game run).
- [x] The aggressor and declared targets still log `sc_focus` when they
      complete a spliced focus (gate present in the call shape).
- [x] No `sc_focus` call site uses the base writer directly in either mod.

## Out of scope

- The misplaced-indent defect (issue 17); fixing the gate does not restore
  dropped splices and vice versa.
- The set of spliced focuses.

## Verification: PASSED (includes + compiled output + guard)

- All 86 ungated Rt56 calls swapped to `$sandbox_log_sc_focus(...)`: france
  16, germany 10, hungary 4, italy 11, japan 12, soviet 14, uk 10, usa 9.
  Both mods now show zero ungated calls (vanilla 63 gated, 0 ungated; Rt56
  86 gated, 0 ungated).
- Forced recompile of both mods clean. In the compiled focus files every
  `sc_focus` line sits behind `is_scenario_actor = yes`: vanilla 63/63, Rt56
  86/86.
- The shared guard `.scratch/scripts/check_focus_splices.py` now enforces
  both rules (tree-level splice, ungated call); negatives verified by hand.
- The observer half (a non-actor major logs nothing) needs the next session.
