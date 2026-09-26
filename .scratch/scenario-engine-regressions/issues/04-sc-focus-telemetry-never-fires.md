# 04 - `sc_focus` telemetry never fires

Status: resolved
Type: bug
Blocked by: none

## Problem

`sandbox_extract.txt` has **zero** `sc_focus` lines over 54 months, while three scenarios were
selected in the same session (`sc_pick` fired 3 times) and `sc_power` logged throughout.

The gate is compiled and present in the focus trees - 63 occurrences across six files:

```
common/national_focus/germany.txt  16
common/national_focus/italy.txt    18
common/national_focus/japan.txt     9
common/national_focus/soviet.txt    5
common/national_focus/uk.txt        9
common/national_focus/usa.txt       6
```

The source macro is `sandbox_log_sc_focus` (`core/common/macros.hml`), spliced into the focus
files by `.scratch/scripts/add_sc_focus_to_boosted.py` and gated by
`.scratch/scripts/gate_sc_focus_to_actors.py`.

## Root cause (found: explanation 1, the gate is genuinely dead)

`is_live_scenario_aggressor` is always false because `scenario_enemies[]` is never populated.
The seeding function reads the target array **without the `global.` prefix**, so it reads an
always-empty country variable instead of the global array the writer fills.

`core/common/scripted_effects/99_sandbox_engine.hsl`:

```hsl
sandbox_seed_from_targets():
  add_war_support(0.10)
  if sandbox_targets[0] != 0:      # <-- reads a COUNTRY variable
    var:sandbox_targets[0]:        # <-- scopes a COUNTRY variable
      PREV:
        $sandbox_seed_rival(PREV, 65)
        &scenario_enemies[].add(PREV)
```

The array is written as a global in the per-mod catalog
(`common/scripted_effects/99_sandbox_scenarios.hsl`):

```hsl
global.&sandbox_targets[].add(CZE)
```

and read as a global in the trigger (`core/common/scripted_triggers/99_sandbox_engine_triggers.hsl`):

```hsl
is_scenario_actor:
  ...
  OR:
    is_live_scenario_aggressor()
    THIS in global.sandbox_targets[]    # <-- global, and it works
```

So `is_scenario_actor`'s second branch works (declared targets pass) but the first branch
(`is_live_scenario_aggressor`, which needs `scenario_enemies[]`) never can. Compiled evidence -
`common/scripted_effects/99_sandbox_engine.txt`:

```
check_variable = { var=sandbox_targets^0 value=0 compare=not_equals }   # country var, always 0
var:sandbox_targets^0 = { ... }                                         # never entered
```

The same bug is in `sandbox_ignite_if_at_war` (lines 53-72), which is the only writer of
`sc_ignite` / `sc_success`.

## Wider impact (same root cause, not just telemetry)

- `sandbox_scenario_ignite` gates on `FROM in &scenario_enemies[]`. Empty array -> the arc can
  never ignite. Session evidence: `sc_ignite` 0, `sc_success` 0, only `sc_derail` 2.
- `ai_scenario_focus_boost()` (x5, "live aggressor only", GDD "Levers") gates on the same
  trigger, so the aggressor's war focuses were **never boosted**. This is the long-standing
  "Japan completed zero war focuses" observation in `docs/gdd/Scenarios.md` - it was not the AI
  ignoring the boost, the boost was never applied.
- `scenario_enemies[]` empty also means the betrayal exemption
  (`is_scenario_enemy_of_PREV`) and the symmetric target-side seeding are dead.

## Session evidence (issue 04 logging session, `_sandbox`, 1936.1 - 1939.7, 42 months)

Instrumentation: `sc_focus` logs every boosted-focus completion with `gate=`; a monthly
`sc_actor` probe logs one line per arc candidate. Build: local dev copy `_sandbox.mod`, all six
`sandbox_log_*` gates raised.

- `sc_focus`: **17 lines, all `gate=0`** (was 0 lines before instrumentation).
- `sc_actor`: **80 lines, all `agg=0`**; every line is a declared target (`tgt=1`) with
  `enemies=0`. The aggressor never appears at all - `agg=0` and not a target means the probe
  body is skipped, so the aggressor is invisible.
- Example rows:

  ```
  ITA sc_seed t0=YUG t1=GRE sc=4 phase=0 t=0          # targets seeded into the global array
  YUG sc_actor gate=1 agg=0 tgt=1 enemies=0 sc=4 ...  # target passes, aggressor branch dead
  GER sc_focus GER_anschluss gate=0 sc=1 phase=2 ...  # GER is the aggressor of arc 1 -> dead
  ```

