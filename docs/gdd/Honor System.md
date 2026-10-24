# Honor

Honor is a per-ruler reputation for keeping one's word (*pacta sunt servanda*). It answers one question other countries ask about a leader: "if we sign something with them, will they honor it?"

Honor is **not**:
- Tyranny (domestic freedom vs. repression). Nukes, purges, conscription, annexations do not touch Honor.
- Opinion (how much a given country likes us). Honor feeds opinion through leader traits, never the other way around.
- Rivalry (whom we want to fight; see `docs/gdd/Rivals System.md`). A rival under a pact or guarantee is protected by Honor like anyone else; rivalry never lowers the cost of a betrayal.

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`.

## Scale and bands

`honor` is a country variable in `[-100.0, 100.0]`, clamped by `$add_honor()` in `common/macros.hml`.

Bands (existing, `update_country_leader_traits()` in `common/scripted_effects/99_sandbox_scripted_effects.hsl` and `common/country_leader/99_sandbox_traits.hsl`):
- `< -75` Treacherous (`treacherous_leader`: opinion -20 in vanilla / -40 in Rt56, `opinion_gain_monthly_factor -0.15`, `trade_opinion_factor -0.30`, `license_purchase_cost +0.35`)
- `< -25` Dishonorable (`dishonorable_leader`: opinion -10 in vanilla / -20 in Rt56, `opinion_gain_monthly_factor -0.05`, `trade_opinion_factor -0.10`, `license_purchase_cost +0.15`)
- `< 25` Inglorious (`inglorious_leader`, no modifiers)
- `< 75` Honorable (`honorable_leader`: opinion +10 in vanilla / +20 in Rt56, `opinion_gain_monthly_factor +0.05`, `trade_opinion_factor +0.10`, `license_purchase_cost -0.15`)
- `>= 75` Righteous (`righteous_leader`: opinion +20 in vanilla / +40 in Rt56, `opinion_gain_monthly_factor +0.15`, `trade_opinion_factor +0.30`, `license_purchase_cost -0.35`)

Initial value for a fresh sandbox leader: `randi(-100, 100)` (existing, `initialize_new_country_leader()`).

## Design goals

1. Trust is lost fast and in large discrete chunks; it is earned slowly and passively by actually carrying obligations.
2. Only promise-related conduct moves Honor: non-aggression pacts, guarantees, factions, calls to arms.
3. Numbers are tuned to the bands: one betrayal (-50) always drops an Inglorious leader to at least Dishonorable; a second one drops them to Treacherous. Climbing from Inglorious to Honorable by honest conduct takes roughly 3-5 game years.
4. Reputation that is not backed by deeds fades toward zero, in both directions.

## Definitions

A country is a **friend** of ours if `$is_friend_of()` holds: we are allied (same faction), guaranteed by them, or share a non-aggression pact. This is the existing macro in `common/macros.hml`.

A **betrayal focus** is any national focus that breaks a promise to a friend (removes a pact, leaves a faction, or grants a wargoal on a friend). These are the focuses currently gated by `is_honored_leader(no)` / `can_PREV_get_wargoal_on_THIS()` (see `docs/gdd/National Focuses.md`, "Antagonism").

## Honor losses (discrete events)

All values are applied once per event via `$add_honor(-X)` and are shown in the tooltip of the effect that causes them.

Declared scenario enemies (`docs/gdd/Scenarios.md`, "Levers") are exempt: wars between them skip every charge in this section, including the justification drip.

### Breaking a non-aggression pact by war: -50

The pact partner is attacked (the focus removes the pact via `diplomatic_relation ... active = no`, then a wargoal is granted or war is declared).

Implementation: the macro `$break_non_aggression_pact_with(_tag_)` (in `common/macros.hml`) removes the pact, applies `$add_honor(-50, honor_break_pact_focus)`, and erases the tag from `na_pacts[]` and `prev_na_pacts[]` in one place; use it in sandbox-authored focuses instead of a bare `diplomatic_relation`. Vanilla focuses remove pacts with their own `diplomatic_relation` inside `completion_reward`, which the include deltas cannot replace, so the general path is `on_declare_war` -> `apply_honor_on_declare_war()` (ROOT = attacker, FROM = target): charge -50 (`honor_war_break_pact`) if FROM is in the current or **previous week's** `na_pacts[]` snapshot, or in the **dropped-obligation window** (`honor_war_break_pact_window`, below). A hit erases FROM from both snapshots so the charge cannot repeat.

### Attacking a country we guarantee: -40

Declared in `apply_honor_on_declare_war()` when `FROM` is in the current or previous week's `guaranting[]` (event `honor_war_attack_guaranteed`), or in the dropped-obligation window (then -30, event `honor_war_attack_dropped_guarantee`, because -10 was already paid when the guarantee was withdrawn). The checks are an ordered `elif` chain, not independent tests: pact (current, then dropped) beats guarantee, so a declaration that breaks both costs only the larger -50.

### Dropped-obligation window: 6 months

The AI typically removes a pact or guarantee, *then* justifies a wargoal for weeks, *then* declares war. A one-week snapshot would miss that. Every dropped pact/guarantee is therefore remembered with the month it was dropped (`dropped_pacts[]` / `dropped_guarantees[]` plus parallel `*_month[]` arrays, `months_elapsed` counter). A war declared on that country within **6 months** is charged as a betrayal; `expire_dropped_obligations()` purges older entries monthly and logs `honor_window_expire` with the age. A hit logs `honor_window_hit` with the age and then forgets the entry (`forget_dropped_pact_with_FROM()` / `forget_dropped_guarantee_of_FROM()`), so the same window cannot be charged twice.

A withdrawn guarantee is charged -10 **and** recorded in `dropped_guarantees[]`; a cancelled pact is recorded in `dropped_pacts[]` with the `honor_pact_dropped` line and no immediate charge. The drop is skipped when the partner vanished for a reason outside our control: it does not exist, capitulated, became our subject, joined our faction, or we are already at war with it (`apply_honor_for_dropped_obligations()` tests all five before recording).

### Leaving a faction: -30 at war, -10 in peace

`on_leave_faction` (ROOT = leaving country, FROM = faction leader; events `honor_leave_faction_war` / `honor_leave_faction_peace`). "At war" means the faction leader `has_war()` at the moment of leaving.

Exception: no penalty if the leaving country is a subject of the leader (`is_subject_of(FROM)`), or if the faction is dissolving because the leader capitulated (`FROM->has_capitulated()`). Both skip the charge entirely. A released nation's automatic exit is caught one step earlier by the `sandbox_honor_skip_leave_faction` one-shot flag, which the hook consumes on first read.

### Faction leader expels a member at war: -15 to the leader

Same hook, with the member as ROOT and the leader as FROM, charged through `FROM: $add_honor(-15, honor_expel_member)`. Expulsion does fire `on_leave_faction` and is indistinguishable from a voluntary exit, so the shape is: whatever expels the member sets `expelled_by_leader` on it immediately before the removal, and the hook reads that flag (and clears it). **Implemented in the hook, but not wired at any call site**: no focus or decision sets `expelled_by_leader` in either mod, so this penalty is currently unreachable.

### Withdrawing a guarantee without war: -10

Detected in the weekly update by diffing `guaranting[]` against last week's snapshot (`apply_honor_for_dropped_obligations()`, event `honor_withdraw_guarantee`); only the guarantor can withdraw a guarantee, so the penalty is attributable. Skip it if the partner disappeared for reasons outside our control: it was annexed, capitulated, became our subject, joined our faction, or we are already at war with it (that case is the -40 above). Every drop that is charged is also recorded in the 6-month window, which is where the later -30 comes from.

Cancelling a non-aggression pact carries **no immediate penalty**: either side may have cancelled it and the game does not report who. The drop is still recorded in the 6-month window, so a war that follows is charged the full -50. Known limitation: a pact partner who cancels and attacks *us* is charged by their own `on_declare_war`; we are not charged anything.

### Justifying a wargoal on a friend: -2 per 30 pulses

`on_justifying_wargoal_pulse` (ROOT = justifier, FROM = target) fires **daily** in vanilla. Count pulses against a friend in `honor_justify_pulses` and charge -2 every 30 of them (event `honor_justify_friend`, ~ -2 per month of justification); the counter resets to 0 on each charge. This telegraphs the coming betrayal: neighbours see the leader slide toward Dishonorable before war starts, without wiping out the whole band during a single justification. Declared scenario enemies are exempt (`FROM not in &scenario_enemies[]`).

### Ignoring obligations (monthly): -5 / -3 per case

`apply_honor_for_unmet_obligations()`, from `on_monthly`. Each month it snapshots the previous lists into `prev_unmet_guarantees[]` / `prev_unmet_allies[]`, rebuilds `unmet_guarantees[]` / `unmet_allies[]`, and then charges only the entries present in **both**:
- A country we guarantee (`other->is_guaranteed_by(ROOT)`) has a defensive war and is at war with some X that we are neither at war with nor in a faction with, and X is not our subject: **-5 per such country per month** (`honor_ignore_guarantee`, an aggregate `-5 * n_g`).
- A faction ally is at war with some X that we are neither at war with nor in a faction with, and X is not our subject (declined or ignored call to arms): **-3 per such ally per month** (`honor_ignore_call`, an aggregate `-3 * n_a`).

Grace period: the first full month of the war is free, so a country that simply has not been called yet is not punished; that is exactly what the both-snapshots test buys.

Subjects are exempt: `if is_subject()` skips the whole obligation scan and logs `honor_ignore_skip_subject` when the overlord is at war. They cannot declare war on their own, so their overlord's wars are not their broken promises.

Refusing a call to arms has no on_action, so this monthly check is the only reliable detection. The aggregate is passed through a temp (`guarantee_penalty` / `ally_penalty`) because a macro argument must be a plain value, not an arithmetic expression.

## Honor gains

### Passive gain for obligations carried (monthly)

`update_honor_gain_monthly_factor()` (runs weekly, applies monthly):
- `+0.20` per country we guarantee (`guaranting[]`)
- `+0.05` per non-aggression pact (`na_pacts[]`)
- `+0.05` per faction ally (`is_in_faction_with(ROOT)`, counted into `allies` and not stored in an array)
- Sum is **capped at +1.00 per month** (`honor_obligation_gain`)

Rationale for the cap: a major with ten allies and several guarantees would otherwise reach Righteous within a year.

### Honoring a guarantee: +15

We enter a war on the side of a country we guarantee after it was attacked, either by answering its call (`on_join_allies`, FROM = caller, `FROM->is_guaranteed_by(ROOT)`, event `honor_join_allies_guarantee`) or by declaring war ourselves on a country that is at war with a guaranteed country in a defensive war (`apply_honor_on_declare_war()`, else-branch after all betrayal checks, event `honor_honor_guarantee`). Once per war: the else-branch walks `guaranting[]`, and the first match sets the one-shot flag `honor_guarantee_granted`, which the same effect clears before and after the walk.

### Answering a call to arms: +10

`on_join_allies` (ROOT = joining country, FROM = caller, event `honor_join_allies_call`). Once per war. If both this and the guarantee bonus apply, grant only the larger (+15) - the `on_join_allies` handler tests `FROM->is_guaranteed_by(ROOT)` first and never awards both.

"Once per war" is tracked in `honor_answered_call[]` (one entry per country we joined for); the list is cleared in `on_monthly` whenever we are at peace, so the same ally can be rewarded again in a later war. The `on_join_allies` handler shares that array with the `on_declare_war` guarantee branch, so a country cannot collect twice for the same war.

### Releasing a nation as independent: +5

`on_release_as_free` (event `honor_release`) and `on_liberate` (event `honor_liberate`), granted to the releasing/liberating country (FROM). Puppeting and annexing grant nothing. `on_release_as_free` also sets the one-shot flag `sandbox_honor_skip_leave_faction` on the released nation, so its automatic exit from our faction is not charged as a betrayal.

### Natural pact expiry: 0

A pact that ends without war is already rewarded monthly through the passive gain.

## Drift toward zero

Every month Honor moves **0.25 toward 0** regardless of sign, in addition to the passive gain:

```
drift = -0.25 if honor > 0.25, +0.25 if honor < -0.25, 0 otherwise
honor_gain_monthly_factor = clamp(obligation_gain, 0, 1.0) + drift
```

Consequences to preserve when tuning:
- A Treacherous leader with no new betrayals recovers to Dishonorable in about 8 years.
- Righteous is stable only for a leader who actually carries obligations: one guarantee roughly offsets the drift; two or more raise Honor.
- Without drift every non-belligerent would become Honorable within a few years, which makes the bands meaningless.

The tooltip `LocKey_honor_tt` shows `honor_gain_monthly_factor` (formatted `|.2=+`); it keeps showing the combined value (gain + drift).

## Leader change

Honor belongs to the ruler, not the state. On `on_ruling_party_change` (`inherit_honor_on_ruling_party_change()`):

```
honor = clamp(0.5 * honor + randi(0, 100) - 50, -100, 100)
```

Half is inherited as the state's diplomatic reputation, half is the new ruler's personal disposition. `prev_honor` is reset to the `999` "no previous value" sentinel first, so the band logger reports the whole change as one step. Then `update_country_leader_traits()` runs and `reroll_leader_rival()` gives the new ruler a fresh personal rival (`docs/gdd/Rivals System.md`).

Civil war winner (`on_civil_war_end`, ROOT = winner, `reset_honor_for_new_ruler()`): the ruler gets a fresh `randi(-100, 100)`; nothing is inherited.

Rebel tags, coup regimes, and released nations are created after startup and never saw `on_startup`. They are initialised lazily: `on_weekly` runs `initialize_country_for_sandbox_mode()` for any country without the `sandbox_initialized` flag, which rolls Honor/Tyranny exactly like a startup country. `on_coup_succeeded` is deliberately not used: its ROOT is the country the coup was staged *against*, not the new regime.

A new character installed without a party change (a civil-war split, a `promote_leader`) is caught by `on_government_change`, which re-runs `update_country_leader_traits()`. That function is guarded by `has_ruling_country_leader()` (exists, and has a `is_country_leader()` character), because `add_country_leader_trait` is invalid without one; a missing band trait forces `prev_honor` / `prev_tyranny` back to `999`, so the next tick applies the right trait from scratch.

## Programmatic surface

No caller reads `&honor` directly. Everything goes through these entry points, all in `core/common/scripted_effects/99_sandbox_scripted_effects.hsl` unless noted:

- `$add_honor(_var_, _event_)` (`common/macros.hml`): the only writer. Clamps, updates traits, and owns the logging rule.
- `initialize_new_country_leader()`: rolls `honor`, sets `prev_honor = 999`, applies traits, picks the personal rival.
- `update_country_leader_traits()` / `remove_honor_leader_traits()` / `remove_tyranny_leader_traits()`: band-trait maintenance. The remove helpers exist because civil-war copies can already carry the parent's traits.
- `sandbox_log_honor_band_if_changed()` / `sandbox_log_tyranny_band_if_changed()`: emit `honor_band_*` / `tyranny_band_*` only on a band crossing, which is the only place the 0.25 monthly drift becomes visible (the `|d| >= 2` rule in `$add_honor` suppresses it).
- `update_honor_gain_monthly_factor()` and `update_tyranny_gain_monthly_factor()`: recompute the monthly factors on `on_weekly`.
- `apply_honor_on_declare_war()`, `apply_honor_for_dropped_obligations()`, `apply_honor_for_unmet_obligations()`, `expire_dropped_obligations()`, `forget_dropped_pact_with_FROM()`, `forget_dropped_guarantee_of_FROM()`: the on_action and monthly bodies.
- `inherit_honor_on_ruling_party_change()`, `reset_honor_for_new_ruler()`: the leader-change rules.

The change log has two layers. Every discrete act above has its own event name in the `#sandbox honor_*` line: `honor_init`, `honor_war_break_pact`, `honor_war_break_pact_window`, `honor_war_attack_guaranteed`, `honor_war_attack_dropped_guarantee`, `honor_withdraw_guarantee`, `honor_pact_dropped`, `honor_window_hit`, `honor_window_expire`, `honor_justify_friend`, `honor_ignore_guarantee`, `honor_ignore_call`, `honor_ignore_skip_subject`, `honor_honor_guarantee`, `honor_join_allies_guarantee`, `honor_join_allies_call`, `honor_leave_faction_war`, `honor_leave_faction_peace`, `honor_expel_member`, `honor_release`, `honor_liberate`, `honor_break_pact_focus`, `honor_scenario_exempt`, `honor_ruling_party`, `honor_civil_war`, `honor_factor_change` and the `honor_band_*` set. The `#sandbox` gate is `sandbox_log_honor`, off by default; the monthly cross-system census (`sandbox_log_census()`, the nine `is_sandbox_census_country()` tags) prints honor, factor, obligation gain, tyranny, the two tyranny rates, obligations, justification pulses, all three rival slots and the civil-war count in one line whenever any of the honor/tyranny/rivals gates is up.

