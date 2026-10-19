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

- `sandbox-mod-core/common/macros.hml`: the band predicates
  (`$is_rivalry_at_least`, `$is_rival_or_above`, `$is_feud`, `$is_cold_band`),
  the opinion threshold (`$opinion_good`, built from
  `$sandbox_opinion_scale()`), the shields (`$target_still_exists`,
  `$can_act_hostile_towards`) and the ledger readers (`$is_embargoed_by_us`,
  `$embargo_cooldown_holds`), plus the economic `ai_strategy` entries folded
  into `rival_base`, `rival_contain` and `rival_feud` (ADR-0007).
- `common/ai_strategy/99_sandbox_rivals_system.hsl` (per mod, generated): the
  three plans per tag that carry them.
- `common/scripted_effects/99_sandbox_scripted_effects.hsl`:
  `sandbox_economic_posture_monthly()`, the bounded embargo ledger and the
  forced licence.
- `common/on_actions/99_sandbox_on_actions.hsl`: the monthly call beside
  `review_rivals()`, and the commented `sandbox_log_economic` gate.
- `.scratch/economic-posture/`: the spec, the eight issues and the design
  record of the two ADRs.
- `.scratch/scripts/check_economic_posture.py`: the static guard over the
  generated plans (`.scratch/economic-posture` issue 06). It reads both mods by
  default; `--update` rewrites its baseline when the tag list legitimately
  moves.

## Model

Two axes; every act reads one of them. The macros in `common/macros.hml` are the
only place either axis is read.

- **Hostility**: `rivalry[]` in the country's own slots, bands Cold below 25,
  Rival 25-74, Feud 75 and above (`$is_rivalry_at_least`, `$is_rival_or_above`,
  `$is_feud`, `$is_cold_band`). Only the three rival slots are ever addressed.
  A band below 25 - including no slot at all - is **Cold**, and Cold is the only
  band a positive act may read an opinion in.
- **Sympathy**: the country's own opinion of the target
  (`$opinion_good` = `has_opinion` at or above half the opinion scale: 100 in
  vanilla, 200 in Rt56), never a literal.

The three plans of a tag are mutually exclusive on the band: `rival_base` is
enabled on any slot, `rival_contain` on 25 up to (not including) 75, and
`rival_feud` on 75 and above. The exclusivity is what keeps the -50 of the
Rival tier from stacking with the -200 of the Feud tier (issue 02).

Rules:

1. A slot at Rival or above vetoes every positive act towards that country,
   whatever its opinion: `$is_cold_band` is the veto every positive act calls.
2. Negative opinion without a rival slot is neutral: no hostile act.
3. Asymmetric: a country acts on its own slots and its own opinion, never on
   the other side's.
4. AI only: `sandbox_economic_posture_monthly()` opens with `is_ai`. Nothing
   here runs for the player or outside sandbox mode.

## Ladder

| Attitude towards the country | Buying | Selling and licences | Embargo |
| --- | --- | --- | --- |
| Cold (below 25, or no slot) | neutral | neutral | no |
| Cold and opinion below 0 | neutral | neutral | no |
| Cold, opinion at half scale or better | engine default | engine default plus the forced grant | no |
| Rival (25-74) | never from that country (-200), trade desire -50 | no forced grant | no |
| Feud (75 and above) | never from that country (-200), trade desire -200 | no forced grant | yes |

Cold covers the no-slot case too: nothing is bought less from a country the mod
holds no grudge against. The buying exclusion is the Rival-and-above tier, so a
Cold slot buys as the engine would.

Embargoes: at most two at once, sent at most one a month, minimum duration six
months, lifted once the band falls below 60, and no re-embargo of the same
target within six months of a lift. No embargo against an ally, a faction
partner or a pact partner, even when that country holds a rival slot (the same
shield, `$can_act_hostile_towards`, guards the send). An embargo follows the
nation, not the ruler: a government change does not lift it.

The ledger of our own embargoes is ours, not the engine's: `is_embargoing` and
`is_embargoed_by` are per country, so finding our own embargoes would mean
walking every country every month. Three slots (`embargoes[]` with
`embargo_since[]`, plus `embargo_cooldown[]` with `embargo_cooldown_month[]`)
bound the sweep, which reads only this country's own slots and ledgers.

An embargo lifts on three reasons, named in the log line: `gone` (the target no
longer exists), `alliance` (the two became allies, faction partners or pact
partners) or `detente` (the band fell below 60 after the six-month minimum).
A third-party annexation has no distinct signal in the engine, so it surfaces as
`gone`.

Licences: the grant side only, because no lever exists for the asking side. At
most one granted licence per country per 12 months (`last_license_month`), only
to a faction partner that is at war, and only while the country is Cold towards
it and thinks well of it. The candidate list is the country's own faction members
(`every_allied_country`), not a world scan: the pass stays bounded by the
faction's size. The equipment is the best infantry equipment the
receiver can field (`infantry_equipment_3/2/1` by the receiver's own
`advanced_infantry_weapons` / `improved_infantry_weapons` / `infantry_weapons1`
tech), so the pick is deterministic per receiver and per year rather than
random, and no grant is attempted to a receiver that can field none of them.

## Waves

1. **Embargoes and market exclusion** - shipped: the sweep in
   `sandbox_economic_posture_monthly()` and the addressed entries in
   `rival_contain` / `rival_feud`.
2. **Licensed production** - shipped: the grant side, under its Death or
   Dishonor guard.
