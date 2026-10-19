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

## Configuration 2: base game, no DLC (2026-10-19)

The same command with all 35 installed DLC disabled through the launcher
(`dlc_load.json` lists every one of them under `disabled_dlcs`):

```
hoi4.exe -hands_off -autosave=YEARLY -historical=no -gamelog
```

- Disabling took effect: the run raises 9 `game rule ... does not exist` errors
  for rules whose `required_dlc` is off (`LIT_ai_behavior` / `EST_ai_behavior`,
  No Step Back), 5 missing-equipment-entity errors and 2 unknown-character
  errors, none of which the full-DLC run had. Sandbox mode was on
  (`sandbox_start historical=0`), the telemetry gate was raised for the run.
- End: `target reached: in-game 1939.01.05.03 - the year 1938 is played out`,
  window closed on request.
- `error.log`: 1285 lines, **0 of them from `99_sandbox*`** and 0 mentioning
  `equipment_market`, `embargo`, `create_production_license` or
  `market_access`. The unguarded declarative market entries parse clean without
  Arms Against Tyranny: **spec risk 4 is settled**.
- `ec_` lines: 4, all licences, no embargo:

```
1937.08.01 MON ec_license_granted_infantry_equipment_1 age=19 other=SOV
1937.08.01 PRC ec_license_granted_infantry_equipment_1 age=19 other=SOV
1938.08.01 MON ec_license_granted_infantry_equipment_1 age=12 other=SOV
1938.08.01 PRC ec_license_granted_infantry_equipment_1 age=12 other=SOV
```

- Embargoes: 0 in 36 months, against 200 in the full-DLC run - the By Blood
  Alone guard holds.
- Licences: still granted. Death or Dishonor became free and was permanently
  integrated into the base game in patch 1.14.3, and this machine runs 1.19.3.0,
  so `has_dlc("Death or Dishonor")` is true even with every launcher-visible DLC
  disabled: there is no `dlc004_*` package, and the `allow_licensing` game rule
  (whose `required_dlc` names DoD) exists at runtime, while rules of genuinely
  absent DLC are dropped with `game rule ... does not exist`. **The licence
  guard is therefore a pass-through on current builds**: licensing is base
  content in practice, and a "no DLC" install still grants licences. The guard
  stays for hosts older than 1.14.3, but ADR-0008's "no licence on the base game"
  cannot be observed on a modern install.
- Consequence for the acceptance list: the base-game item is met for embargoes
  and the market, and unobservable for licences.

## Configuration 3: Road to 56, 1936-1941 (2026-10-19)

The fork with The Road to 56, full DLC, telemetry gate raised in the fork's own
`on_actions`:

```
hoi4.exe -hands_off -autosave=YEARLY -historical=no -gamelog
hoi4-bot-session.ps1 -UntilYear 1941 -Historical no
```

- Active mods (system.log): Sandbox Mode Overhaul for The Road to 56, The Road to
  56, and three cosmetics. Load markers: `#sandbox Mode Overhaul for The Road to
  56 v0.3.0` and `sandbox_start historical=0` at 1936.01.01.12.
- End: `target reached: in-game 1942.01.04.01 - the year 1941 is played out`,
  window closed on request; `autosave.hoi4` on 1942.01.01, 112 MB.
- `ec_` lines: 411 in six years, against 223 in the three-year vanilla run:

| Event | Count |
| --- | --- |
| `ec_embargo_sent` | 284, from 125 actors |
| `ec_embargo_lifted_detente` | 37 |
| `ec_embargo_lifted_alliance` | 10 |
| `ec_embargo_lifted_gone` | 5 (first data for this reason) |
| `ec_license_granted_infantry_equipment_2` | 45 |
| `ec_license_granted_infantry_equipment_1` | 30 |

- `error.log`: 5533 lines, **none from `99_sandbox*`**. The only posture-adjacent
  hits are content, not code: `give_market_access: Market access between JAP and
  INS is not valid` (`common/national_focus/indonesia.txt`, present in the vanilla
  run too) and Rt56's own `Malformed token: Strelkovaya Diviziya` division-name
  errors, which name no file.
- The 200 opinion scale is visible statically: the fork's compiled `has_opinion`
  threshold is **100** against vanilla's 50, so "good" is half of the fork's
  clamp, and the 75 grants show the gate is practical there. The checker now
  asserts that half-scale ratio for whichever mod it reads.
