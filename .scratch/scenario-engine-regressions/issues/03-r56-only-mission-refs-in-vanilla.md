# 03 - Road-to-56-only content refs live in the shared core

Status: resolved
Type: task
Blocked by: none

## Problem

`6760a43` moved `sandbox_delay_capped_cw_missions()` and `sandbox_afg_bop_cw_fuse_ready` into
the shared core, and they reference ids that exist only in Road to 56. In `_sandbox` (vanilla)
every one of them fails validation:

```
error.log:41 Trigger failed to validate: common/scripted_triggers/99_sandbox_scripted_triggers.txt:329: is_power_balance_in_range
error.log:42 Invalid decision in has_active_timed_decision trigger: has_active_mission = AFG_march_on_tehran
error.log:44 ... AFG_the_internal_crisis_mission
error.log:46 ... GER_freikorps_riots
error.log:48 ... EGY_impending_nationalist_uprising
error.log:50 ... LIT_communist_revolution_uprising_mission
error.log:52 Invalid Decision ID for add_days_mission_timeout AFG_march_on_tehran
error.log:53 ... AFG_the_internal_crisis_mission
error.log:54 ... GER_freikorps_riots
error.log:55 ... EGY_impending_nationalist_uprising
error.log:56 ... LIT_communist_revolution_uprising_mission
```

The five `has_active_timed_decision` errors and the five `add_days_mission_timeout` errors are
two effects of the same five ids.

## Which entries are R56-only

`sandbox_delay_capped_cw_missions()` has 28 entries. 23 are valid in vanilla. Exactly 5 are
Road-to-56-only:

| Mission id | vanilla | Rt56 |
| --- | --- | --- |
| `AFG_march_on_tehran` | - | `common/decisions/r56_AFG.txt:3189` |
| `AFG_the_internal_crisis_mission` | - | `common/decisions/r56_AFG.txt:6805` |
| `GER_freikorps_riots` | - | Rt56 |
| `EGY_impending_nationalist_uprising` | - | Rt56 |
| `LIT_communist_revolution_uprising_mission` | - | Rt56 |

Verified against the whole vanilla install (including `dlc/`) and the Rt56 workshop copy
(`394360/820260968`). `AFG_power_balance` / `AFG_total_government_influence`
(`core/common/scripted_triggers/99_sandbox_scripted_triggers.hsl:200-206`) are R56-only too:
vanilla `common/bop/` ships BRA, CZE, DEN, ETH, FIN, ITA, PRC, SWE, SWI - no AFG. Rt56 has
`afg_power_balance` 306 times.

`_sandbox` is the only mod in the whole install that mentions these ids; the published vanilla
build (workshop `3797101483`) does not contain them at all.

## Decision

Split by mod, do not guard at runtime (chosen by the maintainer): the content refs are per-mod
by design (`docs/gdd/Scenarios.md:42`), and the per-mod catalogs are never overwritten by
`sync_core.py`.

## Fix

Move the R56-only refs into the per-mod catalogs:

- `core/common/scripted_effects/99_sandbox_scripted_effects.hsl`: keep the 23 vanilla entries
  in `sandbox_delay_capped_cw_missions()`, drop the 5 R56-only calls, and split the loop so
  the mod-specific part is called from a per-mod hook (for example a
  `sandbox_delay_capped_cw_missions_mod()` defined in each mod's
  `common/scripted_effects/99_sandbox_scenarios.hsl`).
- `core/common/scripted_triggers/99_sandbox_scripted_triggers.hsl`: move
  `sandbox_afg_bop_cw_fuse_ready` (lines 200-206) to `_sandbox-r56`'s per-mod trigger catalog
  (`common/scripted_triggers/99_sandbox_scenario_triggers.hsl`).
- `core/common/scripted_effects/99_sandbox_scripted_effects.hsl:815`: move
  `sandbox_retry_afg_bop_civil_war_fuse` to `_sandbox-r56`'s per-mod effect catalog.
- `_sandbox`: nothing left to reference the five missions or the AFG BoP. `SIA_war_fervor_coup`
  stays in core - it is valid in vanilla (`common/decisions/SIA.txt`).
- `_sandbox-r56`: add the five calls, the trigger, and the retry fuse to its per-mod catalogs.

The 23 remaining vanilla entries stay in core, so `_sandbox-r56` inherits them (Rt56 contains
all 23).

## Acceptance

- `python core/tools/sync_core.py --check` reports `drifted=0` for both mods after the sync.
- `_sandbox` compiled alone: zero `AFG_*`, `GER_freikorps_riots`, `EGY_*`, `LIT_*` errors in
  `error.log`; `99_sandbox_scripted_triggers.txt` no longer mentions `is_power_balance_in_range`.
- `_sandbox-r56` compiled alone against the Rt56 workshop copy: the five missions and the AFG
  BoP trigger still validate, and `sandbox_retry_afg_bop_civil_war_fuse` still fires from
  `on_weekly` once issue 01 lands.
- Do not enable `_sandbox` and `_sandbox-r56` together (`.cursor/rules/r56-overlay.mdc`).

## Comments

- Done in core `7336310`, synced outward; `sync_core.py --check` reports `drifted=0` for both
  mods.
- `sandbox_delay_capped_cw_missions()` keeps the 23 vanilla ids and ends with a call to the new
  per-mod `sandbox_delay_capped_cw_missions_mod()`. `_sandbox` defines it with `pass`;
  `_sandbox-r56` defines it with the five Rt56-only calls. The per-mod hook is defined in
  `common/scripted_effects/99_sandbox_scenarios.hsl`, which the sync never overwrites.
- `sandbox_retry_afg_bop_civil_war_fuse` moved to the r56 effect catalog (right after the
  mission hook) and `sandbox_afg_bop_cw_fuse_ready` to the r56 trigger catalog
  (`99_sandbox_scenario_triggers.hsl`). Both were deleted from core. `sandbox_arc_on_weekly()`
  in the r56 catalog still calls the retry, so the on_weekly path is intact.
- `extract_arc_hooks.py` now also requires `sandbox_delay_capped_cw_missions_mod` in every mod
  catalog (`MOD_CATALOG_HOOKS`), alongside the two hand-written arc hooks. Verified with a
  negative test: deleting the hook makes the tool exit 1 with
  `must define sandbox_delay_capped_cw_missions_mod`.
- `sync_core.py` docstring and both `.cursor/rules/sync-core-first.mdc` copies now list the
  per-mod hooks so the split is discoverable.
- Acceptance verified after compiling both mods:
  - `_sandbox`: zero `AFG_*` / `GER_freikorps_riots` / `EGY_*` / `LIT_*` occurrences anywhere
    under `common/` (compiled `.txt`). `99_sandbox_scripted_triggers.txt` still has three
    `is_power_balance_in_range` blocks, all vanilla: `ITA_power_balance` and the two
    `ETH_centralization_balance` ranges. The AFG one is gone.
  - `_sandbox-r56`: the five missions compile into `99_sandbox_scenarios.txt` (with their
    `cw_defer` logging), the `sandbox_afg_bop_cw_fuse_ready` trigger compiles with
    `id = AFG_power_balance`, and `sandbox_arc_on_weekly = { sandbox_retry_afg_bop_civil_war_fuse = yes }`
    still reaches the retry.
- Not verified in a live session: the runtime error.log lines for these ids need a playtest.
- `SIA_war_fervor_coup` stayed in core as the issue required; it is valid in vanilla.
