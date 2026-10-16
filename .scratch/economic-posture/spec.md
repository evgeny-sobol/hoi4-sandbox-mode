# Economic posture

Status: ready
Type: spec

## Context

The sandbox rebuilds AI behaviour around the mod's own hostility model
(Rivals: three slots, `rivalry[]` 0-100), but that hostility only reaches the
military and diplomatic AI strategies: `antagonize`, `contain`, `conquer`,
`prepare_for_war`, and the negative face of `alliance` / `befriend`. A country
that hates another one still trades with it, still sells it equipment, still
approves its licence requests, and never embargoes it. The four economic levers
the engine exposes - trade and market relations, licensed production, equipment
purchases, embargoes - never see the mod's hostility at all.

Goal: the AI's economic diplomacy follows its attitude. Enemies are excluded
from the market and embargoed; partners buy and sell more eagerly.

This document records the design agreed in a grilling session (2026-10-17).
No code is written yet.

## Vocabulary

Terms to add to `CONTEXT.md` at implementation time (in both mods):

- **Economic posture** - the economic-diplomacy behaviour a country derives
  from its attitude towards another country. Two axes: hostility (Rivalry) and
  sympathy (Opinion); the axes never mix arithmetically.
- **Embargo** - a persistent hostile act; the engine effects `send_embargo`
  and `break_embargo` (By Blood Alone).
- **Licensed production** - engine licensing. The mod steers who grants it; it
  cannot make an AI ask for one.
- **Equipment purchase** - buying and selling on the engine's international
  equipment market (Arms Against Tyranny).
- **Trade agreement** - the market relationship the engine creates (market
  access plus purchase contracts), which posture biases. Not a diplomatic
  action of our own.

_Avoid_: relation (that is Opinion), sanction (no such engine concept), friend
(this design has no friend list), trade deal (that is Trade agreement), stance.

## Model

Two axes; every act reads exactly one of them.

- **Hostility**: `rivalry[]` in our own slots, bands Cold < 25, Rival 25-74,
  Feud >= 75 (`docs/gdd/Rivals System.md`). Only the three rival slots are ever
  addressed.
- **Sympathy**: our own opinion of the target (`opinion@TAG`). Thresholds are
  fractions of the mod's opinion scale (`$sandbox_opinion_scale()`: 100 in
  vanilla, 200 in Rt56), so "good" is `scale/2`.

Rules:

1. A slot at Rival or above vetoes every positive act towards that country,
   whatever its opinion.
2. Negative opinion without a rival slot is neutral: no hostile act.
3. Asymmetric: a country acts on its own slots and its own opinion, never on
   the other side's.
4. AI only; everything runs under `is_sandbox_mode_on()`.

## Ladder

| Attitude towards the country | Equipment purchase | Selling and licences | Embargo |
| --- | --- | --- | --- |
| No slot, opinion < 0 | neutral | neutral | no |
| No slot, opinion >= scale/2 | engine default + wave 3 seller channel | engine default | no |
| Rival (25-74) | seller exclusion | no grant | no |
| Feud (>= 75) | seller exclusion | no grant | yes |

The positive row is deliberately thin. The engine already weighs opinion in its
own purchase and market-access acceptance (`EQUIPMENT_PURCHASE_ACCEPTANCE_OPINION`
and `MARKET_ACCESS_ACCEPTANCE_OPINION` are 1.1 per opinion point), and a
target-free buy bias of our own cannot be attitude-scoped: any country-scoped
scan of the whole world per country per month is O(n) per country, which the
embargo design already refuses (see State and limits). What we add on the
positive side is wave 3's seller channel only.

## Mechanisms

- Declarative bias lives inside the existing three macros `rival_base`,
  `rival_contain` and `rival_feud` (`sandbox-mod-core/common/macros.hml`),
  generated per tag into `common/ai_strategy/99_sandbox_rivals_system.hsl` with
  `allowed = { always = yes }`. The file stays at three plans per tag (see
  ADR-0007).
- Scripted effects only where no declarative lever exists: `send_embargo`,
  `break_embargo`, `create_production_license`.
- Engine defines are not edited: they are global and would change countries
  that have no rivals at all.
- The sweep entry point is `sandbox_economic_posture_monthly()`, called from
  the existing `on_monthly` block in `common/on_actions/99_sandbox_on_actions.hsl`
  beside `review_rivals()` / `update_rivalry_monthly()`, so it runs in the same
  per-country pass and sees a settled `rivals[]`.

## Waves

1. **Wave 1** - embargoes and addressed equipment-market exclusion.
2. **Wave 2** - licensed production.
3. **Wave 3** - trade agreement: market-access denial towards rivals, plus the
   positive seller channel if the scoped-variable form works (see Risks).

Every wave is shippable on its own; nothing in a later wave is needed for an
earlier one to be coherent.

## State and limits

- Embargoes are tracked in a bounded three-slot array beside `rivals[]`, the
  pattern `rivals` / `rivalry` already uses (`&rivals[].resize(3)` in
  `initialize_country_for_sandbox_mode()`). The engine offers no cheap reverse
  query: `is_embargoing` and `is_embargoed_by` are per country, so finding our
  own embargoes would mean walking every country every month.
- At most 2 embargoes at once: `EMBARGO_COST` is 100 political power each, so a
  minor power rarely affords more.
- Minimum duration 6 months; lifted once the band falls below 60 (hysteresis
  against the 75 send threshold); the same target cannot be embargoed again
  within 6 months of a lift.
- An embargo is dropped the moment its slot disappears (detente, annexation,
  alliance, target gone), with the reason in telemetry.
