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

State after the 2026-10-18 run (`.scratch/economic-posture/verification-run.md`):
configuration 1 (vanilla, sandbox, full DLC) ran to 1939.01.01 and settled the
embargo and licence behaviour - 200 `ec_embargo_sent`, 5 `detente` lifts, 11
alliance lifts, 7 licence grants, and 0 violations of the two-embargo ceiling,
the six-month cooldown and the six-month floor when the log is replayed per
actor. The run also caught three engine rejections in the first cut of the code
(an arithmetic expression in a trigger comparison, a bare temp as a
`has_opinion` target, a `var:` licence target); after the fix, no posture line
reaches `error.log` at all. Static evidence from the same session:

```
$ python .scratch/scripts/check_economic_posture.py          # from either mod
problems: 0
```

and the checker's negative case, with a `-50` edited to `-60` in a copy and a
fourth plan for `ENG` carrying `send_embargo`:

```
FAIL ...:28: ENG_is_rival_contain equipment_market_trade_desire value is '-60', expected -50
FAIL ...:33831: unexpected plan ENG_is_rival_extra
FAIL ...:33835: send_embargo belongs in a scripted effect, not here
problems: 3
```

Still owed: configuration 2 (base game, no By Blood Alone or Arms Against
Tyranny - settles spec risk 4 and the unguarded declarative entries),
configuration 3 (Rt56 on the 200 scale), a historical (non-sandbox) session, and
a data point for the `gone` lift reason. Risk 5 (licensing DLC) is already
answered from vanilla evidence and needs no run; risk 2 is settled by this run;
risk 3's entry parses but its behavioural effect was not measured.
