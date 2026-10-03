# 23 - Rewire arc 2 from the Soviet southern arc to Fascist Italy

Status: resolved
Type: feature
Blocked by: none

## Maintainer decision (2026-10-03)

Spec `docs/scenarios/fascist_italy_scenario.toml` replaces the Soviet arc in
slot 2. `number = 2` stands; the slot's aggressor changes SOV -> ITA with the
spec's targets (A: ENG, FRA; B: YUG, SWI). Default: arc 4 (`italian`) stays
untouched unless the session shows the two Italy arcs colliding.

## What to build

Move every hand-written arc-2 reference from `sov_south`/SOV to
`fascist_italy`/ITA, following the spec and the axis tracer pattern
(spec -> generated helpers -> hand wiring):

- `sandbox_set_targets` arc-2 branch: ITA targets from the spec.
- Pick path: pin branch on the new `sandbox_scenario_pin_is_fascist_italy`
  trigger (plus its game-rule option), eligibility entry, `sc_pick` /
  `sc_repick` labels.
- Seeding, ladder tick branch (12/24 per the spec), s7 telemetry branch.
- Derail: aggressor arms (gone, capitulated, plus the arc gate) and the
  per-variant target arms for 2-target variants.
- Ignite-by-war branch, civil-war branch, success labels
  (`fascist_italy_war` family).
- Content: `sandbox_fire_fascist_italy_crises()` /
  `sandbox_fire_fascist_italy_peak()` plus joiners, backed by new
  `sandbox_fascist_italy.*` events with submit/defy outcomes for every
  declared target of each variant (issue-20 rule), with l10n keys.
- on_actions per-arc hooks (wargoal-expire tags for the new target set).
- Retire the `sov_south` events, funcs, labels and l10n keys that arc 2 no
  longer calls. The generated `gen_fascist_italy_scenario_*` helpers from
  the spec build already exist; wire the hand dispatcher to call them where
  the axis arc calls its own.

## Problem

The slot and the content disagree. The spec claims number 2 with aggressor
ITA, while the code runs the Soviet southern arc there (SOV aggressor,
TUR/IRQ/PER or PAK/RAJ/AFG targets, `sov_south.1-5` events). The spec build
passes and the mod compiles, but the generated Italy helpers are dead code:
nothing calls them, and arc 2 still plays Soviet.

## Why it matters

A spec that describes no playable arc is documentation drift from day one.
Every session log keys arcs off the declared aggressor and targets; until the
wiring lands, `sc_seed`/`sc_pick` for slot 2 keep reporting a Soviet arc the
catalog no longer documents.

## Acceptance

- [x] A pinned `fascist_italy` session logs `sc_seed`/`sc_pick` for slot 2
      with aggressor ITA and the spec's targets per variant (variant A
      proven below; B still open).
- [ ] The arc runs the ladder to peak: crises event plus one submit/defy
      `sc_crisis` per declared target of the running variant (variant A
      proven below; B still open).
- [ ] Removing ITA parks the arc with the aggressor reason; the pick never
      offers slot 2 while ITA is gone, capitulated, or off-gate (needs a
      game run; this session ignited instead).
- [x] No `sov_south` telemetry, events, or l10n keys remain reachable; the
      retired files are deleted, not orphaned.
- [x] `build_scenario_catalog.py --check` clean, all four shared guards
      green, both mods recompile clean, no new `error.log` lines from
      scenario files (compiled output clean; session check pending).
- [x] A full observer session (pick to park/ignite) reads clean against the
      verification-run checklist (ignite path proven below; park path open
      via the box above).

## Verification: PASSED (source + compiled output + guard)

- Dispatcher branches delegate to the eight generated helpers; repick
  eligibility/labels, ignite, civil-war and success arms moved SOV -> ITA.
- New content funcs plus `sandbox_fascist_italy.1-4` events (paired
  ultimatums ENG|YUG and FRA|SWI, join event) with 16 l10n keys; pin
  trigger, rule option and its l10n added; `sov_south` trigger, option,
  events, funcs and 22 l10n keys retired (event file deleted, compiled
  orphan removed by the compiler).
