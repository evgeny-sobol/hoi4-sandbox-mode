# 05 - Label check over the generated file plus golden tests

Status: ready-for-agent
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