3. **Trade agreement** - half shipped: denying market access to Feud targets is
   in `rival_feud`; the positive seller channel is deferred (see "Not yet
   verified").

Each wave stands on its own; the spec (`.scratch/economic-posture/spec.md`) is
the design record, and each wave has its own issue.

## DLC

Posture depends on paid content by decision (ADR-0008). Embargoes are By Blood
Alone, the equipment market and market access are Arms Against Tyranny, and
licensing turned out to be Death or Dishonor: vanilla wraps every
`create_production_license` in that `has_dlc` (`common/scripted_effects/BLT_scripted_effects.txt`),
and the `allow_licensing` game rule itself declares `required_dlc = "Death or
Dishonor"`. On the base game posture is invisible: no embargoes, no market bias,
no licence. The branches are guarded, so `error.log` stays clean instead of the
mechanics half-working, and no screen advertises an action the AI cannot take.

Declarative market entries are the one exception: an `ai_strategy` entry carries
no conditions of its own, so the entries inside the three band plans are written
unguarded and verified clean on the base game (issue 02). The 2026-10-19
no-DLC run raised no posture line and no market token in `error.log`, so the
tokens parse and do nothing when the market does not exist.

One surprise from that same run: Death or Dishonor became free and was
permanently integrated into the base game in patch 1.14.3, and this game is
1.19.3.0, so `has_dlc("Death or Dishonor")` is true even with every
launcher-visible DLC disabled (no `dlc004_*` package; the `allow_licensing` rule
exists at runtime while rules of genuinely absent DLC are dropped). Licensing is
therefore base content in practice: a no-DLC session still grants licences, and
nothing else. The guard stays for hosts older than 1.14.3, but "no licence on the
base game" is no longer an observable acceptance item; ADR-0008 carries the
second amendment.

## Telemetry

Discrete acts only, behind the `sandbox_log_economic` gate, raised the same way
as the other systems (the commented line sits with its siblings in
`on_actions`). The shared `#sandbox` line format has fields for the actor, the
target, the band and a duration, but no free text, so what has no field travels
in the event name:

- `ec_embargo_sent` - actor is the line's tag, target is `other`, `new` is the
  band that triggered it, `delta` is -100 (the `EMBARGO_COST` political power),
  `slot` is the rival slot.
- `ec_embargo_lifted_detente` / `ec_embargo_lifted_alliance` /
  `ec_embargo_lifted_gone` - the reason is the name's suffix; `age` and `old`
  are the months held, `delta` is their negation, `slot` is the ledger slot.
- `ec_license_granted_infantry_equipment_3` (and `_2`, `_1`) - receiver is
  `other`, the equipment is the name's suffix, `new` is the tier code,
  `age` is the months since the previous grant.
- `ec_channel_unavailable` - reserved for the wave 3 seller channel (see "Not
  yet verified"); nothing emits it yet.

## Not yet verified

Each of the three assumed engine behaviours below is now either settled from
vanilla evidence or carried by the observer run (issue 08), which is the only
thing that can settle the rest:

1. A scoped variable accepted as `equipment_market_buy`'s `seller`: **not
   shipped**. The positive seller channel is deferred rather than guessed: the
   picking half needs a monthly scan of the country's best-opinion partner,
   which is exactly the O(n) scan this design refuses everywhere else
   (`docs/adr/0007-economic-bias-inside-rival-plans.md`), and the engine half is
   unverified. The denial half of wave 3 (no market access to a Feud target) did
   ship, folded into `rival_feud`.
2. `send_embargo` needing no threat threshold: **settled in game** (1936-38
   run, 2026-10-18): 200 embargoes were sent and logged, the first ETH -> ITA on
   1936.07.01 at band 80, with no script error from the call.
3. `create_production_license` being base-game: **settled true in practice**.
   Vanilla's own script guards it with `has_dlc("Death or Dishonor")` and the
   `allow_licensing` rule names DoD as required, but DoD became free and part of
   the base game in patch 1.14.3, so on 1.19.3.0 the guard passes through: the
   2026-10-19 no-DLC run still granted licences. The guard stays for older hosts;
   see ADR-0008's second amendment.
4. Declarative market entries written unguarded: unresolved until the base-game
   configuration of the observer run shows a clean `error.log`. The 1936-38
   sandbox run (full DLC) raised no error from the plans, which says nothing
   about the base game.

The run's full evidence, including the three engine rejections it caught in the
first cut of the sweep, is `.scratch/economic-posture/verification-run.md`.

## Acceptance checklist

- [x] A Feud pair produces an embargo within a year, it lifts below 60, and it
      does not return within six months. The 1936-38 run: 200 sends from 99
      actors, 5 `detente` lifts (6, 6, 8, 16, 22 months held) and no re-embargo
      inside the cooldown.
- [x] Two active embargoes block a third; an alliance or a pact lifts one.
      0 third-embargo violations and 11 `ec_embargo_lifted_alliance` lines
      replaying the log per actor.
- [x] A rival never receives a granted licence; a faction partner at war
      receives at most one per 12 months. 7 grants, one country twice exactly
      12 months apart.
- [ ] Base game: no behaviour, clean `error.log`.
- [ ] Rt56: thresholds behave on the 200 opinion scale.
- [x] Historical session: nothing happens, no `ec_` lines. Configuration 4 of
      the 2026-10-19 run: `sandbox_start historical=1`, then the log carries only
      the two startup `#sandbox` lines for three years.
- [x] `check_economic_posture.py` passes on both mods' generated files
      (`problems: 0`, 825 plans, 275 tags each; the checker's negative case
      fails on a deliberately edited value and on a fourth plan).

## Out of scope

- Player decisions ("embargo this country", "seek a trade agreement"): the
  vanilla actions stay as they are.
- News events and notifications: a player who learns of an AI embargo reads the
  diplomacy screen, as today.
- Lend-lease bias, volunteers and loans: the same attitude link, but each needs
  its own acceptance story.
- Tuning: the shipped numbers are starter values, calibrated from the telemetry
  above rather than reasoned from balance.