## Tooltips

`$add_honor` / `$add_tyranny` carry a `custom_effect_tooltip` (`LocKey_honor_change_tt` / `_tyranny_change_tt`), so a focus that grants Honor shows "Honor -50" in its own tooltip without a hand-written `effect_tooltip`.

## Gating betrayal focuses by band

Shipped. Each Honor band has its own meaning, and the required band depends on the relation between the two countries:

- **Inglorious or worse** (`honor < 25`): may break a non-aggression pact.
- **Dishonorable or worse** (`honor < -25`): may additionally attack a country it guarantees.
- **Treacherous** (`honor < -75`): may additionally attack a faction ally it fights alongside.

Implementation: `can_PREV_get_wargoal_on_THIS` in `core/common/scripted_triggers/99_sandbox_scripted_triggers.hsl` is tier-aware. Its `OR` is ordered and evaluated as written:

```
THIS in PREV.scenario_enemies[]          # declared scenario enemies: always allowed
is_friend_of_PREV(no)                    # a non-friend is always allowed
AND: is_ally_with(PREV)      + PREV->is_treacherous_leader()
AND: not ally, is_guaranteed_by(PREV) + PREV->is_dishonorable_leader()
AND: not ally, not guaranteed, has_non_aggression_pact_with(PREV) + PREV->is_honored_leader(no)
```

