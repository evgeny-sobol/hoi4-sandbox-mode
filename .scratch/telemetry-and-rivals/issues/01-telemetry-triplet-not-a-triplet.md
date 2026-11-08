# 01: The telemetry triplet is not a triplet

**What to build:** every `#sandbox` line that carries a `was -> became d=`
triplet obeys the rule from `Design Decisions - RU.md:411`: `was` is the value
before, `became` the value after, and `d` their difference. A session extract
can be read by trusting `d`, and by trusting `became - was`, and both give the
same answer.

**Blocked by:** None (can start immediately).

**Status:** resolved

## Problem

The 1936-1940 vanilla session produces 388 lines that break the rule, in two
classes that need separate fixes.

**Class A - `d` is not a difference (351 lines).** Three independent causes:

- `ec_embargo_sent` (230 lines). In
  `common/scripted_effects/99_sandbox_scripted_effects.hsl`,
  `sandbox_economic_embargo_send()` sets `sandbox_log_old = 0`,
  `sandbox_log_new = r` and `sandbox_log_delta = -100` (source line 1517). The three fields describe
  three different things: the embargo starts at 0, the target's rivalry was `r`,
  and the political power cost was 100. Sample:
  `MEN ec_embargo_sent 0.00->78.00 d=-100.00`.
- `ec_license_granted_infantry_equipment_1` (32) and `_2` (29). These log
  `0.00->1.00 d=0.00` and `0.00->2.00 d=0.00`. The same effect carries the grant
  count as `new` and leaves `delta` at zero.
- `GER_inner_circle_census` (57) and the three `ascension` lines. The macro
  `sandbox_log_ger_inner_circle_state` in `common/macros.hml` sets `old`, `new`
  and `delta` all to `GER_inner_circle_count`, so `1.00->1.00 d=1.00`.

**Class B - `d` is right but `became` is clamped (37 lines).**
`$add_rivalry` in `common/macros.hml:597-609` computes
`new_rivalry = clamp(cur + var, 0, 100)`, then logs `sandbox_log_delta = _var_`
and `sandbox_log_new = new_rivalry`. When the clamp bites, `new - old` is not
`delta`: `ETH rivals_intensity 98.00->100.00 d=25.00`. Same shape in
`tyranny_focus` (5) and `honor_join_allies_call` (2).

None of these is a regression from the playtest-audit work; all three predate it.

## Why it matters

The GDD calls this rule the reason a log reader can be trusted: break it once and
analysis lies quietly instead of failing. The audit that found the eight
playtest regressions read this same extract; a reader who had trusted `d` would
have drawn wrong conclusions on 351 lines, and one who had trusted `new - old`
wrong conclusions on 37.

## Acceptance

- [ ] `ec_embargo_sent` carries a triplet whose three fields describe one
      quantity. Either `was`/`became` are the embargo's own state and `d` its
      change, or the political-power cost moves to its own field; the rivalry
      strength must not sit in `became` while a cost sits in `d`.
- [ ] `ec_license_granted_*` lines agree: `became - was` equals `d`.
- [ ] `GER_inner_circle_census` and the `ascension` lines agree the same way.
- [ ] `$add_rivalry` and every other clamp site log a `became` that is the real
      post-clamp value and a `d` that equals `became - was`, or they log the
      intended delta in a separate field. No line leaves the reader guessing
      which of the two numbers is true.
- [x] A re-extract of a session shows zero lines where `abs((became - was) - d)`
      exceeds rounding, run as a counted check rather than by eye. The 1936 run
      gives **0 violations over 860 triplet lines**, against 388 in the original
      session. The check was verified to be non-vacuous on the same data: a
      clamped line is present and now agrees with itself -
      `NOR tyranny_election -97.75->-100.00 d=-2.25`, where the pre-fix code
      would have written `d=-5.00`.
