# Scenario engine regressions (v0.2.0)

Status: ready-for-agent
Type: task

## Context

The scenario engine was split into the `sandbox-mod-core` submodule in commit `6760a43`
("Split scenario engine into sandbox-mod-core submodule"). That refactor introduced four
regressions that all show up in `error.log` and `game.log` from the first session played on
the new layout.

This spec collects the evidence and splits the work into four issues. Nothing here is a
design change: every issue restores behaviour the GDD already describes.

## Session under analysis

- Build: local dev copy, `mod/_sandbox.mod`, `descriptor.mod` version `0.2.0`.
- Compiled: 2026-09-23 23:14:51; game logged 23:19:30 - 23:47.
- Game: Operation Postern v1.19.3.0.c01a (5632).
- `sandbox_extract.txt`: 660 lines, up to 1 July 1940 (54 months, 3 scenarios selected).
- Enabled third-party mods: Rt56 is NOT active in this session; active are RGFX (707267197),
  HOI4 Multi-Optimization (3796036936), and this mod.

## Symptoms

| Symptom | Count | Source |
| --- | --- | --- |
| `Unexpected token: sandbox_arc_*` in `common/on_actions/99_sandbox_arc_hooks.txt` | 4 | `error.log:7-10` |
| `Invalid effect` / `Unknown effect-type` for the same four names in `99_sandbox_on_actions.txt` | 8 | `error.log:11-26` |
| `script_math.cpp:350 Errors occurred while reading math expression defaulting to 0` | 11 | `error.log:13-40` |
| `Invalid decision in has_active_timed_decision` + `Invalid Decision ID for add_days_mission_timeout` | 20 | `error.log:42-71` |
| `Trigger failed to validate: ...:329: is_power_balance_in_range` | 1 | `error.log:41` |
| `sc_goal_end` / `sc_justify` telemetry lines | 0 | `sandbox_extract.txt` |
| `sc_focus` telemetry lines | 0 | `sandbox_extract.txt` |
| `sc_ignite` / `sc_success` lines | 0 | `sandbox_extract.txt` (issue 04 session) |

## Root causes

1. **Arc hooks are compiled into `common/on_actions/`.** That directory is parsed as an
   on_actions file, but `99_sandbox_arc_hooks.hsl` contains effect definitions
   (`sandbox_arc_on_weekly():`), not on_action blocks. The game rejects the file, so all four
   calls in the shared skeleton resolve to nothing. Details: issue 01.
2. **`$add_honor` / `$add_tyranny` use a nested math block on a persistent variable inside
   on_actions.** The shape `set_variable = { honor = { value = { ... } clamp = { ... } } }`
   fails only in `common/on_actions/`, only for `set_variable`, and every failure logs the
   math error. Details: issue 02.
3. **Five mission ids and one BoP trigger that only exist in Road to 56 live in the shared
   core.** They validate in `_sandbox-r56` and fail in `_sandbox`. Details: issue 03.
4. **`sc_focus` never fires.** The gate is compiled into six focus trees but produced zero
   lines in 54 months. Root cause found in the issue 04 logging session: `sandbox_seed_from_targets`
   and `sandbox_ignite_if_at_war` read `sandbox_targets[]` without the `global.` prefix, so
   `scenario_enemies[]` is never populated, `is_live_scenario_aggressor` is always false, and
   both the focus boost and arc ignition are dead. Details: issue 04.

## Verification session (second run)

A second `_sandbox` session (4306 `#sandbox` lines, 1936.1 - 1942.1, 72 months, three arcs)
confirmed all four original fixes:

| Symptom | Before | After |
| --- | --- | --- |
| `sc_actor` aggressor lines (`agg=1`) | 0 | 50 (SOV 36, GER 13, JAP 1) |
| `sc_focus` with `gate=1` | 0 | 1 (`SOV_the_path_of_marxism_leninism`) |
| `sc_ignite` / `sc_success` / `sc_end` | 0 / 0 / 0 | 1 / 1 / 3 |
| `error.log` lines from `99_sandbox_*` | 26 | 0 |
| `script_math` / `is_power_balance` / `Invalid Decision` | 32 | 0 |

The same session surfaced six further defects, filed as issues 06-10 plus one open question:

- `06-honor-tyranny-delta-fields-are-not-deltas.md` - the `999` sentinel leaks into `old`/`delta`
  (478 band lines), `honor_window_expire` writes the window age into `delta`, and `tyranny_init`
  writes `tyranny_home` into `delta`. Telemetry only.
