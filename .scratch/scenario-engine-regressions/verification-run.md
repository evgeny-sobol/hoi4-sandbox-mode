# Verification run for the open observer halves (17-22)

Status: ready-to-run
Scope: one `_sandbox-r56` observer session per check below, or one longer
session that covers them in sequence.

The source halves of issues 17, 19, 20, 21 and 22 are done and guarded; 13 and
14 are still open tickets. Each check here turns one `[ ]` observer box into
`[x]` with a telemetry quote. No code changes are expected from this run; if a
check fails, file a new issue in the usual place.

## How to steer the run

The scenario is chosen at game start by the game rule `sandbox_scenario`
(see `common/scripted_triggers/99_sandbox_scenario_triggers.hsl`). Pinning an
option forces `sandbox_scenario_pin = 1` and the matching arc, so the run does
not depend on the random pick. Run with the Rt56 mod set and observe as an
uninvolved country.

| Check | Rule option | Arc | Why this arc |
|-------|-------------|-----|--------------|
| 21 | `sandbox_fra_plan_xiv` | 22 | FRA aggressor, inline derail branch |
| 19 | `sandbox_fra_plan_xiv` | 22 | same run: inline gone/capitulated arms |
| 20 | `sandbox_sov_south` | 11 | three targets in both variants |
| 22 | `sandbox_axis_expansion` | 1 | A-variant peak with CZE and POL |
| 13 | `sandbox_axis_expansion` | 1 | event-path pressure with no wargoals |
| 14 | any | any | watch a target whose tag is split by civil war |

Checks 19 and 21 share the arc-22 run. 22 and 13 share the arc-1 run.

## Analyse the log

Always through the extractor, never raw grep:

```
python "C:\Users\evgeny\Documents\Paradox Interactive\Hearts of Iron IV\mod\_sandbox-r56\.scratch\scripts\extract_sandbox.py"
```

Read `logs/sandbox_extract.txt`. `sc_power` lines are the s7 sampling package;
every other `sc_*` line is scenario telemetry.

## Check 19: an inline arc parks on a dead aggressor

Arc 22 (`fra_plan_xiv`) is inline in the derail dispatcher, not a named helper.
Let FRA be defeated while the arc is live (or console-`annex FRA` / let it
capitulate), after the arc has been picked.

Pass when the extract shows the aggressor arm firing on the inline branch:

```
<date> HAI sc_derail france_capitulated  sc=22 phase=<0..2>
<date> HAI sc_end     france_capitulated  sc=22 phase=3
```

Gone variant (console `annex FRA` or a tag change):

```
<date> HAI sc_derail france_gone  sc=22 ...
```

Fail if the arc sits at peak until `peak_timeout`, keeps logging `sc_power`,
or parks with a target reason instead of the aggressor reason.

Quoting the observed lines into issue 19 closes its remaining acceptance box.
The label for an inline arc is the same shape as the named helpers
(`<country>_gone` / `<country>_capitulated`).

## Check 21: a dead arc is not offered at the pick

Same arc-22 run. Once FRA is dead, the pick/repick pool must not offer arc
22 again.

Pass when, after the derail, the repick lands on another arc:

```
<date> HAI sc_repick <other arc>  sc=<n> ...
<date> HAI sc_pick   <other arc>  sc=<n> ...
```

and there is no `sc_pick fra_plan_xiv` after the derail. If nothing else is
eligible, `scenario = 0` is the correct outcome.

Fail if arc 22 is re-picked while FRA is gone or capitulated. The pick now
also requires the aggressor's government (breadcrumb: `check_pick_gate.py`),
so an off-ideology aggressor must be skipped the same way.

## Check 20: a three-target arc arms all three

Pin `sandbox_sov_south` (arc 11). Variant is random; either set is fine:

- A: TUR, IRQ, PER
- B: PAK, RAJ, AFG

Arc 11 reaches crises at 18 months and peak at 30 months. Wait for peak. Pass
when every declared target of the running variant logs both a status line and a
crisis outcome:

```
<date> <T1> sc_target <state>
<date> <T2> sc_target <state>
<date> <T3> sc_target <state>
<date> <T1> sc_crisis <t1>_submit   (or _defy)
<date> <T2> sc_crisis <t2>_submit   (or _defy)
<date> <T3> sc_crisis <t3>_submit   (or _defy)
```

Fail if any declared target logs `sc_target` and then nothing (the pre-fix
symptom: PER logged `open` with no outcome). Note the variant in the report so
the B set is covered too; a run covers one variant, so a second run with the
other is needed to close the ticket fully.

## Check 22: arc 1 variant A presses both targets at peak

Pin `sandbox_axis_expansion` (arc 1). The arc was repicked at `t=31` in the
last run and ignited by war before its peak rung. Arc 1 reaches crises at 12
months and peak at 24 months (`arc_months`), so to see variant A's peak keep
the aggressor out of a war until month 24 after the pick. Pinning at game
start is the deterministic way to get those 24 clean months.

Variant A targets CZE and POL. Pass when both log a submit/defy outcome:

```
<date> <CZE|POL> sc_target <state>
<date> <POL> sc_crisis polish_submit   (or polish_defy)
<date> <CZE> sc_crisis czech_submit    (or czech_defy)
```

Fail if the peak logs status lines for both but no `sc_crisis` for one of them
(the pre-fix symptom: both calls dropped because the event trigger rejected the
receiving tag). Quote the lines into issue 22.

## Check 13: event-path pressure is readable without goal lines

Same arc-1 run. Arc 1 wars through ultimatum events, not wargoals, so
`sc_goal` / `sc_justify` stay silent by design. Pass when the ignition is
preceded by crisis lines for the targets:

```
<date> GER sc_crisis <target>_submit   (or _defy)
...
<date> GER sc_ignite axis_war + sc_success + sc_end
```

with `sc_goal` count zero and the crisis lines carrying the pressure. Record
the counts side by side: this is the evidence that the `sc_crisis` lines are
the pressure proof on the event path (`sc_goal` is wargoal-only). The GDD
"Scenarios" coverage rule and the acceptance checklist both key off this.

## Check 14: a declared target whose tag drifts

The hard one to force: a declared target that stops resolving to its country
(civil war, annexation, re-tag). The earlier evidence was POL splitting into
`D09` in January 1938 while the derail arm keyed to POL stayed silent.

Pass when the slot logs the declared tag plus `_gone` rather than a different
live tag:

```
<date> GER sc_target pol_gone
```

or the arc parks with a target-gone derail:

```
<date> HAI sc_derail targets_gone
<date> HAI sc_end     targets_gone
```

Fail if `sc_power` shows a tag that is not the declared one filling the slot
(the pre-fix symptom: `POL sc_power` through 1937.12, then `D09 sc_power` from
1938.1) while the derail arm stays silent and the arc runs on. This check is
probabilistic; a run where POL, CZE or another declared target civil-wars is
the useful one. If no target drifts, the check stays open.

## After the run

- Quote the observed lines into the matching ticket's acceptance box and flip
  it to `[x]`.
- Run all guards once more (`.scratch/scripts/check_*.py`); a run should not
  change them.
- If a check fails, file a new issue; do not reopen 17-22 (their source halves
  are done and guarded).
