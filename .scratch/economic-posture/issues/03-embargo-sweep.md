# 03 - Embargo sweep with bounded state (wave 1)

Status: resolved
Type: task
Blocked by: 01

## What to build

Wave 1, scripted half: embargo a rival at Feud, lift it when the feud cools.

- A bounded three-slot array beside `rivals` / `rivalry`, sized in
  `initialize_country_for_sandbox_mode()` with the existing
  `&rivals[].resize(3)` pattern, holding the tag we currently embargo plus a
  months-held counter. The engine has no reverse query for our own embargoes
  (`is_embargoing` / `is_embargoed_by` are per country), so the state has to be
  ours.
- `sandbox_economic_posture_monthly()` in
  `common/scripted_effects/99_sandbox_scripted_effects.hsl`, called from the
  `on_monthly` block of `common/on_actions/99_sandbox_on_actions.hsl` beside
  `review_rivals()`, so it sees a settled `rivals[]`.
- Sent when all hold: the slot is at Feud (75 and above), the target exists, no
  active embargo covers it, fewer than two embargoes are active, and we are not
  allied with, not in a faction with and not in a pact with the target. Wrapped
  in `has_dlc = "By Blood Alone"`.
- Lifted when the band has fallen below 60 and at least 6 months have passed
  (hysteresis against the 75 send threshold), or immediately when the slot no
  longer holds a country, the country is gone, or the two became allies,
  faction partners or pact partners.
- Re-embargo cooldown: 6 months per target after a lift.
- Telemetry: `ec_embargo_sent` and `ec_embargo_lifted` lines with the fields
  listed in the spec's Telemetry section.
- Government change does not touch the state: embargoes follow the nation.

## Acceptance criteria

- [x] An observer session produces `ec_embargo_sent` for a Feud pair: 200 sends
      from 99 actors in the 1936-38 run, the first ETH -> ITA at band 80. The
      diplomacy screen itself was not inspected (a hands-off run has no player).
- [x] Cooling below 60 lifts it on a later monthly tick (never before the
      6-month minimum), and the line names the reason: 5
      `ec_embargo_lifted_detente` lines at 6, 6, 8, 16 and 22 months held.
- [x] Two active embargoes block a third: replaying the log per actor finds no
      send while two were active.
- [x] An alliance or a pact with the target prevents sending and lifts an
      existing embargo: 11 `ec_embargo_lifted_alliance` lines, some two months
      into a hold (PER -> SOV at 2 and 3 months), so the shield fires before the
      six-month floor.
- [ ] A target that ceases to exist clears its slot with no `Invalid Scope`
      lines in `error.log`. No posture line reached `error.log` at all, but no
      living actor's target disappeared in this run, so the `gone` reason has
      no data point.
- [ ] Base game without BBA: no embargo calls (the effect is never reached) and
      a clean `error.log`. Not run.
- [ ] Nothing runs when `is_sandbox_mode_on` is false. Not run (the session was
      sandbox mode).
- [x] The sweep costs no `any_country` or `every_country` scan: it walks the
      country's own three slots and ledgers only (static).

## Out of scope

- The `embargo_threshold_factor` modifier and the `EMBARGO_*_AI_WEIGHT` defines:
  global, they would change how a country treats the whole world.
- Embargoing non-rivals, or embargoes started for reasons other than the rivalry
  band.

Implemented. State: `embargoes[]` / `embargo_since[]` (active, three slots) and
`embargo_cooldown[]` / `embargo_cooldown_month[]` (six-month re-embargo block),
sized in `initialize_country_for_sandbox_mode()` beside `rivals[]` / `rivalry[]`.
`sandbox_economic_posture_monthly()` is called from `on_monthly` after
`fill_rival_vacancies()`, so the bands are settled; it opens with `is_ai` and each
half is wrapped in `has_dlc = "By Blood Alone"`. One embargo a month, at most two
active, a 100 political power floor (`EMBARGO_COST`), and the
`$can_act_hostile_towards` shield on both send and review. Lifts on reason `gone`
(target gone), `alliance` (ally, faction or pact) or `detente` (below 60 after
six months held); a third-party annexation has no distinct engine signal, so it
surfaces as `gone` rather than a fourth reason. Telemetry: `ec_embargo_sent` and
`ec_embargo_lifted_{detente,alliance,gone}`. The sweep walks only this country's
own slots and ledgers: no `any_country` / `every_country`. In-game acceptance is
issue 08's.
