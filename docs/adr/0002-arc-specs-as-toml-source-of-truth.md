# Author arcs as per-mod TOML specs; tooling derives the rest

Status: partially superseded by ADR-0003 (the "no HSL generation" option only;
specs stay the source of truth for decisions).

## Context

Authoring a scenario arc meant editing several places at once: the HSL catalog
(`sandbox_set_targets`, `sandbox_seed_actors`, `fire_*` functions), hardcoded
Python lists in the boost splicer (`KEYS` in `boost_focus_ancestors.py`,
`SPLICES` in `add_vanilla_focus_boosts.py`), the arc list in
`build_scenario_graphs.py`, and hand-pasted Mermaid blocks in
`docs/gdd/Scenarios Catalog.md`. The same decision lived in four places, so the
diagram, the boost and the catalog could disagree (the s10 dead-boost lesson;
the 05 label-case drift; the r56 table-vs-code arc-number drift).

## Decision

Every arc gets one TOML **arc spec** per mod under `docs/scenarios/<id>.toml`.
It records the arc's decisions only: aggressor, target variants, ordered focus
paths, ladder months, joiners, optional ideology gate, status, and notes. The
shared tooling in `core/tools/` reads the specs and derives: the generated
`Scenarios Catalog.md`, the per-arc Mermaid diagrams, the focus-boost closure
against the real focus trees, and the expected `sc_goal` / `sc_justify` labels.
Scripted events and effects stay hand-written in the HSL catalog.

Specs are **per-mod** (one per arc per mod), not shared in core, because arc
content ids differ by mod. Each mod's `docs/scenarios/` is excluded from
`sync_core.py`; only the tooling is shared.

## Considered Options

- **Shared spec in core, per-mod content block.** Rejected: it merges two
  mods' data into one file and rebuilds the cross-mod coupling we are removing.
- **Keep authoring in HSL plus the hardcoded Python lists.** Rejected: it keeps
  the four-sources-of-truth problem this replaces.
- **Generate the HSL arc skeleton from the spec too.** Rejected: the fire/peak
  functions carry event logic, not arc decisions.

## Consequences

- `build_scenario_catalog.py --check` (and a `--check` on the boost splicer)
  makes spec-to-artifact drift a build error, replacing hand-kept agreement.
- The two mods' specs of the same arc can drift; a cross-mod check is a later
  option, not part of this decision.
- `docs/gdd/Scenarios.md` carries the TOML schema; the old inline YAML
  "generator-ready schema" block is superseded by it.