- `07-arc-ladder-uses-session-time.md` - the ladder rungs gate on `months_elapsed`, so a repicked
  arc reaches crises and peak in the same month. Affects pacing, not telemetry.
- `08-peak-never-converts.md` - the aggressor produced zero `sc_goal` / `sc_justify` / `sc_focus`
  in 72 months and both peaks died on `peak_timeout` with `sc_target open`. The levers are wired
  and the gate is now healthy, so the AI does not walk the war branch.
- `09-symmetric-seeding-writes-aggressor-array-twice.md` - the "symmetric" seed loop flips scope
  back to the aggressor, so the aggressor's `scenario_enemies[]` holds every target twice
  (`enemies=6` for three targets) and every target's array stays empty (180/180 lines). Makes the
  GDD's "either direction" ignition one-directional and disables the F1 exemption target-side.
- `10-repick-is-not-random.md` - repick takes `eligible[0]` instead of rolling, so a session
  walks arcs in ascending id order.

False alarms checked and dismissed: the `cw_count` vs `t0..t3` "mismatch" is a logging artifact
(out-of-range array indices echo `THIS`); the `random_list: all entries ... 0 chance` errors come
from a third-party mod (`common/on_actions/14_sea_on_actions.txt`); the `france.txt` /
`new_zealand.txt` / `SPR.txt` / `ITA.txt` errors are in vanilla content this mod copies unchanged
and are out of scope.


## Third session (2026-09-25)

`_sandbox` alone, 942 `#sandbox` lines, 1936.1 - 1942.6 (77 months, two arcs). The arc engine is
healthy end to end: `smolder` -> `crises` -> `peak` -> `sc_ignite` -> `sc_success` -> `sc_end`,
with `sc_focus` firing on the boosted war focuses (`GER_reassert_eastern_claims`,
`GER_demand_sudetenland`, `GER_danzig_or_war`). `error.log` has **zero** lines attributable to
`99_sandbox_*`. Two new defects surfaced, filed as issues 11 and 12:

- `11-honor-tyranny-rivals-telemetry-bypasses-gate.md` - `add_honor` / `add_tyranny` /
  `add_rivalry` call the base `$sandbox_log` instead of the gated wrappers, so 805 of 942 lines
  came from three systems whose gates were off. Telemetry only.
- `12-derail-checks-fire-after-park.md` - the derail dispatcher has no phase guard, so a parked
  arc re-logs `sc_derail targets_neutralized` + `sc_end` every month (two phantom `sc_end`
  lines in 1942 for the arc that ended in 1939).

Issue 08 (`peak-never-converts`) did **not** reproduce in this session and should be re-scoped:
the `axis` arc reached `peak`, GER completed its war focuses, and the arc ignited
(`sc_ignite axis_war`, GER vs POL, 1939.8) - the AI did walk the branch here. What stayed at
zero is the goal telemetry: `sc_goal` / `sc_justify` sample the **wargoal** path
(`has_wargoal_against`), but the historical war focuses do not grant wargoals - they send a
`country_event` ultimatum (`germany.86`) and the war follows from the event options. The zero is
therefore expected, not a symptom. (The earlier note that the telemetry is "sampled only once, at
peak entry" is also wrong for the current code: `sandbox_scenario_s7_telemetry()` is called every
month from `sandbox_scenario_tick()`, verified in the compiled `on_actions`.) Triage closed 08 as
`wontfix` and filed the real defect as issue 13: the goal telemetry cannot see the event path the
arcs actually use.

## Issues

- `issues/01-arc-hooks-wrong-directory.md` - move arc hooks out of `common/on_actions/`.
  Resolved in core b7d9cd1.
- `issues/02-add-honor-tyranny-math-in-on-actions.md` - rewrite the two macros to the vanilla
  `add_to_variable` + `clamp_variable` idiom. Resolved in core 929464f.
- `issues/03-r56-only-mission-refs-in-vanilla.md` - split the R56-only content refs into the
  per-mod catalogs (decision: per-mod catalog, not a runtime guard). Resolved in core
  7336310: the core keeps 23 vanilla mission ids and calls a per-mod
  `sandbox_delay_capped_cw_missions_mod()`; the AFG BoP trigger and retry fuse moved to the
  r56 catalogs.
