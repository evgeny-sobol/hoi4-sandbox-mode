# 09 - Make the two-embargo ceiling provable from the log

Status: ready-for-agent
Type: task
Blocked by: none

## What to build

The 1936-41 Road to 56 run (configuration 3 of issue 08,
`.scratch/economic-posture/verification-run.md`) shows two sends while the replay
believed two embargoes were already active: DEN -> GRE on 1941.06 and IRE -> HUN
on 1941.11. The replay counts `ec_embargo_sent` minus `ec_embargo_lifted_*` per
actor, and it cannot see the ledger, so the two cases are ambiguous:

- either the ledger really held fewer than two entries and the engine carried
  more embargoes than the ceiling allows (a genuine break), or
- the log over-counts, because a country that Rt56 re-creates (both actors are
  tags the fork reshapes) starts with an empty ledger while its older lines
  remain in the log.

Both actors' histories are consistent with the second reading: DEN shows two
`lifted_gone` lines for the same target (MNC, 1939.12 and 1940.01), which means
the target sat in two ledger slots, and DEN's 1937 embargo of ITA never lifts in
the log at all.

Make the ceiling provable, then re-run configuration 3:

- On `ec_embargo_sent`, write the number of active embargoes *after* the ledger
  write into a field the send does not otherwise use (`age` is 0 for sends and is
  documented as the months held on a lift; either reuse it with a comment or
  extend the documented field meaning in `docs/gdd/Economic Posture.md`).
- Log the ledger slot a send landed in, so the ledger can be reconstructed. The
  shared line carries one `slot`; sends currently put the *rival* slot there,
  which is what makes the two indistinguishable today.
- Add the replay to the checker or a sibling script: read the log, rebuild each
  actor's ledger from the sends and lifts, and fail on a send that reports more
  than two active.
- If the break is real, the fix is the one the code already implies: treat
  `active >= 2` as final (it is), and clear any duplicate ledger entry for a
  target in the same pass that lifts it, so a re-initialised country cannot end
  up with the same target twice.

## Acceptance criteria

- [ ] The replay can name the active count at every send, and the ceiling is
      asserted, not inferred.
- [ ] Configuration 3 re-run: either 0 violations, or every violation names the
      ledger state that produced it.
- [ ] `docs/gdd/Economic Posture.md` documents the field the send now carries.
- [ ] If the code changes, both mods compile and `check_economic_posture.py`
      still passes.

## Out of scope

- Raising the ceiling or making it configurable: the design fixes it at two.
- Resume/wipe semantics for a country that ceases to exist and returns; that is
  a ledger-lifetime question worth its own decision if the re-run shows the
  engine keeps embargoes across a re-creation.