- Zero `error.log` lines attributable to the engine, the trigger, or `is_in_array`.

## Fix

Applied in core `fa607a9` ("Read sandbox_targets as a global in the scenario engine seeding
and ignition"), synced outward to both mods and recompiled.

Added the `global.` prefix to every `sandbox_targets` read in
`core/common/scripted_effects/99_sandbox_engine.hsl` (10 guards + 10 `var:` scopes across
`sandbox_seed_from_targets` and `sandbox_ignite_if_at_war`):

```hsl
  if global.sandbox_targets[0] != 0:
    var:global.sandbox_targets[0]:
```

Canonical vanilla idiom: `common/scripted_effects/NORDIC_scripted_effects.txt:498` uses
`var:GLOBAL.NORDIC_at_defensive_war^0 = { ... }`. The same `var:global.<name> = { ... }` form
appears 80 times in vanilla (e.g. `common/decisions/CZE.txt:6321`) and 60 times in Rt56, so the
prefixed read is the established convention, not a guess.

Compiled proof after the fix (`common/scripted_effects/99_sandbox_engine.txt`, both mods):

```text
check_variable = { var=global.sandbox_targets^0 value=0 compare=not_equals }
var:global.sandbox_targets^0 = { ... }
```

This was a core file: edited under `core/`, committed to `sandbox-mod-core`, then synced
outward (`drifted=0` for both mods). Both mods carried the same bug.

## Verification: PASSED

Second `_sandbox` session (`sandbox_extract.txt`, 4306 lines, 1936.1 - 1942.1, 72 months, three
arcs). The gate is alive in every direction:

- `sc_actor`: **230 lines**. The aggressor now appears at all - `agg=1` with `enemies=6` (SOV),
  `4` (GER), `4` (JAP), each holding across every month of its arc. Before the fix: 80 lines,
  all `agg=0`, `enemies=0`.
- `sc_focus`: 10 lines, and the first `gate=1` line in the project's history:

  ```
  SOV sc_focus SOV_the_path_of_marxism_leninism gate=1 sc=2 phase=0 pin=0 t=1
  ```

- `sc_ignite` / `sc_success` / `sc_end` fired for the first time
  (`JAP sc_ignite japanese_war sc=3 phase=3 t=50`); before the fix all three were 0.
- `error.log`: zero lines attributable to the engine, the trigger, or `is_in_array`.

Two caveats, both filed separately rather than reopened here:

- `sc_focus` `gate=1` fired once, not for every boosted completion, and never for GER or SOV.
  That is the AI-walks-the-war-branch problem, not the gate: issue 08.
- The aggressor's `enemies=` is `2 x` the declared target count and every target shows
  `enemies=0`, which is the symmetric-seeding scoping bug: issue 09.

## Follow-up

Verification is complete, so the temporary instrumentation from the logging session (core
`5866fa7`) was reverted in core `2cf0e69` and synced outward:

- `sandbox_log_sc_focus` is back to the gated form (`if is_scenario_actor():`), with no `gate=`
  field;
- `sandbox_log_sc_actor_probe` is gone, and its `on_monthly` call with it;
- the five extra `sandbox_log_*` gates are commented back out in `on_startup` (only
  `sandbox_log_scenarios` stays raised).

Both mods were resynced (`drifted=0`) and recompiled; the compiled `on_actions` and focus trees
carry no `sc_actor` / `gate=` / probe residue.

## Clone topology note

`core/` in each mod is a gitlink to a **separate** repo, not the standalone checkout:

- `_sandbox/core` -> `Repos/HoI4/sandbox-mod/modules/core` (git dir; worktree is the mod's `core/`)
- `_sandbox-r56/core` -> `Repos/HoI4/sandbox-mod-r56/modules/core`
- `Repos/HoI4/sandbox-mod-core` is a **third, standalone** clone - the one a Git client opens,
  and the one whose `origin` is GitHub.

A commit made in `_sandbox/core` lands in `sandbox-mod/modules/core` and is invisible in
`sandbox-mod-core` until it is fetched. After core commits, fast-forward all clones from the
one that received them:

```
git -C <sandbox-mod-core> fetch <sandbox-mod/modules/core> develop
git -C <sandbox-mod-core> merge --ff-only FETCH_HEAD
git -C <sandbox-mod-r56/modules/core> fetch <sandbox-mod/modules/core> develop
git -C <sandbox-mod-r56/modules/core> merge --ff-only FETCH_HEAD
```

Also note the mod repos still record the **old** core gitlink (`_sandbox` 7336310,
`_sandbox-r56` b7d9cd1) while their working `core/` is newer. That gitlink drift is pre-existing
and unrelated to this issue.

## Comments
