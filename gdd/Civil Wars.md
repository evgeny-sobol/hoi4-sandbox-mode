# Civil wars

A civil war is the most expensive way a country can change its politics: it splits the tag, burns divisions, and pulls neighbours in. In a randomised sandbox world a few of these are flavour. A dozen at once is noise — the player cannot tell a story in a map that is already on fire.

This document is about **how often** the AI starts one. It does not redesign vanilla civil-war content (Spanish Civil War, Cedillo, Vaps, second Finnish war). Those scripts stay. Sandbox only changes whether the AI walks into them, and whether a second country is allowed to explode while the first is still burning.

Civil wars are **not**:
- Honor. Starting a civil war does not cost Honor; Honor is about promises to *other* countries (`gdd/Honor System.md`).
- Tyranny as a value. A purge or a coup may raise Tyranny; the civil war itself is a method, not a Tyranny source (`gdd/Tyranny System.md`). Unconstitutional focuses that happen to start a war still use the existing tyranny tilt.
- A substitute for the revolution events `political.21/22/23`. Those already have an AI-only peaceful referendum; do not touch them here.

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`. Historical mode is unchanged.

## Why this is needed

`$ai_sandbox_modifier()` (`gdd/National Focuses.md`) sets every focus to weight 40 and historical AI plans are aborted. Political roots that vanilla AI almost never takes — `USA_america_first`, Baltic "break the silence" / Vaps, Norwegian fascist and communist openers — now compete with industry. Party-popularity factors then pull those roots. By 1936–37 several AIs complete the focus that actually fires `start_civil_war` in the same window.

Observed pile-up (one sandbox game): Norway, Estonia, Lithuania, Poland, Spain, Mexico, USA all in civil war at once. Spain is the scripted 1936 war and is expected. The others are alt-history focus branches.

What does **not** cause this pile-up (leave it alone in this iteration):
- Generic `prepare_for_*_civil_war` decisions: `ai_will_do = 0`.
- Revolution events `political.21/22/23`: AI picks the hidden referendum.
- Wartime stability crises (`stability.3` → draft dodging / strikes / mutiny). They can still start a war if a crisis at level 3 meets stability < 21%, but that is rare and sequential, not a 1936 cluster.

## Design goals

1. At most a handful of civil wars run at the same time. Spain plus one other is the default picture; a third waits until one of them ends.
2. A civil-war focus is a rare political beat, not a peer of "build civilian factories". The AI may still take it, especially a high-Tyranny ruler on an ideological branch.
3. Weight the **root** of a civil-war branch, not only the last focus. Otherwise the AI spends a year on the branch and detonates the moment a slot frees.
4. Do not cancel or rewrite vanilla start scripts (Spain 1936, Cedillo when its focus is taken, scripted revolts in Persia / Afghanistan). The cap applies to *new* AI-chosen wars, not to wars that have already started.
5. Player-taken focuses are unrestricted. The cap and the 0.25 factor are `ai_will_do` only.

## Model

### Active-war counter

Country-agnostic global `sandbox_civil_war_count`: number of **distinct `original_tag`** that currently have `has_civil_war = yes`.

Both sides of one war share an `original_tag` (SPR and SPA, USA and CSA, a Baltic government and its rebel). Counting tags, not countries, means Spain is 1, not 2–4.

Rebuild every `on_weekly` (and on `on_civil_war_end` so a slot frees without waiting a week):

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

**Cap: 2.** Scripted trigger `sandbox_civil_war_cap_reached`: `is_sandbox_mode_on()` and `sandbox_civil_war_count >= 2`.

While the cap is reached, AI weight on civil-war **ignition** focuses is 0. Wars already running continue. The player may still ignite another.

### Civil-war focus (definition)

A focus is a **civil-war ignition** focus if its `completion_reward` (or a scripted effect / event it always calls) can `start_civil_war` for ROOT.

A focus is a **civil-war root** if it is the first mutually exclusive pick that commits the tree to a branch whose later ignition focus is the normal outcome (not a rare random_list). Examples: `USA_america_first`, `USA_union_representation_act`, `FIN_the_second_finnish_civil_war`, `BALTIC_overthrow_the_government`, `EST_march_on_talinn`'s exclusive opener toward the Vaps, the Norwegian fascist / communist / "democratic to civil war" openers.

A focus that merely *reacts* to someone else's war (`SPR_lessons_from_the_civil_war`, intervention, volunteers) is neither. Do not tag it.

Spain's 1936 event is not a focus. It does not take an ignition tag. It still increments the counter once SPR is at war with itself.

## AI weighting

Macros in `common/macros.hml`, patterns in `gdd/National Focuses.md`.

**Ignition** (`$ai_civil_war_ignition_modifier()`), next to `$ai_sandbox_modifier()`:

```
macro ai_civil_war_ignition_modifier():
  factor(0.25)
  is_sandbox_mode_on()
  # same modifier block, second factor:
  # engine multiplies; a later standalone factor(0) would wipe add(40).
