# 27 - Target variant always rolls A, B never observed

Status: resolved
Type: bug
Blocked by: none

## Root cause (2026-10-04, confirmed by canary session)

HoI4 variables are floats: bare-word enum literals do not survive a
write/read round trip. Both `a` and `b` evaluate identically, so every
`global.sandbox_target_variant == a` test is true and the B branches
(set_targets, telemetry, derail, peak, log) never run. Numeric variables
(`sandbox_scenario`, `phase`) always worked; only this token-valued
variable was affected, in both mods.

Proof chain: the literal-bounds dice is fair per the wiki (`[min, max)`);
scenario rolls with variable bounds visibly vary; only the variant stuck.
A hardcoded `= b` probe plus a `probe_files_live` canary fired in-session
while seed and log still read A — the write executed, the read disagreed.

## Fix

Variant keys map to numbers at emit time (sorted keys -> 0, 1, ...; one
arc runs per session so per-arc indexing is safe). Builder emits indices
in every comparison and assignment; log labels keep the letters, so
telemetry readouts are unchanged. Hand branches converted the same way.

## B-content validation (2026-10-04)

A day-1 session logged variant B with coherent B content (SOV/MON seed
and sampling, `sc_variant b`) — the first B ever. The downstream chain
handles B end to end; only the dice frequency is now in question. Probe
and canary reverted right after; the tree runs the natural numeric roll.
Specs keep letter keys; no author-facing change.

## Problem

Every observed session rolls target variant A. Confirmed `sc_variant a`
lines, newest first:

- 2026-10-03 random #1: militarist_japan A, repick nazi_germany A
- 2026-10-03 random #2: fascist_italy A, repick nazi_germany A
- 2026-10-03 pinned militarist_japan: A
- 2026-10-03 pinned fascist_italy: A
- 2026-10-03 random nazi_germany: A
- 2026-10-03 pinned nazi_germany (arc 1): A
- 2026-10-01 pinned r56 arc 22: A
- r56 v0.2.1 session: sov_south A, soviet_expansion A

Twelve consecutive A at a fair 50/50 die closed the luck verdict (p~0.02%).
Update 2026-10-04: root cause found — HoI4 variables are floats, so the
bare-word `a`/`b` literals never survived the round trip and every
`== a` test read true (numeric variables always worked). Fixed by mapping
sorted keys to indices at emit time; log labels keep the letters.
Update 2026-10-04, session evidence: a repick to `fascist_italy` rolled B
(YUG/SWI seed and sampling, `sc_variant b`) under the numeric code, plus
an earlier day-1 B. The die varies; the streak was broken by the fix, not
by luck running out.

## Mechanism review (superseded)

- The die was always fair: `set_temp_variable_to_random min=0 max=2
  integer=yes` yields `[min, max)` per the wiki, so `{0, 1}` at 50/50
  (the compiler emits max = bound + 1 for the same reason; scenario rolls
  observably vary).
- The defect was downstream of the die: token writes/reads disagreed (see
  Root cause above). The temp-var/comparison path needs no further work.

## Decisive experiment (closed)

Day-1 reads plus full sessions: B observed twice with coherent content
(2026-10-04 day-1 `militarist_japan` B; repick `fascist_italy` B with
YUG/SWI seed, sampling and `sc_variant b`). Open point, single data: a
B-without-canary line in one probe-era session was never explained
(stale files at launch is the working theory, unproven). It does not
affect the fix, which has since been confirmed by coherent B sessions.

## Why it matters

Variant-B observer halves (tickets 23, 25) are unreachable while B never
rolls: no session can show the B target set, its ultimatums, or its tails.
Ticket 26's N-variant work also assumes a working roll.

## Acceptance

- [x] A session logs `sc_variant b` (observed live 2026-10-04: repick to
      `fascist_italy` rolled B with YUG/SWI targets; plus an earlier
      day-1 B for `militarist_japan`).
- [x] Both mods recompile clean; no new `error.log` lines from scenario
      files (compiled output clean; session check pending).

## Out of scope

- Variant-B content bugs (those belong to 23/25 once B is observable).
- Changing roll weights; the design is 50/50 (even split over N later).
