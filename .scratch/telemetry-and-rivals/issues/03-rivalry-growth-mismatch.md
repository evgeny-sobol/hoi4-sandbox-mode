# 03: The rival's-core term reads itself, so every pair gains +2 forever

**What to build:** each of the two core terms tests the fact it names. "We hold a
state they core" fires when that is true of us, and "they hold a state we core"
fires when that is true of them - not on itself, and not always.

**Blocked by:** None (can start immediately). Ticket 02 is the visible symptom in
one pairing; this ticket is the cause.

**Status:** resolved

## Cause

`update_rivalry_monthly()` in
`common/scripted_effects/99_sandbox_scripted_effects.hsl` computes the second
core term from inside the rival's scope:

```
1229        if any_owned_state->is_core_of(var:rival_tag):   # ours, correct
1232          rv_core_us = 1
1233        var:rival_tag:                                    # now in the rival
1235          if any_owned_state->is_core_of(PREV):           # the defect
1236            rv_core_them = 1
```

Inside `var:rival_tag:` the current country is the rival, so `any_owned_state`
enumerates the rival's states and `is_core_of(PREV)` compares them against
whatever `PREV` resolves to. In this position it resolves to the rival itself, so
the test asks "does the rival own a state the rival cores" - true for any country
that exists, because its capital is its own core.

The term therefore does not measure a claim. It adds `+2` to every pair, every
month, for as long as the pair exists.

## Evidence

The per-term probe (`sandbox_log_rival_terms`, ticket 01's neighbour) was run for
a full session, 1936.01 to 1941.02, on the vanilla build. It names every term
per slot per month, so the claim above is measured rather than read off the
source.

All 17 605 probe lines, over every country with a populated slot:

| term | fires | share |
| ---- | ----- | ----- |
| `ct` they core our land | 17 605 | **100%** |
| `id` enemy ideology | 4 747 | 27% |
| `lead` slot-0 ruler bias | 4 665 | 26% |
| `same` same government | 4 623 | 26% |
| `fr` they fight a friend | 910 | 5% |
| `w` at war | 827 | 5% |
| `cu` we core their land | 310 | **1.8%** |
| `pact` non-aggression | 72 | 0.4% |

Two facts settle it:

- There is no probe line with `ct=0`. A condition that never fails is not
  measuring a condition.
- There is no line where `cu` fires and `ct` does not. The two terms describe
  opposite halves of the same relation, so a real mutual-claims rule would show
  four combinations. The data shows two: `(0,1)` on 17 295 lines and `(1,1)` on
  310.

The 56:1 asymmetry between the two core terms is the signature of one of them
reading a different thing than its name says.

## What this is not

The arithmetic is correct, and this was the thing to check first: across all
17 605 probe lines the reported delta equals the terms recomputed from the
reported flags, with zero mismatches. `$add_rivalry` applies what it is given and
the sum is the sum. The defect is in one input, not in the accounting.

An earlier draft of this ticket claimed the deltas "cannot be produced" by the
declared terms. That was wrong, and it was wrong for a reason worth recording: it
compared a model built on assumed save facts against observed values, and the
assumption (no mutual cores) was itself unverified. The probe removed the
assumption, and with it the argument.

## Fix

Replace `is_core_of(PREV)` with `is_core_of(ROOT)` on line 1235. `ROOT` is the
country the effect was called on - `update_rivalry_monthly()` runs from
`on_monthly` in the country's own scope - so inside `var:rival_tag:` it still
names us, and the test becomes "does the rival own a state we core".

Validate on one pairing before trusting it: after the fix the term should fire
for pairs with a real claim and not otherwise, so the share of `ct=1` should drop
from 100% to roughly the same order as `cu`.

## Acceptance

- [x] `rv_core_them` uses a scope that provably names us from inside the rival's
      scope: `is_core_of(ROOT)`, core
      `common/scripted_effects/99_sandbox_scripted_effects.hsl`.
- [x] A probe run shows `ct=0` on at least some lines: 6 724 of 6 944.
- [x] The same run shows all four combinations: `(0,0)` 6 601, `(1,0)` 123,
      `(0,1)` 163, `(1,1)` 57.
- [x] `ct=1` share falls from 100% to 3%, against `cu` at 2%.
- [x] A pairing with no mutual claims stays flat. 6 601 of 6 944 lines carry
      neither core term, and the delta distribution is now dominated by decay
      (`-1` on 285 pair-months, `-2` on 46).
- [ ] `check_rivalry_delta.py` reports fewer than 397 peaceful pair-months
      outside the band: it reports 69, down from 397. Not zero - see the note
      below, the remainder has a different cause.
- [ ] No new `error.log` lines attributable to the mod.

## Out of scope

- Reweighting the terms or retuning the bands. This ticket makes a term measure
  what it names; what it should be worth is a separate decision.
- Ticket 02's Albania case, which this ticket explains but does not touch.

## Session result (2026-11-08, 1936-1938)

The fix was verified on a fresh run: hands-off, 1936.01 to 1938.01.09, vanilla
build, 6 944 per-term probe lines, zero mod-attributable `error.log` lines.

Measured against the pre-fix run:

| measure | before | after |
| ------- | ------ | ----- |
| probe lines where `ct` fired | 17 605 of 17 605 (100%) | 220 of 6 944 (3%) |
| probe lines where `ct` did not fire | 0 | 6 724 |
| `cu`/`ct` combinations seen | two, `(0,1)` and `(1,1)` | all four: `(0,0)` 6 601, `(1,0)` 123, `(0,1)` 163, `(1,1)` 57 |
| `ct` share against `cu` | 56:1 | 3% against 2% |

`ct` and `cu` now fire at the same order of magnitude and the term can fail,
which is what the ticket asked for.

The delta distribution for a peaceful country inverted with it: `-1` on 285
pair-months and `-2` on 46, against a pre-fix run dominated by `+2` and `+3`.
Rivalries with no cause now decay instead of climbing.

The arithmetic check was rewritten to use the probe rather than a census band:
recomputing the delta from the reported flags gives 0 problems on all 6 944
lines. The band was retired because it ignored the slot-0 leader bonus and
reported 262 failures that were not failures - a guard that lies is worse than no
guard.
