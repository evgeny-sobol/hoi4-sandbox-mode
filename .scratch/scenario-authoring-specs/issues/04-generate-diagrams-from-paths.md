# 04 - Generate the focus diagrams from paths

Status: ready-for-agent
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
