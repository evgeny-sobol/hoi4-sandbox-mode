# 03 - Generate the catalog tables and notes

Status: resolved
Type: task
Blocked by: 02

## What to build

The `build` mode writes the generated `Scenarios Catalog.md` from the specs.
The designer never hand-pastes a table again: the catalog's per-country tables
(aggressor, targets A and B, key focuses, status) and each arc's `notes` prose
are emitted from the spec data. Arcs grouped as `ready` versus `draft`. The
generated file is committed, and `--check` fails when the file on disk differs
from what the specs produce, so a spec edit that is not rebuilt is a build
error.

## Acceptance criteria

- [ ] `build` writes the catalog from the specs alone; no hand-written table
      survives.
- [ ] Each arc's row shows aggressor, both target variants, its key focuses and
      its status.
- [ ] `ready` and `draft` arcs are grouped per the schema.
- [ ] Each arc's `notes` prose appears in the catalog.
- [ ] Editing a spec without rebuilding makes `--check` fail; rebuilding makes
      it green.
- [ ] The generated catalog is deterministic: two builds produce byte-identical
      output.

## Out of scope

- Diagrams, boosts and telemetry labels; those are later tickets.

## Verification: PASSED (tests + live build)

- `build` writes `docs/gdd/Scenarios Catalog.md` from the specs alone; the old
  hand-pasted file is replaced. Table shows aggressor, both variants, key
  focuses and status; arcs grouped `ready`/`draft`; each arc's `notes` appear.
- Spec edit without rebuild makes `--check` fail; rebuild greens it.
- Determinism covered by `test_build_deterministic` (two builds byte-identical).
- Pool/excluded-majors prose moved into `docs/gdd/Scenarios.md` (Selection
  area) so no content was lost; the redundant Arc-anatomy section dropped
  (covered by Selection and ADR-0001).
