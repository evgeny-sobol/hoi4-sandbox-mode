# Rivals

Rivals answer one question about a country: "**whom** does it want to fight?" Honor answers "how does it treat its promises" (`docs/gdd/Honor System.md`), Tyranny "how does it rule at home" (`docs/gdd/Tyranny System.md`), Opinion "how do others feel about it". In a randomised sandbox world rivalries are the source of long, readable conflicts: they steer AI aggression and tell the player why someone is sharpening a knife for them.

Rivalry is **not**:
- An excuse. Attacking a rival protected by a pact or guarantee costs the same Honor as attacking anyone else.
- Opinion. Rivalry *feeds* opinion through two opinion modifiers; opinion never creates or removes a rival.
- War. Being at war makes `$is_rival_of()` true for gating purposes, but war alone does not put a country into `rivals[]` (declaring war on us does, see "Event-driven rivals").

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`.

## Where it lives

Shared code lives in `core/` and syncs into both mods; the two per-mod files are the opinion-modifier values and the generated AI plans.

- `core/common/scripted_effects/99_sandbox_scripted_effects.hsl`: selection (`select_major_rival`, `select_minor_rival`), slot discipline (`set_rival`, `clear_rival`, `reroll_leader_rival`, `add_rivalry_vs`, `become_event_rival`), monthly loop (`review_rivals`, `update_rivalry_monthly`, `fill_rival_vacancies`, `expire_former_rivals`), hooks (`apply_rivalry_on_declare_war`, `apply_rivalry_on_capitulation`, `clear_annexed_from_rivals`).
- `core/common/macros.hml`: `$add_rivalry`, `$rivalry_vs_into`, `$ai_rivalry_modifier`, `$ai_rivalry_modifier_max`, `$not_rival_of_PREV`, `$is_rival_of`, `$sandbox_add_rivalry_vs`, `$sandbox_seed_rival`, the AI-plan macros `rival_base` / `rival_contain` / `rival_feud`, and the economic-posture band predicates that ride on top of them (`$is_rivalry_at_least`, `$is_rival_or_above`, `$is_feud`, `$is_cold_band`; ADR-0007).
- `core/common/ai_strategy/99_sandbox_rivals_system.hsl`: three plan bodies per tag (`<TAG>_is_rival`, `<TAG>_is_rival_contain`, `<TAG>_is_rival_feud`), each a one-line call to the matching macro. The file is synced from core, so the tag list is shared by both mods; edit core, never the mod copy.
- `core/common/scorers/country/99_sandbox_scorer.hsl`: `major_rivals_scorer` (from `global.majors`, ideology-driven), `minor_rivals_scorer` (from `global.countries`, geography-driven), plus `scenario_join_scorer` for the scenario join lever. The scorer file is on the sync **exclude** list (`tools/sync_core.py` `EXCLUDE`): core holds the vanilla copy, each mod keeps its own, and Rt56 doubles only the join-staircase thresholds. An edit to a scorer has to be applied to `_sandbox` and `_sandbox-r56` separately.
- `common/opinion_modifiers/99_sandbox_opinion_modifiers.hsl` (per mod, also on the sync exclude list): the modifier **values** are doubled in Rt56; `core/` holds the vanilla-magnitude copy.
- `core/common/scripted_localisation/99_sandbox_scripted_localisation.hsl`, `localisation/english/99_sandbox_l_english.yml`.

Defects of the pre-2026-09 implementation that this design removed: rivals were selected once and never changed; rivalry did not reach opinion; `var:rival_ideology` was never set; the single AI plan used `antagonize value(-200)` (vanilla uses positive values for hostility); cooperation focuses blocked by a rival could never unblock.

## Model

Three slots, as today, with different natures:
- `rivals[0]` - the **ruler's rival**. Always a major. Bound to the person: re-rolled on every ruler change. Tooltip "Dislikes X".
- `rivals[1]`, `rivals[2]` - **national rivals**. Neighbours and regional powers, bound to the nation, outlive rulers.

New parallel array `rivalry[]` - the **intensity** of each slot, an integer in `[0, 100]` (`$add_rivalry` clamps), initialised to 50 when a slot is filled, or to 75 by the event-driven rule.

Bands (shipped boundaries: the Rival tier tests `>= 25` and `< 75`, so it is 25-74, not 25-75):
- `< 25` **Cold** - residual dislike.
- `25-74` **Rival** - the working state.
- `>= 75` **Feud** - the AI prepares for war; focuses against the rival get a large weight bonus.

The same tag may occupy slot 0 and a national slot at once (Soviet Union for Finland); effects stack.

An empty slot holds `0` in both arrays.

## Design goals

1. Rivalries have a beginning, a middle, and an end. Every rival can be lost (detente, annexation, alliance) and every loss opens a slot for someone else after a pause.
2. Rivalry has teeth outside the AI: opinion, war support, focus weights and gates.
3. The world is two-sided: rivals tend to pick each other back, victory cools the winner and heats the loser.
4. Honor stays pure: rivalry never touches `honor` and never lowers the cost of betrayal.

## Selecting a rival (scorer body)

Both scorers (`FROM` is the selecting country, `THIS` the candidate), `base(40)`, with `targets_dynamic(no)` and `target_non_existing(no)`:
- `factor(0)`: `FROM == THIS`; `is_in_faction_with(FROM)`; `is_subject_of(FROM)`; `FROM->is_subject_of(THIS)`; `THIS in FROM.former_rivals[]` (cooldown, see "Losing a rival").
- `x0.25`: `is_friend_of_FROM()` (ally, guarantee or pact). A rival under a pact is possible but rare.
- `x2`: `THIS` owns a core of `FROM`, or `FROM` owns a core of `THIS` (`any_owned_state->is_core_of(...)`). The main "historical" driver.
- `x2`: `FROM in rivals[]` - i.e. `THIS` already lists `FROM`. Reciprocity turns one-sided dislikes into two-sided conflicts.
- `x1000`: at war with `FROM` (existing).

The dead `rival_ideology` branch is gone from `$ideology_factor`, so the scorers read ideology through `has_enemy_ideology_with_FROM()` from `99_sandbox_scripted_triggers.hsl` instead of `has_government(var:FROM.rival_ideology)`.

`major_rivals_scorer` keeps its ideology logic: `add(40)` and `has_enemy_ideology_with_FROM()` with `has_war_with_major(no)`, then `factor(0.5)` for `has_government(FROM)` with `has_war_with_major(no)`. It draws from `global.majors`.

`minor_rivals_scorer` keeps its geography logic: `add(40)` for `is_neighbor_of(FROM)` and `add(40)` for `is_on_same_continent_as(FROM)`, `factor(1.25)` for enemy ideology, and a `factor(0)` block that drops a candidate on a different continent region unless the two are at war (`has_defensive_war_with(FROM)` scores `x1000`). It draws from `global.countries`.

## Lifecycle

### Initialisation

`initialize_country_for_sandbox_mode()` resizes `rivals[]` and `rivalry[]` to 3, then calls `initialize_new_country_leader()`, which calls `select_major_rival()` for slot 0, and then loops `for i in range(2)` over `select_minor_rival()` for the two national slots. Every filled slot gets `rivalry = 50` (`set_rival()` also resets `rival_intensity` to 50, so the event-driven 75 is the only other value). The weekly `sandbox_initialized` guard covers late-created countries (rebels, released nations).

### Ruler change

On `on_ruling_party_change` and for the winner of `on_civil_war_end`: `reroll_leader_rival()` runs - it sets `sandbox_clear_rival_no_cooldown`, calls `clear_rival()` on slot 0, clears the flag, then `select_major_rival()` immediately. National slots are untouched. A new ruler therefore always has a fresh personal enemy, matching the tooltip.

### Losing a rival

Immediate clear, checked monthly by `review_rivals()` and on the hooks `on_annex`, `on_join_faction` / `on_join_allies`, `on_puppet`:
- the rival no longer exists;
- the rival is in our faction;
- the rival is our overlord or our subject.

Known latency: vanilla `on_join_faction` does not fire for the `add_to_faction` effect, and `on_puppet` fires only from peace conferences. Focus-driven faction joins and puppeting - the usual sandbox path - are therefore caught by the monthly review, so a rival may sit in our faction with the -20 opinion modifier (-40 in Rt56) for up to a month.

Detente: `rivalry` reaching 0 clears the slot.

On any clear (`clear_rival(slot)`): remove our opinion modifiers toward it, zero both arrays at that index, and append the tag with the current `months_elapsed` to `former_rivals[]` / `former_rivals_month[]`. The cooldown is **24 months**: during it the country scores 0 in both scorers. Entries older than 24 months are purged monthly, same mechanism as `dropped_pacts[]` in Honor.

### Filling a vacancy

Monthly, `fill_rival_vacancies()`:
- an empty national slot is filled with probability 1/6 (`randi(1, 6) == 1`), so a vacancy lasts six months on average - the world does not instantly find a replacement enemy;
- an empty slot 0 is filled immediately after a ruler change (above) and otherwise with the same 1/6 chance.

### Event-driven rivals

A country that declares war on us and is not in `rivals[]` becomes a national rival at once (`on_declare_war` -> `apply_rivalry_on_declare_war()` -> `become_event_rival()`, run in `FROM`'s scope): it takes an empty national slot with `rivalry = 75`; if there is none, it replaces the national slot with the lowest `rivalry`, provided that value is `< 25` (`sandbox_clear_kind = 7`, so the displaced tag gets the usual 24-month cooldown). Otherwise nothing happens (the war still counts through `$is_rival_of()`). Note that `become_event_rival()` only ever touches slots 1-2: a war declaration never displaces the ruler's personal rival.

## Rivalry changes

### Monthly (per slot, summed, then clamped to `[0, 100]`)

- `+2` we are at war with the rival (`has_war_with(var:rival_tag)`).
- `+2` the rival owns a core of ours or we own a core of theirs (`any_owned_state->is_core_of(...)` in both directions).
- `+1` enemy ideology (`has_enemy_ideology_with_PREV`); `-1` same government (`has_government(PREV)`).
- `+1` the rival is at war with at least one friend of ours; once, not per friend. Implemented from the rival's scope as `any_enemy_country->is_friend_of_ROOT()`, so `update_rivalry_monthly()` must only be called with ROOT = the country (as `on_monthly` does).
- Slot 0 only: `+1` if our ruler is Authoritarian or Despotic (a regime needs an external enemy); `-1` if Libertarian or Liberal (`is_authoritarian_leader` / `is_liberal_leader`). This is the only Tyranny interaction.
- `-1` we have a non-aggression pact with the rival.
- `-1` baseline drift, applied only when none of the `+` conditions above fired (`has_plus == 0`). A slot that only accrued `-` terms does not get the extra `-1`.

Result: an unfuelled rivalry fades from 50 to 0 in about four years (the drift is `-1` per month); cores plus war push it to Feud within a year.

### Discrete events

- `+25` the rival declares war on us (`on_declare_war`: ROOT attacker, FROM target; applied in FROM's scope to the slot holding ROOT).
- `+15` the rival declares war on a friend of ours (applied in every other country's scope that is `is_friend_of_FROM()` and lists ROOT as a rival).
- `-50` the rival capitulates to us (`on_capitulation`: ROOT capitulating country, FROM winner; applied in FROM's scope). Victory satisfies.
- `+25` we capitulate to the rival (applied in ROOT's scope). Revanchism. If the winner is not in our `rivals[]`, it enters by the event-driven rule above.

The pair is asymmetric on purpose: after a war the winner cools down and the loser keeps the grudge.

All changes go through `$add_rivalry(slot, value)`, which clamps and triggers the detente clear at 0. There is no slot-lookup helper: each call site writes the three slot comparisons itself, and `rival_slot` is a temp the caller sets (`add_rivalry_vs()` loops over the three slots; `clear_rival()` reads `rival_slot`).

## Effects

### Opinion

Two opinion modifiers, added with `add_opinion_modifier` (target = rival) by `set_rival()` and removed by `clear_rival()`:
- `national_rival` -20 in vanilla / -40 in Rt56 (slots 1-2),
- `leaders_rival` -10 in vanilla / -20 in Rt56 (slot 0).

The values live in each mod's `common/opinion_modifiers/99_sandbox_opinion_modifiers.hsl`; `core/` holds the vanilla-magnitude copy, which is never copied out (the sync treats that file as per-mod).

They stack to -30 (-60 in Rt56) when the same tag is in both. Through opinion, rivalry flows into every existing `$ai_antagonism_modifier` / `$ai_cooperation_modifier` without touching the focus files.

### AI strategies

`common/ai_strategy/99_sandbox_rivals_system.hsl` (per mod, generated from the tag list) holds three plans per tag, enabled by the `rivalry` of the slot that holds the tag:
- `$rival_base($TAG)` - any slot: `antagonize 200` (sign fixed), `alliance -200`, `befriend -200`;
- `$rival_contain($TAG)` - Rival band (`rivalry >= 25` and `< 75`): `contain 100`, plus the economic-posture entries `equipment_market_trade_desire -50` and `equipment_market_buy seller=<tag> -200`;
- `$rival_feud($TAG)` - Feud (`rivalry >= 75`): `conquer 100`, `prepare_for_war 100`, `equipment_market_trade_desire -200`, `equipment_market_buy -200`, and `diplo_action_desire target=market_access_rights -200`.

The Rival tier stops at 75 so the three plans are mutually exclusive on the band: at Feud, `conquer` / `prepare_for_war` replace `contain`, which they superseded there anyway. The exclusivity is also what keeps the economic-posture entries of the tiers from stacking (a -50 trade desire at Rival and a -200 at Feud would sum to -250 otherwise); see `docs/gdd/Economic Posture.md` and ADR-0007, which fold those addressed entries into the same three macros. In the shipped macro bodies the market-access denial (`diplo_action_desire target=market_access_rights -200`) sits only in `$rival_feud`, so a Rival-band target gets the buy exclusion and the -50 trade desire but keeps its market access.

The old per-tag plan macro is gone; the three `rival_*` macros above replaced it, and the generator that produced the tag list stays.

### National focuses

Patterns are in `docs/gdd/National Focuses.md`, "Diplomacy modifiers":
- cooperation focuses with **one or two** named partners are gated: `available: $not_rival_of_PREV($TAG)` (alias-safe form of `$TAG->is_rival_of_PREV(no)`) and `factor(0)` on `$TAG in rivals[]`;
- cooperation focuses that invite **three or more** countries (faction-building focuses such as `USA_hemisphere_defense`, `ITA_south_american_alliances`, the Baltic and Balkan invitations) are **not** gated and get no `factor(0)`. National rivals are drawn from neighbours and the same continent, so one of many invitees is almost always a rival and a gate would block the focus permanently; the rival opinion modifiers already lower the averaged cooperation factor, and the rival's own AI refuses the alliance (`alliance -200`);
- antagonism focuses add `$ai_rivalry_modifier($TAG)` next to `$ai_antagonism_modifier($TAG)`: `factor(1 + rivalry_vs / 50)` where `rivalry_vs` is the highest `rivalry` among slots holding `TAG` (x1 for a non-rival, x2 at 50, x3 at Feud); two targets use `$ai_rivalry_modifier_max($TAG1, $TAG2)`; three or more targets spell the same modifier out with one `$rivalry_vs_into($TAG)` line per target (pattern in `docs/gdd/National Focuses.md`);
- the macros compute `rivalry_vs` inside the modifier with temp variables and `if` triggers over the three slots (`ai_will_do` is a trigger context, so no scripted effect can be called); the focus files never index `rivalry[]` directly;
- coverage is complete: every `$ai_antagonism_modifier` and every multi-target `antagonism = ...` block, including the shared trees (`baltic_shared`, `china_shared*`, `indonesia_joint`, `TSR_*`), has a rivalry modifier;
- tag aliases follow the `country_exists` guard rule from the same document.

### War support

- Declaring war on a rival with `rivalry >= 50`: `add_war_support(0.05)` once (a popular war).
- A rival declaring war on us: `add_war_support(0.10)` once.

### Honor and Tyranny

Honor: no changes. `can_PREV_get_wargoal_on_THIS` and the betrayal penalties ignore rivalry. Rivalry touches Honor only indirectly: friends are unlikely rivals (x0.25) and a pact cools an existing rivalry (-1 per month).

Tyranny: only the slot-0 monthly term above.

## Tooltips and localisation

- `LocKey_personality_tt` is `"[GetSandboxLeaderRivalText][GetSandboxNationalRivalsText]"`, so the shape is fixed by two `defined_text` blocks in `core/common/scripted_localisation/99_sandbox_scripted_localisation.hsl`: `GetSandboxLeaderRivalText` (slot 0) and `GetSandboxNationalRivalsText` (three variants: both national slots, only slot 1, only slot 2). Each block ends in `localization_key(LocKey_empty)`, so an empty slot prints nothing rather than a raw key.
- The strings themselves: `LocKey_leader_rival_tt` -> "Dislikes [leader] ([flag] [name], [band])."; `LocKey_national_rivals_both_tt` -> "[Adjective] citizens dislike [flag][name] ([band]), [flag][name] ([band])."; `LocKey_national_rivals_1_tt` / `_2_tt` for the single-slot variants.
- The band keys come from `GetSandboxRivalBand0` / `1` / `2`: `LocKey_rivalry_band_cold` "Cold", `LocKey_rivalry_band_rival` "Rival", `LocKey_rivalry_band_feud` "Feud", with `LocKey_empty` as the fall-through.
- Opinion modifiers: `national_rival` "National rival", `leaders_rival` "Personal rival of the ruler", `cw_back_kin` / `cw_back_rival` for the civil-war backing (`docs/gdd/Civil Wars.md`).
- `LocKey_is_rival_of_PREV_tt` / `_NOT` and `LocKey_is_rival_of_ROOT_tt` / `_NOT` all exist, plus `LocKey_is_honored_leader_tt`, `LocKey_is_dishonorable_leader_tt`, `LocKey_is_treacherous_leader_tt`, `LocKey_is_authoritarian_leader_tt` and `LocKey_is_liberal_leader_tt`, each with a `_NOT` variant.
- `localisation/english/99_sandbox_l_english.yml` must stay UTF-8 **with BOM**: HOI4 silently drops a localisation file without it and every key falls back to its raw name.

## Implementation notes

Arrays and variables (country scope): `rivals[]` (3), `rivalry[]` (3), `former_rivals[]`, `former_rivals_month[]`; stamps use the existing `months_elapsed` counter.

Effects in `core/common/scripted_effects/99_sandbox_scripted_effects.hsl` (scripted effects take no parameters; arguments travel in temp variables `rival_slot`, `rival_tag`, `rival_intensity`, `rivalry_delta`, `lowest_slot` / `lowest_val`, `should_clear`, `sandbox_clear_kind`):
- `set_rival()`: writes both arrays, adds the opinion modifier for the slot type (`leaders_rival` for slot 0, `national_rival` for slots 1-2) only if the country exists, resets `rival_intensity` to 50.
- `clear_rival()`: removes the opinion modifier, zeroes both arrays, appends to `former_rivals[]` / `former_rivals_month[]` unless the one-shot flag `sandbox_clear_rival_no_cooldown` is set (ruler-change re-roll). `sandbox_clear_kind` selects the log event: `1` gone, `2` faction, `3` subject, `4` detente, `6` annex, `7` replace.
- `$add_rivalry(slot, value)` (macro in `common/macros.hml`): clamp, detente check, and the logging rules. Same discipline as `$add_honor()`: never write `&rivalry[i]` elsewhere. `add_rivalry_vs()` (effect) applies `rivalry_delta` to every slot holding `rival_tag`; `$sandbox_add_rivalry_vs(_tag_, _var_)` is the macro form the scenario events use.
- `review_rivals()`, `update_rivalry_monthly()`, `fill_rival_vacancies()`, `expire_former_rivals()`: monthly, from `on_monthly`.
- `select_major_rival()` / `select_minor_rival()`: weighted-random body; they call `set_rival()` instead of writing `&rivals[i]` so the opinion modifier is applied. `select_minor_rival()` adds one slot per call, so `initialize_country_for_sandbox_mode()` loops `for i in range(2)`.
- `reroll_leader_rival()`: slots-0 re-roll for a new ruler (clears without a cooldown entry, then `select_major_rival()`).
- `become_event_rival()`: the event-driven rule (free national slot, else the lowest slot if it is below 25).
- `$sandbox_seed_rival(_tag_, _intensity_)` (macro): the scenario director's seeding path, same slot discipline, raising an already-listed rival to `_intensity_` instead of duplicating it.
- `apply_rivalry_on_declare_war()`, `apply_rivalry_on_capitulation()`, `clear_annexed_from_rivals()`: the hook bodies.

There is no slot-lookup helper in the shipped code. Slot lookups are written out per site: `set_rival()` / `clear_rival()` take `rival_slot` as a temp, and `apply_rivalry_on_declare_war()` computes the highest `rivalry` over the three slots with an inline `if` chain. Code that needs "which slot holds this tag" writes the three comparisons; do not assume a helper exists.

Cross-scope reads of temp variables (`var:PREV.some_temp`) are not used anywhere in the system; where another country's state is needed the effect enters that scope and comes back through `PREV` or `ROOT`.

Hooks (`core/common/on_actions/99_sandbox_core_on_actions.hsl`, copied into each mod as the generated `99_sandbox_on_actions.hsl`):
- `on_monthly`: `expire_former_rivals()`, `review_rivals()`, `update_rivalry_monthly()`, `fill_rival_vacancies()` after `months_elapsed += 1`; `sandbox_economic_posture_monthly()` runs after them so the bands are settled.
- `on_ruling_party_change`: through `inherit_honor_on_ruling_party_change()` -> `reroll_leader_rival()`.
- `on_civil_war_end` (ROOT winner): through `reset_honor_for_new_ruler()` -> `reroll_leader_rival()`.
- `on_declare_war` (ROOT attacker, FROM target): `apply_rivalry_on_declare_war()` - attacker side war-support bonus at `rivalry >= 50`; target side `+25` plus `become_event_rival()` plus `+0.10` war support; every other country `+15` if it is a friend of FROM and ROOT is in its `rivals[]`.
- `on_capitulation` (ROOT capitulating, FROM winner): `apply_rivalry_on_capitulation()` - FROM `-50` toward ROOT; ROOT `+25` (or `become_event_rival()` if FROM was not already a rival).
- `on_annex` (ROOT annexer, FROM annexed): `clear_annexed_from_rivals()`.
- `on_join_allies`, `on_join_faction`, `on_puppet`: run `review_rivals()` for both parties.

Scorers cannot read the selector's temp variables; the cooldown test is `THIS in FROM.former_rivals[]`, written as a plain `modifier: factor(0)` block in both scorers.

Arithmetic passed to macros must be computed into a temp variable first. Two distinct engine limits sit behind this rule:

- A macro argument must be a plain value, not an expression - `$add_honor(guarantee_penalty)` works where `$add_honor(-5 * n_g)` does not.
- Array elements inside a math block are not trusted by the expression parser, so `clamp(rivalry[i] + d, 0, 100)` is written as `cur_rivalry = rivalry[i]` first (see the engine-limitations list below).

The same shape covers `set_variable = clamp(...)` inside `common/on_actions/`: it is rejected there (`script_math` "defaulting to 0"), which is why `$add_honor` / `$add_tyranny` use `&var += x` plus `$clamp_variable(...)`.

Engine limitations found at first launch (2026-09-06 `error.log`):
- `add_opinion_modifier` / `remove_opinion_modifier` reject `target = var:x` ("Malformed token"). `set_rival()` / `clear_rival()` enter the rival's scope (`var:rival_tag:`) and come back with `PREV:` so the target can be written as `PREV`.
- Array elements inside a math block (`clamp(rivalry[i] + d, ...)`) are read into a temp first (`cur_rivalry = rivalry[i]`); the malformed-token errors above were followed by "math expression" errors on every later expression in the file, so the two are kept apart to make the log attributable.

Verified in game since:
- Tags and scopes as variable values: `check_variable = { rivals^0 = GER }` in the generated AI plans and `set_temp_variable = { rival_tag = ROOT }` in the hooks. Same mechanism as the long-standing `is_in_array = { rivals = SOV }`.
- `has_government = <scope>` (used in `update_rivalry_monthly` and `major_rivals_scorer`) is valid: vanilla `USA_hemisphere_defense` uses `has_government = ROOT`.
- Nested scripted localisation: `LocKey_personality_tt` -> `[GetSandboxLeaderRivalText]` -> `LocKey_leader_rival_tt`, which contains `[?rivals^0.GetLeader]` and `[GetSandboxRivalBand0]`; the national half goes through `[GetSandboxNationalRivalsText]` -> `LocKey_national_rivals_{both,1,2}_tt`. All three band keys (`cold` / `rival` / `feud`) and `LocKey_empty` exist.

Still to verify (not yet settled by an acceptance run):
- Scopes of `on_capitulation` (FROM = winner) in faction wars.
- Cost of the AI plans: three per tag with variable checks in `enable`. If AI ticks slow down, merge the three tiers into one plan per tag with `contain`/`conquer` gated by `rivalry` inside the plan.

## Telemetry

The `#sandbox` gate is `sandbox_log_rivals`, off by default. `$add_rivalry` logs `rivals_intensity` for any discrete change of 10 or more, and for monthly moves it logs only band crossings: `rivals_feud` (crossing up to 75), `rivals_cold` (dropping below 25), `rivals_rival_band` (crossing up to 25). `set_rival()` logs `rivals_set`; `clear_rival()` logs one of `rivals_clear_reroll` / `rivals_clear_gone` / `rivals_clear_faction` / `rivals_clear_subject` / `rivals_clear_detente` / `rivals_clear_annex` / `rivals_clear_replace` / `rivals_clear`; `expire_former_rivals()` logs `rivals_cooldown_expire`; `apply_rivalry_on_declare_war()` logs `rivals_war_support_declare` / `rivals_war_support_attacked`. The monthly `sandbox_log_census()` line prints all three slots as `r0=<tag>:<intensity>` beside the Honor/Tyranny numbers.

