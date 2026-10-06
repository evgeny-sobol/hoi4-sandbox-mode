# 28 - Port numeric variant ids to _sandbox-r56

Status: ready-for-agent
Type: bug
Blocked by: issue 27 session box (first live B in vanilla, proving the fix)

## Problem

The stuck-variant root cause from issue 27 (bare-word enum literals do
not survive a HoI4 variable round trip) applies to `_sandbox-r56`
unchanged: 157 lines across three files test
`sandbox_target_variant == a/b`, so every B branch in all 28 arcs is
dead there too (sessions never showed B in r56 either).

## What to build

- Convert `sandbox_target_variant == a/b` to `== 0/1` in
  `common/scripted_effects/99_sandbox_scenarios.hsl`,
  `99_sandbox_scenarios_gen.hsl` and `99_sandbox_arc_hooks.hsl`
  (mechanical regex, same as the vanilla pass; flip-gate and ideology
  arms need a human look since r56 branches carry extra conditions).
- Keep log labels (`sc_variant, a/b`) and spec keys untouched.
- Verify: spec build is a no-op for r56 (no specs yet — confirm),
  all shared guards green, forced recompile clean, no new `error.log`
  lines from scenario files.

## Why it matters

Without the port, r56 keeps playing A-only across 28 arcs: half of every
arc's declared content (all B target sets, ultimatums, tails) never runs,
and the coming N-variant work would inherit the same blindness.

## Acceptance

- [ ] Zero letter-variant branches in the three files; digits everywhere
      a comparison or assignment runs.
- [ ] A session logs `sc_variant b`.
- [ ] Both mods recompile clean; no new `error.log` lines from scenario
      files.

## Out of scope

- N-variant specs for r56 (ticket 26 covers the builder; r56 specs land
  separately).
- Touching vanilla (done in 27).
