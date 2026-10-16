# 04 - Licensed production: deny rivals, grant to a faction partner at war

Status: ready-for-agent
Type: task
Blocked by: 01

## What to build

Wave 2. The mod steers who grants a licence. It cannot make an AI ask for one:
there is no `ai_strategy` type for licensing, and the only acceptance lever is
the self-scoped modifier `ai_license_acceptance` plus opinion
(`LICENSE_ACCEPTANCE_OPINION_FACTOR = 0.4` per point), which the engine applies
whether or not we write anything.

- Denial side: nothing to write. Rivals already carry the rivalry opinion
  modifiers, and issue 02's market exclusion does not touch licensing. The GDD
  records this as a decision so the absence reads as deliberate.
- Grant side: at most one forced licence per country per 12 months, via
  `create_production_license = { target = <partner> equipment = { type = <pick> } cost_factor = 0 }`,
  when all hold: the partner is in our faction, is at war, our band towards it
  is Cold (below 25), and our opinion of it is scale/2 or better.
- Equipment pick: reuse the vanilla BBA helper chain if it fits
  (`bba_create_*_license_effect` in
  `common/scripted_effects/00_scripted_effects.txt`); otherwise the cheapest
  equipment the partner can produce at the current date. The pick is
  deterministic per year, not random.
- Cooldown: a per-country months counter (12), reset on grant.
- Respect the `allow_licensing` game rule: when it forbids the action, grant
  nothing.
- Telemetry: `ec_license_granted` with granter, receiver and equipment.

## Acceptance criteria

- [ ] A faction partner at war receives at most one granted licence in
      12 months; `ec_license_granted` names granter, receiver and equipment.
- [ ] A rival at Rival band or above is never the receiver, whatever its
      opinion, including one that shares our faction.
- [ ] With `allow_licensing` set to block, no grant happens.
- [ ] No grant is attempted when the receiver cannot use the equipment.
- [ ] `error.log` clean in both mods, base game included.

## Verification item

`create_production_license` is accepted without BBA: vanilla only uses it
inside BBA helper chains, which proves nothing either way. Check before wave 2
is called done; if it needs BBA, wave 2 goes under the same `has_dlc` guard as
the embargo (ADR-0008 covers the consequence).

## Out of scope

- Forcing the AI to ask for licences: no lever exists.
- Per-pair `ai_license_acceptance` through targeted modifiers: needs generated
  per-pair content and a much larger content budget.