## Acceptance checklist

Log-first: raise `sandbox_log_rivals` and read the `#sandbox rivals_*` lines plus the monthly census (`r0=<tag>:<intensity>`). An unticked box has its code shipped unless the item says otherwise; the tick waits for a session that shows it.

- [ ] A new Soviet ruler gets a new personal rival within the same day; the two national rivals are unchanged.
- [ ] Romania is Hungary's national rival at `rivalry` 50; Romania joins Hungary's faction: the slot is cleared, Hungary's -20 opinion modifier toward Romania disappears, and Romania cannot be selected again for 24 months.
- [ ] The Soviet Union owns Finnish cores: Finland's `rivalry` toward it rises by >=2 per month and reaches Feud within ~13 months; the Soviet AI (if it lists Finland) gets `conquer`.
- [ ] A country with a rival it shares no cores, wars, or ideology conflict with: `rivalry` falls from 50 to 0 in ~50 months, the slot empties, and is refilled after ~6 months on average.
- [x] Y declares war on Z without being Z's rival: Y occupies a free national slot of Z with `rivalry` 75 the same day, Z gains +10 war support.
- [x] Z capitulates to Y: Y's `rivalry` toward Z drops by 50; Z's toward Y rises by 25.
- [ ] A pact partner is also a rival at `rivalry` 40: declaring war costs the usual -50 Honor; monthly growth is reduced by 1.
- [ ] `USA_us_ussr_economic_cooperation` is unavailable while SOV is in USA's `rivals[]` or USA in SOV's, and its AI weight is 0.
- [ ] With a rival at Feud, the antagonism focus against it weighs three times its non-rival weight; a focus against several countries of which one is at Feud weighs the same.
- [ ] `USA_hemisphere_defense` stays available and keeps a non-zero AI weight while Mexico is a US national rival; `USA_liberty_for_the_philippines` is unavailable while the Philippines are.
- [ ] A rival at war with one, two, or five of our friends gains exactly +1 per month from that term.
- [x] No `Invalid Scope` lines in `error.log` from rival effects when a rival slot holds a country that has ceased to exist mid-month.

## Out of scope for this iteration

- Player decisions "declare rival" / "seek detente": no decision touches rivalry today. (`common/decisions/` is no longer empty - it holds the civil-war overlays - so the earlier reason wording is stale; the gap is the missing player-facing lever, not the directory.)
- Targeted ideas per rival (`targeted_modifier`: `attack_bonus_against`, `generate_wargoal_tension_against`); requires per-tag generation like the AI-strategy file.
- News events and notifications about rivalry changes.
- Opinion by Tyranny band distance (listed under "Second iteration" in `docs/gdd/Tyranny System.md`; independent of rivals).
- Historical-mode behaviour: everything here is sandbox-only.
