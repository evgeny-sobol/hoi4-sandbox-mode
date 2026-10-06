# 04 - Generate derail branch and pick data for axis

Status: resolved
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

## Verification: PASSED (tests + compile)

- `render_derail()` emits `gen_axis_expansion_derail()` (gone/capitulated
  arms plus per-variant target arms with arity from the spec), verified
  byte-identical to the deleted hand branch modulo the function header.
- Pick data renders as three small functions (`gen_axis_expansion_pin`,
  `gen_axis_expansion_eligible`, `gen_axis_expansion_pick_log`) hosted at the
  three dispatcher positions; shared loops unchanged apart from the calls.
- The short pin/pick slug required a new optional spec field `key`
  (documented in the GDD schema); variant target lists are validated to 1-4
  entries (the derail macro range).
- Harness at 23/23 (incl. key-shape, arity and golden tests); real `build` +
  `--check` green; full recompile clean with all four gen calls in the
  compiled dispatcher and no stale hand branches.
