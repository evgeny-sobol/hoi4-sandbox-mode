# 02 - Walking skeleton: spec schema, loader, validator, CLI check

Status: ready-for-agent
Type: task
Blocked by: none

## What to build

The single CLI seam for the whole pipeline, proven end to end on one real arc.
The designer's spec is a TOML **arc spec**; the CLI reads a mod's specs,
validates them, and exposes a `build` mode and a `--check` mode. On a valid spec
the CLI succeeds; on a broken spec it fails hard with a message naming the
problem. A test harness drives the CLI as a process (exit code plus output),
matching the repo's existing use of a check mode and compiler exit code as a
build gate.

This ticket delivers the schema, the loader and the validator, not the
generated artifacts: `build` may write nothing yet beyond validating, and
`--check` validates only.

The arc spec carries: `id` (slug), `number` (the director's arc id, written
when the arc has code), `status` (`ready` or `draft`), `aggressor`, `targets`
(variants `a` and `b`), `ladder` (crises and peak month from arc start),
`joiners` (select rule and count), optional `gate` (ideology and phase),
`paths` (ordered key-focus lists) and `notes` prose.

Author one real spec for `axis_expansion` in the vanilla mod as the fixture.

## Acceptance criteria

- [ ] The CLI loads `docs/scenarios/*.toml` and validates every field of the
      schema above.
- [ ] `id` is unique across the mod's specs; `number` is unique across the
      mod's specs.
- [ ] The aggressor exists in the mod's focus graphs.
- [ ] Every target tag exists; every key focus exists in the aggressor's focus
      graph.
- [ ] A spec missing a required field, or naming an unknown focus id, fails
      with a message that names the field and the value.
- [ ] `axis_expansion` validates green in vanilla.
- [ ] A test harness runs the CLI and asserts exit codes and messages.

## Out of scope

- Generating the catalog, diagrams, boosts or labels; those are later tickets.
