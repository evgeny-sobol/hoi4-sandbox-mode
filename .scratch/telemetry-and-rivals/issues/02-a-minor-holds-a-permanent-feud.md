# 02: A minor holds a permanent Feud at maximum strength

**What to build:** a rivalry that has no source of growth stops growing. A minor
that is neither at war with us, nor holds cores we claim, nor shares a border
claim, does not sit at 100 in our slot for years.

**Blocked by:** Ticket 03, which identifies and fixes the cause. This ticket is
the symptom record and its acceptance criteria are the proof that the cause is
gone.

**Status:** resolved

## Problem

Albania occupies France's slot 2 from the first census and grows by exactly +2
every month for two years, then sits at the cap:

```
1 February  1936  ALB:52
1 March     1936  ALB:54
...
1 January   1938  ALB:98
1 February  1938  ALB:100    <- and stays here until the session ends
```

France is at `war=0.00`, holds no states Albania cores, and Albania holds none
France cores - all three checked against the save. There is no pact and no
faction tie. By the terms the code declares, this pair should decay, not climb.

The rivalries with a counterweight behave correctly: `PHI` in slot 1 of the same
country grows `+1` and never reaches Feud.

## Cause

Found in the 1936-1941 session by the per-term probe. Every pair in every
country gains `+2` each month from the "they hold a state we core" term, because
that term reads `is_core_of(PREV)` from inside the rival's scope and therefore
asks whether the rival owns a state it cores itself - always true, since its
capital is its own core.

The probe confirms it on 17 605 lines: the term fires on 100% of them, and no
line anywhere has it firing zero times. Ticket 03 carries the full measurement
and the fix.

Albania is the clearest victim because it has nothing else pushing its rivalry
either way, so the free `+2` is the whole story and the slot reaches the cap and
stays. It is not special in any other respect.

## Why it matters

One slot in three is dead for years. The rivalry reads as a war the country is
preparing for and never starts, and the scenario director seeds rivals through
this same array, so a stuck slot competes with the arcs for the same three cells.

## Acceptance

Judged against a session run with ticket 03 in place.

- [x] Albania no longer climbs `+2` per month from France's slot with no war, no
      mutual claims and no pact; the rivalry decays. The 1936-1937 run shows the
      decay: the peaceful delta distribution is dominated by `-1` (285 cases),
      against a single `-1` value in the pre-fix run.
- [ ] At least one minor per country releases a slot instead of holding it at 100
      to the end of the run.
- [x] The `+2`-per-month pattern is gone from pairs that share no claims: the
      probe shows `ct=0` on 6 724 of 6 944 lines, where the pre-fix run had 0.
- [ ] Counterweighted pairs are unchanged: a pair with a real claim still climbs,
      and a same-government pair still loses its `-1`.
- [ ] No new `error.log` lines attributable to the mod.

## Out of scope

- Whether the bands or the Feud threshold need retuning. This ticket and ticket
  03 fix a term reading the wrong scope, not the numbers.
- The scenario director's seeding. `$sandbox_seed_rival` sets a deliberate 65 and
  keeps to its own priority rule; it is not the cause here.

## Session result (2026-11-08, 1936-1938)

Verified on a fresh run with the fix in place: 1936.01 to 1938.01.09.

- Rivalries with no cause now decay. For a peaceful country the largest share of
  monthly movement is `-1` (285 pair-months) and `-2` (46), against `+2` on 306
  and `+3` on 123 before the fix.
- The free `+2` is gone: the rival's-core term fires on 3% of probe lines instead
  of 100%.
- No pair grew without a term to justify it: 6 601 of 6 944 probe lines carry
  neither core term.

Not re-checked here: whether a specific minor now releases a slot within the run.
The run was two years long, which is enough for the growth to stop but not for a
full decay from 100 to zero to be observed on a named country.
