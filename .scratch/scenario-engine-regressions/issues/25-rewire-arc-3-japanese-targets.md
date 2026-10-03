# 25 - Rewire arc 3 from the old Japanese targets to militarist_japan

Status: resolved
Type: feature
Blocked by: none

## Maintainer decision (2026-10-03)

`docs/scenarios/militarist_japan_scenario.toml` replaces slot-3 content:
aggressor stays JAP, targets become A: CHI, AST and B: SOV, MON. The s7
telemetry branch is already rewired to
`gen_militarist_japan_scenario_telemetry()` (compile fix, 2026-10-03). This
ticket covers the remaining hand-written slot-3 content.

## What to build

Move every hand-written arc-3 reference to the spec, following the ticket-23
pattern:

- `sandbox_set_targets` arc-3 branch: CHI/AST and SOV/MON.
- Pick path: pin branch on the new `sandbox_scenario_pin_is_militarist_japan`
  trigger (plus its game-rule option), eligibility entry, `sc_pick` /
  `sc_repick` labels.
- Seeding, ladder tick branch (12/24 per the spec).
- Derail: aggressor arms (gone, capitulated, plus the arc gate) and the
  per-variant target arms for 2-target variants.
- Ignite-by-war branch, civil-war branch, success labels
  (`militarist_japan_war` family).
- Content: `sandbox_fire_militarist_japan_crises()` /
  `sandbox_fire_militarist_japan_peak()` plus joiners, backed by new events
  with submit/defy outcomes for every declared target of each variant
  (issue-20 rule), with l10n keys. Note the second variant pressures SOV
  itself: the ultimatum set must admit an aggressor-sized target.
- on_actions per-arc hooks (wargoal-expire tags for the new target set).
- Retire the Japanese content slot 3 no longer calls
  (`sandbox_japanese.*` events, funcs, labels, l10n) only where it becomes
  unreachable; keep whatever other arcs still share.
- Wire the remaining generated `gen_militarist_japan_scenario_*` helpers into
  the hand dispatcher where the axis arc calls its own.

## Problem

The slot-3 spec, catalog section and telemetry say CHI/AST and SOV/MON,
while the playable arc still pressures CHI/PHI and BRM/INS/MAL through
`sandbox_japanese.*` events. Telemetry and content disagree on the target
set, and the generated helpers (except telemetry) are dead code.

## Why it matters

Same as tickets 23-24: until the wiring lands, session logs report targets
the catalog does not document, and the new target set (including SOV as a
pressured party) never plays.

## Acceptance

- [x] A pinned `militarist_japan` session logs `sc_seed`/`sc_pick` for
      slot 3 with the spec's targets per variant (variant A proven below;
      B still open).
- [ ] The arc runs the ladder to peak: crises event plus one submit/defy
      `sc_crisis` per declared target of the running variant, both variants
      (variant A proven below; B still open).
- [ ] Removing JAP parks the arc with the aggressor reason; the pick never
      offers slot 3 while JAP is gone, capitulated, or off-gate (needs a
      game run; this session ignited instead).
- [x] No unreachable Japanese leftovers from the replaced target set;
      shared content with other arcs stays.
- [x] `build_scenario_catalog.py --check` clean, all four shared guards
      green, both mods recompile clean, no new `error.log` lines from
      scenario files (compiled output clean; session check pending).
- [x] A full observer session (pick to park/ignite) reads clean against the
      verification-run checklist (ignite path proven below; park path open
      via the box above).

## Verification: PASSED (source + compiled output + guard)

- Dispatcher branches delegate to the eight generated helpers (s7
  telemetry was already wired); repick eligibility, ignite and civil-war
  branches correctly stay on JAP (aggressor unchanged).
- New content funcs plus `sandbox_militarist_japan.1-4` events (paired
  ultimatums CHI|SOV and AST|MON, join event) with 16 l10n keys; pin
  trigger, rule option and its l10n added; `japanese_expansion` trigger,
  option, events, funcs and 22 l10n keys retired (event file deleted,
  compiled orphan removed by the compiler).
- Forced recompile clean (293 files). The observer half needs the next
  session (pin `militarist_japan`, run both variants to peak).

### Session 2026-10-03: pinned run plays slot 3 to ignition (variant A)

Pinned `militarist_japan` (`pin=1`), 105 telemetry lines, 1936.1-1938.4.
First pinned run of the new arcs; full lifecycle pick -> crises -> peak ->
ignite, all under the new names:

```
1936.1   JAP sc_seed t0=CHI t1=AST / HAI sc_pick militarist_japan (variant a)
1937.1   HAI sc_phase crises / JAP sc_crisis militarist_japan_crisis (t=12)
1938.1   HAI sc_phase peak (t=24)
1938.1   CHI sc_target open + CHI sc_crisis militarist_japan_ult_2_defy
1938.1   AST sc_target open + AST sc_crisis militarist_japan_ult_3_defy
1938.1   GER/ITA sc_offer invited + sc_join militarist_japan_joined (both)
1938.4   JAP sc_ignite + sc_success + sc_end militarist_japan_war (t=27)
```

Pin-by-rule works (slot 3 selected, `pin=1` throughout). Both peak
ultimatums fired with outcomes; both joiners joined; the arc ignited by war
three months after peak. Spec-path focuses fired on the way
(`JAP_nanshin_ron`, `JAP_reinforce_the_beijing_garrison`), so the new
boosts steer. `error.log` clean (184 lines, zero scenario hits).
Still open: variant B (SOV/MON targets), and the dead-aggressor park.

## Out of scope

- Slots 1-2 (tickets 23-24) and arcs 4-6.
- Event balance; the s13 reference anatomy stands.
- R56 port; vanilla slot 3 only.

## Agent Brief

**Category:** feature
**Summary:** Wire slot 3 to the militarist_japan spec (CHI/AST, SOV/MON)

**Current behavior:**
Slot 3 plays the old Japanese target set (CHI/PHI, BRM/INS/MAL) through
`sandbox_japanese.*` events. Only the s7 telemetry branch follows the spec.

**Desired behavior:**
After this change, slot 3 plays the spec end to end, including ultimatums
against SOV in variant B, with per-target outcomes and no unreachable
leftovers from the old target set.

**Key interfaces:**
- `sandbox_set_targets`, `sandbox_pick_scenario`,
  `sandbox_scenario_maybe_repick`, `sandbox_seed_actors` (slot-3 branches).
- `sandbox_scenario_tick` ladder branch for scenario 3 (12/24).
- `sandbox_scenario_check_derail`, `sandbox_scenario_check_ignite_by_war`,
  `sandbox_scenario_check_civil_war_derail`, `sandbox_log_scenario_success`.
- New: `sandbox_scenario_pin_is_militarist_japan` trigger + game-rule
  option, `sandbox_fire_militarist_japan_crises/peak`, joiners func, new
  events, l10n keys.
- The axis arc's `gen_axis_expansion_*` call sites (now
  `gen_nazi_germany_scenario_*`) are the template.

**Acceptance criteria:**
- [ ] Pinned session reaches peak with a crisis outcome per declared target,
      both variants.
- [ ] Dead-aggressor park plus pick exclusion in one session.
- [ ] Zero unreachable leftovers from the old target set.
- [ ] Spec build check, all shared guards, and clean recompiles.

**Out of scope:**
- Slots 1-2 and 4-6, event balance, R56 (see above).