The triggers `is_dishonorable_leader` (Dishonorable or Treacherous) and `is_treacherous_leader` (Treacherous only) live beside `is_honored_leader` (Honorable or Righteous) and carry `LocKey_is_*_leader_tt` / `_tt_NOT` tooltip keys. The alias-safe wrapper `$can_get_wargoal_on($TAG)` (in `common/macros.hml`, `OR: not country_exists / $TAG->can_PREV_get_wargoal_on_THIS`) is what focus files should call for a tag that may be an alias; the `docs/gdd/National Focuses.md` "Antagonism" patterns already use the tiered trigger.

Note the pact branch still reads `is_honored_leader(no)`, i.e. its negation: a leader who is **not** Honorable or Righteous may break a pact. That is deliberately the Inglorious-or-worse band, but it is expressed through the inverted trigger rather than a dedicated `is_inglorious_leader`, so no extra tooltip key is needed.

## AI weighting

Every betrayal focus gets a betrayal factor next to the existing antagonism modifier: `clamp((25 - honor) / 125, 0, 1)`, applied only while at least one target is a friend. It is packaged as `$ai_betrayal_modifier()` (bare factor, caller supplies the friend trigger) and `$ai_betrayal_modifier_vs($TAG)` (single fixed target; also checks `country_exists` before entering the scope, then `is_friend_of_PREV()` and `is_scenario_enemy_of_PREV(no)`) in `common/macros.hml`; the exact focus-side patterns for single, multiple, and state-owner targets are in `docs/gdd/National Focuses.md`, "Antagonism".

