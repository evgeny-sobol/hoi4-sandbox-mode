# 21 - The pick offers an arc whose aggressor already fails its gate

Status: resolved
Type: bug
Blocked by: none

## Decision (maintainer, 2026-10-01)

Reading 1: the immediate derail is a symptom, not the defect. Pick eligibility
must exclude an arc whose aggressor already fails that arc's gate, so a fresh
pick or repick never lands on a dead arc. The ideology arms of arcs 1-4 keep
firing immediately when the aggressor leaves the arc mid-session; no phase
guard is added to them.

## What to build

The director's pick and repick paths must offer only arcs that can still
fire. Today eligibility tests only that the aggressor exists, so a repick can
hand the session an arc whose aggressor is already off-ideology; the arc then
derails at the first monthly tick after wasting the pick.

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

Three facts settle the cause:

1. The ideology arms are asymmetric. Arcs 1-4 test
   `not X->has_government(ideo) and not X->has_civil_war()` with **no phase
   guard**, so they fire the moment the aggressor is off-ideology. The flip
   arcs (5-6, 17, 20, 23-28) add `and global.sandbox_scenario_phase == 1`, so
   they only judge the aggressor at the crises rung.
2. Pick eligibility never tests ideology: `sandbox_pick_scenario()` adds an
   arc to `eligible[]` on `country_exists(<aggressor>)` alone.
3. The repick path calls the same `sandbox_pick_scenario()`, so the same
   hole serves both the startup pick and every repick.

The session shows the consequence: SOV had left communism earlier in the
session, the repick still offered arc 2, and the arc died at the first tick.

## Why it matters

A repick is the director's second chance after a derail; handing it an arc
that cannot fire burns that chance and logs two `sc_*` transitions
(`sc_derail` + `sc_end`) for a pick that never had a chance. The catalog also
already documents per-arc gates, so the pick is the only place that ignores
them.

## Acceptance

- [x] `sandbox_pick_scenario()` excludes an arc from `eligible[]` when its
      aggressor already fails that arc's gate: gone, capitulated, or
      off-ideology for arcs 1-4; off-ideology for the flip/imperial arcs at
      the gate they document.
- [ ] A session where the aggressor of an arc is off-ideology logs no
      `sc_pick` for that arc; the pick lands on another eligible arc (or
      `scenario = 0` when none is eligible) (needs a game run).
- [ ] A freshly picked arc in such a session runs at least to its crises rung
      instead of derailing the next month (needs a game run).
- [x] Arcs 1-4 keep their immediate ideology arm for a mid-session change of
      government (no phase guard added).
- [x] Both mods recompile clean; no new `error.log` lines attributable to
      scenario files (compiled output clean; session check pending).

## Out of scope

- Adding a phase guard to the ideology arms of arcs 1-4; that is the rejected
  reading 2.
- The arcs 9-28 aggressor arms (issue 19), which is about absent arms rather
  than eligibility.

## Verification: PASSED (source + compiled output + guard)

- Eligibility now mirrors the derail gate per arc: each `eligible[].add(N)`
  sits behind `not <agg>->has_capitulated()` plus the arc's government test
  (fascism/communism/neutrality, the JAP democratic-or-communist exclusion,
  the ENG imperial neutrality-or-fascism pair, the SOV-not-communist inverted
  gate). The gate set is read from the derail helpers, so the pick and the
  derail cannot drift.
- The gate table covers 22 gated arcs (vanilla 1-6; r56 1-6, 9-17, 20, 23-28).
  Arcs with no ideology arm (7, 8, 18, 19, 21, 22) keep the existence and
  capitulation checks only.
- The gated adds were written as HSL `not ...` / `or ...` conditions after the
  first pass used raw trigger blocks, which the compiler rejected
  (`Unexpected token INLINE_RAW`). Forced recompile of both mods is clean
  (471 + 293 files).
- Shared guard `.scratch/scripts/check_pick_gate.py` fails when an arc's
  eligible add lacks its gate; negatives verified by hand. It is listed in the
  core `SHARED_MISC` set.
- The observer half (no `sc_pick` for a dead arc, fresh arc reaching crises)
  needs the next session.

## Verification run

See `.scratch/scenario-engine-regressions/verification-run.md`, check 21
(unpinned `sandbox_random` run; a repick only happens when
`sandbox_scenario_pin == 0`).

Not covered by the 2026-10-01 arc-22 run: that run was pinned
(`pin=1`), so no repick path ran. The observer half still needs an unpinned
session.

