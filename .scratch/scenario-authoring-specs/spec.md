# Scenario authoring specs

Status: ready-for-agent
Type: enhancement

## Problem Statement

A game designer cannot write a scenario arc in one place. An arc's decisions
live in four surfaces at once: the HSL catalog (`sandbox_set_targets`,
`sandbox_seed_actors`, the `fire_*` functions), hardcoded Python lists in the
boost splicer (`KEYS`, `SPLICES`), the arc list in the graph builder, and
hand-pasted Mermaid blocks in the catalog doc. The same decision edited in one
surface silently disagrees with the others, so the diagram, the focus boost and
the catalog drift apart. This is not hypothetical: the s10 dead-boost lesson, the
`sc_goal` label-case drift (issue 05), and the r56 table-vs-code arc-number
drift are all instances of it.

## Solution

The designer authors one TOML **arc spec** per arc, per mod, under
`docs/scenarios/<id>.toml`. The spec holds only the arc's decisions: aggressor,
target variants, ordered focus paths, ladder months, joiners, an optional
ideology gate, status and notes. Shared tooling in `core/tools/` reads the specs
and derives everything mechanical: the generated
`docs/gdd/Scenarios Catalog.md`, the per-arc Mermaid diagrams, the focus-boost
closure against the real focus trees, and the expected `sc_goal` / `sc_justify`
telemetry labels. Scripted events and effects stay hand-written in the HSL
catalog. The designer never writes Mermaid or focus ids twice.

## User Stories

1. As a game designer, I want to describe an arc in one TOML file, so that I do
   not edit the same decision in four places.
2. As a game designer, I want the focus diagram generated from the arc's focus
   paths, so that the diagram cannot disagree with the boost the director
   applies.
3. As a game designer, I want to list the key focuses of an arc as ordered
   paths, so that the tooling knows which fork side leads to the next focus.
4. As a game designer, I want the prerequisite closure of each path boosted
   automatically, so that a boost behind an unboosted fork is impossible.
5. As a game designer, I want a mutually exclusive fork boosted on the side
   leading to the next focus of the path, and both sides otherwise, so that the
   AI can still walk any path the arc allows.
6. As a game designer, I want to write the arc's rationale as free prose in the
   spec, so that the catalog's explanation is stored beside the decisions it
   explains.
7. As a game designer, I want to record an arc's target variants A and B, so
   that the rolled pair is data, not a hand-maintained table.
8. As a game designer, I want to record the ladder months per arc, so that
   arcs that start at different times still escalate on their own clock.
9. As a game designer, I want to record the joiner rule per arc, so that the
   join lever stays data-driven.
10. As a game designer, I want an optional ideology gate per arc, so that flip
    arcs declare their condition and historical arcs declare nothing.
11. As a game designer, I want to mark an arc `ready` or `draft`, so that the
    catalog shows which arcs ship in the pool and which are authored but not
    yet selected.
12. As a game designer, I want to record the director's arc number when the arc
    has code, so that the spec matches `sandbox_scenario == N`.
13. As a game designer, I want the engine's arc number checked against the code
    dispatcher, so that the table numbering cannot drift from the code again.
14. As a game designer, I want the catalog generated from the specs, so that I
    never hand-paste a table or a diagram.
15. As a game designer, I want a hand check (`--check`) that fails on any
    spec-to-artifact drift, so that a stale catalog or a stale boost is a build
    error, not a silent lie.
16. As a game designer, I want the expected telemetry labels derived from the
    spec, so that a label-casing drift like issue 05 cannot recur.
17. As a game designer, I want the reverse-direction `sc_goal` labels included,
    so that the pair is complete in both directions.
18. As a game designer, I want the catalog to note when the focus graphs are
    stale, so that I know to re-export them before trusting the diagrams.
19. As a maintainer, I want the tooling shared in core but the specs per-mod, so
    that both mods use one implementation over their own content.
20. As a maintainer, I want per-mod `docs/scenarios/` excluded from core sync,
    so that syncing never overwrites a mod's arc specs.
21. As a maintainer, I want the spec's `number` validated against the tick
    dispatcher, so that an orphaned or misnumbered arc is caught.
22. As a maintainer, I want a build-time failure on an unknown focus id, an
    unknown aggressor, or an unreal target tag, so that typos surface at build
    time.
23. As a maintainer, I want only the shared tooling in core and only the specs
    in each mod, so that the two-mod split stays clean.
24. As a maintainer, I want the arc TOML schema documented in the engine GDD, so
    that the schema has one home and the old inline YAML draft is superseded.
25. As a maintainer, I want the tooling proven on two arcs of different shapes
    (a multi-path historical arc and a gated flip arc) before mass migration, so
    that a schema flaw is found on two arcs, not thirty-four.
26. As an agent, I want a single CLI seam with a `--check` mode, so that I can
    verify the whole pipeline without touching game code.
27. As an agent, I want the catalog build to be deterministic, so that a
    `--check` diff is stable.

