# 04 - Generate derail branch and pick data for axis

Status: ready-for-agent
Type: task
Blocked by: 01

## What to build

The gone and capitulated derail arms for the axis arc and its pick branch and
pin data are generated from the spec's targets, aggressor and number. The
shared derail and pick loops stay hand-written and call the generated branch.
The mod recompiles clean.

## Acceptance criteria

- [ ] The generated derail branch covers gone and capitulated cases for the
      spec's pairs.
- [ ] The generated pick data carries the spec's number, aggressor and pin.
- [ ] Shared loops are unchanged apart from calling the branch.
- [ ] The mod recompiles clean.
- [ ] A golden test pins the generated text.

## Out of scope

- Ladder, telemetry; those are other tickets.
- Flip gates; the axis arc has none.
