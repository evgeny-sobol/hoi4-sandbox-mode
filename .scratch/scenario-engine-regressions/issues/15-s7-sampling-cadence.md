# 15 - The s7 diagnostic package has no sampling policy, so one probe floods the log daily

Status: resolved
Type: bug
Blocked by: none

## What to build

One documented sampling cadence for the whole s7 diagnostic package, so a
long-running arc produces a readable log instead of a per-day repeat of the same fact.

## Problem

The s7 package has four members, and each fires on whatever hook happened to carry it, so their
frequencies differ by three orders of magnitude with nothing in the GDD to say what is intended:

| Line | Hook | Frequency |
| --- | --- | --- |
| `sc_power` | monthly tick | once per month per live actor |
| `sc_goal` | monthly tick | once per month per held wargoal |
| `sc_justify` | `on_justifying_wargoal_pulse` | **daily** while a justification runs |
| `sc_goal_end` | `on_wargoal_expire` | discrete event |

The daily one dominates. In the `_sandbox-r56` session a single justification against Poland
produced 61 `sc_justify` lines over 61 consecutive days - all identical except the date:

```
1937.10.08  GER sc_justify ger_on_pol  sc=1 phase=1 t=21
1937.10.09  GER sc_justify ger_on_pol  sc=1 phase=1 t=21
... 61 lines, one per day ...
1937.12.07  GER sc_justify ger_on_pol  sc=1 phase=1 t=23
```

That is 40% of the session's 152 telemetry lines spent restating one fact. The pulse is genuinely
daily in vanilla (the code comment says so: "Daily while active"), so the hook is right and the
volume is the design question.

Nothing states the intended cadence: `docs/gdd/Scenarios.md` lists the line names under "Hooks and
telemetry" but never says how often each fires.

## Why it matters

The s7 package exists to make a session diagnosable from `sandbox_extract.txt`. A per-day repeat
works against that: it buries the transitions an analyst is looking for (when a justification
started, whether it completed) under near-identical rows, and the extract grows with session
length rather than with the number of distinct events.

## Acceptance

- [ ] `docs/gdd/Scenarios.md` states the sampling cadence for each s7 member and the rule behind it
      (a recurring state is sampled on a schedule; a transition is logged when it happens).
- [ ] `sc_justify` no longer writes one line per day for an ongoing justification: it logs the
      transitions (a justification starting, ending, or being abandoned) or a scheduled sample,
      matching whatever cadence the GDD now states.
- [ ] `sc_power` and `sc_goal` keep their monthly cadence, or move to the newly stated one.
- [ ] An observer session with a long justification produces a bounded number of `sc_justify` lines
      that still answer "when did this start, and did it complete".
- [ ] Both mods recompiled clean; no new `error.log` lines attributable to scenario files.

## Out of scope

- The content of each line (which fields it carries); that is settled.
- Adding new s7 members.
- The `sc_goal` silence reported in issue 16, which is a missing line rather than a cadence problem.

## Verification: PASSED (static)

Code:
- The daily `on_justifying_wargoal_pulse` no longer logs: the shared skeleton
  (`core/common/on_actions/99_sandbox_core_on_actions.hsl`) and both mods drop
  the `sandbox_arc_justify_hook()` call; the pulse keeps the Honor drip only.
- `core/tools/extract_arc_hooks.py` no longer emits a justify hook; both mods'
  regenerated `99_sandbox_arc_hooks.hsl` carry only the expire hook.
- `sc_justify` is sampled in the monthly s7 telemetry: one guard per
  aggressor-direction declared pair (`is_justifying_wargoal_against(T)`),
  added by `.scratch/scripts/add_monthly_justify_sample.py` (24 sites in
  `_sandbox`, 106 in `_sandbox-r56`).
- Both `docs/gdd/Scenarios.md` state the cadence and the rule: a recurring
  state is sampled monthly (`sc_power`, `sc_goal`, `sc_justify`); a transition
  is logged when it happens (`sc_goal_end`).

Compile: both mods recompile clean; generated `.txt` carry 0 daily `sc_justify`
lines (the hook is gone) and 24/106 monthly `sc_justify` lines.

Observer confirmation is deferred by maintainer decision: across three
`_sandbox` sessions the AI never opened a justification, so no positive session
case was reachable. Accepted on code + compiler.
