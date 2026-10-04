# 33 - soviet_west peak still times out: the gate focus is never completed

Status: needs-triage
Type: bug
Blocked by: none

## Problem

The 2026-10-04 observer session (clean build, random, `pin=0`) picked
`sc=4 soviet_west` variant A and ran 1936.1-1942.1. The arc peaked on the
`t=36` fallback and derailed:

```
1936.2  SOV sc_focus SOV_the_path_of_marxism_leninism  sc=4 phase=0 t=1
1937.1  HAI sc_phase crises                             sc=4 phase=1 t=12
1937.1  SOV sc_crisis soviet_west_crisis                sc=4 phase=1 t=12
1939.1  SOV sc_phase peak                               sc=4 phase=2 t=36
1939.1  EST sc_crisis soviet_west_ult_2_defy            sc=4 phase=2 t=36
1939.1  LAT sc_crisis soviet_west_ult_3_submit          sc=4 phase=2 t=36
1939.1  LIT sc_crisis soviet_west_ult_5_defy            sc=4 phase=2 t=36
1940.1  HAI sc_derail peak_timeout                      sc=4 phase=3 t=48
```

Two facts:

1. Peak fired at `t=36`, the fallback, so the variant-A gate
   `SOV_control_scandinavia` was not complete at `t=24`.
2. `sc_focus` logged exactly **one** plan focus all session
   (`SOV_the_path_of_marxism_leninism`); SOV never completed
   `SOV_the_comintern`, the shared trunk of both variants, let alone the
   baltic chain.

`error.log` has zero scenario-attributable lines, so the build is clean; this
is behaviour, not a parse defect.

## Context

Issue 30 removed the ex-`sov_south` Middle East boosts so the fork is neutral
(`SOV_baltic_security` plain x5, branches variant-gated), and issue 31 gave
every plan focus an `sc_focus` line. Neither changed the outcome. In the
earlier 2026-10-04 mixed-build session SOV did walk the trunk and then the
Middle East branch (four `sc_focus` lines), so the AI is not simply failing to
pick focuses; it is choosing focuses outside the plan, or the baltic chain is
unavailable to it.

## Diagnosis plan

- Establish which focuses SOV actually completes. `sc_focus` only sees the
  plan set; add a debug path (a flag-gated log of every SOV focus completion,
  or read `completed_focus` from a lobby save) and rerun.
- Check whether `SOV_baltic_security` is available under the vanilla paranoia
  system at the relevant date (`SOV_paranoia_system_active_flag`), and whether
  the chain's vanilla `available` / `bypass` conditions block the boosted
  priority.
- Confirm the boost weight actually applies in play (`is_live_scenario_aggressor`
  is true for SOV, so the x5 should land); if it does, the branch weights still
  lose to the AI's other priorities.

## Acceptance

- [ ] The completed-focus set for SOV in a `soviet_west` session is recorded
      and quoted.
- [ ] The root cause is named: unavailable chain, losing weights, or a wrong
      gate.
- [ ] Either the AI reliably completes the peak gate before `t=24`, or the
      arc's ladder gate / boost is redesigned so the peak is reached.

## Out of scope

- The peak-timeout arm itself, which fired as designed.
- Pinned-run acceptance on issue 29.

## Session evidence

`logs/sandbox_extract.txt`, 292 `#sandbox` lines, 1936.1-1942.1. `sc_variant`
present for both arcs (slot-4 wiring works). Repeated repick to `nazi_germany`
at `t=48` with no `none_eligible` (see issue 32).
