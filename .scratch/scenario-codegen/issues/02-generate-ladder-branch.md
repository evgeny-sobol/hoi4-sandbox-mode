# 02 - Generate the ladder tick branch for axis

Status: resolved
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

## Verification: PASSED (tests + compile)

- `render_gen_hsl()` emits `gen_axis_expansion_tick()` from the spec ladder
  months; the hand tick loop calls it at the old branch position and the old
  axis branches are deleted, with no duplicate definitions left.
- The rung content functions are new optional spec fields
  (`ladder.crises_func` + `ladder.peak_func`, validated as a pair of HSL
  identifiers); absent means no generated tick branch. Documented in the GDD
  Arc schema section.
- Arc-hooks regen unaffected (set_targets/seed_actors untouched): regenerated
  file byte-identical.
- Harness at 21/21 (incl. the pair test); real `build` + `--check` green;
  full recompile clean with the dispatcher calling the generated branch.
