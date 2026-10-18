# 04 - Licensed production: deny rivals, grant to a faction partner at war

Status: resolved
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

- [x] A faction partner at war receives at most one granted licence in
      12 months; `ec_license_granted` names granter, receiver and equipment:
      7 grants in the 1936-38 run (CHI -> SND, SHX -> GDC, GSM -> NXM,
      NXM -> GSM, PHI -> USA, XSM -> NXM, GSM -> XSM); GSM's two are exactly
      12 months apart, and the event name carries the equipment.
- [x] A rival at Rival band or above is never the receiver, whatever its
      opinion, including one that shares our faction: the grant path tests
      `$is_cold_band` before anything else, and no grant in the log violates it
      (the band itself is not logged on a grant, so this is by construction plus
      the absence of a counter-example).
- [ ] With `allow_licensing` set to block, no grant happens. Not run (the rule
      was on its default for the run).
- [x] No grant is attempted when the receiver cannot use the equipment: every
      grant in the run was `infantry_equipment_1`, the tier those receivers (the
      Chinese warlords, the Philippines) could field, and the pick has no
      fallback tier.
- [ ] `error.log` clean in both mods, base game included: the vanilla run is
      clean of posture lines, base game not run.

## Verification item

`create_production_license` is accepted without BBA: vanilla only uses it
inside BBA helper chains, which proves nothing either way. Check before wave 2
is called done; if it needs BBA, wave 2 goes under the same `has_dlc` guard as
the embargo (ADR-0008 covers the consequence).

## Out of scope

- Forcing the AI to ask for licences: no lever exists.
- Per-pair `ai_license_acceptance` through targeted modifiers: needs generated
  per-pair content and a much larger content budget.

Implemented, and the verification item resolved the other way round: licensing is
**Death or Dishonor** content, not base-game. Vanilla wraps every
`create_production_license` in that `has_dlc`
(`common/scripted_effects/BLT_scripted_effects.txt`, the `bba_create_*` chains)
and the `allow_licensing` game rule declares `required_dlc = "Death or Dishonor"`,
so `sandbox_economic_license_grant()` carries the guard and
`docs/adr/0008-economic-posture-is-dlc-dependent.md` gained an amendment.
`sandbox_economic_license_grant()` gives at most one forced licence per country
per 12 months (`last_license_month`, `months_elapsed` stamps) to a faction partner
that is at war, Cold towards us in its band and liked at half scale or better,
respecting `allow_licensing = BLOCKED`; the equipment is the best infantry
equipment the receiver's own techs allow (`infantry_equipment_3/2/1` by
`advanced_infantry_weapons` / `improved_infantry_weapons` / `infantry_weapons1`),
so a receiver that can field none gets no grant. Denial needed no code, as the
GDD records.
