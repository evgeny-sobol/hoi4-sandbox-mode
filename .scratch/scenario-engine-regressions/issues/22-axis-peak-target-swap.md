# 22 - Arc 1 variant A sends each peak ultimatum to the wrong target

Status: resolved
Type: bug
Blocked by: none

## What to build

`sandbox_fire_axis_peak()` must send each peak ultimatum to the country the
event is written for, so both declared targets of arc 1 variant A reach peak
with an armed crisis line.

## Problem

In the `v0.2.1` Rt56 session arc 1 (`axis_expansion`) was repicked at `t=31`
and ignited by war at `t=47` before its peak rung, so the defect never
surfaced in telemetry. Reading the code shows it is latent.

Arc 1 variant A declares CZE and POL. The peak function sends:

```
sandbox_fire_axis_peak():
  if country_exists(CZE) and not GER->has_war_with(CZE):
    CZE:
      country_event: id(sandbox_axis.2)
  if country_exists(POL) and not GER->has_war_with(POL):
    POL:
      country_event: id(sandbox_axis.3)
```

But the events are authored the other way round:

- `sandbox_axis.2` (`events/99_sandbox_scenario_axis.hsl`) carries
  `trigger: tag(POL)`, the Warsaw ultimatum, and logs `polish_submit` /
  `polish_defy`.
- `sandbox_axis.3` carries `trigger: tag(CZE)`, the Prague ultimatum, and
  logs `czech_submit` / `czech_defy`.

HoI4 evaluates a `country_event`'s own `trigger` even when the event is sent
to an explicit country, so both calls are dropped: CZE is sent the Poland
event (trigger fails) and POL is sent the Czech event (trigger fails). Arc 1
variant A therefore reaches peak with **no** armed target.

Vanilla pairs the two ultimatums in one event each, `sandbox_axis.2` on
`tag(CZE | FRA)` and `sandbox_axis.3` on `tag(POL | ENG)`, so the r56 split
into per-tag events inverted the mapping.

## Why it matters

This is the issue-20 class in the opposite direction: a declared target that
cannot be lit. An unarmed target distorts the derail accounting (the arc can
derail on `targets_neutralized` while a declared enemy stands) and makes the
acceptance checklist unable to tell an inert target from a pressed one.

## Acceptance

- [x] Every peak `country_event` call sends the event to a tag its own
      `trigger` admits: the call-site audit reports zero mismatches in both
      mods.
- [ ] Arc 1 variant A logs a submit/defy `sc_crisis` for both CZE and POL at
      peak (needs a game run).
- [x] The l10n and the option effects keep matching the country each event is
      written for (the Warsaw event stays `polish_*`, the Prague event stays
      `czech_*`).
- [x] No new `error.log` lines attributable to scenario files (compiled output
      clean; session check pending).

## Out of scope

- Re-pairing the r56 events into vanilla's `tag(A | B)` form. The r56 catalog
  splits the pair deliberately; only the call sites are wrong.
- The `sandbox_select_axis_joiners()` tail, which is unrelated.

## Verification: PASSED (source + compiled output + guard)

- The two A-variant call sites in `sandbox_fire_axis_peak()` were swapped: the
  Warsaw ultimatum (`sandbox_axis.2`, trigger `tag(POL)`) now goes to POL and
  the Prague ultimatum (`sandbox_axis.3`, trigger `tag(CZE)`) now goes to CZE.
  The events and their l10n were left untouched, since the event content was
  correct and only the calls were inverted.
- The guard `.scratch/scripts/check_peak_coverage.py` grew a call-site pass:
  it pairs every peak call's target scope with the event's own trigger tag and
  reports a call whose target the trigger does not admit. The prior union
  coverage could not see this class (the union of `{POL}` and `{CZE}` still
  equals the declared pair).
- The merged guard fails on the pre-fix shape with exactly the two expected
  messages and is clean after the fix; the negative probe was run by hand
  against a broken copy and then reverted.
- Forced recompile of r56 clean (471 files). Both guards report zero problems.
- The observer half (both CZE and POL log a submit/defy at peak) needs a game
  run where arc 1 variant A reaches peak rather than igniting by war first.

## Notes

The existing coverage guard (`.scratch/scripts/check_peak_coverage.py`) takes
the union of trigger tags over the events an arc's peak can fire, so a swap
where the union still equals the declared targets passes. The new call-site
audit (`.scratch/scripts/check_peak_callsites.py`) pairs each call's target
scope with the event's trigger tag and catches this class.
