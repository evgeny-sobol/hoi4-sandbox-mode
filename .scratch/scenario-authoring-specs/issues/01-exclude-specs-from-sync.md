# 01 - Exclude per-mod scenario specs from core sync

Status: ready-for-agent
Type: task
Blocked by: none

## What to build

Arc specs live per mod under `docs/scenarios/`, while the tooling that reads
them is shared in core. Core sync must never copy, overwrite, or carry a mod's
`docs/scenarios/` tree, so a sync run cannot clobber an author's arcs. After
this change, running the sync check and the sync itself leaves each mod's
`docs/scenarios/` untouched, and the sync reports clean.

## Acceptance criteria

- [ ] `sync_core.py --check` reports `drifted=0` with a `docs/scenarios/`
      present in a mod.
- [ ] A sync run does not create, overwrite, or delete any file under a mod's
      `docs/scenarios/`.
- [ ] Editing a spec does not make the sync check report drift.
- [ ] No change to which files the sync otherwise copies.
