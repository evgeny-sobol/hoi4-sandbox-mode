# 03 - Generate the catalog tables and notes

Status: ready-for-agent
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
