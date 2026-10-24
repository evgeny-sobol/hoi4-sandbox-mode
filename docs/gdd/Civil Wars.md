# Civil wars

A civil war is the most expensive way a country can change its politics: it splits the tag, burns divisions, and pulls neighbours in. In a randomised sandbox world a few of these are flavour. A dozen at once is noise - the player cannot tell a story in a map that is already on fire.

This document is about **how often** the AI starts one and **how major powers react** when one runs. It does not redesign vanilla civil-war content (Spanish Civil War, Cedillo, Vaps, second Finnish war). Those scripts stay. Sandbox only changes whether the AI walks into them, whether the AI is allowed to start another while one is already burning, and which side major powers back.

Civil wars are **not**:
- Honor. Starting a civil war does not cost Honor; Honor is about promises to *other* countries (`docs/gdd/Honor System.md`).
- Tyranny as a value. A purge or a coup may raise Tyranny; the civil war itself is a method, not a Tyranny source (`docs/gdd/Tyranny System.md`). Unconstitutional focuses that happen to start a war still use the existing tyranny tilt.
- A substitute for the revolution events `political.21/22/23`. Those already have an AI-only peaceful referendum; do not touch them here.

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`. Historical mode is unchanged.

## Why this is needed

`$ai_sandbox_modifier()` (`docs/gdd/National Focuses.md`) sets every focus to weight 40 and historical AI plans are aborted. Political roots that vanilla AI almost never takes - `USA_america_first`, Baltic "break the silence" / Vaps, Norwegian fascist and communist openers - now compete with industry. Party-popularity factors then pull those roots. By 1936-37 several AIs complete the focus that actually fires `start_civil_war` in the same window.

The first pass zeroed `ai_will_do` on ignition **focuses** once three distinct `original_tag`s were at war. That did not stop the pile-up. Observed sandbox observer game (v0.1.1, `historical=0`, through Feb 1938): `cw` reached **8**. After `cap=1` / `ignition_base=0` the extra wars were still `cw_declare` from rebels (AST, GRE, then MEX, LIT, PER, POL, ITA) - missions, MTTH/plot events, BoP, `on_daily` - not tagged focuses (`cw_ignition` never fired). The counter was honest; the fuse was not on a focus.

Spain is the scripted 1936 war and is expected when a slot is free. The others are alt-history fuses that vanilla fires without asking the focus AI.

What does **not** cause this pile-up (leave it alone in this iteration):
- Generic `prepare_for_*_civil_war` decisions: `ai_will_do = 0`.
- Revolution events `political.21/22/23`: AI picks the hidden referendum.
- Spy coup operations (`00_operations.txt`).

## Design goals

1. At most one event/mission civil war runs for the AI at a time. A focus ignition may overlap it, so the map can still show two wars; a new event/mission ignition waits until the slot frees and its cooldown ends.
2. A civil-war focus is a rare political beat, not a peer of "build civilian factories". The AI may still take it, especially a high-Tyranny ruler on an ideological branch.
3. Weight the **root** of a civil-war branch, not only the last focus. The cooldown, not the root weight, now stops the AI from detonating the moment a slot frees.
4. Do not cancel or rewrite vanilla `start_civil_war` payloads (states, ideology, OOBs, character splits). The cap applies to *new* AI-started wars from **any** script that lights the fuse - focus, event, mission, decision, BoP range, `on_action`. Wars already running continue.
5. Player-started wars are unrestricted. Cap and the 0.25 factor are AI-only (`ai_will_do` / `ai_chance` / `is_ai = yes` on the overlay). A human Spain still gets 1936; a human Mexico still gets Cedillo if they let the mission expire.

## Model

### Active-war counter

Country-agnostic global `sandbox_civil_war_count`: number of **distinct `original_tag`** that currently have `has_civil_war = yes`.

Both sides of one war share an `original_tag` (SPR and SPA, USA and CSA, a Baltic government and its rebel). Counting tags, not countries, means Spain is 1, not 2-4.

Rebuild every `on_weekly` (and on `on_civil_war_end` so a slot frees without waiting a week). Also rebuild on `on_declare_war` when **both** ROOT and FROM have `has_civil_war` (so a new slot is visible the same day, without treating Italy intervening in Spain as a new civil war):

```
sandbox_civil_war_count = 0
seen[] cleared
every_country:
  if has_civil_war:
    t = original_tag
    if t not in seen[]:
      seen[].add(t)
      sandbox_civil_war_count += 1
```

**Cap: 1.** Scripted trigger `sandbox_civil_war_cap_reached`: `is_sandbox_mode_on()` and `sandbox_civil_war_count >= 1`.

While the cap is reached, the AI must not start another event/mission civil war. Wars already running continue. The player may still ignite another. A **focus ignition** is exempt (see "Focus exemption").

AI-blocked helper (events, missions, on_actions, BoP - anything that is not `ai_will_do`):

```
sandbox_civil_war_ai_blocked:
  is_ai = yes
  OR:
    sandbox_civil_war_cap_reached()
    sandbox_civil_war_cooldown_active()
