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
      Configuration 3 ran six (1936-1941); 1, 2 and 4 ran three each
      (1936-1938), so their five-year mark is still owed.
- [x] Every `spec.md` acceptance box is ticked or carries a written reason it
      cannot be: all boxes are ticked, and the licence half of the base-game item
      carries the Death or Dishonor integration reason.
- [x] Risks 1-5 of the spec are replaced by observations, or explicitly marked
      unresolved with what would settle them: 2, 4 and 5 settled in game or from
      vanilla evidence, 3 settled for parsing, 1 not shipped by decision
      (issue 05).
- [x] The checker output (06) is quoted as part of the evidence (below and in
      `verification-run.md`).
- [x] Anything the run contradicts becomes a new issue, not a silent edit of the
      spec: the first run's engine rejections are issue-08 evidence and code
      comments, and the ceiling anomaly became issue 09.

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

Configuration 3 ran on 2026-10-19 (Road to 56, full DLC, 1936-41): mods and load
markers confirmed, 411 `ec_` lines (284 sends from 125 actors, 37 detente + 10
alliance + 5 `gone` lifts, 75 licence grants), no `99_sandbox*` line in
`error.log`, `gone` observed for the first time, and the fork's threshold statically
100 against vanilla's 50. One open item: the log replay flags two sends while two
embargoes looked active (issue 09), which the log cannot settle because a send
records the rival slot, not the ledger slot.

A configuration 1 re-run on the same day, after the half-scale fix
(`verification-run.md`, "Configuration 1 re-run"): 1936-38, 205 `ec_` lines - 188
sends from 96 actors, 8 `detente` + 2 `alliance` + 6 `gone` lifts, 1 licence
(USA -> PHI) - with **0 ceiling violations** and no `99_sandbox*` line in
`error.log`. The clean ceiling on stable vanilla tags supports the re-created
country reading of configuration 3's two anomalies, so issue 09 stays about
observability.

All four configurations of this issue have now run on the vanilla mod or the
fork, on 2026-10-18 and 2026-10-19 (`verification-run.md`):

1. vanilla + DLC (twice: before and after the half-scale fix) - embargo, lifts
   with reasons, licences, ceiling clean on stable tags;
2. no DLC - embargo and market silent, `error.log` clean, licences fire because
   Death or Dishonor is base content since 1.14.3;
3. Road to 56 (1936-41) - 411 `ec_` lines, threshold 100 statically, `gone`
   observed, and two ceiling anomalies that the log cannot settle (issue 09);
4. historical - two startup `#sandbox` lines and nothing else for three years.

Still owed: the ceiling observability of issue 09 (a send must record the ledger
slot and the active count, then configuration 3 is re-run), and the r56 fork's
own historical session is untested (the vanilla one covers the shared code path).
Risks 2, 3, 4 and 5 of the spec are settled or bounded; risk 1's seller channel
is not shipped.

Configuration 2 ran on 2026-10-19 with all 35 installed DLC disabled
(`verification-run.md`, "Configuration 2"): `error.log` carried no posture line
and no market token, and no embargo was sent in 36 months - spec risk 4 is
settled. Licences were still granted (4 lines) because Death or Dishonor became
free and part of the base game in patch 1.14.3 and this game is 1.19.3.0, so the
licence guard passes through while the By Blood Alone and Arms Against Tyranny
guards hold. The base-game acceptance item is therefore met for embargoes and the
market and unobservable for licences; ADR-0008 gained a second amendment.
