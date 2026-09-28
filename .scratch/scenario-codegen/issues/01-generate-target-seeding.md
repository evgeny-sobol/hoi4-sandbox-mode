# 01 - Generate target seeding for axis

Status: resolved
Type: task
Blocked by: none

## What to build

The generator emits a generated HSL sibling file holding the axis arc's
target seeding and actor seeding as `gen_axis_set_targets()` and
`gen_axis_seed()`, derived from the spec's targets and aggressor. The hand
dispatcher calls them in the axis branches, and the old hand-written axis
branches are deleted in the same change, so no definition exists twice. The
mod recompiles clean. This first slice proves the generation shape every
later slice follows.

## Acceptance criteria

- [ ] The generated file holds both per-arc functions with the spec's tags.
- [ ] The hand dispatcher calls them; no duplicate definitions remain.
- [ ] The mod recompiles clean.
- [ ] A golden test pins the generated text for the axis spec.

## Out of scope

- Ladder, telemetry, derail, pick; those are later tickets.

## Verification: PASSED (tests + compile)

- `render_gen_hsl()` emits `gen_axis_expansion_set_targets()` and
  `gen_axis_expansion_seed()` from the spec into the new
  `99_sandbox_scenarios_gen.hsl` (do-not-edit header); the hand dispatcher
  calls them and the old axis branches are deleted, with no duplicate
  definitions left.
- `extract_arc_hooks.py` learned a spec fallback (`load_spec_arcs`), since
  generated branches carry no tags to parse; the regenerated
  `99_sandbox_arc_hooks.hsl` is byte-identical for axis (git diff empty).
- Golden test pins the exact gen text; harness at 20/20.
- Full recompile clean; the compiled dispatcher calls the generated
  functions and the compiled gen file defines them.
