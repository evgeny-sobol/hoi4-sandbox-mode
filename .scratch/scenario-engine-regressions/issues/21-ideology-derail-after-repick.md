# 21 - Unconfirmed: the ideology derail fires a month after repick

Status: needs-triage
Type: bug
Blocked by: none

## What to build

Confirm or refute whether the ideology derail arm is allowed to fire
immediately after a repick, before the new arc has run any ladder rung.

## Problem

The `v0.2.1` Rt56 session repicked into arc 2 on 1939.7 (`sc_repick soviet_expansion`,
phase 0, smolder) and derailed it one month later:

```
1939.7  SOV sc_seed t0=POL t1=FIN            sc=2 phase=0
1939.7  HAI sc_repick soviet_expansion       sc=2 phase=0
1939.7  HAI sc_pick soviet_expansion         sc=2 phase=0
1939.7  HAI sc_phase smolder                 sc=2 phase=0
1939.8  HAI sc_derail soviet_not_communist   sc=2 phase=3
1939.8  HAI sc_end soviet_not_communist      sc=2 phase=3
```

The arc ran one month. The helper's ideology arm guards on
`not SOV->has_government(communism)` and `not SOV->has_civil_war()` and does
not test the phase, so a Soviet Union that stopped being communist at any
earlier point in the session kills the freshly picked arc at the first
monthly tick.

Two readings, and the session alone cannot separate them:

1. **Intended**: a repick into an arc whose aggressor is already off-ideology
   is wasted, so parking it immediately saves the session. The pool should
   not have offered it, which would make the pick-time eligibility the real
   defect.
2. **Defect**: the ideology arm should mirror the flip arcs, which only judge
   the aggressor at the crises rung, so a fresh arc gets a ladder to at least
   try.

The catalog text for arc 2 says "derail if no longer communist" without a
rung, while the flip arcs (5-6, 17, 20, 23-28) all name the crises phase.
That inconsistency is the thing to settle.

## Why it matters

If reading 1 is right, the fix belongs in pick eligibility (do not offer an
arc whose aggressor already fails its gate) and the immediate derail is a
symptom. If reading 2 is right, arcs 2-4 need a phase guard like the flip
arcs. Either way the current behaviour silently consumes a repick and logs
two `sc_*` transitions for one missed chance, which makes session accounting
misleading.

## Acceptance

- [ ] A maintainer decision recorded: is the immediate post-repick ideology
      derail intended, or should the arm wait for a rung.
- [ ] If intended: pick eligibility excludes arcs whose aggressor already
      fails the arc gate, and the session log shows the arc never picked.
- [ ] If a defect: the affected arcs guard the arm on the documented rung,
      and a repaired session shows a fresh arc running at least to crises.
- [ ] The catalog (GDD) states the rung for every arc whose gate is not the
      shared flip gate.

## Out of scope

- The arcs 9-28 missing aggressor arms (issue 19), which is about absent
  arms, not about when an existing one fires.
