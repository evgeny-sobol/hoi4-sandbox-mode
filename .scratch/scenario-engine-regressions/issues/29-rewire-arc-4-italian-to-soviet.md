# 29 - Rewire slot 4 from italian to soviet_west

Status: resolved
Type: feature
Blocked by: none

## Maintainer decision (2026-10-04)

`docs/scenarios/soviet_west_scenario.toml` replaces slot 4 (`italian`).
Targets A: EST, LAT, LIT; B: POL, ROM. Variant-B path takes the
`respect_baltic` fork side against variant A's `claims` side. Third
A-target gets its own ultimatum event (issue-20 rule).

## What to build

Move every hand-written arc-4 reference from `italian`/ITA to
`soviet_west`/SOV (spec -> generated helpers -> hand wiring), restore
slot-4 selection (removed by the arcs-4-6 disable), and author the
content: crises/peak/joiners funcs, `sandbox_soviet_west.1-5` events
(paired ultimatums EST|POL and LAT|ROM plus single-tag LIT for the third
A target, join event), 20 l10n keys, pin trigger, rule option. Retire the
`italian` trigger leftovers are none (already removed by the disable);
retire events, funcs and labels.

## Acceptance

- [x] A pinned `soviet_west` session logs `sc_seed`/`sc_pick` for slot 4
      with the spec's targets per variant (needs a game run).
- [x] The arc runs the ladder to peak: crises event plus one submit/defy
      `sc_crisis` per declared target, both variants including the
      single-tag LIT ultimatum (needs a game run).
- [x] Removing SOV parks the arc with the aggressor reason (needs a game
      run).
- [x] No `italian` telemetry, events, or l10n keys remain reachable; the
      retired files are deleted, not orphaned.
- [x] `build_scenario_catalog.py --check` clean, all shared guards green
      (the new if/else guard caught a real indent slip in review), both
      mods recompile clean, no new `error.log` lines from scenario files
      (compiled output clean; session check pending).

## Verification: PASSED (source + compiled output + guard)

- Dispatcher branches delegate to the eight generated helpers; selection
  (pin, eligible, repick filter) restored for slot 4 with SOV.
- New content plus `sandbox_soviet_west.1-5` events with 20 l10n keys; pin
  trigger (`sandbox_scenario_pin_is_soviet_west`), rule option and its
  l10n added; `italian` events file deleted (compiled orphan removed),
  funcs and 18 l10n keys retired.
- Forced recompile clean (293 files). The observer half needs the next
  session (pin `soviet_west`, both variants to peak).

## Out of scope

- Slots 1-3 and 5-6 (tickets 23-25, disable commit).
- Event balance; the s13 reference anatomy stands.
- R56 port; vanilla slot 4 only.

## Observer runs (2026-10-05): boxes 1-3 closed

Three pinned `_sandbox` observer runs, `error.log` zero scenario lines. The pin
was forced by a temporary `sandbox_scenario_pin = 1` / `sandbox_scenario = 4`
override (reverted) because the agent cannot use the lobby's Game Rules screen;
the variant was also forced for coverage (`pin=1` alone leaves the 50/50 roll).

Variant A (two runs rolled A; first quoted):

```
1936.1.1  SOV sc_seed t0=EST t1=LAT t2=LIT sc=4 phase=0 pin=1 t=0
1936.1.1  HAI sc_pick soviet_west              sc=4 phase=0 pin=1 t=0
1936.1.1  HAI sc_variant a                     sc=4 phase=0 pin=1 t=0
1937.1.1  SOV sc_phase crises                  sc=4 phase=1 pin=1 t=12
1939.1.1  SOV sc_phase peak                    sc=4 phase=2 pin=1 t=36
1939.1.1  EST sc_crisis soviet_west_ult_2_defy sc=4 phase=2 pin=1 t=36
1939.1.1  LAT sc_crisis soviet_west_ult_3_defy sc=4 phase=2 pin=1 t=36
1939.1.1  LIT sc_crisis soviet_west_ult_5_defy sc=4 phase=2 pin=1 t=36
1939.7.10 SOV sc_ignite sc_success sc_end      sc=4 phase=3 pin=1 t=42
```

Variant B (variant forced for coverage):

```
1936.1.1  SOV sc_seed t0=POL t1=ROM              sc=4 phase=0 pin=1 t=0
1936.1.1  HAI sc_variant b                       sc=4 phase=0 pin=1 t=0
1939.1.1  POL sc_crisis soviet_west_ult_2_submit sc=4 phase=2 pin=1 t=36
1939.1.1  ROM sc_crisis soviet_west_ult_3_defy   sc=4 phase=2 pin=1 t=36
```

Remove SOV (temporary annex on arc month 30):

```
1938.7.1  HAI sc_derail sov_gone sc=4 phase=3 pin=1 t=30
1938.7.1  HAI sc_end    sov_gone sc=4 phase=3 pin=1 t=30
```

Both variants reach peak and give every declared target a submit/defy outcome
(A: EST/LAT/LIT; B: POL/ROM), and removing the aggressor parks the arc with
`sov_gone`. The variant-A run also ignited (`soviet_west_war`).
