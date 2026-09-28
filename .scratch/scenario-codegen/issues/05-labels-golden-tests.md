# 05 - Label check over the generated file plus golden tests

Status: resolved
Type: task
Blocked by: 03

## What to build

The expected-label inventory scans the generated file as well as the hand
catalog, so generated log lines obey the same lowercase pair contract. The
harness pins the full generated text for the axis spec, and the check fails
when the generated file on disk differs from what the spec produces.

## Acceptance criteria

- [ ] A label present in generated code but missing from the inventory fails
      the check, naming the label.
- [ ] A label differing in case fails the check.
- [ ] Golden tests pin the generated mechanics text for the axis spec.
- [ ] A stale generated file fails `--check`; rebuilding greens it.

## Out of scope

- Game behaviour changes; generation reproduces proven behaviour.

## Verification: PASSED (tests)

- A rogue label hand-added to the generated file fails `--check` naming the
  label (`test_gen_rogue_label_detected`); hand-catalog labels outside the
  inventory stay skipped for arcs without specs.
- Case drift fails per occurrence, so a drifted copy cannot hide behind a
  correct one; duplication across hand and generated files fails with the
  delete-the-branch message.
- Duplication is arc-aware: the checker attributes each hand occurrence to
  its enclosing `sandbox_scenario == N` guard, so a pair shared by two arcs
  (each arc logs its own direction) does not false-positive
  (`test_shared_pair_no_false_positive`). Verified live on the r56 britain
  migration, whose pairs overlap other arcs.
- Golden tests pin the full generated mechanics text for the axis spec
  (all eight per-arc functions); a stale generated file fails `--check`.
- Harness at 25/25; real `build` + `--check` green in both mods with no code
  changes (tool-only change, no recompile needed).
- Incidental find: a regex name collision (`ARC_GUARD_RE` defined twice, the
  anchored copy winning) silently disabled arc tracking; fixed by renaming to
  `ARC_NUM_RE`.
