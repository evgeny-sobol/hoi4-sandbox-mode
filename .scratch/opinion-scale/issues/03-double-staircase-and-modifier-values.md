# 03 - Double the join staircase and modifier magnitudes for the Rt56 scale

Status: resolved
Type: bug
Blocked by: none

## What to build

Apply the confirmed doubling map (round 2, Q4) to the r56 copies of the
join staircase and the opinion-modifier magnitudes. Vanilla copies stay
byte-identical.

## Problem

Join staircase (`99_sandbox_scorer.hsl:170-183`): thresholds
>25/>50/>75/<0/<-50 with points +10/+20/+30/-10/-20. Under [-200, 200]
the top tiers trigger at quarter-range instead of half, and the +30/-20
extremes fire more often than designed (GDD 60/60/60 balance note).

Modifier magnitudes (`99_sandbox_opinion_modifiers.hsl:1-21`):
-20/-10/+10/+20/+40 (incl. `scenario_ally` +40). Mechanically valid, but
half the relative weight under the doubled clamp; the GDD claim that
-20/-10 already move cooperation (`National Focuses.md:89`) is weaker
by half.

## Fix direction (suggestion, not decision)

Per-mod values per Q5(b), exact map per Q4. Modifiers: -20->-40
(treacherous, national_rival), -10->-20 (dishonorable, leaders_rival),
+10->+20 (honorable), +20->+40 (righteous), +40->+80 (scenario_ally).
Staircase: >25->>50, >50->>100, >75->>150, <-50-><-100, <0 stays; points
and 60/60/60 maxima unchanged.

## Acceptance

- [ ] r56 file values match the map exactly; vanilla files byte-identical.
- [ ] Join offers still fire in a smoke observer run; `error.log` zero
      scenario lines; both mods compile clean.

## Out of scope

- VERY_GOOD, rivalry/honor scales, ai_strategy weights, the <0 threshold
  (stays by design).
- Consumer rebalancing: point values and maxima unchanged by design.
- The divisor mechanism itself (tickets 01, 02).

## Comments

- 2026-10-08: filed from the opinion-scale audit (grill session 3). Q2
  decided rebalance-now (double); Q4 pinned the map.

## Verification: PASSED (smoke observer run, 2026-10-08)

Random r56 session to 1939: ITA arc (variant b, YUG+SWI), peak at t=36 with
2 targets open, 2 sc_offer (SOV, JAP) and 2 sc_join on the same tick;
rror.log zero scenario hits. Staircase values in file match the Q4 map
exactly (50/100/150/0/-100); modifier values match (-40/-20/20/40/-40/-20/80);
vanilla files byte-identical.
