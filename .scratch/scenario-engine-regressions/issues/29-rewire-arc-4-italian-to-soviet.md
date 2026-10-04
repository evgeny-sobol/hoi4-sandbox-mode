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

- [ ] A pinned `soviet_west` session logs `sc_seed`/`sc_pick` for slot 4
      with the spec's targets per variant (needs a game run).
- [ ] The arc runs the ladder to peak: crises event plus one submit/defy
      `sc_crisis` per declared target, both variants including the
      single-tag LIT ultimatum (needs a game run).
- [ ] Removing SOV parks the arc with the aggressor reason (needs a game
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
