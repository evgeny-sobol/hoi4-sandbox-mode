# 02 - Forty inline opinion normalizations bypass the shared factor

Status: resolved
Type: bug
Blocked by: 01

## What to build

Route all 40 inline `clamp(PREV.opinion@THIS / 100, -1.0, 1.0)` sites through
the per-mod scale constant from ticket 01, so the per-country antagonism
precomputes stop saturating at 100 under Rt56.

## Problem

Fourteen per-country `99_sandbox_*_scripted_effects.hsl` files compute
`&<FOCUS>_antagonism = 1 - sum_f / n` from per-owner clamp lines that
duplicate the shared macro instead of calling it.
(AF:50; CHI:24,50,76; CHL:19,40; COG:19,55; ENG:25; EST:19; GER:46,75,95;
HOL:16; HUN:16,34,56,75,95,116,137,158,176,204,225,246,265,325; JAP:21,40;
NOR:17,36,55,74; POL:25,48; SOV:20; SPR:29; USA:17,39. Core paths; the r56
mirrors are identical.)

Under Rt56 every opinion above 100 reads 1.0, so `sum_f / n` tops at 1.0
and antagonism floors at 0 for friendly blocs instead of reaching -1.
Fixing the macro (01) leaves all 40 live.

## Fix direction (suggestion, not decision)

Same mechanism as 01 (round 2, Q5(b)): shared call sites, one per-mod
constant. Either call the shared factor macro where scope allows or
substitute the constant inline; vanilla stays byte-identical with
constant 100.

## Acceptance

- [ ] No remaining `/ 100` opinion normalization outside the single shared
      definition (grep-checkable).
- [ ] Spot-check AFG + HUN: r56 opinion 200 reads 1.0, 100 reads 0.5 in
      these sites.
- [ ] Vanilla compiled output byte-identical; both mods compile clean;
      `error.log` zero scenario lines.

## Out of scope

- Modifier magnitudes and staircase values (ticket 03).
- Consumer rebalancing: output ranges unchanged by construction.
- VERY_GOOD, rivalry/honor scales, ai_strategy weights.

## Comments

- 2026-10-08: filed from the opinion-scale audit (grill session 3).

## Verification: PASSED (static, 2026-10-08)

- All 40 sites route through $sandbox_opinion_scale() (per-file counts
  match the audit: HUN 14, CHI 3, NOR 4, GER 3, rest as listed).
- Grep confirms zero residual opinion@... / 100 in either mod's sources.
- Vanilla byte-identical (same 116-file hash check); both mods compile green.
