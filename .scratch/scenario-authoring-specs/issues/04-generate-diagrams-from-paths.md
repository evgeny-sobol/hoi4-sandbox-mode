# 04 - Generate the focus diagrams from paths

Status: resolved
Type: task
Blocked by: 02

## What to build

The designer picks key focuses as ordered **paths**; the diagrams are generated
from those paths and the focus graph, so a diagram can never disagree with the
boost. The catalog gains the per-arc Mermaid diagrams: key focuses
double-bordered, path roots rounded, path intermediates plain, with the
prerequisite and mutual-exclusion edges taken from the graph data. The focus
graph is a required input and must be fresh; when it is stale the check fails
with a message telling the author to export the focus graphs first, rather than
re-exporting silently.

## Acceptance criteria

- [ ] Each arc's diagram is built from its `paths` and the focus graph.
- [ ] Key focuses are double-bordered, path roots rounded, path intermediates
      plain.
- [ ] Prerequisite and mutual-exclusion edges match the focus graph.
- [ ] `--check` fails with an "export focus graphs first" message when the graph
      is older than the specs, and does not re-export.
- [ ] Editing a spec changes its diagram; `--check` catches the change.

## Out of scope

- The boost splice that acts on the same paths; that is the next ticket.

## Verification: PASSED (tests + live build)

- Diagrams built from spec `paths` plus the focus graph, over the boost set
  itself, so diagram and boost agree by construction. Roles: keys
  double-bordered, roots rounded, intermediates plain (and boosted, per the
  corrected legend).
- Prerequisite and mutual-exclusion edges parsed from the graph data.
- `test_stale_graph_fails_with_export_message`: a graph older than its specs
  fails `--check` without re-exporting.
- Spec edit changes the diagram; `--check` catches it (`test_check_catches_spec_edit`).
