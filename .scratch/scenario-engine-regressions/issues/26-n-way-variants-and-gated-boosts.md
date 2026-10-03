# 26 - N-way target variants with variant-gated focus boosts

Status: resolved
Type: feature
Blocked by: none

## Maintainer decisions (2026-10-03, grill)

- Boosts follow the rolled target variant: in a variant-A session only
  path-A focuses (plus shared ones) are boosted; other paths go quiet.
  Semantics stay priority, never guarantee.
- Path-to-variant mapping is explicit, not positional: each `[[paths]]`
  entry declares `variants`; a missing field means shared.
- Shared focuses (present in paths of every variant) stay ungated.
- Variants generalize beyond a/b: specs may declare a/b/c, sometimes a/b/c/d.
- Peak ultimatums wait for the path tail (grill round 2): the aggressor AI
  issues no ultimatum until it completes the last focus of the live path.
  War declaration itself is not suppressed (it arrives via vanilla focuses
  and AI logic no clean lock can gate). Human aggressors are exempt; the
  peak rung waits in crises instead of firing ultimatums early; only
  completed focuses count (bypassed tails stall to the peak timeout, so
  spec authors put rarely-bypassed focuses last).

## What to build

- Schema: `targets` accepts any variant keys (keep the 1-4 tags rule per
  variant, derail arms cover 1-4); `paths` becomes a list of tables with
  `focuses` plus optional `variants` (absent = all variants).
- Validator: every `targets` key is covered by at least one path; every
  listed variant is a `targets` key; path counts no longer imply variants.
- Macros: one parameterized `$ai_scenario_focus_boost(variant)` emitting
  factor + live-aggressor + the proven `check_variable` variant test (probe
  at implementation; fallback is per-variant macros). Plain
  `$ai_scenario_focus_boost()` stays for shared focuses.
- Builder: closure per path; a focus used in variant set S gets one gated
  modifier per variant in S; a focus in all variants gets the plain boost.
  `expected_boosts` becomes variant-keyed; the splice audit checks suffixes.
- Generated per-arc variant roll from the spec keys, replacing the binary
  hand roll in pick and repick; generalize `sc_variant` logging the same way.
- Peak ultimatums gated on the live path tail (AI aggressors only): the
  peak rung does not advance until `has_completed_focus` holds for the last
  focus of the live variant's path; the peak timeout stays the backstop for
  tails the AI never completes.
- Rewrite the three specs to the new shape (content unchanged); update the
  `Path` entry in `CONTEXT.md` when the behavior lands.

## Problem

Variant selection stops at targets, telemetry and events. Focus choice
ignores it: both paths stay boosted in every session, so the aggressor can
march the dead variant's tail (Italy: sentinels vs roads_to_rome). The
current two-path positional convention cannot express three or four
variants at all.

## Why it matters

Variant-gated boosts are the natural completion of "the variant chooses
the arc's direction". Without them, a third variant would steer targets
one way and focuses the other.

## Acceptance

- [x] Specs declare paths with explicit variants; `--check` enforces the
      coverage rules above.
- [x] A three-variant trial spec builds: gated modifiers per variant set,
      plain boost for shared focuses (core test suite).
- [x] The generated roll covers all declared variants; `sc_variant` logs
      each of them (core test suite + compiled output).
- [ ] A pinned session on a multi-path arc shows the aggressor ignoring
      the dead variant's tail focuses (needs a game run; boost weights are
      not telemetry-visible, read via `sc_focus` lines).
- [ ] A pinned session whose aggressor has not finished the live path tail
      by the peak month logs no ultimatums and stays in crises (needs a
      game run with a slow aggressor).
- [x] `build_scenario_catalog.py --check` clean, all shared guards green
      (splice-gate audit included), both mods recompile clean, no new
      `error.log` lines from scenario files (compiled output clean; session
      check pending).

## Verification: PASSED (tests + compiled output + guard)

- Core suite 29/29 (4 new: gated boosts per variant, 3-variant roll/tick,
  uncovered-variant and unknown-variant rejections; golden regenerated for
  the new tick/roll/log shapes).
- Real build: Italy splices converted 6 plain boosts to gated (3 per
  variant), shared trunk stays plain; Germany untouched (single shared
  path); tails emitted (sentinels/roads, nanshin/hokushin).
- Compiled output verified: `check_variable` variant gates in ai_will_do,
  nested tail gates with human exempt and value=36 fallbacks, roll/log
  funcs per arc; hand pick/repick dispatch to them.
- Probe-driven finding fixed on the way: the splice inserted a wrong macro
  name (caught by the mod compile, not the spec check).
- The observer half (tail-wait and dead-tail discipline in live sessions)
  needs the next sessions.

## Out of scope

- Changing priority into guarantee (ADR-0004 stands).
- R56 specs; the builder change applies automatically when they land.
- Touching 23-25 content; this ticket only re-gates its boosts.

## Agent Brief

**Category:** feature
**Summary:** Make focus boosts follow the rolled target variant and
generalize variants past a/b

**Current behavior:**
All spec paths boost whenever the aggressor is live, regardless of variant;
the variant roll and its logging are hardcoded binary.

**Desired behavior:**
After this change, each path declares its variants, boosts gate on the live
variant, shared focuses stay ungated, and any number of variants rolls and
logs correctly.

**Key interfaces:**
- `docs/scenarios/*.toml` (`targets` keys, `[[paths]]` tables).
- `core/tools/build_scenario_catalog.py` (validator, closure, splice,
  variant roll generation).
- `common/macros.hml` (parameterized boost macro), pick/repick variant roll,
  `sc_variant` logging.
- `CONTEXT.md` `Path` entry at landing time.

**Acceptance criteria:**
- [ ] Three-variant build with correct per-variant gates.
- [ ] Generated roll + logging cover every declared variant.
- [ ] Session evidence of dead-tail discipline.
- [ ] Spec build check, all shared guards, and clean recompiles.

**Out of scope:**
- Guarantee semantics, R56 specs, 23-25 content (see above).
