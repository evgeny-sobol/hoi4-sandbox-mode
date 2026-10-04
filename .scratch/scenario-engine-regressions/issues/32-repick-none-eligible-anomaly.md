# 32 - Repick reports none_eligible while every aggressor is alive

Status: resolved
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

- [x] `sandbox_scenario_maybe_repick()` logs, under the `sandbox_log_scenarios`
      gate, the eligible count plus the `country_exists` result for GER, ITA,
      JAP and SOV and the `derailed_arcs` contents at the moment of the branch.
- [x] One random `_sandbox` session on a clean build either reproduces
      `none_eligible` with the detail line or shows the arc repicking normally;
      the log is quoted into this ticket.
- [x] If reproduced, a follow-up root cause and fix are filed. (Not
      reproduced.)

## Result: NOT REPRODUCED on a clean build (2026-10-04)

Observer session on the rebuilt `_sandbox`, random `pin=0`, 1936.1-1942.1.
After the arc derailed at `t=48` the repick was healthy:

```
1940.1  HAI sc_derail peak_timeout  sc=4 phase=3 pin=0 t=48
1940.1  HAI sc_end    peak_timeout  sc=4 phase=3 pin=0 t=48
1940.1  GER sc_seed t0=FRA t1=ENG    sc=1 phase=0 t=48
1940.1  HAI sc_repick nazi_germany   sc=1 phase=0 t=48
1940.1  HAI sc_pick   nazi_germany   sc=1 phase=0 t=48
```

`sc_variant` fired for both arcs and `error.log` had zero scenario lines. The
only `none_eligible` observation stands on the mixed build (caveat above); one
clean session is not proof, but it points away from a live defect. The
`sc_repick_detail` line stays in the build and fires only on `none_eligible`,
so a future random derail that empties `eligible` will capture the inputs.

## Out of scope

- The soviet_west path gate that caused the derail (issue 33).
- Pinned sessions: a repick only runs when `sandbox_scenario_pin == 0`.
