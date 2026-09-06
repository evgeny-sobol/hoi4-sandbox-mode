# Rivals

Rivals answer one question about a country: "**whom** does it want to fight?" Honor answers "how does it treat its promises" (`gdd/Honor System.md`), Tyranny "how does it rule at home" (`gdd/Tyranny System.md`), Opinion "how do others feel about it". In a randomised sandbox world rivalries are the source of long, readable conflicts: they steer AI aggression and tell the player why someone is sharpening a knife for them.

Rivalry is **not**:
- An excuse. Attacking a rival protected by a pact or guarantee costs the same Honor as attacking anyone else.
- Opinion. Rivalry *feeds* opinion through two opinion modifiers; opinion never creates or removes a rival.
- War. Being at war makes `$is_rival_of()` true for gating purposes, but war alone does not put a country into `rivals[]` (declaring war on us does, see "Event-driven rivals").

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`.

## Where it lives

- `common/scripted_effects/99_sandbox_scripted_effects.hsl`: selection (`select_major_rival`, `select_minor_rival`), slot discipline (`set_rival`, `clear_rival`, `reroll_leader_rival`, `add_rivalry_vs`, `become_event_rival`), monthly loop (`review_rivals`, `update_rivalry_monthly`, `fill_rival_vacancies`, `expire_former_rivals`), hooks (`apply_rivalry_on_declare_war`, `apply_rivalry_on_capitulation`, `clear_annexed_from_rivals`).
- `common/macros.hml`: `$add_rivalry`, `$rivalry_vs_into`, `$ai_rivalry_modifier`, `$ai_rivalry_modifier_max`, `$not_rival_of_PREV`, `$is_rival_of`, AI-plan macros `rival_base` / `rival_contain` / `rival_feud`.
- `common/scorers/country/99_sandbox_scorer.hsl`: `major_rivals_scorer` (from `global.majors`, ideology-driven), `minor_rivals_scorer` (from `global.countries`, geography-driven).
- `common/ai_strategy/99_sandbox_rivals_system.hsl`: three plans per tag (generated list).
- `common/opinion_modifiers/99_sandbox_opinion_modifiers.hsl`, `common/scripted_localisation/99_sandbox_scripted_localisation.hsl`, `localisation/english/99_sandbox_l_english.yml`.

Defects of the pre-2026-09 implementation that this design removed: rivals were selected once and never changed; rivalry did not reach opinion; `var:rival_ideology` was never set; the single AI plan used `antagonize value(-200)` (vanilla uses positive values for hostility); cooperation focuses blocked by a rival could never unblock.

## Model

Three slots, as today, with different natures:
- `rivals[0]` — the **ruler's rival**. Always a major. Bound to the person: re-rolled on every ruler change. Tooltip "Dislikes X".
- `rivals[1]`, `rivals[2]` — **national rivals**. Neighbours and regional powers, bound to the nation, outlive rulers.

New parallel array `rivalry[]` — the **intensity** of each slot, an integer in `[0, 100]`, initialised to 50 when a slot is filled.

Bands:
- `< 25` **Cold** — residual dislike.
- `25–75` **Rival** — the working state.
- `≥ 75` **Feud** — the AI prepares for war; focuses against the rival get a large weight bonus.

The same tag may occupy slot 0 and a national slot at once (Soviet Union for Finland); effects stack.

An empty slot holds `0` in both arrays.

## Design goals

1. Rivalries have a beginning, a middle, and an end. Every rival can be lost (détente, annexation, alliance) and every loss opens a slot for someone else after a pause.
2. Rivalry has teeth outside the AI: opinion, war support, focus weights and gates.
3. The world is two-sided: rivals tend to pick each other back, victory cools the winner and heats the loser.
4. Honor stays pure: rivalry never touches `honor` and never lowers the cost of betrayal.

## Selecting a rival (scorer changes)

Both scorers (`FROM` is the selecting country, `THIS` the candidate):
- `factor(0)`: `FROM == THIS`; same faction as `FROM`; `FROM`'s overlord or subject; listed in `FROM.former_rivals[]` (cooldown, see "Losing a rival").
- `×0.25`: friends by `$is_friend_of()` (pact or guarantee). A rival under a pact is possible but rare.
- `×2`: `THIS` owns a core of `FROM`, or `FROM` owns a core of `THIS` (`any_owned_state: is_core_of(...)`). The main "historical" driver.
- `×2`: `THIS` already lists `FROM` in its `rivals[]`. Reciprocity turns one-sided dislikes into two-sided conflicts.
- `×1000`: at war with `FROM` (existing).
- Replace `has_government(var:FROM.rival_ideology)` with `has_enemy_ideology_with_FROM()` (already in `99_sandbox_scripted_triggers.hsl`) and delete the dead `rival_ideology` branch from `$ideology_factor`.

`major_rivals_scorer` keeps its ideology logic (enemy ideology +40, same government ×0.5); `minor_rivals_scorer` keeps its geography logic (subject/neighbour/continent +40, off-continent ×0 unless at war).

## Lifecycle

### Initialisation

Unchanged: `initialize_country_for_sandbox_mode()` fills all three slots at startup, and the weekly `sandbox_initialized` guard covers late-created countries (rebels, released nations). Every filled slot gets `rivalry = 50`.

### Ruler change

On `on_ruling_party_change` and for the winner of `on_civil_war_end`: `clear_rival(0)` without the cooldown entry, then `select_major_rival()` immediately. National slots are untouched. A new ruler therefore always has a fresh personal enemy, matching the tooltip.

### Losing a rival

Immediate clear, checked monthly by `review_rivals()` and on the hooks `on_annex`, `on_join_faction` / `on_join_allies`, `on_puppet`:
- the rival no longer exists;
- the rival is in our faction;
- the rival is our overlord or our subject.

Known latency: vanilla `on_join_faction` does not fire for the `add_to_faction` effect, and `on_puppet` fires only from peace conferences. Focus-driven faction joins and puppeting — the usual sandbox path — are therefore caught by the monthly review, so a rival may sit in our faction with the −20 opinion modifier for up to a month.

Détente: `rivalry` reaching 0 clears the slot.

On any clear (`clear_rival(slot)`): remove our opinion modifiers toward it, zero both arrays at that index, and append the tag with the current `months_elapsed` to `former_rivals[]` / `former_rivals_month[]`. The cooldown is **24 months**: during it the country scores 0 in both scorers. Entries older than 24 months are purged monthly, same mechanism as `dropped_pacts[]` in Honor.

### Filling a vacancy

Monthly, `fill_rival_vacancies()`:
- an empty national slot is filled with probability 1/6 (`randi(1, 6) == 1`), so a vacancy lasts six months on average — the world does not instantly find a replacement enemy;
- an empty slot 0 is filled immediately after a ruler change (above) and otherwise with the same 1/6 chance.

### Event-driven rivals

A country that declares war on us and is not in `rivals[]` becomes a national rival at once (`on_declare_war`, handled in `FROM`'s scope): it takes an empty national slot with `rivalry = 75`; if there is none, it replaces the national slot with the lowest `rivalry`, provided that value is `< 25`. Otherwise nothing happens (the war still counts through `$is_rival_of()`).

## Rivalry changes

### Monthly (per slot, summed, then clamped to `[0, 100]`)

- `+2` we are at war with the rival.
- `+2` the rival owns a core of ours or we own a core of theirs.
- `+1` enemy ideology (`has_enemy_ideology_with`); `−1` same government.
- `+1` the rival is at war with at least one friend of ours (`$is_friend_of()`); once, not per friend. Implemented from the rival's scope as `any_enemy_country->is_friend_of_ROOT()`, so `update_rivalry_monthly()` must only be called with ROOT = the country (as `on_monthly` does).
- Slot 0 only: `+1` if our ruler is Authoritarian or Despotic (a regime needs an external enemy); `−1` if Libertarian or Liberal. This is the only Tyranny interaction.
- `−1` we have a non-aggression pact with the rival.
- `−1` baseline drift, applied only when none of the `+` conditions above holds.

Result: an unfuelled rivalry fades from 50 to 0 in about four years; cores plus war push it to Feud within a year.

### Discrete events

- `+25` the rival declares war on us (`on_declare_war`: ROOT attacker, FROM target; applied in FROM's scope to the slot holding ROOT).
- `+15` the rival declares war on a friend of ours.
- `−50` the rival capitulates to us (`on_capitulation`: ROOT capitulating country, FROM winner; applied in FROM's scope). Victory satisfies.
- `+25` we capitulate to the rival (applied in ROOT's scope). Revanchism. If the winner is not in our `rivals[]`, it enters by the event-driven rule above.

The pair is asymmetric on purpose: after a war the winner cools down and the loser keeps the grudge.

All changes go through `$add_rivalry(slot, value)`, which clamps and triggers the détente clear at 0. Slot lookups by tag use `rival_slot_of(tag)` (temp variable `rival_slot`, `-1` when absent).

## Effects

### Opinion

Two opinion modifiers in `common/opinion_modifiers/99_sandbox_opinion_modifiers.hsl`, added with `add_opinion_modifier` (target = rival) by `set_rival(slot, tag)` and removed by `clear_rival(slot)`:
- `national_rival` −20 (slots 1–2),
- `leaders_rival` −10 (slot 0).

They stack to −30 when the same tag is in both. Through opinion, rivalry flows into every existing `$ai_antagonism_modifier` / `$ai_cooperation_modifier` without touching the focus files.

### AI strategies

`99_sandbox_rivals_system.hsl` grows from one to three plans per tag, enabled by the `rivalry` of the slot that holds the tag:
- any rival: `antagonize 200` (sign fixed), `alliance −200`, `befriend −200`;
- Rival band or higher (`rivalry >= 25`): `contain 100`;
- Feud (`rivalry >= 75`): `conquer 100`, `prepare_for_war 100`.

The per-tag macro `country_is_rival(_country_)` becomes three macros (`rival_base`, `rival_contain`, `rival_feud`) or one macro emitting three plans; the generator that produced the tag list stays.

### National focuses

Patterns are in `gdd/National Focuses.md`, "Diplomacy modifiers":
- cooperation focuses with **one or two** named partners are gated: `available: $not_rival_of_PREV($TAG)` (alias-safe form of `$TAG->is_rival_of_PREV(no)`) and `factor(0)` on `$TAG in rivals[]`;
- cooperation focuses that invite **three or more** countries (faction-building focuses such as `USA_hemisphere_defense`, `ITA_south_american_alliances`, the Baltic and Balkan invitations) are **not** gated and get no `factor(0)`. National rivals are drawn from neighbours and the same continent, so one of many invitees is almost always a rival and a gate would block the focus permanently; the rival opinion modifiers already lower the averaged cooperation factor, and the rival's own AI refuses the alliance (`alliance −200`);
- antagonism focuses add `$ai_rivalry_modifier($TAG)` next to `$ai_antagonism_modifier($TAG)`: `factor(1 + rivalry_vs / 50)` where `rivalry_vs` is the highest `rivalry` among slots holding `TAG` (×1 for a non-rival, ×2 at 50, ×3 at Feud); two targets use `$ai_rivalry_modifier_max($TAG1, $TAG2)`; three or more targets spell the same modifier out with one `$rivalry_vs_into($TAG)` line per target (pattern in `gdd/National Focuses.md`);
- the macros compute `rivalry_vs` inside the modifier with temp variables and `if` triggers over the three slots (`ai_will_do` is a trigger context, so no scripted effect can be called); the focus files never index `rivalry[]` directly;
- coverage is complete: every `$ai_antagonism_modifier` and every multi-target `antagonism = …` block, including the shared trees (`baltic_shared`, `china_shared*`, `indonesia_joint`, `TSR_*`), has a rivalry modifier;
- tag aliases follow the `country_exists` guard rule from the same document.

### War support

- Declaring war on a rival with `rivalry >= 50`: `add_war_support(0.05)` once (a popular war).
- A rival declaring war on us: `add_war_support(0.10)` once.

### Honor and Tyranny

Honor: no changes. `can_PREV_get_wargoal_on_THIS` and the betrayal penalties ignore rivalry. Rivalry touches Honor only indirectly: friends are unlikely rivals (×0.25) and a pact cools an existing rivalry (−1 per month).

Tyranny: only the slot-0 monthly term above.

## Tooltips and localisation

- `LocKey_personality_tt` shows the band per slot: "Dislikes [leader] ([flag] [name], Feud). [Adjective] citizens dislike [flag] [name] (Rival), [flag] [name] (Cold)." Empty slots are omitted (needs three variants or a scripted-loc helper; the middle designer picks).
- Opinion modifiers: `national_rival` "National rival", `leaders_rival` "Personal rival of the ruler".
- `LocKey_is_rival_of_PREV_tt` / `_NOT` exist; add `LocKey_is_rival_of_ROOT_tt` / `_NOT` if `is_rival_of_ROOT` is used in a tooltip context.

## Implementation notes

Arrays and variables (country scope): `rivals[]` (3), `rivalry[]` (3), `former_rivals[]`, `former_rivals_month[]`; stamps use the existing `months_elapsed` counter.

Effects in `99_sandbox_scripted_effects.hsl` (scripted effects take no parameters; arguments travel in temp variables `rival_slot`, `rival_tag`, `rival_intensity`, `rivalry_delta`):
- `set_rival()`: writes both arrays, adds the opinion modifier for the slot type (only if the country exists), resets `rival_intensity` to 50.
- `clear_rival()`: removes the opinion modifier, zeroes both arrays, appends to `former_rivals[]` unless the one-shot flag `sandbox_clear_rival_no_cooldown` is set (ruler-change re-roll).
- `$add_rivalry(slot, value)` (macro): clamp, détente check. Same discipline as `$add_honor()`: never write `&rivalry[i]` elsewhere. `add_rivalry_vs()` applies `rivalry_delta` to every slot holding `rival_tag`.
- `review_rivals()`, `update_rivalry_monthly()`, `fill_rival_vacancies()`, `expire_former_rivals()`: monthly.
- `select_major_rival()` / `select_minor_rival()`: unchanged weighted-random body; they call `set_rival()` instead of writing `&rivals[i]` so the opinion modifier is applied.

Cross-scope reads of temp variables (`var:PREV.some_temp`) are not used anywhere in the system; where another country's state is needed the effect enters that scope and comes back through `PREV` or `ROOT`.

Hooks (`common/on_actions/99_sandbox_on_actions.hsl`):
- `on_monthly`: the four monthly effects above, after `months_elapsed += 1`.
- `on_ruling_party_change`, `on_civil_war_end` (ROOT winner): slot-0 re-roll.
- `on_declare_war` (ROOT attacker, FROM target): attacker side — war-support bonus vs a rival; target side — `+25`, event-driven rival, war-support bonus; every other country — `+15` if the target is its friend and the attacker is in its `rivals[]`.
- `on_capitulation` (ROOT capitulating, FROM winner; verify scopes in game): `−50` for FROM, `+25` / event-driven rival for ROOT.
- `on_annex` (ROOT annexer, FROM annexed): `every_country: if FROM in rivals[]: clear_rival(...)`.
- `on_join_faction` / `on_join_allies`, `on_puppet`: run `review_rivals()` for both parties.

Scorers cannot read the selector's temp variables; the cooldown test is `THIS in FROM.former_rivals[]`.

Arithmetic passed to macros must be computed into a temp variable first (compiler `MATH` token limitation, see Honor implementation notes).

Engine limitations found at first launch (2026-09-06 `error.log`):
- `add_opinion_modifier` / `remove_opinion_modifier` reject `target = var:x` ("Malformed token"). `set_rival()` / `clear_rival()` enter the rival's scope (`var:rival_tag:`) and come back with `PREV:` so the target can be written as `PREV`.
- Array elements inside a math block (`clamp(rivalry[i] + d, …)`) are read into a temp first (`cur_rivalry = rivalry[i]`); the malformed-token errors above were followed by "math expression" errors on every later expression in the file, so the two are kept apart to make the log attributable.

Verify in game (not yet run after the implementation; `error.log` and the tooltips are the evidence):
- Tags and scopes as variable values: `check_variable = { rivals^0 = GER }` in the 2 475 AI plans and `set_temp_variable = { rival_tag = ROOT }` in the hooks. Same mechanism as the long-standing `is_in_array = { rivals = SOV }`, but the plan `enable` blocks depend on it entirely.
- Nested scripted localisation: `LocKey_personality_tt` → `[GetSandboxLeaderRivalText]` → a key that itself contains `[?rivals^0.GetLeader]` and `[GetSandboxRivalBand0]`. The trait tooltip must not show raw brackets, and `LocKey_empty` (an empty string) must not leak its key name.
- Scopes of `on_capitulation` (FROM = winner) in faction wars.
- Cost of the AI plans: three per tag with variable checks in `enable`. If AI ticks slow down, merge the three tiers into one plan per tag with `contain`/`conquer` gated by `rivalry` inside the plan.
- `has_government = <scope>` (used in `update_rivalry_monthly` and `major_rivals_scorer`) is valid: vanilla `USA_hemisphere_defense` uses `has_government = ROOT`.

## Acceptance checklist

- A new Soviet ruler gets a new personal rival within the same day; the two national rivals are unchanged.
- Romania is Hungary's national rival at `rivalry` 50; Romania joins Hungary's faction: the slot is cleared, Hungary's −20 opinion modifier toward Romania disappears, and Romania cannot be selected again for 24 months.
- The Soviet Union owns Finnish cores: Finland's `rivalry` toward it rises by ≥2 per month and reaches Feud within ~13 months; the Soviet AI (if it lists Finland) gets `conquer`.
- A country with a rival it shares no cores, wars, or ideology conflict with: `rivalry` falls from 50 to 0 in ~50 months, the slot empties, and is refilled after ~6 months on average.
- Y declares war on Z without being Z's rival: Y occupies a free national slot of Z with `rivalry` 75 the same day, Z gains +10 war support.
- Z capitulates to Y: Y's `rivalry` toward Z drops by 50; Z's toward Y rises by 25.
- A pact partner is also a rival at `rivalry` 40: declaring war costs the usual −50 Honor; monthly growth is reduced by 1.
- `USA_us_ussr_economic_cooperation` is unavailable while SOV is in USA's `rivals[]` or USA in SOV's, and its AI weight is 0.
- With a rival at Feud, the antagonism focus against it weighs three times its non-rival weight; a focus against several countries of which one is at Feud weighs the same.
- `USA_hemisphere_defense` stays available and keeps a non-zero AI weight while Mexico is a US national rival; `USA_liberty_for_the_philippines` is unavailable while the Philippines are.
- A rival at war with one, two, or five of our friends gains exactly +1 per month from that term.
- No `Invalid Scope` lines in `error.log` from rival effects when a rival slot holds a country that has ceased to exist mid-month.

## Out of scope for this iteration

- Player decisions "declare rival" / "seek détente" (`common/decisions` is empty; add once the AI loop is tuned).
- Targeted ideas per rival (`targeted_modifier`: `attack_bonus_against`, `generate_wargoal_tension_against`); requires per-tag generation like the AI-strategy file.
- News events and notifications about rivalry changes.
- Opinion by Tyranny band distance (listed under "Second iteration" in `gdd/Tyranny System.md`; independent of rivals).
- Historical-mode behaviour: everything here is sandbox-only.
