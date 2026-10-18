# Playtest run, 1936-1938 (economic posture)

Status: partial
Type: evidence

A hands-off AI session on the vanilla mod, run on 2026-10-18 23:34-23:50, to
settle what the code could not settle statically (issue 08). This file records
what was observed, what it settled, and what it did not.

## Session

```
hoi4.exe -hands_off -autosave=YEARLY -historical=no -gamelog
powershell hoi4-bot-session.ps1 -UntilYear 1938 -Historical no
```

- Load marker: `#sandbox ... HAI sandbox_start historical=0` at 1936.01.01.12,
  so sandbox mode was on and the posture code ran.
- End: `target reached: in-game 1939.01.01.01 - the year 1938 is played out`,
  then `stopping the game: window closed on request, process gone within 30s`.
- Saves: `autosave.hoi4` at 1937.01.01 and 1939.01.01 (73 MB), plus the game's
  own `TEST_FAIL_*` test saves it writes alongside.
- Telemetry gate: `sandbox_log_economic` was raised for the run (the commented
  line in `common/on_actions/99_sandbox_on_actions.hsl`) and commented again
  afterwards.

## Three engine rejections found, and fixed

The run started against the first cut of the code and `error.log` reported eight
parse errors from `common/scripted_effects/99_sandbox_scripted_effects.txt`; the
whole file was dropped, so the feature did not exist in that session. The three
causes, all engine semantics rather than HSL syntax:

| Symptom in `error.log` | Cause | Fix |
| --- | --- | --- |
| `unexpected token ... ( 'MATH' )`, `( '-' )`, `( 'months_elapsed' )`, `( 'stamp' )` | a bare arithmetic expression on the left of a trigger comparison compiled to `check_variable = { var=('MATH', '-', 'months_elapsed', 'stamp') ... }` | the elapsed months go through a temp first (`age = months_elapsed - stamp`), then `if age >= 6` |
| `Malformed token: sandbox_ec_partner` | a bare temp name is not a valid `has_opinion` target | the macro reads the scope keyword (`target = PREV`), the form vanilla uses for `target = ROOT` |
| `Malformed token: var:sandbox_ec_partner` (x3) | `create_production_license` rejects a `var:` target | the grant runs from the candidate's scope and names it `target = PREV` |

The next session loaded with `error.log` carrying no line from the posture files
at all.

## Telemetry

`game.log`, `#sandbox ... ec_` lines, 1936.01-1938.12:

- `ec_embargo_sent`: 200, from 99 actors (first: ETH -> ITA on 1936.07.01, band
  80; also ELS -> ENG, PRU -> SOV, VEN -> FRA, ITA -> USA, MAN -> FRA, ...).
- `ec_embargo_lifted_detente`: 5 (HUN -> ITA at 6 months held, BEL -> ITA at 8,
  GSM -> ITA at 6, URG -> ENG at 16, SIA -> GER at 22).
- `ec_embargo_lifted_alliance`: 11 (e.g. SHX -> XIC, PER -> SOV, NOR -> DEN).
- `ec_license_granted_infantry_equipment_1`: 7 (CHI -> SND, SHX -> GDC,
  GSM -> NXM, NXM -> GSM, PHI -> USA, XSM -> NXM, GSM -> XSM); GSM was granted
  twice, 12 months apart.
- `ec_channel_unavailable`: 0 (the positive seller channel is not shipped).

## Invariants checked against the log

`.scratch/scripts/check_economic_posture.py` is static; the log itself was
checked by replaying the events per actor:

- third embargo while two are active: **0**
- re-embargo of a target within six months of a lift: **0**
- `detente` lift before the six-month floor: **0** (and the detente ages - 6, 6,
  8, 16, 22 - show the band check is not always-passing)

## What the run settles

- Spec risk 2 (`send_embargo` needs no threat threshold): **settled in game**,
  200 calls landed and logged.
- Spec risk 3 (`diplo_action_desire` with `market_access_rights`): the plan
  parses and the game raises no error; its effect on AI behaviour was not
  measured.
- Issue 03's in-game items: send, lift with reason, six-month minimum, six-month
  re-embargo block, two-embargo ceiling - all observed. `gone` did not fire (no
  living actor's target disappeared in this run); an alliance or pact lift did
  (11 lines).
- Issue 04: grants happen, only to faction partners at war, one per 12 months,
  and a receiver without the tech was never granted (`_1` equipment throughout,
  which is what the Chinese warlords could field).

## What it does not settle

- Base-game configuration (no By Blood Alone, no Arms Against Tyranny): not run,
  so spec risk 4 (unguarded declarative entries) and ADR-0008's "invisible on
  the base game" remain unverified.
- Rt56 (200 opinion scale): not run.
- Historical (non-sandbox) session: not run.
- `ec_embargo_lifted_gone`: no data point.
- `error.log` of this run carries one unattributed
  `trigger.cpp:835 (invalid trigger scope)` assertion and 13 vanilla engine
  assertions (air wings, theatres); no script error names a posture file, and
  the short pre-fix session showed none, so it is recorded as unexplained rather
  than assigned to this feature.
