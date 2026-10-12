# 01 - Shared opinion math assumes the vanilla [-100, 100] scale

Status: resolved
Type: bug
Blocked by: none

## What to build

Normalize shared opinion math against the mod's own scale (100 vanilla,
200 Rt56) from a single source, so the Rt56 overlay stops saturating every
opinion above 100 at 1.0.

## Problem

Road to 56 doubles the opinion clamp
(`r56_defines.lua:11-12`: `MAX_OPINION_VALUE = 200`, `MIN_OPINION_VALUE =
-200`, both annotated "Vanilla is 100/-100"; `VERY_GOOD_OPINION` 50 -> 100,
`VERY_BAD_OPINION` -50 -> -100; vanilla `00_defines.lua:41-42,130-131`).
Individual modifiers beyond +-100 exist in both games (vanilla up to
200/-200, Rt56 up to 250); the clamp applies to the total.

The shared `$opinion_factor` (`sandbox-mod-core/common/macros.hml:349`):

```
macro opinion_factor(_tag_):
  clamp(opinion@_tag_ / 100, -1.0, 1.0)
```

divides by the vanilla ceiling. In vanilla the input range is exactly
[-100, 100], so the mapping onto [-1.0, 1.0] is exact. In Rt56 the input
reaches +-200 and everything above 100 saturates at 1.0: +100 and +200
read identically. Every consumer (`cooperation = 1 + factor`, the join
scorer, rivalry math) loses the whole upper half of the Rt56 scale.

A grep for hardcoded 50/100 thresholds next to opinion in shared and r56
`.hsl` found no other sites: the divisor is the one concrete assumption.
(`VERY_GOOD` moving to 100 is Rt56 engine design, not our bug; no action.)

## Fix direction (suggestion, not decision)

A per-mod scale constant (100 / 200) defined where per-mod values live,
consumed by the shared factor macro, mirroring how per-mod catalogs stay
out of `sync_core.py`. The output range stays [-1.0, 1.0] by construction,
so no consumer rebalancing is needed; resolution is restored, not rescaled.

## Acceptance

- [ ] An opinion of 200 in Rt56 reads as 1.0 and 100 reads as 0.5 (upper
      half distinguishable, no saturation cliff).
- [ ] The vanilla mod's compiled output and behavior are unchanged.
- [ ] Both mods compile clean; `error.log` has zero scenario lines.
- [ ] The divisor exists once (no hardcoded 100/200 pair drifting apart).

## Out of scope

- Rebalancing AI weights that consume the factor: the [-1.0, 1.0] range is
  unchanged, so `cooperation` keeps its [0, 2] range in both mods.
- Rt56's own VERY_GOOD/VERY_BAD thresholds and opinion content.

## Comments

- 2026-10-08: filed from an observer-session follow-up. Verdict source:
  vanilla `00_defines.lua:41-42` vs Rt56 `r56_defines.lua:11-14`;
  modifier ranges spot-checked (`00_opinion_modifiers.txt:14,18`,
  `r56_opinion_modifiers.txt:197`).

## Verification: PASSED (static, 2026-10-08)

- New per-mod value-macro sandbox_opinion_scale() (common/_sandbox_scale.hml;
  100 vanilla, 200 r56; mod-only files invisible to sync_core.py).
- Shared opinion_factor divides by $sandbox_opinion_scale(); both mods
  compile green. Gotcha found and fixed: project .hml libraries compile in
  sorted-path order, so the scale file must sort before
  common/macros.hml ('_' < 'm'); first attempt at
  common/macros/99_sandbox_scale.hml failed to resolve.
- Vanilla compiled output byte-identical (116 opinion-bearing .txt hashed
  pre/post, 0 differing). r56 compiled output shows divide = 200.
- No remaining / 100 opinion normalization outside the shared definition.
