# Telemetry triplet and rivalry growth (vanilla 1936-1940 session)

## Problem Statement

A manual vanilla session of `_sandbox` (no Road to 56) ran 1936.01.01 to
1940.12.11. The telemetry extract holds 4927 `#sandbox` lines and `error.log`
carries fewer than 500 lines, none attributable to the mod. The scenario director
behaved correctly for the whole run: four arcs, three repicks, and telemetry
never went quiet.

Two defects show up in that data.

## Findings

1. **The triplet rule is broken on 388 lines.** `docs/gdd/Design Decisions -
   RU.md:411` calls the rule hard: `old` is the value before, `new` after,
   `delta` their difference. 388 lines in this session break it. Two distinct
   classes:

   - 351 lines where `delta` is not a difference at all. `ec_embargo_sent`
     (230) writes `0.00->78.00 d=-100.00`: `new` holds the rivalry strength and
     `delta` holds the political-power price. `ec_license_granted_*` (61) writes
     `0.00->1.00 d=0.00`. `GER_inner_circle_census` (57) writes the same number
     into all three fields.
   - 37 lines where `delta` is correct but `new` is clamped, so the two do not
     agree: `ETH 98.00->100.00 d=25.00`. The delta describes the intent, `new`
     the result, and nothing says which.

   A reader who trusts `delta` is wrong on 351 lines; a reader who trusts
   `new - old` is wrong on 37. The rule exists so neither has to guess.

2. **A minor holds a permanent Feud at maximum strength.** Albania sits in
   France's slot 2 from 1936.01.01 and grows +2 every month without a single
   counterweight, reaching 100 by 1938.02.01 and staying there until the session
   ends in 1940.12. `honor=-64.95`, no war, no shared cores, no pact. Every other
   country that seeded Albania (ROM, POR, BUL) released it; only France keeps it.

## Tickets

- `01` - the triplet rule is broken on 388 lines (351 genuine, 37 clamp).
- `02` - the Albania symptom: a minor at maximum strength for two years.
- `03` - the cause: the "they hold a state we core" term reads `is_core_of(PREV)`
  from inside the rival's scope, so it asks whether the rival owns a state it
  cores itself. Always true, so every pair gains `+2` every month. Found with the
  per-term probe on a 1936-1941 session: the term fires on all 17 605 probe
  lines, and no line has it firing zero.

## Not a finding

`g=` in the census was suspected of not tracking guarantees. It is correct:
4 -> 3 -> 1 -> 0 exactly matches the four withdrawals (BEL 1937.08, CZE and YUG
1938.09, ROM 1940.03).