- `issues/04-sc-focus-telemetry-never-fires.md` - root cause found: `sandbox_targets[]` is read
  without the `global.` prefix in the shared engine, so `scenario_enemies[]` stays empty. This
  also kills the x5 aggressor focus boost and arc ignition. Fixed in core fa607a9; **verified**
  in the second session (`agg=1`, first `gate=1`, first `sc_ignite`).
- `issues/05-normalize-r56-telemetry-labels.md` - the r56 catalog mixes `sc_goal` label casing,
  which the generated `sc_justify` labels cannot mirror. Resolved: all labels normalized to
  lowercase and the non-existent `ROU` tag corrected to `ROM`; the convention is now pinned in
  both mods' `docs/gdd/Scenarios.md`.
- `issues/06-honor-tyranny-delta-fields-are-not-deltas.md` - the `999` sentinel and two
  non-delta writers corrupt the `old` / `d=` columns of the Honor/Tyranny log lines.
- `issues/07-arc-ladder-uses-session-time.md` - the ladder gates on the session-wide
  `months_elapsed`, so a repicked arc collapses smolder and crises into one month.
- `issues/08-peak-never-converts.md` - no wargoal, no justify, no boosted focus for the aggressor
  in 72 months; both peaks derailed on `peak_timeout`. **Closed `wontfix`** in triage: the claim
  did not reproduce in the third session (the arc ignited via the event path), and the zero
  telemetry has a different cause - see issue 13.
- `issues/09-symmetric-seeding-writes-aggressor-array-twice.md` - the symmetric seed loop flips
  scope back to the aggressor, doubling its `scenario_enemies[]` and leaving targets empty.
- `issues/10-repick-is-not-random.md` - repick takes `eligible[0]`, so arcs are walked in id order.
- `issues/11-honor-tyranny-rivals-telemetry-bypasses-gate.md` - `add_honor` / `add_tyranny` /
  `add_rivalry` call the ungated base `$sandbox_log`, so Honor/Tyranny/Rivals telemetry prints
  with its gates off (805 of 942 lines in the third session).
- `issues/12-derail-checks-fire-after-park.md` - the derail dispatcher lacks the `phase < 3`
  guard, so a parked arc re-derails every month (phantom `sc_derail` / `sc_end` in 1942).
- `issues/13-goal-telemetry-blind-to-event-ultimatums.md` - `sc_goal` / `sc_justify` sample
  `has_wargoal_against`, but the historical war focuses war through an event ultimatum instead, so
  the goal telemetry is silent on a working arc. Filed by triage out of issue 08.
- `issues/14-declared-target-tag-drift.md` - a declared target's tag can stop matching (a civil-war
  split re-tags it), and the peak telemetry logs the new tag while the derail arm keyed to the
  declared tag stays silent, so the two disagree about whether the target still exists.
