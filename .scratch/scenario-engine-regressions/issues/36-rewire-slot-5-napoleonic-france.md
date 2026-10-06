# 36 - Rewire slot 5 from eng_soviet to napoleonic_france

Status: resolved
Type: feature
Blocked by: none

## What to build

Move scenario slot 5 from the dormant `eng_soviet` (ENG) to `napoleonic_france`
(FRA), mirroring the issue-29 slot-4 rewire.

## What changed

- Spec `docs/scenarios/napoleonic_france_scenario.toml` (renamed to match its
  id): number 5, aggressor FRA, key `napoleonic_france`, targets a = BEL/HOL/LUX,
  ladder 14/30, `invite_event`, `require = [same_ideology, same_continent]`,
  path `[FRA_proclaim_the_third_empire, FRA_army_reform]`, and a top-level
  `suppress` list.
- `suppress` lost `FRA_defensive_focus`: it is a boosted ancestor of the
  army-reform branch, so the builder rejected it as both boosted and suppressed.
- Pin trigger `sandbox_scenario_pin_is_napoleonic_france`, rule option
  `napoleonic_france` + l10n.
- Events `sandbox_napoleonic_france.1/.2/.3/.5` (crises, ultimatums to
  BEL/HOL/LUX) and `.4` (join), each defy granting FRA a casus belli (issue 34
  pattern). `eng_soviet` events and l10n removed; dispatcher delegates slot 5 to
  the generated helpers; success/ignite/civil-war/derail name FRA; arc hooks
  regenerated (`FRA | BEL | HOL | LUX`).

## Verification: PASSED (observer run, 2026-10-05)

Pinned run (pin forced in code, reverted), 1936.1-1940.1:

```
1936.1  FRA sc_seed t0=BEL t1=HOL t2=LUX sc=5 pin=1
1936.1  HAI sc_pick napoleonic_france / sc_variant a
1937.3  HAI sc_phase crises (t=14)
1937.3  FRA sc_crisis napoleonic_france_crisis
1939.7  FRA sc_phase peak (t=42)
1939.7  BEL/HOL/LUX sc_crisis ..._ult_2/3/5_defy
1939.7  FRA sc_ignite sc_success sc_end napoleonic_france_war
```

`error.log` has zero scenario lines; builder `--check` in sync; guards green.

## Note

The peak entered at `t=42`, the `peak_at_month = 30` fallback: the gate
`FRA_army_reform` sits behind a deep FRA prerequisite chain and is not complete
by month 30. The arc still converts (all three targets defied, the casus belli
ignites the war). If an earlier peak is wanted, raise `peak_at_month` or pick a
shallower gate.

## Out of scope

- `usa_warplan` (slot 6) stays hand-wired and spec-less.
- The r56 port.
