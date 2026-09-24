# 02 - `$add_honor` / `$add_tyranny` math fails inside on_actions

Status: ready-for-agent
Type: task
Blocked by: none

## Problem

All 11 `script_math.cpp` errors in the session come from the two macros that write `honor` and
`tyranny`:

```
error.log:13,15,19,23,27,29,31,33,35,37,39
[script_math.cpp:350]: Errors occurred while reading math expression defaulting to 0
```

Each is followed by an empty `Error: ""` line, and the 11 errors match **exactly** the 11
occurrences of one shape in `common/on_actions/99_sandbox_on_actions.txt` - lines 125, 177,
368, 516, 600, 659, 714, 788, 843, 953, 1017:

```text
set_variable = {
    honor = {
        value = {
            value = honor
            add = honor_gain_monthly_factor
        }
        clamp = {
            min = -100
            max = 100
        }
    }
}
```

## Evidence: the shape is fine elsewhere, broken here

- `common/scripted_effects/99_sandbox_scripted_effects.txt` contains the same shape (12
  occurrences) and produces **zero** math errors. `common/national_focus/*.txt` contains 125
  and also produces none.
- In the focus files the variable is a **temp** (`set_temp_variable`); all 11 failing blocks are
  `set_variable` (persistent). That is the only structural difference.
- Vanilla and Rt56 do not use this shape in `on_actions` at all. A whole-install scan finds
  `clamp = {` exactly once outside `scripted_effects`: `common/scripted_effects/INS_scripted_effects.txt:2587`
  - and `INS_scripted_effects.txt` is itself in the `script_math` error list. Zero occurrences in
  `common/on_actions/`, zero `value = {` accumulators under `events/`.
- The vanilla idiom for "add then clamp" is `add_to_variable` + `clamp_variable`: 241
  occurrences in vanilla (16 of them in `common/on_actions/`), 756 in Rt56. Documented in
  `documentation/effects_documentation.md`.

## Functional impact (visible in telemetry)

`sandbox_extract.txt` records `old -> new` per event. Comparing `new` against
`clamp(old + delta)`:

| Event | Matching | Recorded `new = 0` |
| --- | --- | --- |
| `rivals_feud` | 322 / 322 | - |
| `rivals_intensity` | 9 / 9 | - |
| `tyranny_focus` | 16 / 16 | - |
| `honor_withdraw_guarantee` | 11 / 11 | - |
| `tyranny_election` | - | 45 / 45 |
| `honor_join_allies_call` | - | 23 / 23 |
| `honor_leave_faction_war` | - | 8 / 8 |
| `honor_liberate` | - | 3 / 3 |
| `honor_leave_faction_peace` | - | 2 / 2 |

The left column runs through focuses and scripted effects. The right column is exactly the
event set whose `$add_honor` / `$add_tyranny` calls expand inside `on_actions`. Honor and
Tyranny are silently reset to 0 for those events, which contradicts
`docs/gdd/Honor System.md:14,189` and `docs/gdd/Tyranny System.md:16,156,164`.

## Fix

Rewrite both macros in `common/macros.hml` to the vanilla idiom, keeping the existing logging,
delta threshold, `update_country_leader_traits()` call, and `custom_effect_tooltip` intact:

```text
add_to_variable = { honor = _var_ }
clamp_variable = { var = honor min = -100 max = 100 }
```

The same for `tyranny`. `clamp_variable` applies `Max(Min(var, max), min)`, so the ordering
matches the current intent. Keep the `if _var_ != 0` guard.

`common/macros.hml` is a core file, so edit it in the `sandbox-mod-core` repo and sync outward
(`.cursor/rules/sync-core-first.mdc`).

Watch for a second-order effect: `docs/gdd/Tyranny System.md:151` notes that
`update_country_leader_traits()` currently handles only Honor traits even though
`$add_tyranny` calls it. With Tyranny values now actually moving, that gap becomes reachable -
out of scope for this issue, but do not be surprised if Tyranny bands start crossing.

## Acceptance

- Compile both mods; `99_sandbox_on_actions.txt` contains no nested `value = { ... clamp = { ... } }`
  block, and `grep clamp_variable` finds the new lines.
- Re-run a session: `error.log` has zero `script_math.cpp` lines and zero `99_sandbox_on_actions`
  lines.
- `sandbox_extract.txt`: `tyranny_election`, `honor_join_allies_call`, `honor_leave_faction_war`,
  `honor_liberate`, `honor_leave_faction_peace` record the real new value, no `new=0.00`
  mismatches.
- A +20 Tyranny focus still moves the value by exactly 20 and clamps at the band edges.

## Comments