A Treacherous AI (honor -100) betrays at full weight; an Inglorious AI at 24 almost never does. Combined with the tiered gate this keeps betrayals rare but not impossible for middling leaders. Declared scenario enemies are exempt: `$ai_betrayal_modifier_vs($TAG)` fails when the target is a scenario enemy, so an arc's war focuses are never damped by Honor.

Other countries' AI already reacts through the opinion modifiers of the leader traits (-20/-10/+10/+20 in vanilla, -40/-20/+20/+40 in Rt56); no additional AI strategy is required for this iteration.

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
- Weekly (`update_honor_gain_monthly_factor()`): clear `guaranting[]` / `na_pacts[]`, rebuild them from `every_other_country()`, then copy them into `prev_guaranting[]` / `prev_na_pacts[]` and call `apply_honor_for_dropped_obligations()`, which diffs the two pairs. Drops go into `dropped_guarantees[]` / `dropped_pacts[]` with `months_elapsed` stamps.
- Monthly: `months_elapsed += 1`, `expire_dropped_obligations()` purges drops older than 6 months, `apply_honor_for_unmet_obligations()` keeps last month's list of unmet obligations for the grace period, and `honor_answered_call[]` is cleared whenever the country is at peace.

`update_honor_gain_monthly_factor()` computes `honor_obligation_gain = clamp(0.20*len(guaranting) + 0.05*len(na_pacts) + 0.05*allies, 0, 1.0)`, then adds the drift and stores the sum in `honor_gain_monthly_factor`. The drift reads `honor > 0.25` / `< -0.25`, so the dead band is `|honor| <= 0.25`. The obligation arrays are cleared **before** repopulating, which is the fix for the historical inflation defect; `prev_honor_gain_monthly_factor` holds the previous week's factor so the census logs `honor_factor_change` only when the number actually moves.

