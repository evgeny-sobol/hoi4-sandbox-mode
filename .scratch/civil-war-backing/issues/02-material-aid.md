# 02 - Material aid

Status: resolved
Type: task
Blocked by: 01

## What to build

A backer gives the kin side military access and, for as long as the war
runs, a monthly equipment grant scaled by the backer's strength with a
fixed floor.

## Acceptance criteria

- [ ] The kin side receives military access from the backer.
- [ ] The kin side receives equipment each month the war runs, at a volume
      that scales with the backer's strength and never drops below the floor.
- [ ] A weak major gives noticeably less than a strong one.
- [ ] The grant stops when the war ends.

## Answer

give_military_access on first backing; monthly send_equipment scaled by
num_of_military_factories (floor 100, cap 2000) from sandbox_cw_backing_monthly(). Stops when the war ends via the ledger prune. Observer run clean.