## Implementation Decisions

**Domain language.** Use the `CONTEXT.md` terms: **Arc spec**, **Path**,
**ready / draft**, **Aggressor**, **Target variant**, **Ladder**, **Join lever**.
The **Block** field is removed (no faction forms) and `plausibility` is removed
(no longer a design axis); `Join lever` no longer mentions a bloc.

**Arc spec schema (TOML), one file per arc per mod:**

- `id` (slug; identity and file name), `number` (integer; written when the arc
  has code, in either status), `status` (`ready` = in the shipped pool; `draft`
  = authored but not selected), `aggressor` (tag), `targets` (table with `a`
  and `b` tag lists), `ladder` (table: `crises_at_month`, `peak_at_month`,
  measured from arc start), `joiners` (table: `select`, `n`), optional `gate`
  (table: `ideology`, `at_phase`), `paths` (list of ordered key-focus lists),
  `notes` (prose).

**Tooling.** A single CLI in `core/tools/`, `build_scenario_catalog.py`, with a
`build` mode and a `--check` mode. `build` generates the catalog and applies the
boost closure; `--check` writes nothing, rebuilds in memory and fails on any
drift. A boost splicer (moved into core, taking `<mod_dir>` like
`extract_arc_hooks.py`) applies `$ai_scenario_focus_boost()` to each path's key
focuses and their prerequisite closure, choosing a fork side by the path order.
The spec files themselves are per-mod and excluded from `sync_core.py`.

**Derivation rules.** The catalog (per-country tables plus Mermaid diagrams) is
built from the specs and the focus graphs under `docs/gdd/National Focuses/`.
Mermaid nodes: keys are boosted (double border), path roots rounded, path
intermediates plain; prerequisite and mutual-exclusion edges come from the graph
data. The focus graph is a required input and must be fresh; `--check` fails
with an "export focus graphs first" message rather than re-exporting.

**Telemetry labels.** The generator emits the expected label set derived from
aggressor and targets: `sc_goal` labels in both directions and `sc_justify`
labels aggressor-to-target. `--check` compares this set against the `.hsl`
catalog, closing the issue 05 class of drift.

**Validation (`--check` and build).** `id` unique; `number` unique and matching
the code dispatcher; aggressor exists in the mod's focus graphs; every target
tag exists; every key focus exists in the aggressor's graph; the boost closure
covers every key. Build-time validation fails hard; `--check` also fails when
the generated catalog or the boost closure differs from what is on disk.

**Placement.** Tooling in `core/tools/` (shared, synced). Specs in
`docs/scenarios/` per mod (never synced). Schema documented in
`docs/gdd/Scenarios.md`, replacing the old inline YAML "generator-ready schema"
block.

**Scope step.** First deliverable is the tooling plus two tracer-bullet arcs:
`axis_expansion` in vanilla (hidden multi-path historical) and a gated flip arc
in r56 (exercises `[gate]`). Mass migration of the remaining arcs is separate
work.

## Testing Decisions

Good tests exercise the CLI's external behaviour: given a set of spec fixtures
and focus-graph fixtures, `build` produces the expected catalog and boost
output, and `--check` exits non-zero exactly when an artifact is stale. Tests
must not assert on parser internals or private functions.

The repo currently has no test harness; the codebase's prior art for "verify a
derived artifact" is the `--check` mode of `sync_core.py` and
`check_sc_labels.py`, plus the compiler exit code used as a build gate. The new
seam is the single CLI: a pytest wrapper runs it against fixture specs and
graphs and asserts exit codes and file contents.

Modules to test:

- `build_scenario_catalog.py` `--check`: green on current fixtures, red after a
  spec edit that is not rebuilt, red on a stale focus graph, red on a label that
  disagrees with the `.hsl` catalog.
- The boost splicer: the closure applied to a fixture graph equals the expected
  focus set, and a fork picks the path-leading side.

## Out of Scope

- Generating the HSL arc skeleton (the `fire_*` / `set_targets` functions) from
  the spec; events and effects stay hand-written.
- A cross-mod check that compares the two mods' specs of the same arc (accepted
  drift for now; possible later).
- Migrating the remaining arcs of either mod.
- Changing the director engine, the ladder mechanics, or the telemetry format.

## Further Notes

- One arc spec per arc per mod is a deliberate choice (see
  `docs/adr/0002-arc-specs-as-toml-source-of-truth.md`): content ids differ by
  mod, so a shared spec would rebuild the coupling being removed.
- r56 marks arcs 9-28 (code present, not in the pool) as `draft` under this
  schema; vanilla arcs are `ready`. Participation in the pool is not a spec
  field; it is a code detail.
- The old YAML "generator-ready schema" block in `docs/gdd/Scenarios.md` is the
  prior draft of this schema and is to be replaced, not kept alongside.
- The tracer-bullet arcs are the proof the schema holds for two different arc
  shapes before the mass migration.
