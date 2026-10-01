# 20 - The third declared target gets no ultimatum

Status: ready-for-agent
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

- [ ] In every multi-target arc, each declared target of each variant
      receives a peak pressure line (an ultimatum, or a crisis event where
      the catalog names one).
- [ ] A session running a three-target arc logs a submit/defy crisis outcome
      for all three targets, or a documented reason why a target is
      deliberately passive.
- [ ] No new `error.log` lines attributable to scenario files.

## Out of scope

- Balance of the events (submit/defy shares); the s13 reference anatomy
      stands.
- Targets removed by neutralization, which legitimately log `<tag>_gone`.
