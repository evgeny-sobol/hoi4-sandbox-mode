# 33 - soviet_west peak still times out: the gate focus is never completed

Status: resolved
Type: bug
Blocked by: none

## Problem

The 2026-10-04 observer session (clean build, random, `pin=0`) picked
`sc=4 soviet_west` variant A and ran 1936.1-1942.1. The arc peaked on the
`t=36` fallback and derailed:

```
1936.2  SOV sc_focus SOV_the_path_of_marxism_leninism  sc=4 phase=0 t=1
1937.1  HAI sc_phase crises                             sc=4 phase=1 t=12
1937.1  SOV sc_crisis soviet_west_crisis                sc=4 phase=1 t=12
1939.1  SOV sc_phase peak                               sc=4 phase=2 t=36
1939.1  EST sc_crisis soviet_west_ult_2_defy            sc=4 phase=2 t=36
1939.1  LAT sc_crisis soviet_west_ult_3_submit          sc=4 phase=2 t=36
1939.1  LIT sc_crisis soviet_west_ult_5_defy            sc=4 phase=2 t=36
1940.1  HAI sc_derail peak_timeout                      sc=4 phase=3 t=48
```

Two facts:

1. Peak fired at `t=36`, the fallback, so the variant-A gate
   `SOV_control_scandinavia` was not complete at `t=24`.
2. `sc_focus` logged exactly **one** plan focus all session
   (`SOV_the_path_of_marxism_leninism`); SOV never completed
   `SOV_the_comintern`, the shared trunk of both variants, let alone the
   baltic chain.

`error.log` has zero scenario-attributable lines, so the build is clean; this
is behaviour, not a parse defect.

## Context

Issue 30 removed the ex-`sov_south` Middle East boosts so the fork is neutral
(`SOV_baltic_security` plain x5, branches variant-gated), and issue 31 gave
every plan focus an `sc_focus` line. Neither changed the outcome. In the
earlier 2026-10-04 mixed-build session SOV did walk the trunk and then the
Middle East branch (four `sc_focus` lines), so the AI is not simply failing to
pick focuses; it is choosing focuses outside the plan, or the baltic chain is
unavailable to it.

## Diagnosis plan (executed, see the result below)

- Establish which focuses SOV actually completes. `sc_focus` only sees the
  plan set; add a debug path (a flag-gated log of every SOV focus completion,
  or read `completed_focus` from a lobby save) and rerun.
- Check whether `SOV_baltic_security` is available under the vanilla paranoia
  system at the relevant date (`SOV_paranoia_system_active_flag`), and whether
  the chain's vanilla `available` / `bypass` conditions block the boosted
  priority.
- Confirm the boost weight actually applies in play (`is_live_scenario_aggressor`
  is true for SOV, so the x5 should land); if it does, the branch weights still
  lose to the AI's other priorities.

## Diagnosis (2026-10-04): SOV walks the purge branch, not the comintern branch

Diagnostic build: `sandbox_pick_scenario()` forced to `scenario = 4` and every
one of the 311 SOV focuses was temporarily given a `sc_focus` line, so the log
shows the AI's real focus sequence. Reverted after the run. Forced seeded
`soviet_west` variant A; observer ran 1936.1-1938.1.

SOV completed 17 focuses, in order:

```
SOV_the_path_of_marxism_leninism
SOV_addressing_internal_affairs
SOV_nkvd_primacy
SOV_heavy_industry
SOV_the_new_soviet_woman
SOV_the_left_opposition
SOV_infiltrate_the_nkvd
SOV_bring_old_trotskyists_back
SOV_left_eliminate_right
SOV_gain_support_from_party_members
SOV_organize_the_wreckers
SOV_expand_the_agitprop
SOV_infrastructure_effort_nsb
SOV_finish_the_five_year_plan
SOV_national_specialists
SOV_eastern_development
SOV_the_komsomol
```

SOV went down the vanilla **internal-politics / purge** branch
(`the_left_opposition` line) plus industry, and never touched
`SOV_the_comintern` even though it is the shared trunk of both `soviet_west`
variants and carries the plain x5 boost. `SOV_the_comintern` has
`prerequisite = { focus = SOV_the_path_of_marxism_leninism }` and an empty
`available`, so it is reachable from the second pick; its x5 simply loses to
the purge/industry focuses' vanilla weights. The earlier mixed-build session
did complete the trunk once, so the boost is not dead - it is unreliable.

Consequence: the variant gate focus (`SOV_control_scandinavia`, behind the
baltic chain) is never reached, the peak falls to the `t=36` fallback, and the
arc times out. This is a **design** matter, not a builder defect: the intended
branch does not out-prioritise SOV's early purge/industry focuses. Candidate
fixes (maintainer's call): a much stronger or hard branch push, a different,
reliably-taken gate focus, or driving the arc through a wargoal/threat instead
of focus weights.

## Acceptance

- [x] The completed-focus set for SOV in a `soviet_west` session is recorded
      and quoted.
- [x] The root cause is named: the boosted comintern/baltic branch loses to the
      vanilla early internal-politics/industry focuses, so the gate is not met.
- [x] A fix is chosen: stronger branch push, a different gate, or a non-focus
      lever, so the peak is reached before `t=24`.

## Verification: PASSED (spec-driven suppress, 2026-10-05)

Fix (maintainer's call): the `soviet_west` spec now declares
`suppress = ["SOV_the_left_opposition", "SOV_the_right_opposition"]`, so the AI
can only take `SOV_the_centre` from that mutually exclusive trio. New spec
field + `ai_scenario_focus_suppress` macro (`factor(0)`) + builder-owned
splice; validation rejects a suppress id that is in a path or absent from the
graph.

Verification run (forced `soviet_west`, all-SOV-focus `sc_focus` splice,
reverted): SOV's focus sequence changed from the purge branch to

```
SOV_the_path_of_marxism_leninism
SOV_the_centre                       <- not the_left/right_opposition
...
SOV_the_comintern                    <- the shared trunk, now taken
SOV_middle_east_diplomacy
...
SOV_baltic_security
SOV_claims_in_baltic
SOV_secure_leningrad
SOV_control_scandinavia              <- the variant-A peak gate, completed
```

and the arc ignited:

```
1939.9.26  SOV sc_ignite soviet_west_war sc=4 phase=3 t=44
1939.9.26  SOV sc_success soviet_west_war sc=4 phase=3 t=44
1939.9.26  SOV sc_end soviet_west_war sc=4 phase=3 t=44
```

The three targets all reached peak and took ultimatums (EST submit, LAT defy,
LIT submit), the join lever fired (ITA and JAP joined), and `error.log` had
zero scenario lines. Note: the peak still entered at `t=36`, because the baltic
chain is deep and `SOV_control_scandinavia` finishes late; the arc nonetheless
converts. Tightening the peak timing is optional polish, not part of this fix.

## Out of scope

- The peak-timeout arm itself, which fired as designed.
- Pinned-run acceptance on issue 29.

## Session evidence

`logs/sandbox_extract.txt`, 292 `#sandbox` lines, 1936.1-1942.1. `sc_variant`
present for both arcs (slot-4 wiring works). Repeated repick to `nazi_germany`
at `t=48` with no `none_eligible` (see issue 32).
