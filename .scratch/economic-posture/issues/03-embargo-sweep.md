# 03 - Embargo sweep with bounded state (wave 1)

Status: ready-for-agent
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

- [ ] An observer session produces `ec_embargo_sent` for a Feud pair, and the
      diplomacy screen of that country shows the embargo.
- [ ] Cooling below 60 lifts it on a later monthly tick (never before the
      6-month minimum), and the line names the reason.
- [ ] Two active embargoes block a third.
- [ ] An alliance or a pact with the target prevents sending and lifts an
      existing embargo.
- [ ] A target that ceases to exist clears its slot with no `Invalid Scope`
      lines in `error.log`.
- [ ] Base game without BBA: no embargo calls (the effect is never reached) and
      a clean `error.log`.
- [ ] Nothing runs when `is_sandbox_mode_on` is false.
- [ ] The sweep costs no `any_country` or `every_country` scan.

## Out of scope

- The `embargo_threshold_factor` modifier and the `EMBARGO_*_AI_WEIGHT` defines:
  global, they would change how a country treats the whole world.
- Embargoing non-rivals, or embargoes started for reasons other than the rivalry
  band.
