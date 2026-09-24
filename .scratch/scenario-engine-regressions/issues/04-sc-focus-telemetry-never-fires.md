# 04 - `sc_focus` telemetry never fires

Status: needs-info
Type: task
Blocked by: 02

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

Compiled shape in `common/national_focus/germany.txt`:

```text
limit = {
    is_sandbox_mode_on = yes
    has_global_flag = sandbox_log_scenarios
}
if = {
    limit = { is_scenario_actor = yes }
    log = "#sandbox [GetDateText] [THIS.GetTag] sc_focus GER_remilitarize_the_rhineland ..."
}
```

The source macro is `sandbox_log_sc_focus` (`common/macros.hml:669`), spliced into the focus
files by `.scratch/scripts/add_sc_focus_to_boosted.py` and gated by
`.scratch/scripts/gate_sc_focus_to_actors.py`.

## Why this is needs-info

The gate depends on `is_scenario_actor`, which commit `9227ab6` changed. Two explanations are
still open and the log cannot separate them:

1. The gate is genuinely broken, and no country passes `is_scenario_actor` at the moment a
   boosted focus completes.
2. The gate is correct, but in this session no boosted focus completed while the country was an
   actor - the scenarios may have been derailed before the boosted focuses landed.

Issues 01 and 02 must land first: both silently reset state (arc hooks dead, Honor/Tyranny
zeroed), and either can shift when a scenario survives long enough for a boosted focus to
complete. Issue 01 is resolved (core b7d9cd1), so only 02 is still open.

## What to gather

- Re-run a session with `sandbox_log_scenarios` on and confirm whether `sc_focus` appears.
- If it still does not, log `is_scenario_actor` once per scenario actor per month
  (temporarily) and compare against the moment a boosted focus completes.
- Confirm the `.include` splice actually carries the gate for the six trees above and not just
  the source macro: check that `common/national_focus/*.include` contains 63 `sc_focus`
  call sites (it does today).

## Acceptance

- Either `sc_focus` lines appear for scenario actors, or the issue is reclassified with the
  reason the gate cannot fire in the observed sessions.

## Comments