```

The cap is a **separate** modifier so aiview still shows 0.25 when the cap is free:

```
      +modifier:
        $ai_civil_war_ignition_modifier()
      +modifier:
        factor(0)
        sandbox_civil_war_cap_reached()
```

`factor(0.25)` applies even with an empty map: civil war is uncommon, not "only when the cap is hit". Combined with party/Tyranny factors the ignition focus is still takeable for a fascist/communist despot on an empty cap.

**Root** (`$ai_civil_war_root_modifier()`): same 0.25, **no cap**. Blocking the root when Spain is already at war would freeze every alt-history political branch in 1936. The cap only stops the match that lights the fuse. If the AI walked the branch and the cap is full, it idles on other available focuses until a slot opens, then may take the ignition focus.

Tyranny: ignition focuses that are also unconstitutional already have `$ai_high_tyranny_tilt()` / fork macros. Keep those. Do not add a second tyranny factor on the same block.

## Coverage (first pass)

Tag every vanilla focus whose reward contains `start_civil_war` (or `effect_tooltip` of one that the actual reward then runs). Known list in `common/national_focus/*.txt` as of 1.19 — not exhaustive of event-only wars:

- Direct `start_civil_war` in the focus: `AFG_the_faqirs_revolt`, `AFG_return_of_the_emir`, `AFG_parliamentary_democracy`, `AFG_socialist_coup`, `ARG_viva_la_revolucion`, `BALTIC_overthrow_the_government`, `BALTIC_arm_baltic_reds`, `BRA_ban_political_parties`, `BRA_launch_the_revolution`, `BUL_overthrow_the_tsar`, `BUL_abolish_the_monarchy`, `BUL_depose_the_tsar`, `CHL_avenge_the_pacification_of_araucania`, `COG_strike_while_the_rion_is_hot`, `COG_uniao_dos_povos_do_norte_de_angola`, `CZE_kohler_faction`, `DEN_seize_power`, `DEN_ask_for_support`, `EST_march_on_talinn`, `FIN_the_second_finnish_civil_war`, `FIN_a_fascist_regime`, `FRA_destroy_the_counter_revolution`, `wuw_HUN_reviving_the_spirit_of_1848`, `RAJ_give_me_blood_and_i_will_grant_you_freedom`, `RAJ_indian_peoples_army`, `RAJ_indian_national_army`, `IRQ_kurdish_revolt`, `JAP_cast_the_die`, `JAP_pre_emptive_coup`, `PER_strengthen_iranian_parliament`, `PER_force_abdication`, `PER_iranian_socialist_revolution`, `PER_march_on_saadabad`, `POR_reorganization_of_the_communist_party`, `lar_portugal_iberian_workers_united`, `POR_allow_free_elections`, `POR_ditadura_militar`, `POR_restoration_of_the_monarchy`, `SIA_the_kings_gambit`, `SIA_and_spring_the_trap`, `SIA_unseat_the_government`, `SAF_support_the_german_coup`, `AAT_Sweden_nationalists`, `TUR_restack_the_officer_corps`.

- Event / scripted-effect ignition (tag the focus that fires them): Mexican Cedillo (`mexico.1`), USA MTG civil war (`MTG_USA` events from the America First / Union Representation lines), Polish NSB civil-war events, Lithuanian / Latvian NSB counterparts, Norwegian AAT civil-war scripted effects. The middle designer walks each of NOR / EST / LAT / LIT / POL / USA / MEX from the political root to the war and tags **root + ignition**. If unsure whether a random_list can skip the war, still tag it: the cap only zeroes AI weight, it does not delete the reward.

Do not tag intervention / "lessons from the Spanish Civil War" / volunteer focuses.

## Events and decisions (this iteration)

- No overlay on `political.21/22/23` (AI referendum already).
- No overlay on `election.11/12` (AI ~32% civil war if opposition > 50%). Follow-up if democracies still explode on election night.
- No overlay on `stability.3` missions. Follow-up if wartime crises cluster.
- Generic political decisions stay at `ai_will_do = 0`.
- Country events that fire **without** a focus (Spain 1936, date-triggered revolts) are not capped at the source. They occupy a counter slot once running, which is enough to stop the AI lighting a second fuse.

## Honor, Tyranny, Rivals

No Honor change when a civil war starts. The winner still rolls Honor/Tyranny on `on_civil_war_end` as today.

Rivals: `on_civil_war_end` already re-rolls the winner's personal rival. No extra rule. A civil-war opponent is not auto-added as a rival (they are at war; `$is_rival_of()` already treats that as rivalry for gating).

## Implementation notes

- Counter and `seen[]` live in global scope. `seen[]` is a temp rebuild, not a persistent list of old wars.
- `sandbox_civil_war_cap_reached` is a scripted trigger so focus files do not read the variable with a raw `compare`.
- `$ai_civil_war_ignition_modifier` must **not** fold `factor(0)` for the cap into the same block as `factor(0.25)`: if the cap trigger fails, the whole modifier is skipped and the 0.25 would vanish. Two modifiers, as in the snippet above.
- `$ai_sandbox_modifier()` stays on those focuses. Order: sandbox 40, then 0.25, then cap, then party/Tyranny as today.
- Rebuild the counter on `on_weekly` **and** `on_civil_war_end`. Do not wait a week after Spain ends to open a slot.
- `original_tag` of a rebel is usually the parent's. If a dynamic `Dxx` tag ever shows `has_civil_war` with its own original_tag, it counts as its own slot; accept that.
- Compile after tagging `.include` files (`compile-after-hsl` rule).

## Acceptance checklist

- Spain goes to war in 1936 as vanilla. `sandbox_civil_war_count` becomes 1 (not 2+ for SPA/SPB/SPC).
- While Spain is fighting, a second country (e.g. Finland on the communist civil-war focus) may still take its ignition focus. A third country's ignition focus has AI weight 0.
- When one of those two wars ends, the third country's ignition focus is takeable again the same day (`on_civil_war_end`) or within a week.
- USA AI with moderate fascism may still open `USA_america_first` (root, 0.25, no cap) while Spain is burning, but `ai_will_do` on the actual civil-war event-focus is 0 until a slot is free.
- A human USA is not blocked by the cap.
- Historical mode: no counter, no 0.25, no cap. Vanilla AI plans unchanged.
- aiview on an ignition focus with cap free: sandbox 40 × 0.25 = 10, times party/Tyranny. With cap reached: 0.

## Out of scope for this iteration

- Rewriting Spain, Cedillo, or any `start_civil_war` reward.
- Player decisions "start / join a civil war".
- Spy coup operations (`00_operations.txt`).
- `election.11/12` AI chances.
- Stability-crisis civil wars.
- News events / notifications about the cap.
- A game rule for the cap (2 vs 3). Hard-code 2; promote to a rule only if testers want Spain + two others.

## Second iteration (not blocking)

- If the 1936 cluster is still too hot because many AIs *finish* the branch the week Spain starts: raise root 0.25 to a lower factor, or delay ignition with `days = 30` only when the cap is reached (hidden event) — that second option is a content change, not a weight change, and needs a separate pass.
- `election.11/12`: set civil-war `ai_chance` to 0 in sandbox if democracies still flip by ballot-box war.
- Count "player's civil war" toward the cap or not (currently it does, which is what we want: the player's Spanish playthrough still occupies a slot for the AI).
