# 06 - Observer session and ADR supersession

Status: ready-for-agent
Type: task
Blocked by: 02, 03, 04

## What to build

An observer session with the generated axis mechanics proves the game behaves
as before: pick, variant, ladder, telemetry and ignition-or-derail read
correctly off the checklist, and no scenario-attributable lines appear in the
error log. ADR-0002 is superseded by a new ADR recording the reversed
direction.

## Acceptance criteria

- [ ] Observer session shows pick, variant, ladder phases, target lines and
      ignition or derail for the axis arc.
- [ ] No scenario-attributable lines in the error log.
- [ ] A new ADR supersedes ADR-0002 with the generation direction and why.
- [ ] Both mods recompile clean.

## Out of scope

- Migrating any further arc; each is its own change.

## Progress

- Done: ADR-0003 written, ADR-0002 marked partially superseded.
- Done: forced recompile of both mods clean (293 + 470 files, exit 0).
- Pending (needs a game run): observer session with the generated axis
  mechanics — pick, variant, ladder phases, target lines and ignition or
  derail off the checklist, plus a scenario-clean error log.