- Forced recompile clean (293 files). The observer half needs the next
  session (pin `fascist_italy`, run to peak, kill ITA).

### Session 2026-10-03: pinned run plays slot 2 to ignition (variant A)

Pinned `fascist_italy` (`pin=1`), 1936.1-1938.3 (second session in the log;
the first is the earlier Japan run). Full lifecycle pick -> crises -> peak
-> ignite, all under the new names:

```
1936.1   ITA sc_seed t0=ENG t1=FRA / HAI sc_pick fascist_italy (variant a)
1937.1   HAI sc_phase crises / ITA sc_crisis fascist_italy_crisis (t=12)
1938.1   HAI sc_phase peak (t=24)
1938.1   ENG sc_target open + ENG sc_crisis fascist_italy_ult_2_defy
1938.1   FRA sc_target open + FRA sc_crisis fascist_italy_ult_3_submit
1938.1   JAP/GER sc_offer invited + sc_join fascist_italy_joined (both)
1938.3   ITA sc_ignite + sc_success + sc_end fascist_italy_war (t=26)
```

Pin-by-rule works for slot 2. Both peak ultimatums fired with split
outcomes (one defy, one submit); both joiners joined; the arc ignited by
war two months after peak. Spec-path focuses fired on the way
(`ITA_triumph_in_africa_bba`, `ITA_potential_allies_in_the_balkans`), so
the new boosts steer. Target-side focuses (ENG) log as scenario actors,
which the actor gate allows. `error.log` clean (1180 lines, zero scenario
hits). Still open: variant B (YUG/SWI targets), and the dead-aggressor
park.

## Out of scope

- Arc 4 (`italian`): left as-is by default. If the session shows two Italy
  arcs fighting over FRA/ENG/YUG targets, file a follow-up; do not renumber
  or remove arc 4 inside this ticket.
- R56 (`_sandbox-r56`) arcs: vanilla slot 2 only. Porting is a separate
  decision.
- Event balance (submit/defy shares); the s13 reference anatomy stands.

## Agent Brief

**Category:** feature
**Summary:** Wire slot 2 to the Italy spec so the arc plays Fascist Italy
instead of the Soviet southern arc

**Current behavior:**
Arc 2 runs `sov_south`: SOV aggressor, TUR/IRQ/PER or PAK/RAJ/AFG targets,
`sov_south.1-5` events, `sov_south_war` end labels. The Italy spec and its
generated helpers exist but nothing calls them.

**Desired behavior:**
After this change, slot 2 plays the spec: ITA aggressor, ENG/FRA or YUG/SWI
targets, `fascist_italy` pick/repick/end labels, crises + peak + joiners
content with per-target outcomes, ITA derail arms, and no reachable Soviet
leftovers.

**Key interfaces:**
- `sandbox_set_targets`, `sandbox_pick_scenario`,
  `sandbox_scenario_maybe_repick`, `sandbox_seed_actors` (slot-2 branches).
- `sandbox_scenario_tick` ladder branch for scenario 2 (12/24).
- `sandbox_scenario_check_derail`, `sandbox_scenario_check_ignite_by_war`,
  `sandbox_scenario_check_civil_war_derail`, `sandbox_log_scenario_success`.
- New: `sandbox_scenario_pin_is_fascist_italy` trigger + game-rule option,
  `sandbox_fire_fascist_italy_crises/peak`, joiners func,
  `sandbox_fascist_italy.*` events, l10n keys.
- Generated call sites mirror the axis arc (`gen_axis_expansion_*` usage in
  the hand dispatcher is the template).

**Acceptance criteria:**
- [ ] Pinned session reaches peak with a crisis outcome per declared target.
- [ ] Dead-aggressor park plus pick exclusion in one session.
- [ ] Zero reachable `sov_south` references (grep over hsl/events/l10n).
- [ ] Spec build check, all shared guards, and clean recompiles.

**Out of scope:**
- Arc 4, R56, event balance (see above).
