# 03 - Generate the telemetry block for axis

Status: resolved
Type: task
Blocked by: 01

## What to build

The power, goal and justify sampling for every declared axis pair is
generated from the spec into the gen file, in both label directions where the
convention requires. The old hand-written axis telemetry branches are deleted
in the same change. The mod recompiles clean.

## Acceptance criteria

- [ ] Every spec pair is sampled; no undeclared pair is.
- [ ] Labels match the expected set from the spec inventory.
- [ ] Old hand-written axis telemetry branches are gone, no duplicates remain.
- [ ] The mod recompiles clean.
- [ ] A golden test pins the generated text.

## Out of scope

- Ladder, derail, pick; those are other tickets.

## Verification: PASSED (tests + compile)

- `render_telemetry()` emits `gen_axis_expansion_telemetry()` from spec pairs
  (power per live actor, goal both directions, justify aggressor-to-target);
  verified byte-identical to the deleted hand block modulo the function
  header. The hand s7 branch is now a gen call; no axis label remains in the
  hand catalog and no definition exists twice.
- The label check was reworked for generation: occurrence-based case check
  (a drifted copy can no longer hide behind a correct one) plus a
  hand/gen-duplication check that forces old branches out in the same change.
  Residual missing-label detection is subsumed by the stale-gen comparison.
- Harness at 21/21 (incl. duplication, case-drift and reverse-skip tests).
- Real `build` + `--check` green; full recompile clean.
