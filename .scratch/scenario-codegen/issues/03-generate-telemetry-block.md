# 03 - Generate the telemetry block for axis

Status: ready-for-agent
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
