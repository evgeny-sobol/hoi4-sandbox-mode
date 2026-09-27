# 01 - Exclude per-mod scenario specs from core sync

Status: resolved
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

## Verification: PASSED (static + live sync run)

- Added `EXCLUDED_TREES = ("docs/scenarios/",)` to `core/tools/sync_core.py`
  (mirrored into the authoritative core repo): `core_files()` skips anything
  under the tree, and the shared-list loop skips it too, so a future shared
  entry inside the tree cannot sweep specs in. Docstring updated.
- Live run with a probe spec: `--check` reported no new drift with
  `docs/scenarios/probe.toml` present; a real sync run left the probe byte
  intact; editing the probe caused no drift. File set still 51 core files.
- Side effect caught and reverted: the live sync run overwrote the mod's local
  `AGENTS.md` additions (pre-existing drift); restored via git checkout.
