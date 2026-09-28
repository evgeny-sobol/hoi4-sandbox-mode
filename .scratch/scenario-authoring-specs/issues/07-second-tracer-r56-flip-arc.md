# 07 - Second tracer: author a gated flip arc in the r56 mod

Status: ready-for-agent
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
