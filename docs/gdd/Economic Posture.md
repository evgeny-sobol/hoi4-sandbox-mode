# Economic posture

Economic posture answers one question about a country: "**whom** will it trade
with, and whom will it cut off?" Rivals answers whom it wants to fight
(`docs/gdd/Rivals System.md`), Honor how it treats its promises
(`docs/gdd/Honor System.md`), Tyranny how it rules at home
(`docs/gdd/Tyranny System.md`), Opinion how others feel about it. Posture is the
economic face of the same hostility: an AI stops selling to its enemies and
stops buying from them.

Posture is **not**:

- A new friendship system. There is no friend list and no new relationship
  model: the positive side is the engine's own opinion-driven behaviour plus one
  seller channel.
- A player-facing mechanic. The player keeps the vanilla diplomatic actions;
  only the AI's decisions change.
- A trade rebalance. No engine define is edited, so a country with no rivals
  behaves exactly as before.
- War. The strategic levers stay in the three rival plans; posture adds the
  economic entries beside them.

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`.

## Where it lives

- `sandbox-mod-core/common/macros.hml`: the band predicates and the opinion
  threshold, plus the economic `ai_strategy` entries folded into
  `rival_base`, `rival_contain` and `rival_feud` (ADR-0007).
- `common/ai_strategy/99_sandbox_rivals_system.hsl` (per mod, generated): the
  three plans per tag that carry them.
- `common/scripted_effects/99_sandbox_scripted_effects.hsl`:
  `sandbox_economic_posture_monthly()`, the bounded embargo state and the forced
  licence.
- `common/on_actions/99_sandbox_on_actions.hsl`: the monthly call beside
  `review_rivals()`, and the commented `sandbox_log_economic` gate.
- `.scratch/economic-posture/`: the spec, the eight issues and the checker.

## Model

Two axes; every act reads one of them.

- **Hostility**: `rivalry[]` in the country's own slots, bands Cold below 25,
  Rival 25-74, Feud 75 and above. Only the three rival slots are ever
  addressed.
- **Sympathy**: the country's own opinion of the target. Thresholds are
  fractions of the opinion scale (100 in vanilla, 200 in Rt56), so "good" is
  half the scale in both mods.

Rules:

1. A slot at Rival or above vetoes every positive act towards that country,
   whatever its opinion.
2. Negative opinion without a rival slot is neutral: no hostile act.
3. Asymmetric: a country acts on its own slots and its own opinion, never on
   the other side's.
4. AI only. Nothing here runs for the player or outside sandbox mode.

## Ladder

| Attitude towards the country | Buying | Selling and licences | Embargo |
| --- | --- | --- | --- |
| No slot, opinion below 0 | neutral | neutral | no |
| No slot, opinion at half scale or better | engine default plus the seller channel | engine default | no |
| Rival (25-74) | never from that country | no forced grant | no |
| Feud (75 and above) | never from that country | no forced grant | yes |

Embargoes: at most two at once, minimum duration six months, lifted once the
band falls below 60, and no re-embargo of the same target within six months of a
lift. No embargo against an ally, a faction partner or a pact partner, even when
that country holds a rival slot. An embargo follows the nation, not the ruler: a
government change does not lift it.

Licences: the grant side only, because no lever exists for the asking side. At
most one granted licence per country per 12 months, only to a faction partner
that is at war, and only while the country is Cold towards it and thinks well of
it.

## Waves

1. **Embargoes and market exclusion** - the levers the engine exposes today.
2. **Licensed production** - the grant side.
3. **Trade agreement** - denying market access to Feud targets, plus the
   positive seller channel if the engine accepts a scoped variable for it.

Each wave stands on its own; the spec (`.scratch/economic-posture/spec.md`) is
the design record, and each wave has its own issue.

## DLC

Posture depends on paid content by decision (ADR-0008). Embargoes are By Blood
Alone, the equipment market and market access are Arms Against Tyranny, licences
are base game. On the base game posture is invisible: no embargoes, no market
bias. The branches are guarded, so `error.log` stays clean instead of the
mechanics half-working, and no screen advertises an action the AI cannot take.

## Telemetry

Discrete acts only, behind the `sandbox_log_economic` gate, raised the same way
as the other systems (the commented line sits with its siblings in
`on_actions`): `ec_embargo_sent`, `ec_embargo_lifted` with the reason detente,
annexation, target gone or cooldown, `ec_license_granted`, and
`ec_channel_unavailable` once per session when the wave 3 seller channel is not
available.

## Not yet verified

Three engine behaviours are assumed and checked during implementation (the
spec's Risks section holds the details): a scoped variable accepted as
`equipment_market_buy`'s `seller`; `send_embargo` needing no threat threshold;
and `create_production_license` being base-game rather than By Blood Alone. Each
has a named fallback, and the spec is updated with what the observer run saw
rather than what was expected.

## Acceptance checklist

- [ ] A Feud pair produces an embargo within a year, it lifts below 60, and it
      does not return within six months.
- [ ] Two active embargoes block a third; an alliance or a pact lifts one.
- [ ] A rival never receives a granted licence; a faction partner at war
      receives at most one per 12 months.
- [ ] Base game: no behaviour, clean `error.log`.
- [ ] Rt56: thresholds behave on the 200 opinion scale.
- [ ] Historical session: nothing happens, no `ec_` lines.
- [ ] `check_economic_posture.py` passes on both mods' generated files.

## Out of scope

- Player decisions ("embargo this country", "seek a trade agreement"): the
  vanilla actions stay as they are.
- News events and notifications: a player who learns of an AI embargo reads the
  diplomacy screen, as today.
- Lend-lease bias, volunteers and loans: the same attitude link, but each needs
  its own acceptance story.
- Tuning: the shipped numbers are starter values, calibrated from the telemetry
  above rather than reasoned from balance.

