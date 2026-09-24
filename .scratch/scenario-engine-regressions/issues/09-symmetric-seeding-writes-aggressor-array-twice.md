# 09 - Symmetric seeding writes the aggressor's array twice; targets never get enemies

Status: needs-triage
Type: bug
Blocked by: none

## Problem

`sandbox_seed_from_targets` has two loops over `global.sandbox_targets[]`. The second is
commented as the symmetric side ("each target lists the aggressor"), but it uses the **same**
`PREV:` scoping as the first, so it writes the aggressor's own array a second time instead of the
target's. Result: the aggressor's `scenario_enemies[]` holds every target **twice**, and every
target's `scenario_enemies[]` stays **empty**.

`core/common/scripted_effects/99_sandbox_engine.hsl`:

```hsl
  9:   if global.sandbox_targets[0] != 0:
 10:     var:global.sandbox_targets[0]:   # THIS = target, PREV = aggressor
 11:       PREV:                          # THIS = aggressor, PREV = target
 12:         $sandbox_seed_rival(PREV, 65)
 13:         &scenario_enemies[].add(PREV)  # aggressor.scenario_enemies += target  (correct)
 ...
 24:     # Symmetric side: each target lists the aggressor (scoped as PREV at the
 25:     # var: head; THIS is the target country, PREV is the aggressor tag).
 26:   if global.sandbox_targets[0] != 0:
 27:     var:global.sandbox_targets[0]:   # THIS = target, PREV = aggressor
 28:       PREV:                          # <- flips back to the aggressor
 29:         &scenario_enemies[].add(PREV)  # aggressor.scenario_enemies += target  (duplicate)
```

For the symmetric side the body should run in the target's scope and add `PREV` (the aggressor)
to **THIS** (the target), i.e. without the extra `PREV:` scope:

```hsl
  if global.sandbox_targets[0] != 0:
    var:global.sandbox_targets[0]:
      &scenario_enemies[].add(PREV)   # target.scenario_enemies += aggressor
```

## Session evidence (`_sandbox`, 72 months)

SOV (arc 2, three targets TUR/IRQ/PER) reports **6** enemies:

```
SOV sc_actor gate=1 agg=1 tgt=0 enemies=6 sc=2 phase=0 t=1
SOV sc_seed t0=TUR t1=IRQ t2=PER sc=2 phase=0 pin=0 t=0
```

GER (arc 1, two targets CZE/POL) reports **4**, JAP (arc 3, two targets CHI/PHI) reports **4** -
always exactly `2 x target count`.

Every declared target reports **0** (180 of 180 target-side probe lines):

```
CZE sc_actor gate=1 agg=0 tgt=1 enemies=0 sc=1 phase=1 t=37
POL sc_actor gate=1 agg=0 tgt=1 enemies=0 sc=1 phase=1 t=37
TUR sc_actor gate=1 agg=0 tgt=1 enemies=0 sc=2 phase=0 t=1
```

## Impact

- `is_scenario_enemy_of_PREV` (`core/common/scripted_triggers/99_sandbox_engine_triggers.hsl:4`,
  `THIS in PREV.scenario_enemies[]`) is one-directional in practice: the aggressor sees its
  targets, but a target does not see the aggressor. The F1 betrayal exemption
  (`CZE = { is_scenario_enemy_of_PREV = no }`, 44 sites in `germany.txt`) therefore does not
  apply in the target-to-aggressor direction, so a target AI still pays the full betrayal
  penalty for justifying on its declared enemy.
- `sandbox_scenario_ignite` (`99_sandbox_engine.hsl:45`) gates on `FROM in &scenario_enemies[]`.
  `on_declare_war` sets ROOT = attacker, FROM = target. An aggressor-initiated war matches
  (aggressor's array is populated); a **target-initiated** war does not (target's array is
  empty), so the GDD's "in either direction" ignition
  (`docs/gdd/Scenarios.md:74-76`) is silently one-directional.
- The doubled entries are also wrong for any future size-based logic; the `enemies=` field in
  the `sc_actor` probe reads `2 x` the real count, which makes the telemetry misleading.

## Verification after a fix

- Aggressor `enemies=` should equal its declared target count (2, 3, or 3), not double.
- Target-side `sc_actor` lines should show `enemies=1`.

## Comments
