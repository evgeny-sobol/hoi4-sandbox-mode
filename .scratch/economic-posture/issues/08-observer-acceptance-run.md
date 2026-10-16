# 08 - Observer acceptance run

Status: ready-for-human
Type: task
Blocked by: 02, 03, 04, 05, 07

## What to build

The session that proves the feature rather than describing it. Run three
configurations and paste the evidence into this file.

1. Vanilla mod, observer, sandbox mode, full DLC: does a Feud pair embargo, does
   that embargo lift below 60, is a licence granted to a faction partner at war,
   does the market exclusion show up in actual purchases?
2. Vanilla mod, base game (no By Blood Alone, no Arms Against Tyranny): nothing
   happens, `error.log` clean, no `ec_` lines beyond the licence path.
3. Rt56, observer: the same as (1) on the 200 opinion scale.

Evidence per configuration: the `ec_` lines from `game.log`, the `error.log`
tail, and the `spec.md` acceptance checklist with every box ticked or carrying a
written reason.

## Acceptance criteria

- [ ] All three configurations run at least five in-game years from 1936.
- [ ] Every `spec.md` acceptance box is ticked or carries a written reason it
      cannot be.
- [ ] Risks 1-5 of the spec are replaced by observations, or explicitly marked
      unresolved with what would settle them.
- [ ] The checker output (06) is quoted as part of the evidence.
- [ ] Anything the run contradicts becomes a new issue, not a silent edit of
      the spec.

## Out of scope

- Tuning the starter values to final numbers. That is a follow-up session with
  real telemetry, and the issue that opens it names what this run measured.
