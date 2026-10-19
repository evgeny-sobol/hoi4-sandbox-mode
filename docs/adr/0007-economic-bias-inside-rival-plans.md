# Fold economic bias into the existing rival plans

Status: accepted

## Context

Economic posture needs declarative bias against specific countries: the engine
exposes `equipment_market_trade_desire` (`id = <country>`),
`equipment_market_buy` (`seller = <country>`) and `diplo_action_desire`
(`id = <country>`, `target = market_access_rights`), and every one of them is
addressed at a tag. The rivals system already generates one plan per potential
rival tag, three per tag (`rival_base`, `rival_contain`, `rival_feud`), with
`allowed = { always = yes }` and `enable = { is_in_array = { rivals = TAG } }`.
That is about 2,475 plans which *every* country evaluates, and
`docs/gdd/Rivals System.md` already flags the plan count as a tick cost, with a
note that the three tiers may have to be merged into one plan per tag if AI
ticks slow down.

A grilling session (2026-10-17) had to decide where the new economic entries
live.

## Decision

Add the addressed economic `ai_strategy` entries inside the existing three
band macros (`rival_base`, `rival_contain`, `rival_feud` in
`sandbox-mod-core/common/macros.hml`). The generated plan file stays at three
plans per tag.

- Hostile, addressed bias is free: the plan for that tag already exists and is
  already enabled on the band.
- The positive side gets no plan of its own. Target-free generic bias was
  rejected because it cannot be gated on attitude without a world scan, not
  because of the plan cost.
- The one affordable positive channel is a scoped variable in
  `equipment_market_buy` (`seller`), which costs no plans at all; it is
  verified in game before it is relied on (issue 05).

## Considered Options

- **Generated per-tag economic plans (rejected).** One more plan per tag for
  market bias, another for market access, doubling the universal plan count for
  behaviour that is already keyed on a band the existing plans compute.
- **One flag-gated universal plan with generic entries (rejected).** The flag
  would have to be recomputed monthly by scanning every country's opinion
  (`any_country`), which is O(n) per country per month; and making every AI buy
  more eagerly regardless of whom it faces is not an attitude-driven rule.
- **Scripted effects for the whole feature (rejected).** Removes the per-tick
  cost the engine pays for plans, but adds our own monthly sweep over the same
  data and loses the mod's declarative style, which ADR-0004 fixed as
  "priority, not guarantee".
- **Engine defines (rejected).** Global: they would change the behaviour of
  countries that have no rivals at all.

## Consequences

- The three "military" band macros now also carry trade entries, so a reader
  looking for market bias must read `rival_base` / `rival_contain` /
  `rival_feud`. Comments in the macros say so.
- Measured plan count: 825 (`275` tags x three tiers, the same tag list in both
  mods), against the 2,475 the Context above estimated.
- The Rival tier gained an upper bound (`>= 25` and `< 75`) so the three tiers
  are mutually exclusive: the -50 trade desire of the Rival tier must not stack
  with the -200 of the Feud tier. At Feud, `conquer` / `prepare_for_war` replace
  `contain`, which they superseded there anyway.
- The plan count stays a known quantity: any future addition to this file must
  re-argue the tick cost before it is written.
- If the three tiers are ever merged into one plan per tag (the GDD's fallback),
  the economic entries move with them and need no semantic change.
- The positive per-target channel depends on an undocumented engine behaviour
  (scoped variable as `seller`). If it fails, the feature keeps the addressed
  denial and gives up on actively seeking partners.