- [ ] The GDD triplet rule and the code agree; if the rule has to bend for a
      cost field, `Design Decisions - RU.md:411` says so.
- [ ] No new `error.log` lines attributable to the mod.

## Out of scope

- The 999 service value and the separate window-duration field. Both already
  work; this ticket touches only the three numbers that describe one quantity.
- Adding new log lines. Every fix here is to a line that already exists.

## Verification

Re-extract a session with `extract_sandbox.py` and run the triplet check as a
script: parse every `was -> became d=` line, compare `became - was` against `d`,
and require zero mismatches beyond rounding. The same check found the 388 lines
here, so it is known to work.
## Implementation (2026-11-07)

All four sources fixed in core `common/macros.hml` and
`common/scripted_effects/99_sandbox_scripted_effects.hsl`, then synced outward to
both mods and compiled.

**Class A.**

- `ec_embargo_sent` now reports the embargo as an act: `0 -> 1`, `d = 1`. The
  rivalry strength and the political-power price no longer enter the triplet, so
  the line reads `0.00->1.00 d=1.00`. The strength is still visible on that
  target's `census` line.
- The three `ec_license_granted_*` lines now set `old = 0`, `new = n`, `delta = n`
  for one granted licence, so `became - was == d`.
- `sandbox_log_ger_inner_circle_state` no longer fills the triplet; it sets only
  `slot` and `other`. Two new macros carry the semantics: `_reading` reports a
  state (`was == became`, `d = 0`), and `_done` reports the real `+1` that a
  completed focus produces (`old = count - 1`, `new = count`, `d = 1`).
  `_select`, the overflow/full variants and the `census` call are readings.

**Class B.** `$add_rivalry` now computes `rivalry_change = new - old` after the
clamp and reports that as `d`, in all four branches (the main one and the three
band crossings). `ETH 98.00->100.00` now carries `d=2`, not `d=25`.

### Verification

- Both mods compile clean.
- Compiled output checked per source: embargo `old=0 new=1 delta=1`; licences
  `0/1/1`, `0/2/2`, `0/3/3`; census `old == new`, `delta=0`; `rivalry_change`
  assigned in 16 places in the compiled file.
- Not done: a session run. The criterion asks for a re-extract showing zero
  mismatches, which needs a game session with the fix in place.

## Session result (2026-11-08, 1936-1938)

Re-checked on a fresh run with every earlier fix in place: 1 232 triplet lines,
**4 violations**, down from 388.

The 4 remaining were all the same thing, and it was not one of the four sources
this ticket named:

```
FRA tyranny_election  -97.25->-100.00 d=-5.00
SOV tyranny_focus      86.00->100.00  d=20.00
```

Both are clamp artifacts: `-97.25 + (-5)` would be `-102.25` and `86 + 20` would
be `106`, and the engine clamps to the band before the line is written. So the
delta described an intent the value never took.

Fixed the same way the rivalry term was: both macros now compute the change from
the before and after values. The log gate still tests the intended amount, so a
clamped event is not hidden - it reports the change that happened rather than the
one asked for.

That was the last of the two classes. A run with this in place should show zero.

## Confirmed at zero (2026-11-08, 1936 run)

The clamp fix landed and a fresh session was run to check it: 1936.01 to
1937.01.10, 4 697 `#sandbox` lines, zero mod-attributable `error.log` lines.

```
triplet lines checked: 860
violations: 0
```

The run is not an easy one - 512 of its lines are honour and tyranny, the exact
records that produced the four remaining violations before the clamp fix, and one
of them clamps in this session too:

```
NOR tyranny_election -97.75->-100.00 d=-2.25
```

`-97.75 + (-2.25)` is exactly `-100.00`. The old code would have written `d=-5.00`
here, because it logged the requested amount rather than the change that survived
the band. So the zero is a real zero, not an absence of clamp cases.

All four existing guards also pass on this extract, and the rivalry check judges
3 524 pair-months with no problems.
