# Honor

Honor is a per-ruler reputation for keeping one's word (*pacta sunt servanda*). It answers one question other countries ask about a leader: "if we sign something with them, will they honor it?"

Honor is **not**:
- Tyranny (domestic freedom vs. repression). Nukes, purges, conscription, annexations do not touch Honor.
- Opinion (how much a given country likes us). Honor feeds opinion through leader traits, never the other way around.

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`.

## Scale and bands

`honor` is a country variable in `[-100.0, 100.0]`, clamped by `$add_honor()` in `common/macros.hml`.

Bands (existing, `update_country_leader_traits()` in `common/scripted_effects/99_sandbox_scripted_effects.hsl`):
- `< -75` Treacherous (`treacherous_leader`, opinion −20)
- `< -25` Dishonorable (`dishonorable_leader`, opinion −10)
- `< 25` Inglorious (`inglorious_leader`, no modifiers)
- `< 75` Honorable (`honorable_leader`, opinion +10)
- `>= 75` Righteous (`righteous_leader`, opinion +20)

Initial value for a fresh sandbox leader: `randi(-100, 100)` (existing, `initialize_new_country_leader()`).

## Design goals

1. Trust is lost fast and in large discrete chunks; it is earned slowly and passively by actually carrying obligations.
2. Only promise-related conduct moves Honor: non-aggression pacts, guarantees, factions, calls to arms.
3. Numbers are tuned to the bands: one betrayal (−50) always drops an Inglorious leader to at least Dishonorable; a second one drops them to Treacherous. Climbing from Inglorious to Honorable by honest conduct takes roughly 3–5 game years.
4. Reputation that is not backed by deeds fades toward zero, in both directions.

## Definitions

A country is a **friend** of ours if `$is_friend_of()` holds: we are allied (same faction), guaranteed by them, or share a non-aggression pact. This is the existing macro in `common/macros.hml`.

A **betrayal focus** is any national focus that breaks a promise to a friend (removes a pact, leaves a faction, or grants a wargoal on a friend). These are the focuses currently gated by `is_honored_leader(no)` / `can_PREV_get_wargoal_on_THIS()` (see `gdd/national_focus.md`, "Antagonism").

## Honor losses (discrete events)

All values are applied once per event via `$add_honor(-X)` and are shown in the tooltip of the effect that causes them.

### Breaking a non-aggression pact by war: −50

The pact partner is attacked (the focus removes the pact via `diplomatic_relation ... active = no`, then a wargoal is granted or war is declared).

Implementation: the macro `break_non_aggression_pact_with(_tag_)` removes the pact **and** applies `$add_honor(-50)` in one place; use it in sandbox-authored focuses instead of a bare `diplomatic_relation`. Vanilla focuses remove pacts with their own `diplomatic_relation` inside `completion_reward`, which the include deltas cannot replace, so the general path is `on_declare_war` (ROOT = attacker, FROM = target): charge −50 if FROM is in the current or **previous week's** `na_pacts[]` snapshot, or in the **dropped-obligation window** (below).

### Attacking a country we guarantee: −40

Declared in `on_declare_war` when `FROM` is in the current or previous week's `guaranting[]`, or in the dropped-obligation window (then −30, because −10 was already paid when the guarantee was withdrawn). If the same declaration also breaks a pact, apply only the larger penalty (−50), not both.

### Dropped-obligation window: 6 months

The AI typically removes a pact or guarantee, *then* justifies a wargoal for weeks, *then* declares war. A one-week snapshot would miss that. Every dropped pact/guarantee is therefore remembered with the month it was dropped (`dropped_pacts[]` / `dropped_guarantees[]` plus parallel `*_month[]` arrays, `months_elapsed` counter). A war declared on that country within **6 months** is charged as a betrayal; older entries are purged monthly.

### Leaving a faction: −30 at war, −10 in peace

`on_leave_faction` (ROOT = leaving country, FROM = faction leader). "At war" means the faction leader `has_war()` at the moment of leaving.

Exception: no penalty if the leaving country is a subject leaving its overlord's faction because it was released, or if the faction is dissolving because the leader capitulated.

### Faction leader expels a member at war: −15 to the leader

Same hook; the leader is FROM. Verify in implementation whether expulsion fires `on_leave_faction`. If it cannot be distinguished from a voluntary exit, expulsion focuses/decisions must set a country flag (e.g. `expelled_by_leader`) on the member before the removal, and the hook reads that flag.

### Withdrawing a guarantee without war: −10

Detected in the weekly update by diffing `guaranting[]` against last week's snapshot; only the guarantor can withdraw a guarantee, so the penalty is attributable. Skip it if the partner disappeared for reasons outside our control: it was annexed, capitulated, became our subject, joined our faction, or we are already at war with it (that case is the −40 above).

Cancelling a non-aggression pact carries **no immediate penalty**: either side may have cancelled it and the game does not report who. The drop is still recorded in the 6-month window, so a war that follows is charged the full −50. Known limitation: a pact partner who cancels and attacks *us* is charged by their own `on_declare_war`; we are not charged anything.

### Justifying a wargoal on a friend: −2 per 30 pulses

`on_justifying_wargoal_pulse` (ROOT = justifier, FROM = target) fires **daily** in vanilla. Count pulses against a friend in `honor_justify_pulses` and charge −2 every 30 of them (≈ −2 per month of justification). This telegraphs the coming betrayal: neighbours see the leader slide toward Dishonorable before war starts, without wiping out the whole band during a single justification.

### Ignoring obligations (monthly): −5 / −3 per case

Checked in `on_monthly` for every other country:
- A country we guarantee has a defensive war against X and we are not at war with X: **−5 per such country per month**.
- A faction ally is at war with X, X is not our subject/ally, and we are not at war with X (declined or ignored call to arms): **−3 per such ally per month**.

Grace period: the first full month of the war is free, so a country that simply has not been called yet is not punished. Implementation: compare against a snapshot taken last month; punish only if the same unmet obligation existed in both snapshots.

Subjects are exempt: they cannot declare war on their own, so their overlord's wars are not their broken promises.

Refusing a call to arms has no on_action, so this monthly check is the only reliable detection.

## Honor gains

### Passive gain for obligations carried (monthly)

Extends the existing `update_honor_gain_monthly_factor()`:
- `+0.20` per country we guarantee
- `+0.05` per non-aggression pact
- `+0.05` per faction ally (other members of our faction)
- Sum is **capped at +1.00 per month**

Rationale for the cap: a major with ten allies and several guarantees would otherwise reach Righteous within a year.

### Honoring a guarantee: +15

We enter a war on the side of a country we guarantee after it was attacked, either by answering its call (`on_join_allies`, FROM = caller, `FROM->is_guaranteed_by(ROOT)`) or by declaring war ourselves on a country that is at war with a guaranteed country in a defensive war (`on_declare_war`, else-branch after the betrayal checks). Once per war.

### Answering a call to arms: +10

`on_join_allies` (ROOT = joining country, FROM = caller). Once per war. If both this and the guarantee bonus apply, grant only the larger (+15).

"Once per war" is tracked in `honor_answered_call[]` (one entry per country we joined for); the list is cleared in `on_monthly` whenever we are at peace, so the same ally can be rewarded again in a later war.

### Releasing a nation as independent: +5

`on_release_as_free` and `on_liberate`, granted to the releasing/liberating country. Puppeting and annexing grant nothing.

### Natural pact expiry: 0

A pact that ends without war is already rewarded monthly through the passive gain.

## Drift toward zero

Every month Honor moves **0.25 toward 0** regardless of sign, in addition to the passive gain:

```
drift = -0.25 if honor > 0, +0.25 if honor < 0, 0 if |honor| < 0.25
honor_gain_monthly_factor = clamp(obligation_gain, 0, 1.0) + drift
```

Consequences to preserve when tuning:
- A Treacherous leader with no new betrayals recovers to Dishonorable in about 8 years.
- Righteous is stable only for a leader who actually carries obligations: one guarantee roughly offsets the drift; two or more raise Honor.
- Without drift every non-belligerent would become Honorable within a few years, which makes the bands meaningless.

The tooltip `LocKey_honor_tt` already shows `honor_gain_monthly_factor`; it should keep showing the combined value (gain + drift).

## Leader change

Honor belongs to the ruler, not the state. On `on_ruling_party_change`:

```
honor = 0.5 * honor + randi(-50, 50)
```

Half is inherited as the state's diplomatic reputation, half is the new ruler's personal disposition. Then `update_country_leader_traits()` runs as today.

Civil war winner (`on_civil_war_end`, ROOT = winner): the ruler gets a fresh `randi(-100, 100)`; nothing is inherited.

Rebel tags, coup regimes, and released nations are created after startup and never saw `on_startup`. They are initialised lazily: `on_weekly` runs `initialize_country_for_sandbox_mode()` for any country without the `sandbox_initialized` flag, which rolls Honor/Tyranny exactly like a startup country. `on_coup_succeeded` is deliberately not used: its ROOT is the country the coup was staged *against*, not the new regime.

## Gating betrayal focuses by band

Replace the single `is_honored_leader(no)` gate with tiers, so each band has its own meaning:

- **Inglorious or worse** (`honor < 25`): may break a non-aggression pact.
- **Dishonorable or worse** (`honor < -25`): may additionally attack a country it guarantees.
- **Treacherous** (`honor < -75`): may additionally leave a faction in order to attack a former ally.

Implementation: `can_PREV_get_wargoal_on_THIS` in `common/scripted_triggers/99_sandbox_scripted_triggers.hsl` becomes tier-aware: the required band depends on which relation the target has with us (pact → Inglorious, guarantee → Dishonorable, faction → Treacherous). Add scripted triggers `is_dishonorable_leader` / `is_treacherous_leader` with tooltips analogous to `is_honored_leader`. The "Antagonism" patterns in `gdd/national_focus.md` (single target, multiple targets, state owners) must be updated to the tiered trigger when this ships.

## AI weighting

Every betrayal focus gets a betrayal factor next to the existing antagonism modifier: `clamp((25 - honor) / 125, 0, 1)`, applied only while at least one target is a friend. It is packaged as `$ai_betrayal_modifier()` (bare factor, caller supplies the friend trigger) and `$ai_betrayal_modifier_vs($TAG)` (single fixed target) in `macros.hml`; the exact focus-side patterns for single, multiple, and state-owner targets are in `gdd/national_focus.md`, "Antagonism".

A Treacherous AI (honor −100) betrays at full weight; an Inglorious AI at 24 almost never does. Combined with the tiered gate this keeps betrayals rare but not impossible for middling leaders.

Other countries' AI already reacts through the opinion modifiers of the leader traits (−20/−10/+10/+20); no additional AI strategy is required for this iteration.

## Implementation notes

Hooks and scopes (from vanilla `common/on_actions/00_on_actions.txt`; verify scopes marked "check" in game):
- `on_declare_war`: ROOT attacker, FROM target. Carries all betrayal penalties and the "declared on the aggressor" +15.
- `on_leave_faction`: ROOT leaving country, FROM faction leader.
- `on_join_allies`: ROOT joining country, FROM caller (check).
- `on_justifying_wargoal_pulse`: ROOT justifier, FROM target; **daily**.
- `on_release_as_free`, `on_liberate`: ROOT released country, FROM releasing country (check).
- `on_ruling_party_change`, `on_civil_war_end` (ROOT winner), `on_monthly`, `on_weekly`.
- Not used: `on_coup_succeeded` (ROOT is the victim of the coup), `on_war_relation_added` (redundant with `on_declare_war`).

Diplomatic actions without hooks (cancel guarantee, cancel pact, decline call to arms) are detected by snapshots:
- Weekly: keep `prev_guaranting[]` / `prev_na_pacts[]` before rebuilding `guaranting[]` / `na_pacts[]`; drops go into `dropped_guarantees[]` / `dropped_pacts[]` with `months_elapsed` stamps.
- Monthly: `months_elapsed += 1`, purge drops older than 6 months, keep last month's list of unmet obligations for the grace period, clear `honor_answered_call[]` when at peace.

Late-created countries: `on_weekly` initialises any country without `sandbox_initialized` (flag set inside `initialize_country_for_sandbox_mode()`).

One-shot flags: `sandbox_honor_skip_leave_faction` (set by `on_release_as_free` so the released nation's automatic faction exit is not a betrayal) is cleared every week so it cannot swallow a later, genuine exit. `expelled_by_leader` must be set by the expelling focus/decision right before the removal.

Macros with a `_country_` parameter that build a tooltip key (`$is_friend_of(FROM)` → `LocKey_is_friend_of_FROM_tt`) need that key in localisation even when used inside a hidden effect.

Historical defect fixed by this change: `update_honor_gain_monthly_factor()` did not clear `guaranting[]` / `na_pacts[]` while running weekly, so the monthly factor inflated linearly over time. Both arrays are now cleared (after copying to the `prev_` snapshots) before repopulating.

All Honor changes go through `$add_honor()` so that the trait, the opinion modifiers, and the tooltip stay consistent. Do not write `&honor` directly outside `initialize_new_country_leader()` and the leader-change rule.

## Acceptance checklist

- A leader at Honor 20 with a pact partner completes a betrayal focus against it: Honor becomes −30, trait becomes Dishonorable, all other countries get the −10 opinion modifier, and the focus tooltip showed "Honor −50".
- The same leader betrays a second pact: Honor −80, Treacherous.
- A vanilla focus removes a pact; the AI justifies for 3 months and then declares war: no penalty at removal, −50 at the declaration (window), nothing more afterwards. If it declares after 7 months instead, nothing is charged.
- A guarantee is withdrawn: −10 the same week; war on that country 2 months later adds −30 (total −40). Two guarantees withdrawn in one week: −20.
- Justifying a wargoal on a pact partner for 90 days costs −6 (three batches of 30 daily pulses), not −180.
- A rebel tag spawned by a civil war has Honor/Tyranny traits by the end of its first week; the coup victim's values are untouched.
- A subject whose overlord fights a war the subject has not joined loses nothing for "ignoring" it.
- A country at Honor 0 with no obligations and no events stays at 0 indefinitely.
- A country at Honor 60 with no obligations declines to 30 after 10 years (0.25 × 120 months).
- A country at Honor 0 guaranteeing two minors and in a pact with one more gains `0.20·2 + 0.05 − 0.25 = +0.20` per month and reaches Honorable (25) after ~10.5 years; with four guarantees it reaches it in ~3.5 years.
- Passive gain never exceeds +1.00 before drift, regardless of how many allies/guarantees exist.
- A guarantor that ignores a guaranteed country's defensive war loses 5 per month starting from the second month, and stops losing the moment it declares on the aggressor, gaining +15 once.
- After a peaceful ruling-party change, Honor equals half the old value plus a random offset in [−50, 50], clamped.
- A leader at Honor −30 can take a "break pact" and "attack guaranteed" focus but not a "leave faction to attack ally" focus; at −80 all three are available.
- The monthly factor shown in `LocKey_honor_tt` does not grow week over week when the diplomatic situation is unchanged (regression test for the array-clear bug).

## Out of scope for this iteration

- Honor effects on trade, licensing, and opinion beyond the existing trait modifiers.
- Player-facing decisions to "restore honor" (apologies, reparations).
- Honor for subjects toward their overlord (a puppet leaving its overlord's faction is not a betrayal).
- Attributing a cancelled non-aggression pact to the side that cancelled it (the game does not expose it; see "Withdrawing a guarantee without war").
- Historical-mode behaviour: everything here is sandbox-only.
