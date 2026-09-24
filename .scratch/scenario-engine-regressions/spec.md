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
   lines in 54 months. Details: issue 04.

## Issues

- `issues/01-arc-hooks-wrong-directory.md` - move arc hooks out of `common/on_actions/`.
  Resolved in core b7d9cd1.
- `issues/02-add-honor-tyranny-math-in-on-actions.md` - rewrite the two macros to the vanilla
  `add_to_variable` + `clamp_variable` idiom.
- `issues/03-r56-only-mission-refs-in-vanilla.md` - split the R56-only content refs into the
  per-mod catalogs (decision: per-mod catalog, not a runtime guard).
- `issues/04-sc-focus-telemetry-never-fires.md` - re-check the actor gate once 01 and 02 land.
- `issues/05-normalize-r56-telemetry-labels.md` - the r56 catalog mixes `sc_goal` label casing,
  which the generated `sc_justify` labels cannot mirror.

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
