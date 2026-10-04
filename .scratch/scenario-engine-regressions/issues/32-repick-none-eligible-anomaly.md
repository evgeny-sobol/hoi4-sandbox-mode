# 32 - Repick reports none_eligible while every aggressor is alive

Status: needs-info
Type: bug
Blocked by: none

## What to build

Instrument `sandbox_scenario_maybe_repick()` so a `none_eligible` repick
records the eligible count and each `country_exists` test, then explain the
2026-10-04 observation with a session.

## Problem

The 2026-10-04 `_sandbox` session (random, `sc=4 soviet_west`) derailed the arc
at `t=48` (1940.01) and logged:

```
1940.1.1  HAI sc_derail peak_timeout  sc=4 phase=3 pin=0 t=48
1940.1.1  HAI sc_end    peak_timeout  sc=4 phase=3 pin=0 t=48
1940.1.1  HAI sc_repick none_eligible sc=4 phase=3 pin=0 t=48
```

The same date's `history_dump/47.txt` has `GER`, `ITA`, `JAP` and `SOV` all
alive, and `sandbox_scenario_maybe_repick()` adds each to `eligible[]` on
`country_exists(<tag>)` and membership in `derailed_arcs[]` alone. So `eligible`
should have held `{1,2,3}` and the log should not say `none_eligible`. The code
and the dump disagree; the cause is not visible from reading.

Caveat: the session ran on a mixed build (compiled `game_rules/*.txt` post-dated
the run; see the pin-validation errors in `error.log`), so the running
`maybe_repick` may differ from the git tree. Re-test on a clean build first.

## Acceptance

- [ ] `sandbox_scenario_maybe_repick()` logs, under the `sandbox_log_scenarios`
      gate, the eligible count plus the `country_exists` result for GER, ITA,
      JAP and SOV and the `derailed_arcs` contents at the moment of the branch.
- [ ] One random `_sandbox` session on a clean build either reproduces
      `none_eligible` with the detail line or shows the arc repicking normally;
      the log is quoted into this ticket.
- [ ] If reproduced, a follow-up root cause and fix are filed.

## Out of scope

- The peak-timeout itself (issue 30 owns the arc-4 cause).
- Pinned sessions: a repick only runs when `sandbox_scenario_pin == 0`.
