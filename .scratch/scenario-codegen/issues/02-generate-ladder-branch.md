# 02 - Generate the ladder tick branch for axis

Status: ready-for-agent
Type: task
Blocked by: 01

## What to build

The crises and peak months from the axis spec drive a generated ladder tick
branch for the arc. The shared hand-written tick loop is untouched; it calls
the generated branch. The mod recompiles clean.

## Acceptance criteria

- [ ] The generated branch fires crises and peak on the spec's months.
- [ ] The shared tick loop is unchanged apart from calling the branch.
- [ ] The mod recompiles clean.
- [ ] A golden test pins the generated text.

## Out of scope

- Telemetry, derail, pick; those are other tickets.
