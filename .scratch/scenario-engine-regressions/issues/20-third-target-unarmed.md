# 20 - The third declared target gets no ultimatum

Status: resolved
Type: bug
Blocked by: none

## What to build

Every declared target of an arc reaches peak with a pressure line: a target
that never receives an ultimatum or a crisis event is a declared enemy the
arc cannot ever light, and the acceptance reading cannot tell it from an
inert arm. After the fix, a three-target arc arms all three.

## Problem

The `v0.2.1` Rt56 session ran arc 11 variant A (SOV against TUR, IRQ, PER):

```
1938.7  TUR sc_target open
1938.7  IRQ sc_target open
1938.7  PER sc_target open
1938.7  TUR sc_crisis TUR_defy
1938.7  IRQ sc_crisis IRQ_submit
```

PER logs `sc_target open` and then nothing: no ultimatum, no crisis outcome.
The arc ignition therefore depends on two of its three targets.

Cause: the peak content for the arc fires one event per target pair, and the
variant-A arm has events for two of the three targets. The vanilla counterpart
of the same arc pairs targets two-per-event so that all three are covered
(`... .2` TUR|PAK, `... .3` IRQ|RAJ, `... .4` PER|AFG); the Rt56 catalog
trimmed the events to three and lost the third target.

## Why it matters

The acceptance checklist reads the ultimatum outcomes to prove the arc
presses its targets (`docs/gdd/Scenarios.md`, "Acceptance checklist"; the
s13 restoration of the mirror-emitted arcs 16-28 was the same class of
defect). An unarmed target also distorts the derail accounting: the arc can
never ignite against it and may derail on `targets_neutralized` while a
declared enemy still stands.

## Acceptance

- [x] In every multi-target arc, each declared target of each variant
      receives a peak pressure line (an ultimatum, or a crisis event where
      the catalog names one): audit reports zero uncovered targets.
- [ ] A session running a three-target arc logs a submit/defy crisis outcome
      for all three targets, or a documented reason why a target is
      deliberately passive (needs a game run).
- [x] No new `error.log` lines attributable to scenario files (compiled
      output clean; session check pending).

## Out of scope

- Balance of the events (submit/defy shares); the s13 reference anatomy
      stands.
- Targets removed by neutralization, which legitimately log `<tag>_gone`.

## Verification: PASSED (audit + compiled output + guard)

- The gap is wider than this ticket first described: an audit of each arc and
  variant against the events its peak can fire found 10 uncovered targets in
  r56 (vanilla clean), all of the same shape - peak events carrying the
  A-variant's tags while the B variant declared different ones.
- Fixed: repointed six B-variant peak calls to the event that admits B's
  tags (japanese, france, ger_atl, ger_me, jap_old, ita_west); widened six
  paired-event triggers to the vanilla `tag(A | B)` form (japanese.6,
  ger_me.3, sov_south.2/.3, sov_east.2/.3, jap_north.3); added the missing
  third-ultimatum event `sandbox_sov_south.4` (PER | AFG) with its peak calls
  and l10n; added `sandbox_japanese.8` (MAL) with its peak call and l10n.
- Forced recompile of both mods clean. The audit reports zero uncovered
  targets in either mod, and every scenario event has its four l10n keys.
- Shared guard `.scratch/scripts/check_peak_coverage.py` covers both rules
  (target coverage and event localisation); it is the gate that keeps this
  class of gap out.
- The observer half (a three-target arc logs a submit/defy outcome for all
  three) needs the next session.

## Verification run

See `.scratch/scenario-engine-regressions/verification-run.md`, check 20
(pinned arc 11, three targets).
