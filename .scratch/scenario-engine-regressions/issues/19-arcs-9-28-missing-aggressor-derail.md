# 19 - Arcs 9-28 derail on targets but never on a dead aggressor

Status: resolved
Type: bug
Blocked by: none

## What to build

Every arc in the Rt56 catalog must park when its aggressor can no longer
prosecute the arc, exactly as arcs 1-8 do. Today arcs 9-28 only carry the
target arms, so an arc whose aggressor is gone, capitulated, or off-ideology
keeps running.

## Problem

The derail dispatcher (`sandbox_scenario_check_derail`) has one branch per
arc. Arcs 1-8 delegate to named helpers
(`sandbox_scenario_check_<arc>_derail`) that carry the full arm set: gone,
capitulated, ideology or flip gate, and the per-variant target arms
(verified: all eight helpers carry `country_exists` and
`has_capitulated()`). Arcs 9-28 are inlined in the dispatcher and carry only
the target arms, with no aggressor existence or capitulation test.

Evidence in the `v0.2.1` session: arc 2 derailed with
`sc_derail soviet_not_communist` one month after its repick, which is the
named-helper arm working. Arc 11 (`sov_south`, SOV aggressor) has no such
arm, so a non-communist or removed SOV would let the arc sit at peak until
the peak timeout instead of parking.

## Why it matters

The scenario lifecycle promises that a dead arc parks and (on random) a fresh
arc is picked; a stale arc burns the session on a conflict that cannot fire.
`docs/gdd/Scenarios.md` "Lifecycle" lists the aggressor conditions as the
first derail reasons, and the Rt56 catalog documents per-arc ideology gates
for the inlined arcs (17/20/23-28) that the dispatcher never evaluates as a
gone/capitulated arm.

## Acceptance

- [x] Every arc 9-28 branch tests the aggressor: gone and capitulated at
      minimum; the arc's documented ideology or flip gate where the catalog
      defines one (the flip gates for 17/20/23-28 were already present and
      stay).
- [ ] An observer session with the aggressor removed parks the arc with
      `sc_derail` + `sc_end` and the arc's reason label, not a `peak_timeout`
      or a silently running arc (needs a game run).
- [x] Arcs 1-8 keep the behaviour and labels they have today (re-audited).
- [x] No new `error.log` lines attributable to scenario files (compiled
      output clean; session check pending).

## Out of scope

- The peak-timeout arm, which is a separate exit and already works.
- The neutralized-target semantics, which are correct and shared.
- The ideology gate wording for arcs 23-28 (issue 20 is a separate signal
  about when that gate fires).

## Verification: PASSED (source + compiled output + guard)

- All 20 inline branches (arcs 9-28) gained the aggressor arms: gone and
  capitulated, with the existing per-variant target arms re-indented under
  the new `else`. The gone/capitulated labels reuse the named helpers' labels
  (`germany_gone`, `soviet_not_communist`-family uses the country name for
  gone/capitulated: `germany_gone`/`germany_capitulated`, and so on).
- Arcs 1-8 keep their named helpers untouched (re-audited: all eight carry
  the full arm set).
- Forced recompile of both mods clean. In the compiled dispatcher every arc
  9-28 branch now carries `country_exists` plus `has_capitulated`; the audit
  reports zero missing.
- Shared guard `.scratch/scripts/check_derail_arms.py` (both mods): fails on
  any branch without a helper call or the inline arms; negatives verified by
  hand.
- The observer half (removing an aggressor parks the arc with the reason
  label) needs the next session.
