# 24 - Rewire arc 1 content from axis names to nazi_germany

Status: resolved
Type: feature
Blocked by: none

## Maintainer decision (2026-10-03)

`docs/scenarios/axis_expansion.toml` is deleted on purpose, replaced by
`docs/scenarios/nazi_germany_scenario.toml` (same slot 1, same targets and
ladder). The eight `gen_axis_expansion_*` call sites are already repointed at
`gen_nazi_germany_scenario_*` (compile fix, 2026-10-03). This ticket covers
the remaining hand-written `axis` content.

## What to build

Rename the hand-written arc-1 content identifiers from `axis` to
`nazi_germany`, mirroring the spec key:

- Content funcs: `sandbox_fire_axis_crises/peak` plus joiners, and every
  caller (ladder tick branch).
- Events: `sandbox_axis.*` ids (and the event file name if it carries one).
- Labels: `sc_pick`/`sc_repick`/`sc_end` values and any `axis_war`-family
  end labels.
- Selection: pin trigger `sandbox_scenario_pin_is_axis` plus its game-rule
  option `sandbox_axis_expansion` (rename or repoint at the new key; the
  generated pin branch already references
  `sandbox_scenario_pin_is_nazi_germany`, which does not exist yet).
- L10n keys following the rename; docs mentioning the old names.

## Problem

The slot-1 spec, catalog section and generated helpers now say
`nazi_germany`, while the playable content still says `axis`. The game runs
(the gen call sites are rewired and the mod compiles), but telemetry, events
and the game-rule option carry the retired name, and the generated pin branch
points at a trigger that does not exist, so the arc cannot be pinned by rule.

## Why it matters

Same as ticket 23: spec, catalog, telemetry and playable content must agree
on the arc's name, or session logs and the rule UI describe different arcs.

## Acceptance

- [x] Zero reachable `axis`/`sandbox_axis` scenario references (grep over
      hsl/events/l10n/rules); the retired names are gone, not orphaned.
- [ ] Pinning the arc by game rule selects slot 1 with the new key (needs a
      game run).
- [ ] A pinned session runs pick -> crises -> peak -> park/ignite with the
      new labels throughout (needs a game run).
- [x] `build_scenario_catalog.py --check` clean, all four shared guards
      green, both mods recompile clean, no new `error.log` lines from
      scenario files (compiled output clean; session check pending).

## Out of scope

- Slot 2 (ticket 23) and slot 3 (ticket 25).
- Event balance; the s13 reference anatomy stands.
- R56 port; vanilla slot 1 only.

## Verification: PASSED (source + compiled output + guard)

- Renamed via script (longest match first): `sandbox_axis_expansion`,
  `sandbox_axis`, content funcs, `axis_war`/`axis_ult_*`/`axis_crisis`/
  `axis_joined` labels, repick labels, pin trigger, rule option
  (`sandbox_nazi_germany`, text "German expansion"), header comments, and
  the events file itself. Vanilla "Axis faction" references
  (ai_strategy_plans etc.) are game data and untouched.
- Forced recompile clean (293 files); the orphaned `axis.txt` was removed
  by the compiler and `nazi_germany.txt` generated. Pin trigger and rule
  option present in compiled output.
- The observer half (rule-pinned session under the new labels) needs the
  next session.

## Agent Brief

**Category:** feature
**Summary:** Rename playable arc-1 content to the nazi_germany key the spec
already uses

**Current behavior:**
Slot 1 plays under `axis` names (funcs, events, labels, pin trigger, rule
option) while the spec, catalog and generated helpers say `nazi_germany`;
the generated pin branch references a trigger that does not exist.

**Desired behavior:**
After this change, every arc-1 identifier carries the spec key end to end,
and the arc is pinnable by rule again.

**Key interfaces:**
- `sandbox_fire_axis_crises/peak`, joiners func, ladder tick branch.
- `sandbox_axis.*` events, `axis_war`-family labels, l10n keys.
- `sandbox_scenario_pin_is_axis` trigger, `sandbox_axis_expansion` rule
  option (see `99_sandbox_scenario_rules.hsl` and the triggers file).
- The eight rewired `gen_nazi_germany_scenario_*` call sites are the
  template for how generated and hand code meet.

**Acceptance criteria:**
- [ ] Grep-clean rename with no orphans.
- [ ] Rule-pinned session plays to park/ignite under the new labels.
- [ ] Spec build check, all shared guards, clean recompiles.

**Out of scope:**
- Slots 2-3, event balance, R56 (see above).