Late-created countries: `on_weekly` initialises any country without `sandbox_initialized` (flag set inside `initialize_country_for_sandbox_mode()`).

One-shot flags: `sandbox_honor_skip_leave_faction` (set by `on_release_as_free` so the released nation's automatic faction exit is not a betrayal) is cleared every week so it cannot swallow a later, genuine exit. `expelled_by_leader` is **read by `on_leave_faction` and cleared by it**, but nothing in the mod sets it: no focus or decision calls `set_country_flag(expelled_by_leader)` today. The -15 expulsion penalty is therefore unreachable until an expelling focus or decision sets the flag immediately before the removal.

Macros with a `_country_` parameter that build a tooltip key (`$is_friend_of(FROM)` -> `LocKey_is_friend_of_FROM_tt`) need that key in localisation even when used inside a hidden effect.

Historical defect fixed by this change: `update_honor_gain_monthly_factor()` did not clear `guaranting[]` / `na_pacts[]` while running weekly, so the monthly factor inflated linearly over time. Both arrays are now cleared (after copying to the `prev_` snapshots) before repopulating.

All Honor changes go through `$add_honor()` so that the trait, the opinion modifiers, and the tooltip stay consistent. Do not write `&honor` directly outside `initialize_new_country_leader()` and the leader-change rule.

## Acceptance checklist

Log-first: a box is ticked only when the corresponding `#sandbox honor_*` line (raise the `sandbox_log_honor` gate first) or the census line proves it. An unticked box may still have its code shipped - see the section that describes it.

- [ ] A leader at Honor 20 with a pact partner completes a betrayal focus against it: Honor becomes -30, trait becomes Dishonorable, all other countries get the -10 opinion modifier, and the focus tooltip showed "Honor -50".
- [ ] The same leader betrays a second pact: Honor -80, Treacherous.
- [ ] A vanilla focus removes a pact; the AI justifies for 3 months and then declares war: no penalty at removal, -50 at the declaration (window), nothing more afterwards. If it declares after 7 months instead, nothing is charged.
- [ ] A guarantee is withdrawn: -10 the same week; war on that country 2 months later adds -30 (total -40). Two guarantees withdrawn in one week: -20.
- [ ] Justifying a wargoal on a pact partner for 90 days costs -6 (three batches of 30 daily pulses), not -180.
- [x] A rebel tag spawned by a civil war has Honor/Tyranny traits by the end of its first week; the coup victim's values are untouched.
- [x] A subject whose overlord fights a war the subject has not joined loses nothing for "ignoring" it.
- [ ] A country at Honor 0 with no obligations and no events stays at 0 indefinitely.
- [ ] A country at Honor 60 with no obligations declines to 30 after 10 years (0.25 x 120 months).
- [ ] A country at Honor 0 guaranteeing two minors and in a pact with one more gains `0.20*2 + 0.05 - 0.25 = +0.20` per month and reaches Honorable (25) after ~10.5 years; with four guarantees it reaches it in ~3.5 years.
- [x] Passive gain never exceeds +1.00 before drift, regardless of how many allies/guarantees exist.
- [ ] A guarantor that ignores a guaranteed country's defensive war loses 5 per month starting from the second month, and stops losing the moment it declares on the aggressor, gaining +15 once.
- [x] After a peaceful ruling-party change, Honor equals half the old value plus a random offset in [-50, 50], clamped.
- [ ] A leader at Honor -30 can take a "break pact" and "attack guaranteed" focus but not a "leave faction to attack ally" focus; at -80 all three are available. Unblocked by code: `can_PREV_get_wargoal_on_THIS` is tiered (`is_honored_leader(no)` for a pact, `is_dishonorable_leader()` for a guarantee, `is_treacherous_leader()` for a faction ally). What is still missing is the run itself.
- [x] The monthly factor shown in `LocKey_honor_tt` does not grow week over week when the diplomatic situation is unchanged (regression test for the array-clear bug).

## Out of scope for this iteration

- Honor effects on trade, licensing, and opinion beyond the existing trait modifiers.
- Player-facing decisions to "restore honor" (apologies, reparations).
- Honor for subjects toward their overlord (a puppet leaving its overlord's faction is not a betrayal).
- Attributing a cancelled non-aggression pact to the side that cancelled it (the game does not expose it; see "Withdrawing a guarantee without war").
- Historical-mode behaviour: everything here is sandbox-only.
