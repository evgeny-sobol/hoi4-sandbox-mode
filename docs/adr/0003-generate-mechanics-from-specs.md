# Generate scenario mechanics from arc specs

Status: accepted

Supersedes ADR-0002's rejected option "generate the HSL arc skeleton from the
spec" (recorded there under Considered Options).

## Context

ADR-0002 made TOML arc specs the source of truth for decisions but kept all
HSL hand-written, rejecting skeleton generation as too risky. Authoring the
first spec by hand showed the remaining duplication: every target pair,
ladder month, telemetry label and pick datum exists both in the spec and in
the catalog, so the same drift the specs were built to kill re-enters through
the code (a tag changed in TOML lingers in HSL). The axis tracer proved the
mechanical parts reproduce the proven hand-written code byte-identically.

## Decision

Mechanics derivable from the spec are generated per arc into a generated
sibling file beside the hand catalog, overwritten on every build: target
seeding, seed actors, ladder tick branches, telemetry blocks, derail arms and
pick data. Hand-written code keeps the shared loops (tick, derail and pick
dispatchers call generated per-arc functions), all content (`fire_*`
functions, events, localisation) and the arcs without specs. The old
hand-written branches of a migrated arc are deleted in the same change, so no
definition exists twice.

## Considered Options

- **Keep all HSL hand-written (ADR-0002 as written).** Rejected: it preserves
  the spec-to-code drift the tracer was built to remove.
- **Generate whole catalog functions.** Rejected: arcs without specs still
  live in the hand catalog; whole-function generation cannot land until the
  last arc migrates.
- **Generate per-arc functions called from the hand dispatchers (chosen).**
  Each migrated arc is self-contained; migration proceeds arc by arc with the
  build green throughout.

## Consequences

- The label inventory scans the generated file too; a label in generated code
  outside the inventory fails the check.
- Spec numbers must match the code dispatcher; a generated call dangles
  otherwise, so the number check runs before any generation.
- Flip gates and remaining aspects follow the same per-arc shape when their
  arcs migrate; the schema grows a field only with a validator, docs and
  tests, as the `key` and ladder content-function fields did.
