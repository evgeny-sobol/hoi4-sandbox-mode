# 11 - Honor, Tyranny and Rivals telemetry bypasses its logging gate

Status: needs-triage
Type: bug
Blocked by: none

## Problem

The on_startup skeleton raises one logging gate per system, and `macros.hml` documents the
contract at the top:

```
# This base macro is a generic writer; callers pick the gated wrapper for their
# system:
#   $sandbox_log_honor / $sandbox_log_tyranny / $sandbox_log_rivals
```

`$sandbox_log_honor`, `$sandbox_log_tyranny` and `$sandbox_log_rivals` each check their
`sandbox_log_*` global flag and then call the base `$sandbox_log`. But the three macros that
emit most of the traffic call the **base** macro directly, so the gate never sees them:

`core/common/macros.hml`:

```hsl
 57  macro add_honor(_var_, _event_ = honor_change):
 ...
 71        $sandbox_log(_event_)          # <- ungated: skips $sandbox_log_honor

 80  macro add_tyranny(_var_, _event_ = tyranny_focus):
 ...
 91        $sandbox_log(_event_)          # <- ungated: skips $sandbox_log_tyranny

417  macro add_rivalry(_slot_, _var_):
 ...
431        $sandbox_log(rivals_intensity) # <- ungated: skips $sandbox_log_rivals
444        $sandbox_log(rivals_feud)
451        $sandbox_log(rivals_cold)
458        $sandbox_log(rivals_rival_band)
```

The base `$sandbox_log` only checks `is_sandbox_mode_on()` (macros.hml:7-8), not the system
gate, so those lines print whenever sandbox mode is on.

## Session evidence (`_sandbox`, 1936.1 - 1942.6)

Only `sandbox_log_scenarios` was raised; the other five gates are commented out in
`common/on_actions/99_sandbox_on_actions.txt`:

```
flag = sandbox_log_scenarios
# HAI->$set_global_flag(sandbox_log_honor, 1)
# HAI->$set_global_flag(sandbox_log_rivals, 1)
# HAI->$set_global_flag(sandbox_log_tyranny, 1)
```

Yet the extract holds 805 lines from the three supposedly-off systems:

| Event | Lines | Emitted by |
| --- | --- | --- |
| `rivals_feud` | 513 | `add_rivalry` (ungated) |
| `rivals_intensity` | 24 | `add_rivalry` (ungated) |
| `tyranny_election` | 104 | `$add_tyranny` (ungated) |
| `tyranny_focus` | 39 | `$add_tyranny` (ungated) |
| `honor_leave_faction_peace` / `_war` | 30 / 30 | `$add_honor` (ungated) |
| `honor_join_allies_call` | 25 | `$add_honor` (ungated) |
| `honor_liberate` | 23 | `$add_honor` (ungated) |
| `honor_withdraw_guarantee` | 17 | `$add_honor` (ungated) |

The gated call sites are correctly suppressed in the same session: `honor_init`,
`tyranny_init`, `honor_band_*`, `tyranny_band_*` all call `$sandbox_log_honor` /
`$sandbox_log_tyranny` (99_sandbox_scripted_effects.hsl:36,41,322-330,366-374) and produced
**0** lines. That asymmetry is the proof: the gate works, the high-traffic emitters bypass it.

## Impact

Telemetry only - no gameplay effect. But the gate exists to make a session log readable, and
right now three of the five gates are dead for the events that matter most (81% of all
`#sandbox` lines in this session are from supposedly-gated systems).

## Fix sketch

Point the emitters at the gated wrappers:

```hsl
  # add_honor
        $sandbox_log_honor(_event_)
  # add_tyranny
        $sandbox_log_tyranny(_event_)
  # add_rivalry
      $sandbox_log_rivals(rivals_intensity)
      $sandbox_log_rivals(rivals_feud)
      ...
```

`add_honor` / `add_tyranny` / `add_rivalry` are core macros, so the edit lands in
`sandbox-mod-core` and is synced outward (`.cursor/rules/sync-core-first.mdc`).

## GDD anchors

- `docs/gdd/Honor System.md` / `Tyranny System.md` / `Rivals System.md` - telemetry sections.
- The on_startup comment: "each system logs only while its gate is up".

## Comments