- `issues/15-s7-sampling-cadence.md` - the s7 package has no stated sampling policy: `sc_power` and
  `sc_goal` are monthly, `sc_goal_end` is discrete, but `sc_justify` rides the daily justify pulse
  and produced 61 identical lines for one justification (40% of a session's telemetry).
- `issues/16-sc-goal-blind-to-justification-window.md` - `sc_goal` samples a completed wargoal, so it
  is silent while the aggressor is actively justifying and the arc ignites before the wargoal lands.
  A second cause of issue 13's symptom, on the wargoal path rather than the event path.

## Fourth session (2026-09-26, `_sandbox-r56`)

152 telemetry lines, 1936.1 - 1938.2, the `axis` arc. The first r56 session with a full ignition:
`sc_justify` fired (61 lines, the generated arc hooks work), the join lever fired (JAP and CSA
invited and joined), and `sc_ignite` / `sc_success` / `sc_end` closed the arc on 1938.2. All fixes
from the triage round hold: zero `honor_*` / `tyranny_*` / `rivals_*` lines with their gates down,
the ladder rungs spaced correctly, `sc_power` covering the aggressor and both targets, and zero
`error.log` lines attributable to the mod.

Three defects surfaced, filed as issues 14-16:

- The declared second target (`POL`) stopped matching mid-arc; the peak telemetry logged `D09`
  instead while the derail arm keyed to `POL` stayed silent (issue 14).
- One justification produced 61 daily `sc_justify` lines with no stated sampling policy to bound
  them (issue 15).
- `sc_goal` stayed at zero through a two-month justification and a successful ignition (issue 16).

## Third session (2026-09-26, `_sandbox`)

90 telemetry lines, 1936.1 - 1937.12, the `italian` arc. The first clean vanilla ignition: Italy
walked its whole war branch (`ITA_struggle_in_ethiopia` through `ITA_war_with_greece`), held a
wargoal (`sc_goal ita_on_gre`), and ignited on 1937.12 - on the crises rung, before peak, so
`sc_offer` / `sc_join` never ran. Every triage fix held: zero gated telemetry, no `999` sentinel,
arc-relative ladder spacing, zero mod-attributable `error.log` lines.

## Triage (Sep 2026)

All seven open tickets were verified against the code before their state was set. Findings:

- **Confirmed and briefed** (`ready-for-agent`): 06, 07, 09, 10, 11, 12. Each carries an agent
  brief under `## Comments`, and the defects were reproduced from the source (the `999` sentinel
  path, the `months_elapsed` rung gates, the doubled `PREV:` seeding loop, `eligible[0]`, the
  ungated `$sandbox_log` calls, the missing phase guard).
- **Closed** (`wontfix`): 08. Its claim did not reproduce in the third session; the zero telemetry
  it reported has a different, non-bug cause (wargoal-only sampling), filed as 13.
- **New** (`needs-triage`): 13, which needs a maintainer decision on what the goal telemetry should
  sample before an agent can take it.

Ownership for the briefed tickets: 06 and 11 are core files (`macros.hml`,
`99_sandbox_scripted_effects.hsl`), so they are edited in `sandbox-mod-core` and synced outward;
07, 09 and 12 are per-mod catalogs or the shared engine, applied in both mods; 10 is per-mod.

## Ownership note

`common/macros.hml`, `common/scripted_effects/99_sandbox_scripted_effects.hsl`, and
`common/scripted_triggers/99_sandbox_scripted_triggers.hsl` are core files (present under
`core/`, `drifted=0` in both mods). Issues 02 and 03 must be edited in the `sandbox-mod-core`
repo and synced outward, per `.cursor/rules/sync-core-first.mdc`. Issue 01 touches
`core/tools/extract_arc_hooks.py` and `core/common/on_actions/99_sandbox_core_on_actions.hsl`,
and the per-mod generated `common/on_actions/99_sandbox_arc_hooks.hsl`.

## GDD anchors

- `docs/gdd/Honor System.md:14` - `honor` is `[-100, 100]`, clamped by `$add_honor()`.
- `docs/gdd/Honor System.md:189` - all Honor changes go through `$add_honor()`.
- `docs/gdd/Tyranny System.md:16` - `tyranny` is `[-100, 100]`, clamped by `$add_tyranny()`.
- `docs/gdd/Tyranny System.md:156` - all Tyranny changes go through `$add_tyranny()`.
- `docs/gdd/Tyranny System.md:164` - a +20 focus must move the value by exactly 20, clamped.
- `docs/gdd/Civil Wars.md:32,56,152,165` - the cap is 3 and forced fuses are delayed, not
  deleted; BoP is an explicitly named forced-fuse source.
- `docs/gdd/Scenarios.md:42` - content refs are per-mod.

## Out of scope

- `news.263` "No valid option for event" (71x): the definition in `events/NewsEvents.txt:10730`
  is fine in vanilla; Rt56 overrides the file. Not this mod.
- `has_trait` / `has_character_flag` in country scope at `common/decisions/SOV.txt:16239-16244`:
  vanilla content.
- `Invalid supported_version` on five third-party `.mod` files.
- `set_popularities` with `party_popularity_100@*` in `common/national_focus/austria.txt`:
  byte-identical to vanilla, not a sandbox regression.

## Verification plan

1. `python core/tools/sync_core.py --check` reports `drifted=0` for both mods before editing.
2. Compile `_sandbox` against vanilla and `_sandbox-r56` against the Rt56 workshop copy.
3. Re-run the session and check:
   - `error.log`: zero `99_sandbox_arc_hooks` and `99_sandbox_on_actions` lines.
   - `sandbox_extract.txt`: `honor_*` and `tyranny_*` events record the real new value, no
     `new=0.00` mismatches; `sc_goal_end` and `sc_justify` produce lines when a scenario runs.
4. `_sandbox` alone: zero `AFG_*` / `GER_freikorps_riots` / `EGY_*` / `LIT_*` errors.
   `_sandbox-r56` alone: the five missions still validate.
