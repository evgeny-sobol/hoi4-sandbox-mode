# 07 - Second tracer: author a gated flip arc in the r56 mod

Status: resolved
Type: task
Blocked by: 03, 04, 05, 06

## What to build

The schema is proven on a second, differently shaped arc in the other mod, so a
schema flaw is found on two arcs rather than on the full migration. Author one
real r56 spec for a flip arc: it exercises the optional ideology `gate`, carries
`status` and `number`, and has a different path shape from the vanilla arc. With
it in place, the full build and check pass in r56 for both arc shapes together,
and the generated catalog and diagrams cover the r56 arc.

## Acceptance criteria

- [ ] One r56 spec with a `[gate]`, a `status` and a `number` validates green.
- [ ] `build` and `--check` pass in r56 with both tracer arcs present.
- [ ] The generated r56 catalog shows the gated arc and its diagram.
- [ ] The boost splice covers the r56 arc's paths.
- [ ] The expected telemetry labels for the r56 arc are emitted and checked.

## Out of scope

- Migrating the remaining r56 arcs; that is separate work.

## Verification: PASSED (tests + live build + compile)

- `docs/scenarios/fascist_britain.toml` (r56, arc 5): aggressor ENG, targets
  A FRA/SOV and B GER/ITA (match the code dispatcher), ladder 12/30 (match
  the tick thresholds), joiners top-2, `[gate]` fascism at crises (match the
  derail arm), two paths sharing the flip entry, `status = "ready"`.
- `build` + `--check` green in r56; generated catalog shows the arc, its
  notes, its diagram and its label set (8 goal + 4 justify).
- Splice: 22 expected boosts, 17 added to `uk.include` (5 already placed by
  hand); add-only migration mode left other arcs' boosts untouched; 0
  deletions. Full r56 recompile clean.
- New machinery proven by this ticket: spec-number-vs-dispatcher check,
  strict/migration splice modes (add-only plus notes until every coded arc
  has a spec), direction-aware label coverage (reverse justify belongs to
  another arc). Harness at 19/19.
- Known state: the generated r56 catalog covers 1 of 28 arcs until migration;
  the old hand catalog survives in git history.
