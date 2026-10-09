# 01 - Backing ledger and public stance

Status: ready-for-agent
Type: task
Blocked by: none

## What to build

Each week, find every ongoing civil war, resolve each side's ruling
government, and for every major whose government matches one side (the kin
side) record a backing. On first sight, shift opinion: positive toward the
kin side, negative toward the rival side. Log `cw_support`. Freeze the
choice at first sight and clear it when the war ends.

Gates: only major powers (the engine's `is_major`); AI only; skip a major's
own civil war; skip when the major is at war with the war's original tag;
skip when the major is itself in a civil war or near collapse. Ideology is
the government group (democratic, fascism, communism, neutrality); no
proximity requirement.

## Acceptance criteria

- [ ] In an observer session, a civil war between two governments yields one
      `cw_support` line per matching major, naming the kin side.
- [ ] The kin side receives a positive opinion modifier and the rival side a
      negative one.
- [ ] A major already at war with the war's original tag, or itself in a
      civil war, produces no `cw_support` for that war.
- [ ] No player-controlled major is forced to back a side.
- [ ] Backing applies once per war per major and is cleared when the war ends,
      so a later war can be backed fresh.