- No embargo against an ally, a faction member, or a pact partner, even when
  listed as a rival.
- Forced licence: at most one per country per 12 months, only to a faction
  partner that is at war, only while our band towards it is Cold and our
  opinion of it is `scale/2` or better.
- A government change does not lift embargoes: they follow the nation, not the
  ruler.

## Values

Starter values, calibrated from telemetry; opinion thresholds are scale
fractions, never literals.

Addressed, folded into the band macros (wave 1):

- `equipment_market_trade_desire` (`id` = the tagged country): -50 at Rival,
  -200 at Feud.
- `equipment_market_buy` (`seller` = the tagged country): -200 at Rival and
  above.

Addressed, wave 3:

- `diplo_action_desire` (`id` = the tagged country,
  `target = market_access_rights`): -200 at Feud.
- `equipment_market_buy` (`seller` = our best-opinion partner, via a scoped
  variable): +30 at good opinion, if the variable form works.

## Telemetry

`ec_` lines through the existing `$sandbox_log_*` machinery, gated by a new
`sandbox_log_economic` flag set at startup the way `sandbox_log_rivals` is
(`common/on_actions/99_sandbox_on_actions.hsl`, with the commented line
alongside the others so it can be raised from `game.log`). Discrete acts only;
no monthly snapshots (the Rivals precedent: log discrete changes and band
crossings, not censuses).

- `ec_embargo_sent` - actor, target, band, political power spent.
- `ec_embargo_lifted` - actor, target, reason (detente, annexation, gone,
  cooldown), months held.
- `ec_license_granted` - granter, receiver, equipment.
- `ec_channel_unavailable` - the wave 3 variable form failed at runtime (once
  per session, so the log says why the positive channel is missing).

## Repositories

- Shared logic (macros, effects, telemetry) belongs to
  `C:\Users\evgeny\Repos\HoI4\sandbox-mod-core` and reaches both mods through
  the usual sync, per `.cursor/rules/sync-core-first.mdc`.
- Per mod: the generated `99_sandbox_rivals_system` output, the opinion scale
  (`common/_sandbox_scale.hml`: 100 vanilla, 200 Rt56), the DLC availability of
  the shipped content and the logging gate.

## DLC policy

DLC dependent by decision (ADR-0008). Scripted branches are guarded: embargoes
with `has_dlc = "By Blood Alone"`, market calls with
`has_dlc = "Arms Against Tyranny"`. Licence branches respect the
`allow_licensing` game rule. Declarative market entries cannot be guarded per
entry (a plan's conditions all live in its `enable`), so they are written
unguarded and verified clean on the base game: see Risks 4. Without the relevant
DLC the behaviour does not exist and `error.log` stays clean; nothing degrades
silently.

## Acceptance

In-game (observer session, both mods):

- [ ] A country at Feud with a threat-generating country sends an embargo
      within 12 months; `ec_embargo_sent` names actor and target.
- [ ] That embargo is lifted once the band falls below 60, and the same target
      is not embargoed again within 6 months (`ec_embargo_lifted` reason).
- [ ] No third embargo is sent while two are active.
- [ ] A rival is never granted a licence; a faction partner at war receives at
      most one per 12 months (`ec_license_granted`).
- [ ] Base game (no BBA, no AAT): no posture behaviour, no `error.log` lines.
- [ ] Rt56: opinion thresholds behave on the 200 scale; nothing saturates.
- [ ] Historical (non-sandbox) session: no posture behaviour, no `ec_` lines.
- [ ] No `Invalid Scope` lines from the sweep when a rival slot holds a country
      that ceased to exist mid-month.

Static: `.scratch/scripts/check_economic_posture.py` over the generated files
(issue 06).

## Risks and verification items

1. `equipment_market_buy` accepts a scoped variable for `seller`
   (`common/ai_strategy/_documentation.md`: "Can be scoped variable"). If it
   does not hold in game, wave 3 keeps market-access denial and drops the
   positive seller channel, without paying the plan cost instead.
2. The `send_embargo` effect does not require the `EMBARGO_THREAT_THRESHOLD`
   gate: vanilla uses it as a plain effect inside a `has_dlc` wrapper. Must be
   seen in game before wave 1 is called done.
3. `diplo_action_desire` with `target = market_access_rights` is accepted in
   our plan entry (vanilla uses that target, guarded by AAT).
4. `ai_strategy` entries cannot be guarded individually: every condition of a
   plan lives in its `enable`, next to the military entries. The declarative
   market entries are therefore written unguarded and verified clean on the
   base game. If that verification fails, the fallback is three DLC-gated
   economic band plans per tag, which must be brought back to ADR-0007 as an
   amendment first (issue 02).
5. `create_production_license` is accepted without BBA: vanilla uses it inside
   BBA helper chains, which is not proof either way. If it needs BBA, wave 2
   moves under the same guard as the embargo.

## Out of scope

- Player-facing content: no new decisions, no news events, no localisation.
- New `scripted_diplomatic_actions`: the folder holds a documentation stub in
  vanilla, no shipped definition anywhere, and Rt56 does not use it.
- Lend-lease bias (`send_lend_lease_desire`), volunteers and loans: the same
  attitude link belongs to this family, but each needs its own acceptance
  story.
- Define tuning (`EMBARGO_*_AI_WEIGHT`, `embargo_threshold_factor`): global,
  hits countries with no rivals.
- Targeted modifiers per rival pair (a per-pair `ai_license_acceptance`): needs
  generated per-pair content and a much larger content budget.


