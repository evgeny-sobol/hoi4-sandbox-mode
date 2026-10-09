# 04 - Re-evaluate civil-war backing when a backer's government changes

Status: ready-for-agent
Type: task
Blocked by: 01, 02, 03

## What to build

When a backer's ruling ideology changes while a civil war it is backing is
still running, revisit that backing instead of keeping the choice frozen for
the whole war.

## Why this is deferred

The civil-war backing feature fixes the backer-to-side choice once, at the
start of each war, for predictability (see `../spec.md`). A backer that
switches government mid-war currently keeps backing the old side.

## Done when

- A backer that changes ruling ideology stops backing a side it no longer
  matches.
- The intended follow-up behaviour is decided and implemented: either the
  backer starts backing the newly matching side, or it drops support and
  backs nothing until the war ends.
- The `cw_support` telemetry records the change.

## Open question

Should a government change let a backer switch sides mid-war (start backing
the newly matching side), or only withdraw from a side it no longer matches?
Switching sides is the more interesting behaviour but the larger change;
decide before implementing.
