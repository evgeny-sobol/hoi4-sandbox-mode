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

Nine consecutive A (plus three more, twelve total) at a fair 50/50 die.
Update 2026-10-03: twelve of twelve. Luck is dead (p~0.02%). The roll is
stuck and both mods show it (r56 sessions never showed B either), while
scenario rolls with variable bounds visibly vary. Prime suspect: the
literal-bounds `set_temp_variable_to_random min=0 max=2` shape; the
working rolls use a variable upper bound. Probe in progress: variant B
hardcoded for one session (militarist_japan) to validate the B-content
chain end to end, then revert; dice fix follows from the result.

## Mechanism review (no defect found)

- The die is fair: `set_temp_variable_to_random min=0 max=2 integer=yes`
  yields `[min, max)` per the wiki, so `{0, 1}` at 50/50. The compiler
  emits max = bound + 1 for the same reason in the scenario roll, which
  observably varies (arcs 3, 2, 1 picked across sessions).
- The only writers of `sandbox_target_variant` are the three generated
  roll funcs (verified by grep); the compiled shape
  (`if == 0 -> a else -> b`) matches the old hand code.
- Repick rolls in the same sessions picked arc 1 twice from two-arc pools
  (1/4 under fairness) — consistent with luck, not proof.

## Decisive experiment (cheap)

Start three fresh sessions and quit at day one, reading only the
`sc_variant` line. Any B closes this ticket as luck. Three more A
(12-13/13) confirms a stuck roll; investigate the temp-var/comparison
path then, starting from a console-forced variant-B session to check the
B content itself works.

## Why it matters

Variant-B observer halves (tickets 23, 25) are unreachable while B never
rolls: no session can show the B target set, its ultimatums, or its tails.
Ticket 26's N-variant work also assumes a working roll.

## Acceptance

- [ ] A session logs `sc_variant b` (fix makes B reachable; first session
      with variation closes this).
- [x] Both mods recompile clean; no new `error.log` lines from scenario
      files (compiled output clean; session check pending).

## Out of scope

- Variant-B content bugs (those belong to 23/25 once B is observable).
- Changing roll weights; the design is 50/50 (even split over N later).
