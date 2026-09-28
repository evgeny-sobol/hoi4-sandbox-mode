# 08 - Document the arc spec schema in the engine GDD

Status: ready-for-agent
Type: task
Blocked by: 02

## What to build

The arc spec schema has one home in the engine GDD. The old inline YAML
"generator-ready schema" block is replaced by the TOML schema as it actually
shipped: every field, what it means, and which are optional, using the project's
domain terms (Arc spec, Path, ready/draft, Aggressor, Target variant, Ladder,
Join lever). The `Block` field and the `plausibility` field are gone, and the
Join lever description no longer mentions a bloc.

## Acceptance criteria

- [ ] The engine GDD documents the TOML arc spec schema and every field.
- [ ] The old YAML "generator-ready schema" block is removed, not kept beside
      the new one.
- [ ] The documented fields match the validator exactly (same names, same
      required/optional split).
- [ ] The prose uses the CONTEXT.md terms and drops `Block` and `plausibility`.

## Out of scope

- Documenting the tooling internals; only the schema is documented here.