- Invariants replayed from the log: 0 re-embargoes inside the six-month cooldown,
  0 `detente` lifts before the six-month floor, and **2 sends while two embargoes
  were already active** (DEN -> GRE on 1941.06, IRE -> HUN on 1941.11). The replay
  sees the lines, not the ledger slots, so these are recorded as open rather than
  as a confirmed break: issue 09 asks for the observability that settles it. Both
  actors are tags Rt56 reshapes heavily (Denmark, Ireland), which points at a
  re-created country losing its ledger while its older lines still count.

## Configuration 1 re-run: vanilla, fixed threshold, 1936-1938 (2026-10-19)

The same vanilla configuration as the first run, after the half-scale fix, to
check the threshold change against the game and to give the ceiling a second
data point on a stable tag set:

```
hoi4.exe -hands_off -autosave=YEARLY -historical=no -gamelog
hoi4-bot-session.ps1 -UntilYear 1938 -Historical no
```

- `sandbox_start historical=0`, telemetry gate raised for the run, end on
  1939.01.01.01 with the window closed on request.
- `ec_` lines: 205 - 188 sends from 96 actors, 8 `detente` lifts, 2 `alliance`
  lifts, **6 `gone` lifts** (first vanilla data for that reason) and 1 licence
  (USA -> PHI, 1937.09).
- Replayed invariants: **0 third-embargo sends while two were active**, 0
  re-embargoes inside the cooldown, 0 `detente` lifts before the floor. So the
  two anomalies of configuration 3 stay specific to the fork's reshaped tags and
  issue 09 remains about observability, not about a confirmed break.
- `error.log`: no line from `99_sandbox*`.

## Configuration 4: historical, non-sandbox, 1936-1938 (2026-10-19)

The vanilla mod without `-historical=no`, so the game runs with historical
focuses on and sandbox mode never starts:

```
hoi4.exe -hands_off -autosave=YEARLY -gamelog
hoi4-bot-session.ps1 -UntilYear 1938
```

- Load marker: `#sandbox ... HAI sandbox_start historical=1` - the historical
  branch of `on_startup`.
- `game.log` carries exactly two `#sandbox` lines for the whole session, both
  from the startup block: the version banner and the `historical=1` marker. No
  `ec_`, no `cw_`, no `rivals_` line afterwards, through 1939.03.
- End: `target reached: in-game 1939.03.21.07 - the year 1938 is played out`,
  window closed on request; `autosave.hoi4` on 1939.01.01.
- `error.log`: 35 lines, none from `99_sandbox*`; the only posture-adjacent hits
  are vanilla's own `give_market_access` calls in
  `common/national_focus/indonesia.txt`.

So the historical session's acceptance item is met: nothing in the posture runs
when sandbox mode is off, exactly as rule 4 of the model requires.

## What the run settles

- Spec risk 2 (`send_embargo` needs no threat threshold): **settled in game**,
  200 calls landed and logged.
- Spec risk 3 (`diplo_action_desire` with `market_access_rights`): the plan
  parses and the game raises no error; its effect on AI behaviour was not
  measured.
- Issue 03's in-game items: send, lift with reason, six-month minimum, six-month
  re-embargo block - all observed, and `gone` fired in configuration 3 (5 lines).
  The two-embargo ceiling is observed in configuration 1 and open in
  configuration 3, where the log cannot show the ledger slots (issue 09).
- Issue 04: grants happen, only to faction partners at war, one per 12 months,
  and a receiver without the tech was never granted (`_1` equipment throughout,
  which is what the Chinese warlords could field).

## What it does not settle

- Rt56 (200 opinion scale): run on 2026-10-19 (configuration 3 below) - the
  scale is confirmed statically at 100/200 and the acts all fire; nothing
  saturates in the log.
- Historical (non-sandbox) session: not run.
- `ec_embargo_lifted_gone`: no data point.
- A true "no Death or Dishonor" install: this machine cannot produce one, since
  DoD content ships with the base game here.
- `error.log` of this run carries one unattributed
  `trigger.cpp:835 (invalid trigger scope)` assertion and 13 vanilla engine
  assertions (air wings, theatres); no script error names a posture file, and
  the short pre-fix session showed none, so it is recorded as unexplained rather
  than assigned to this feature.