```

`sandbox_civil_war_cap_reached` already requires sandbox mode. Do not fold `is_ai` into the cap trigger: aiview should still show the cap as a country-level fact.

### Focus exemption

A war that starts from a national-focus completion reward, directly or through a script the focus always calls, is a **focus ignition**. It is exempt from both the cap and the cooldown: the AI chose that branch on purpose, and the observed pile-up came from event/mission fuses, not focuses. A running focus ignition still counts in `sandbox_civil_war_count`, so it occupies the slot and blocks event/mission ignitions. Do not add a cap modifier to an ignition focus's `ai_will_do`; keep `$ai_civil_war_ignition_modifier()` (0.25) alone. No origin is recorded: the exemption lives at the ignition site, not in the counter.

### Cooldown

After a capped civil war ends, the slot is not free at once. A global `sandbox_civil_war_cooldown` holds the months left: it is set to `randi(0, 12)` at session start and every time `sandbox_civil_war_count` drops to 0, and decremented once a month. `sandbox_civil_war_cooldown_active` is `sandbox_civil_war_cooldown > 0`. The cooldown gates event/mission and decision ignitions; a focus ignition ignores it.

### Civil-war backing

For every ongoing civil war, each eligible AI major power backs the **kin side**: the side whose ruling government group matches the major's own. Eligibility is `sandbox_cw_backer_eligible` (`is_major = yes`, `is_ai = yes`, `not has_civil_war()`, `$has_stability(0.2)`). The existing `not has_war_with(<the war's original_tag>)` rule is applied **per kin side**, not as a gate on the major: the sweep only picks up a side the major is not already at war with (`if not PREV->has_war_with(THIS)`).

The sweep (`sandbox_cw_backing_sweep()`) runs weekly in HAI scope, fans out to every eligible major, and each major runs its own pass (`sandbox_cw_backing_for_major()`).

The choice is **frozen: only a war end drops it.** There is no ongoing check that the side still matches the backer's government. A backer that changes its own government mid-war re-evaluates on `on_government_change` (`sandbox_cw_backing_on_gov_change()`), which runs the same pass in strict mode: it drops any kin side it no longer matches, logging `cw_withdraw`, and picks up the newly matching side without waiting for the weekly sweep. Nothing else re-evaluates.

Per backed war, from the major's scope:

- **Opinion**: `cw_back_kin` (+20 in vanilla, +40 in Rt56) toward the kin side, and `cw_back_rival` (-20 in vanilla, -40 in Rt56) toward the **rival side** (the other side of the same war, found by walking `every_country_with_original_tag` for a side whose government differs). The ledger is per major: `cw_back_kin[]` / `cw_back_rival[]` hold the two sides of each backed war, index-aligned, with `0` in `cw_back_rival[]` when no rival side was resolved.
- **Access and AI pressure**: `give_military_access` to the kin side, `send_lend_lease_desire` (`value = 200`), and `send_volunteers_desire` (`value = 200` when the backer is fascist or communist).
- **Material aid**: `sandbox_cw_backing_monthly()` sends `infantry_equipment` monthly to each backed kin side, `clamp(5 * num_of_military_factories, 100, 2000)` with a floor of 100 when the backer has no military factories. It runs from the monthly HAI host, so the grant repeats while the war runs and stops once the prune drops the ended war.
- **Lifecycle**: backing is logged once per (backer, war) as `cw_support`; the weekly sweep is the prune and drops a backing (plus its two opinion modifiers) once the kin side no longer has `has_civil_war()`.

Gaps to know about: an ally-of-the-war check exists only in the sense above (backer vs the kin side); and a backer that is at war with the *rival* side is unaffected, since the shield reads the kin side.

### Civil-war focus (definition)

A focus is a **civil-war ignition** focus if its `completion_reward` (or a scripted effect / event it always calls) can `start_civil_war` for ROOT.

A focus is a **civil-war root** if it is the first mutually exclusive pick that commits the tree to a branch whose later ignition focus is the normal outcome (not a rare random_list). Examples: `USA_america_first`, `USA_union_representation_act`, `FIN_the_second_finnish_civil_war`, `BALTIC_overthrow_the_government`, `EST_march_on_talinn`'s exclusive opener toward the Vaps, the Norwegian fascist / communist / "democratic to civil war" openers.

A focus that merely *reacts* to someone else's war (`SPR_lessons_from_the_civil_war`, intervention, volunteers) is neither. Do not tag it.

### Event and mission ignition (definition)

An **event/mission ignition** is any vanilla script **outside** a national-focus `completion_reward` that can `start_civil_war` for ROOT (or for FROM / a scripted target) and thereby occupy a new `original_tag` slot.

Surfaces:
- Country events with MTTH / `trigger` (no-LaR `spain.1` / `spain.10`).
- `is_triggered_only` events whose `immediate` or only option always starts the war (`mexico.1`, `PER_revolution_events.1`).
- Events with an AI-chosen civil-war option (`election.11.b` / `election.12.b`, some GRE/BFTB options).
- Decision `complete_effect` / mission `timeout_effect` / `complete_effect` (Cedillo, Polish peasant strike, AST veterans).
- `on_action` / `on_daily_TAG` (`on_daily_AST` veterans revolt).
- BoP `on_activate` that fires a civil-war event (ITA grand council total-control range -> `BBA_italy_civil_war.1`).

Not ignition (do not overlay):
- Intervention, volunteers, "lessons from the Spanish Civil War".
- Character/OOB follow-ups that run **after** `has_civil_war` is already true.
- `political.21/22/23` (AI civil-war options already have `ai_chance = 0`).

Spain's 1936 war is an event/mission ignition (no-LaR: `spain.1`; LaR: election `lar_spain.1` then military-plot **missions**). It is **not** exempt from the cap. When a slot is free it fires as vanilla. When the cap is reached, AI Spain waits; it still occupies a slot once the war starts. A human SPR is never delayed.

A war started **by another tag** (ENG decision lighting AST, LIT event lighting POL) is still an ignition for the **target**'s `original_tag`. Gate the AI actor. The player taking that decision is unrestricted.

## AI weighting (focuses)

Macros in `common/macros.hml`, patterns in `docs/gdd/National Focuses.md`. Unchanged from the first pass.

**Ignition** (`$ai_civil_war_ignition_modifier()`), next to `$ai_sandbox_modifier()`:

```
macro ai_civil_war_ignition_modifier():
  factor(0.25)
  is_sandbox_mode_on()
```

No cap modifier sits on the ignition focus: a focus ignition is exempt from the cap and cooldown ("Focus exemption"). The weight is only:

```
      +modifier:
        $ai_civil_war_ignition_modifier()
```

`factor(0.25)` applies even with an empty map: civil war is uncommon, not "only when the cap is hit". Combined with party/Tyranny factors the ignition focus is still takeable for a fascist/communist despot on an empty cap.

**Root** (`$ai_civil_war_root_modifier()`): same 0.25, **no cap**. Neither root nor ignition is capped now: a focus ignition is exempt, so a branch the AI committed to can always fire. The cap and cooldown stop event/mission ignitions only.

Tyranny: ignition focuses that are also unconstitutional already have `$ai_high_tyranny_tilt()` / fork macros. Keep those. Do not add a second tyranny factor on the same block.

## Event and mission overlays

Do **not** wrap `start_civil_war` in a generic scripted effect: the payload (ideology, size, states, characters) is different at every call site. Overlay around the call. Delay; do not delete the fuse.

`is_triggered_only` events and mission timeouts often set "already revolted" flags in `immediate` **before** `start_civil_war`. If you skip the war after those flags, the revolt is eaten forever. Gate **before** the flag, or restart the mission / re-fire the event without setting the flag.

### Pattern A - MTTH / daily trigger (Spain no-LaR)

The event re-evaluates every day. Add `NOT sandbox_civil_war_ai_blocked()` to `trigger` (or an equivalent `OR = { is_ai = no NOT cap }`). When the cap frees, vanilla MTTH continues. A failed trigger cannot log: weekly `cw_defer spain` is what proves AI Spain is waiting. When the event actually fires, `cw_event spain.1` / `spain.10`.

LaR Spain: overlay the **military-plot missions** that actually start the war, not only `lar_spain.1` (that event is the 1936 election and must still fire). Active plot missions already emit `cw_defer`.

### Pattern B - AI-choice option (elections, some country events)

On the option that calls `start_civil_war`:

```
ai_chance:
  +modifier:
    factor(0)
    sandbox_civil_war_ai_blocked()
```

The peaceful / other option stays. Player still sees both. If **every** option starts a war (ITA `BBA_italy_civil_war.1`), this pattern cannot save it - use C at the **caller** (BoP `on_activate`, focus, mission). `ai_chance = 0` cannot log a skip; the civil-war option logs `cw_event` when taken.

### Pattern C - Forced fuse (immediate, timeout, on_daily, BoP)

```
if:
  sandbox_civil_war_ai_blocked()
  # defer: activate_mission again, or country_event = { id = X days = 7 }, or skip this on_daily tick
  log("#sandbox ... cw_defer ...")
else:
  # vanilla start_civil_war / country_event unchanged
```

For `on_daily_AST` veterans: add `NOT sandbox_civil_war_ai_blocked()` to the existing `if` limit. Next day, if stability is still low and a slot is free, it fires. Do not clear `AST_veterans_revolt_active` on a deferred tick.

For ITA BoP: do not fire `BBA_italy_civil_war.1` while blocked; check again when the range is still active and the cap frees (weekly / next `on_activate` if the range re-triggers; if it does not, a short hidden event on `on_weekly` while the range is active).

### Pattern D - Decisions the AI can take

Same as focuses: `ai_will_do` `factor(0)` via `$ai_civil_war_decision_cap()`, which fires when `sandbox_civil_war_cap_reached()` OR `sandbox_civil_war_cooldown_active()` (the cooldown gates decision ignitions too). `available` unchanged (player). Includes ENG decisions that `start_civil_war` on a dominion.

## Coverage

### Focuses (first pass, keep)

Tag every vanilla focus whose reward contains `start_civil_war` (or `effect_tooltip` of one that the actual reward then runs). Known list in `common/national_focus/*.txt` as of 1.19:

- Direct `start_civil_war` in the focus: `AFG_the_faqirs_revolt`, `AFG_return_of_the_emir`, `AFG_parliamentary_democracy`, `AFG_socialist_coup`, `ARG_viva_la_revolucion`, `BALTIC_overthrow_the_government`, `BALTIC_arm_baltic_reds`, `BRA_ban_political_parties`, `BRA_launch_the_revolution`, `BUL_overthrow_the_tsar`, `BUL_abolish_the_monarchy`, `BUL_depose_the_tsar`, `CHL_avenge_the_pacification_of_araucania`, `COG_strike_while_the_rion_is_hot`, `COG_uniao_dos_povos_do_norte_de_angola`, `CZE_kohler_faction`, `DEN_seize_power`, `DEN_ask_for_support`, `EST_march_on_talinn`, `FIN_the_second_finnish_civil_war`, `FIN_a_fascist_regime`, `FRA_destroy_the_counter_revolution`, `wuw_HUN_reviving_the_spirit_of_1848`, `RAJ_give_me_blood_and_i_will_grant_you_freedom`, `RAJ_indian_peoples_army`, `RAJ_indian_national_army`, `IRQ_kurdish_revolt`, `JAP_cast_the_die`, `JAP_pre_emptive_coup`, `PER_strengthen_iranian_parliament`, `PER_force_abdication`, `PER_iranian_socialist_revolution`, `PER_march_on_saadabad`, `POR_reorganization_of_the_communist_party`, `lar_portugal_iberian_workers_united`, `POR_allow_free_elections`, `POR_ditadura_militar`, `POR_restoration_of_the_monarchy`, `SIA_the_kings_gambit`, `SIA_and_spring_the_trap`, `SIA_unseat_the_government`, `SAF_support_the_german_coup`, `AAT_Sweden_nationalists`, `TUR_restack_the_officer_corps`.

- Event / scripted-effect ignition **from a focus**: tag **root + ignition** on NOR / EST / LAT / LIT / POL / USA / MEX. A focus ignition is exempt from the cap, so the overlay must not block the event/mission the focus fires. Un-overlay the events reachable only from an ignition focus (`PER_revolution_events.1` in both mods; r56 `lithuania.16`, `portugal.44` / `portugal.45`; the vanilla NSB war-starters `.001` / `.003` / `fascist.001`). Keep the overlay where a non-focus fuse shares the event (r56 `NSB_soviet_civil_war_common.003` from `on_daily_SOV`): there the focus ignition stays capped. The r56 USA focuses that fire `mtg_usa_civil_war_*` are untagged; tag them with `$ai_civil_war_ignition_modifier()`.

Do not tag intervention / "lessons from the Spanish Civil War" / volunteer focuses.

### Events, missions, decisions, on_actions (this pass)

Walk vanilla `start_civil_war` outside `common/national_focus/`. Overlay every ignition. Known holes from the v0.1.1 playtest, plus the same-family scripts:

- **Spain**: no-LaR `spain.1` / `spain.10`; LaR military-plot missions (not the election event).
- **Mexico**: `MEX_mission_cedillos_rebellion` timeout -> `mexico.1`; Cristiada / second-revolution missions -> `mexico.28` / `mexico.30`.
- **Australia**: `on_daily_AST` veterans revolt; `AST_veterans_revolt` mission timeout; TAOG paths that call `AST_instigate_civil_war_in_target` on AST itself.
- **Greece**: BFTB events that `start_civil_war` (`bftb_greece.105` via `bftb_greece.100` else_if + weekly retry, `.218` from `.207.b` Pattern B - not the "start a war in Turkey" options unless TUR is the target slot).
- **Poland**: sanation decisions (`POL.txt` -> `POL_sanation_left_opposition_up` / `POL_sanation_right_opposition_up`, Pattern D), `NSB_poland_monarchist_events.5` (Pattern B), and the peasant-strike timeout (Pattern C). The sanation path was the prime ungated hole; the peasant strike was gated only at `activation`.
- **Baltic**: LIT/LAT/EST decisions and NSB events that start a war in ROOT (and LIT events that start one in POL - gate the actor, count the target). `EST_vaps_down_effect` (same pattern as Iron Wolf). `EST_events.7` trigger + weekly retry (`sandbox_retry_est_civil_war_fuse`). `LAT_events.8` (both options war; mission `available` + event trigger). `LIT_events.10` / `EST_events.9` Pattern B. The mission delay covers `EST_vaps_uprising`, `EST_stomp_the_vaps`, `LAT_perkonkrust_uprising`, `LIT_iron_wolf_partisans` and `BALTIC_belarus_uprising`.
- **Persia**: `PER_revolution_events.1` (event trigger + weekly retry, `sandbox_retry_per_civil_war_fuse`) and ignition on `PER_revive_old_ways`; `PER_civil_war_imminent` mission delay.
- **Italy**: BoP `ITA_grand_council_total_control_range` -> `BBA_italy_civil_war.1` (event trigger + weekly retry). Overlays use `sandbox_civil_war_ai_allowed()` (`= yes`), not `scripted_trigger = no`.
- **Ethiopia**: BoP total-control ranges -> `BBA_ethiopia_balance_of_power_events.01`; weekly retry while the range is still live.
- **Siam**: `siam.8` (Songsuradet, delayed from `siam.7`); `SIA_war_fervor_coup` mission; the khana-ratsadon coup missions `SIA_khana_ratsadon_military_coup_mission` / `SIA_khana_ratsadon_civilian_coup_mission` (activation gate + mission delay). `SIA_war_fervor_coup_dummy` has no caller in vanilla and is unreachable.
- **The remaining ids in the shared delay loop** (Mexico is covered above): the four `ENG_support_imperialist_coup_in_{canada,south_africa,australia,new_zealand}_mission_1`, `GRE_civil_war_imminent` plus `_1`..`_4`, `HUN_the_incoming_fascist_civil_war_mission`, `GUAY_military_coup_mission`, `CHL_nacista_coup_attempt`, `ARG_military_coup_attempt`, and the two `RAJ_communist_unions_promised_*_mission` ids. The list lives in `sandbox_delay_capped_cw_missions()` in core plus the per-mod tail; `MEX_mission_second_cristiada` and `MEX_mission_second_revolution` are there too, beside the Cedillo mission.
- **Soviets**: ignition focuses `SOV_left_opposition_coup` / `SOV_coup_detat` / `SOV_the_hands_do`, plus the events they queue.
- **Lithuania**: `LIT_iron_wolf_partisans` / `LIT_iron_wolf_down_effect` (Iron Wolf idea tick at bad_4). `EST_vaps_down_effect` is the same family.
- **Elections**: `election.11.b` / `election.12.b` - Pattern B.
- **UK/dominions**: ENG decisions that `start_civil_war` on CAN/SAF/AST/NZL.
- **Stability crises**: `common/decisions/stability_war_support.txt` missions - Pattern C. The v0.2 playtest showed they cluster, so they are now under the cap. The ids the weekly delay loop actually holds are `draft_dodging_mission`, `strikes_mission`, `mutiny_mission`, `demob_economic_mission` and `demob_manpower_mission` (the GDD previously named the missions without their `_mission` suffix).
- **Decisions**: the CHL / BUL / GUAY / HUN / USA / RAJ_GOE / SWE / BALTIC decisions that `start_civil_war` - each AI path verified and gated (Pattern D). CHL / BUL / SWE now have overlays; GUAY / HUN / RAJ_GOE go through the mission delay; USA / BALTIC were already gated. CHL also has the `CHL_nacista_coup_attempt` mission (978-day timeout -> `CHL_political_events.14`) - Pattern A + C. The `ignite_the_*_civil_war` decisions are player-only (`ai_will_do factor = 0`).
- **Spy coups**: `common/operations/00_operations.txt` (`operation_coup_government`) and the LaR_FRA coup can start an AI civil war past the cap. Deliberately left ungated (see Out of scope).
- **Ethiopia (BBA)**: the BoP `.01` event - Pattern A (a Pattern B `ai_chance` gate did not stop the forced option). The fascist `.02` / `.03` / `.04` events only carry `custom_effect_tooltip` tooltips, not a real `start_civil_war`, so they are not gated; `.07` is focus-queued and exempt.
- **Bulgaria (BFTB)**: `bftb_bulgaria_fatherland_front.2` (Pattern A; the weekly `on_weekly_BUL` retry re-fires `BUL_ff_tries_to_stage_a_coup_effect`).
- **Yugoslavia (DOD)**: `DOD_yugoslavia.701.b` (Pattern B; the resist option runs `YUG_start_peters_coup`). `DOD_yugoslavia.1` has no caller in vanilla.
- **Japan (SEA)**: `SEA_japan_popup_events.22` / `.29` are queued only by the Japan focus tree, so they are focus-exempt and left ungated.
- **Focus-queued ignitions**: a focus whose reward queues a civil-war event is a focus ignition (exempt). Log `cw_ignition` on the focus (`$sandbox_log_cw_ignition`) plus the `$ai_civil_war_ignition_modifier()`, so the acceptance run can tell an exempt ignition from a leak. Tagged this pass: `GER_oppose_hitler_ww` (queues `wtt_germany.1`), `ETH_declare_for_italy` (`BBA_ethiopia_fascist_events.07`), `ITA_defy_the_duce` (`BBA_italy_civil_war.300`), `JAP_revoke_the_peace_preservation_law` (`SEA_japan_popup_events.22` / `.29`), `LIT_king_of_poland` (`NSB_poland_monarchist_events.5`), `SPR_portuguese_anarchism` / `SPR_support_french_communists`, `ARG_march_to_la_casa_rosada` / `ARG_joint_military_exercises`, `TUR_democratic_capstone_focus` / `TUR_support_the_golden_square`, `GRE_ally_tito`, `ENG_isolate_the_mediterranean_threat`, `POR_the_empire_of_brazil`, `JAP_ignite_the_korean_peninsula`, `AST_support_indonesian_uprising`. (`CZE_exclude_the_slovaks`, `BEL_adriaan_martens_crisis` / `BEL_snap_election`, `YUG_purchase_foreign` and `MAN_tsr_a_new_dawn_over_manchuria` were checked and are NOT ignitions, so they are not tagged.)
- **Self-rearming / countdown missions**: `POL_sanation_left_irritation` / `POL_sanation_right_irritation` start the war in their `timeout_effect` and re-arm. The Pattern C mission delay alone did not hold (observed POL 1937-09, PER 1937-11), so the `timeout_effect` is replaced (`-timeout_effect:` + `+timeout_effect:`) with a gated version that skips the war while `sandbox_civil_war_ai_allowed()` is false but keeps re-arming. `PER_civil_war_imminent` gets the same `timeout_effect` gate. `BUL_impending_zveno_coup` gets only an activation gate (it auto-activates on `BUL_impending_zveno_coup_flag`); its 236-line `timeout_effect` is not expressible in the overlay DSL, so a cap that fills mid-mission relies on the Pattern C delay alone. The `-name:` removal is a new overlay capability, used only here.
- **Event / idea / on_action families** (Pattern A unless noted, all confirmed not focus-queued): `france.14`, `germany.65` / `germany.73`, the eight `SEA_japan_foreign_policy.*` war events, `wuw_GER_civil_war.6` / `wuw_GER_diplomacy.75` / `wuw_GER_realpolitik.27-29`, `mtg_britain.33` / `.55`, `mtg_netherlands.73`, `mtg_usa_civil_war_democrats.20`, `mtg_news.58`, `AAT_Sweden_communism.4` / `AAT_Sweden_flashpoints.53`, `AUS_political_events.89`, `ARG_political_events.11`, `INS_communist_events.4`, `tfv_canada.30`, `south_american_news.8`, `GOE_RAJ.46`, `lar_low_stability_civil_war.1` / `.2`, `wtt_germany.31-34`, `britain.23`, `CHL_political_events.83` / `.85`, `ss_recruitment_event.14` / `.26`, `stability.33`, `DOD_yugoslavia.184.a` (Pattern B).
- **Player-only, not gated**: `political_decisions.txt` `ignite_the_*_civil_war` (`ai_will_do factor = 0`), the spy coups (`common/operations`), and the commented-out `soviet.24` / `.36` / `czech.14` sites.
- **Focus-queued, left exempt**: `congo_independence_struggle.15` / `.24`, `SEA_warlords.39` / `.46`, `wtt_germany.28`, `germany.61` / `.66` / `.92`, `SEA_japan_popup_events.38`, `SEA_china_democratic.5`, `denmark_fascist_event.3` (Danish focus -> `.1.b` -> `.3`).
- **Not ignitions, do not overlay**: `political.5` / `.7` (every `start_civil_war` is commented out) and `political.21` / `.22` / `.23` (AI war options already `ai_chance = 0`; the AI takes the referendum).
- **Soviets (NSB)**: the war-starter events are queued only by the SOV ignition focuses, so they are focus-exempt and left ungated.
- **Norway**: `NOR_start_communist_civil_war` / `NOR_fcw_effect_*` are reached only from the focus tree, a debug decision, or player-only paths, so no AI-reachable non-focus fuse remains.
- Pattern B (`ai_chance` 0) blocks on `sandbox_civil_war_ai_blocked()` (cap OR cooldown), not `sandbox_civil_war_cap_reached()` alone, so a cooldown also steers the AI off the war option.

If unsure whether a `random_list` can skip the war, still overlay: the cap only delays the AI, it does not delete the reward.

## Honor, Tyranny, Rivals

No Honor change when a civil war starts. The winner still rolls Honor/Tyranny on `on_civil_war_end` as today.

Rivals: `on_civil_war_end` already re-rolls the winner's personal rival. No extra rule. A civil-war opponent is not auto-added as a rival (they are at war; `$is_rival_of()` already treats that as rivalry for gating).

## Implementation notes

- Counter and `seen[]` live in global scope. `seen[]` is a temp rebuild, not a persistent list of old wars. Dedup with `every_country_with_original_tag` / `original_tag_to_check = THIS` - do not bind a loop variable that compiles `THIS` to the weekly ROOT.
- `sandbox_civil_war_cap_reached` is a scripted trigger so focus files do not read the variable with a raw `compare`. Vanilla overlay `limit` / `trigger` blocks use `sandbox_civil_war_ai_allowed()` (`NOT` of `sandbox_civil_war_ai_blocked`). Do not write `sandbox_civil_war_ai_blocked = no`: custom `scripted_trigger = no` does not reliably invert.
- `$ai_civil_war_ignition_modifier` is `factor(0.25)` alone. Do not add a `factor(0)` cap block: a focus ignition is exempt from the cap and cooldown.
- `$ai_sandbox_modifier()` stays on those focuses. Order: sandbox 40, then 0.25, then party/Tyranny as today.
- Rebuild the counter on `on_weekly`, `on_civil_war_end`, and civil-war `on_declare_war`. Do not wait a week after Spain ends to open a slot.
- `original_tag` of a rebel is usually the parent's. If a dynamic `Dxx` tag ever shows `has_civil_war` with its own original_tag, it counts as its own slot; accept that.
- Empty `t*` in `#sandbox` pulses often print the pulse ROOT (HAI) when the array slot is empty. Trust `cw=`, not unique `t*` tags.
- Compile after tagging `.include` files (`compile-after-hsl` rule), including `events/` and `common/decisions/` overlays.
- The cooldown is global (`sandbox_civil_war_cooldown`), rolled by `sandbox_civil_war_roll_cooldown()` at session start and again inside `update_sandbox_civil_war_count()` whenever the count drops to 0, and decremented monthly by `sandbox_civil_war_cooldown_tick()` from the HAI host.
- The delay helper is `$sandbox_delay_mission_if_capped(_mission_)`: it adds 8 days to an **active** mission's timeout and logs `cw_defer`. The loop lives in `sandbox_delay_capped_cw_missions()` in core, which holds only vanilla ids; `sandbox_delay_capped_cw_missions_mod()` in each mod's per-mod catalog appends the ids that are not portable (vanilla adds `POL_sanation_left_irritation` / `POL_sanation_right_irritation`; the Rt56 catalog has its own tail). `on_weekly` calls the pair once per country, so every country's own active missions get the extension.
- The weekly retry helpers `sandbox_retry_ita_civil_war_fuse()`, `sandbox_retry_eth_civil_war_fuse()`, `sandbox_retry_sov_civil_war_fuse()`, `sandbox_retry_gre_civil_war_fuse()`, `sandbox_retry_per_civil_war_fuse()` and `sandbox_retry_est_civil_war_fuse()` fire the fuse **from `on_weekly`, in every country's scope**, each guarded by `original_tag(...)` and `not has_civil_war()`. They are the deferred-ignition path for a `on_activate`/`on_daily` fuse that a Pattern C skip would otherwise eat. `sandbox_log_waiting_cw_fuses()` is the read-only companion that logs `cw_defer` for the Pattern A fuses that cannot log themselves (`spain`, `on_daily_AST`, `sfl.1`).
- Backing liveness is `has_civil_war()` on the ledger's kin side, not the backer's government. A `cw_back_kin[]` entry whose side still fights is kept even after the backer's government changed; only the `on_government_change` strict pass removes it.

## How to read `game.log`

First line is the version (`#sandbox Mode Overhaul v0.4.0`, matching `descriptor.mod`). Next is `sandbox_start historical=0` or `historical=1`.

| Token | When | What to read |
| --- | --- | --- |
| `cw_pulse` | weekly, HAI | Census. Use `cw=` and `cap=`. The `N->N` arrow is the post-rebuild snapshot, not a weekly delta. Ignore `t*` for identity. |
| `cw_count` | counter actually changed | Same fields; the arrow *is* the delta. |
| `cw_declare` | civil-war `on_declare_war` | Slot taken. Arrow should be `N->N+1` (Spain is 1, not SPR+SPA). `ai=0` if **either** ROOT or FROM is human (ROOT is often a Dxx rebel). `other=` is the other side - use that, not Dxx, to name the war. |
| `cw_end` | `on_civil_war_end` | Slot freed the same day. Then a waiting fuse may fire that day or within a week. |
| `cw_ignition` / `cw_root` | focus `completion_reward` | `ai=0` is the player. Neither root nor ignition is capped; a focus ignition is exempt. |
| `cw_defer` | Pattern C skip this week | Tag + fuse id (`spain`, mission id, `BBA_italy_civil_war.1`, `on_daily_AST`). Proves the AI is waiting, not that vanilla has not rolled yet. |
| `cw_event` | fuse actually fired | `spain.1` / `spain.10`, `election.11.b` / `12.b`, ITA retry. `ai=` is THIS (the country running the event), not a rebel. |
| `cw_support` | weekly backing sweep | A major backs a civil-war kin side (feature: civil-war backing). `kin=` / `rival=` name the two sides; `ai=1` always (backing is AI-only). Emitted once per (backer, war). |
| `cw_withdraw` | `on_government_change` | A backer drops a kin side it no longer matches after its own government changed (issue 04). `kin=` names the dropped side. |

**Fail the cap** if an event/mission ignition starts while `cap=1` or `cool>0`, or if `cw=` rises without a focus ignition behind it. `cool=` is months left in the cooldown (0 = inactive). A player (`ai=0`) is unrestricted.

**Name an ungated fuse:** an AI `cw_declare` that raises the count with no `cw_ignition`, `cw_event`, or `cw_defer` for that original_tag in the days before it. v0.1.1 playtest extras (AST, GRE, MEX, LIT, PER, POL, ITA) must now show `cw_defer` or `cw_event` first. A new extra without those tokens is a hole (NSB events, `bftb_greece.105` from `.100`, `bftb_greece.218`).

**Silent by design:** Pattern A (`+trigger`), Pattern B skip (`ai_chance` 0) and Pattern D (`ai_will_do` 0) do not log the *deferral*: while the cap is full the event / option / decision is discarded, so no `cw_*` line is emitted. A Pattern A overlay may still log `cw_event` when the event fires once the cap frees (e.g. Ethiopia). Prove them by the fail rule above, not by a defer line. (Pattern C logs `cw_defer`.)

Historical: after `sandbox_start historical=1` the rest of the log must not contain `cw_`. Overlay files still exist; their gates require sandbox mode, so they are no-ops.

## Acceptance checklist

Log-first. Observer sandbox unless the item says human or aiview. Tick only when the grep holds (compound items split so a partial pass is visible).

- [x] First `#sandbox` line is the current version; next is `sandbox_start historical=0`.
- [ ] Spain 1936 with `cw=0` once the session-start cooldown expires (the start roll may delay it 0-12 months): `cw_event spain.1` / `spain.10` / `lar_spain.2` then `cw_count` whose arrow is `0->1` (not +2 for SPA/SPB).
- [ ] AI Spain while `cap=1` and no SCW yet: weekly `cw_defer spain` (and `cw_defer SPA_military_plot_nationalists` / `SPR_military_plot_republicans` if LaR missions are already ticking). No `cw_event spain.1` until a `cw_end` drops the count to 0 and the cooldown expires.
- [ ] Human SPR at `cap=1`: no `cw_defer spain`; `cw_event spain.1` with `ai=0`; `cw_declare` `ai=0`.
- [x] After Spain, one more event/mission war may start (`cw=` 1) from event (`cw_event`) or mission (`cw_defer` then `cw_declare`); a focus ignition (`cw_ignition`) may overlap it.
- [x] No AI event/mission `cw_declare` while `cap=1` or `cool>0`, except a spy coup. v0.1.1 hit 8 via event/mission after `cap=1`; that must not recur through 1938.
- [ ] Capped ITA BoP: `cw_defer BBA_italy_civil_war.1` weekly while the range is active; after `cw_end`, `cw_event BBA_italy_civil_war.1` (same week or next).
- [x] Capped Cedillo / peasants / veterans with the mission already ticking: `cw_defer MEX_mission_cedillos_rebellion` (or `POL_peasants_strike` / `AST_veterans_revolt` / `on_daily_AST`); after `cw_end`, the timeout may fire within a week (no more defer, then `cw_declare`). `POL_peasants_strike` is gated in its own decision file (`common/decisions/POL.include` puts `sandbox_civil_war_ai_allowed()` on the decision's `activation`), not through the weekly mission-delay loop.
- [ ] `cw_root USA_america_first` may appear while `cap=1`. A focus ignition (`cw_ignition USA_ally_with_the_silver_shirts` / `USA_union_representation_act`) is exempt, so it may appear at `cap=1`; only event/mission ignitions must wait.
- [ ] Human USA ignition or human Mexico Cedillo timeout at `cap=1`: `cw_ignition` / `cw_declare` with `ai=0`; no `cw_defer` from that player tag.
- [ ] Historical: `sandbox_start historical=1`, then no `cw_` lines. Vanilla Spain 1936 still happens in-game.
- [ ] aiview (in-game, not the log) on an ignition focus: sandbox 40 x 0.25 = 10, times party/Tyranny, at any cap (a focus ignition is not capped).

## Out of scope for this iteration

- Rewriting Spain, Cedillo, or any `start_civil_war` payload (states, ideology, OOBs).
- Player decisions "start / join a civil war" besides applying the same AI gate as other decisions.
- Spy coup operations (`00_operations.txt`). They can still start an AI civil war past the cap. This is deliberate: the coup is the spy system's outcome, not a scripted civil-war fuse, and a spy-coup `cw_declare` is an allowed exception to the acceptance rule.
- (Stability-crisis missions moved in scope: the v0.2 playtest showed they cluster - see Coverage.)
- News events / notifications about the cap.
- A game rule for the cap. Hard-code 1; promote to a rule only if testers want it tighter.

## Second iteration (not blocking)

- If the 1936 cluster is still too hot because many AIs *finish* the branch the week Spain starts: lower root 0.25, or delay ignition with `days = 30` only when the cap is reached (hidden event) - that second option is a content change, not a weight change, and needs a separate pass.
- Reserve a slot for Spain so 1936 always fires even if another war went first - only if testers want Spain guaranteed.
- Count "player's civil war" toward the cap or not (currently it does, which is what we want: the player's Spanish playthrough still occupies a slot for the AI).
- `stability.3` is now gated (see Coverage); revisit if the mission delay proves too weak.
