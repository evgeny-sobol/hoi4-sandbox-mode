# 07 - Observer acceptance run

Status: resolved
Type: task
Blocked by: 01, 02, 03, 04, 05, 06

## What to build

A sandbox observer session to 1938 (or later) that proves the whole rule: the
AI runs at most one event/mission civil war, a focus ignition may overlap it,
the slot is held by a 0..12 month cooldown after a capped war ends, and `cool=`
appears in the `cw_` lines. Run it for both mods.

## Acceptance criteria

- [ ] The `docs/gdd/Civil Wars.md` acceptance checklist passes, or the failures are recorded.
- [ ] No AI event/mission ignition starts at `cap=1` or `cool>0`.
- [ ] At least one focus ignition starts while `cap=1`.
- [ ] No new `error.log` entries from sandbox files.

## Answer

Partial. Ran sandbox observers to 1938 and to 1943.

Passed: `cool=` is present in every `cw_` line (490/490 in 1936-38); the cap
blocked 373 event/mission fuses; the cooldown rolled 5 months when SPR ended
(1939-06-11) and the next war waited to 1939-11-05; a focus ignition
(`TUR_restack_the_officer_corps`) fired at `cap=1` (1941-07-24).

Recorded failures:
1. Event/mission fuses still leak past `cap=1`: the count reached 2 via
   D04/POL (1937-08-14) and D04/BRA (1938-04-20), with no `cw_ignition` /
   `cw_event` / `cw_defer` first. These are ungated fuses in the known POL/BRA
   families, not a regression from this change.
2. `cool=` is wrong on a line whose ROOT is a freshly created rebel tag: its
   `months_elapsed` is 0 until the next weekly init, so `cool` reads the
   absolute `cooldown_until` (e.g. `cool=46` on the 1939-11-05 declare). The
   gate is unaffected for established actors; only the telemetry (and a fresh
   tag's own view) is off.

No new `error.log` entries from sandbox files.
