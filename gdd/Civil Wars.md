# Civil wars

A civil war is the most expensive way a country can change its politics: it splits the tag, burns divisions, and pulls neighbours in. In a randomised sandbox world a few of these are flavour. A dozen at once is noise — the player cannot tell a story in a map that is already on fire.

This document is about **how often** the AI starts one. It does not redesign vanilla civil-war content (Spanish Civil War, Cedillo, Vaps, second Finnish war). Those scripts stay. Sandbox only changes whether the AI walks into them, and whether a fourth country is allowed to explode while three are already burning.

Civil wars are **not**:
- Honor. Starting a civil war does not cost Honor; Honor is about promises to *other* countries (`gdd/Honor System.md`).
- Tyranny as a value. A purge or a coup may raise Tyranny; the civil war itself is a method, not a Tyranny source (`gdd/Tyranny System.md`). Unconstitutional focuses that happen to start a war still use the existing tyranny tilt.
- A substitute for the revolution events `political.21/22/23`. Those already have an AI-only peaceful referendum; do not touch them here.

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`. Historical mode is unchanged.

## Why this is needed

`$ai_sandbox_modifier()` (`gdd/National Focuses.md`) sets every focus to weight 40 and historical AI plans are aborted. Political roots that vanilla AI almost never takes — `USA_america_first`, Baltic "break the silence" / Vaps, Norwegian fascist and communist openers — now compete with industry. Party-popularity factors then pull those roots. By 1936–37 several AIs complete the focus that actually fires `start_civil_war` in the same window.

The first pass zeroed `ai_will_do` on ignition **focuses** once three distinct `original_tag`s were at war. That did not stop the pile-up. Observed sandbox observer game (v0.1.1, `historical=0`, through Feb 1938): `cw` reached **8**. After `cap=1` / `ignition_base=0` the extra wars were still `cw_declare` from rebels (AST, GRE, then MEX, LIT, PER, POL, ITA) — missions, MTTH/plot events, BoP, `on_daily` — not tagged focuses (`cw_ignition` never fired). The counter was honest; the fuse was not on a focus.

Spain is the scripted 1936 war and is expected when a slot is free. The others are alt-history fuses that vanilla fires without asking the focus AI.

What does **not** cause this pile-up (leave it alone in this iteration):
- Generic `prepare_for_*_civil_war` decisions: `ai_will_do = 0`.
- Revolution events `political.21/22/23`: AI picks the hidden referendum.
- Spy coup operations (`00_operations.txt`).

## Design goals

1. At most a handful of civil wars run at the same time. Spain plus two others is the default picture; a fourth waits until one of them ends.
2. A civil-war focus is a rare political beat, not a peer of "build civilian factories". The AI may still take it, especially a high-Tyranny ruler on an ideological branch.
3. Weight the **root** of a civil-war branch, not only the last focus. Otherwise the AI spends a year on the branch and detonates the moment a slot frees.
4. Do not cancel or rewrite vanilla `start_civil_war` payloads (states, ideology, OOBs, character splits). The cap applies to *new* AI-started wars from **any** script that lights the fuse — focus, event, mission, decision, BoP range, `on_action`. Wars already running continue.
5. Player-started wars are unrestricted. Cap and the 0.25 factor are AI-only (`ai_will_do` / `ai_chance` / `is_ai = yes` on the overlay). A human Spain still gets 1936; a human Mexico still gets Cedillo if they let the mission expire.

## Model

### Active-war counter

Country-agnostic global `sandbox_civil_war_count`: number of **distinct `original_tag`** that currently have `has_civil_war = yes`.

Both sides of one war share an `original_tag` (SPR and SPA, USA and CSA, a Baltic government and its rebel). Counting tags, not countries, means Spain is 1, not 2–4.

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

**Cap: 3.** Scripted trigger `sandbox_civil_war_cap_reached`: `is_sandbox_mode_on()` and `sandbox_civil_war_count >= 3`.

While the cap is reached, the AI must not start another civil war. Wars already running continue. The player may still ignite another.

AI-blocked helper (events, missions, on_actions, BoP — anything that is not `ai_will_do`):

```
sandbox_civil_war_ai_blocked:
  is_ai = yes
  sandbox_civil_war_cap_reached()
```

`sandbox_civil_war_cap_reached` already requires sandbox mode. Do not fold `is_ai` into the cap trigger: focus `ai_will_do` is already AI-only, and aiview should still show the cap as a country-level fact.

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
- BoP `on_activate` that fires a civil-war event (ITA grand council total-control range → `BBA_italy_civil_war.1`).

Not ignition (do not overlay):
- Intervention, volunteers, "lessons from the Spanish Civil War".
- Character/OOB follow-ups that run **after** `has_civil_war` is already true.
- `political.21/22/23` (AI civil-war options already have `ai_chance = 0`).

Spain's 1936 war is an event/mission ignition (no-LaR: `spain.1`; LaR: election `lar_spain.1` then military-plot **missions**). It is **not** exempt from the cap. When a slot is free it fires as vanilla. When the cap is reached, AI Spain waits; it still occupies a slot once the war starts. A human SPR is never delayed.

A war started **by another tag** (ENG decision lighting AST, LIT event lighting POL) is still an ignition for the **target**'s `original_tag`. Gate the AI actor. The player taking that decision is unrestricted.

## AI weighting (focuses)

Macros in `common/macros.hml`, patterns in `gdd/National Focuses.md`. Unchanged from the first pass.

**Ignition** (`$ai_civil_war_ignition_modifier()`), next to `$ai_sandbox_modifier()`:

```
macro ai_civil_war_ignition_modifier():
  factor(0.25)
  is_sandbox_mode_on()
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

## Event and mission overlays

Do **not** wrap `start_civil_war` in a generic scripted effect: the payload (ideology, size, states, characters) is different at every call site. Overlay around the call. Delay; do not delete the fuse.

`is_triggered_only` events and mission timeouts often set "already revolted" flags in `immediate` **before** `start_civil_war`. If you skip the war after those flags, the revolt is eaten forever. Gate **before** the flag, or restart the mission / re-fire the event without setting the flag.

### Pattern A — MTTH / daily trigger (Spain no-LaR)

The event re-evaluates every day. Add `NOT sandbox_civil_war_ai_blocked()` to `trigger` (or an equivalent `OR = { is_ai = no NOT cap }`). When the cap frees, vanilla MTTH continues. A failed trigger cannot log: weekly `cw_defer spain` is what proves AI Spain is waiting. When the event actually fires, `cw_event spain.1` / `spain.10`.

LaR Spain: overlay the **military-plot missions** that actually start the war, not only `lar_spain.1` (that event is the 1936 election and must still fire). Active plot missions already emit `cw_defer`.

### Pattern B — AI-choice option (elections, some country events)

On the option that calls `start_civil_war`:

```
ai_chance:
  +modifier:
    factor(0)
    sandbox_civil_war_cap_reached()
```

The peaceful / other option stays. Player still sees both. If **every** option starts a war (ITA `BBA_italy_civil_war.1`), this pattern cannot save it — use C at the **caller** (BoP `on_activate`, focus, mission). `ai_chance = 0` cannot log a skip; the civil-war option logs `cw_event` when taken.

### Pattern C — Forced fuse (immediate, timeout, on_daily, BoP)

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

### Pattern D — Decisions the AI can take

Same as focuses: `ai_will_do` `factor(0)` when `sandbox_civil_war_cap_reached()`. `available` unchanged (player). Includes ENG decisions that `start_civil_war` on a dominion.

## Coverage

### Focuses (first pass, keep)

Tag every vanilla focus whose reward contains `start_civil_war` (or `effect_tooltip` of one that the actual reward then runs). Known list in `common/national_focus/*.txt` as of 1.19:

- Direct `start_civil_war` in the focus: `AFG_the_faqirs_revolt`, `AFG_return_of_the_emir`, `AFG_parliamentary_democracy`, `AFG_socialist_coup`, `ARG_viva_la_revolucion`, `BALTIC_overthrow_the_government`, `BALTIC_arm_baltic_reds`, `BRA_ban_political_parties`, `BRA_launch_the_revolution`, `BUL_overthrow_the_tsar`, `BUL_abolish_the_monarchy`, `BUL_depose_the_tsar`, `CHL_avenge_the_pacification_of_araucania`, `COG_strike_while_the_rion_is_hot`, `COG_uniao_dos_povos_do_norte_de_angola`, `CZE_kohler_faction`, `DEN_seize_power`, `DEN_ask_for_support`, `EST_march_on_talinn`, `FIN_the_second_finnish_civil_war`, `FIN_a_fascist_regime`, `FRA_destroy_the_counter_revolution`, `wuw_HUN_reviving_the_spirit_of_1848`, `RAJ_give_me_blood_and_i_will_grant_you_freedom`, `RAJ_indian_peoples_army`, `RAJ_indian_national_army`, `IRQ_kurdish_revolt`, `JAP_cast_the_die`, `JAP_pre_emptive_coup`, `PER_strengthen_iranian_parliament`, `PER_force_abdication`, `PER_iranian_socialist_revolution`, `PER_march_on_saadabad`, `POR_reorganization_of_the_communist_party`, `lar_portugal_iberian_workers_united`, `POR_allow_free_elections`, `POR_ditadura_militar`, `POR_restoration_of_the_monarchy`, `SIA_the_kings_gambit`, `SIA_and_spring_the_trap`, `SIA_unseat_the_government`, `SAF_support_the_german_coup`, `AAT_Sweden_nationalists`, `TUR_restack_the_officer_corps`.

- Event / scripted-effect ignition **from a focus**: still tag **root + ignition** on NOR / EST / LAT / LIT / POL / USA / MEX. The focus cap remains; this pass also overlays the event/mission the focus fires, so a player-completed focus at cap still starts the war, and an AI-completed focus cannot sneak around the cap via the event.

Do not tag intervention / "lessons from the Spanish Civil War" / volunteer focuses.

### Events, missions, decisions, on_actions (this pass)

Walk vanilla `start_civil_war` outside `common/national_focus/`. Overlay every ignition. Known holes from the v0.1.1 playtest, plus the same-family scripts:

- **Spain**: no-LaR `spain.1` / `spain.10`; LaR military-plot missions (not the election event).
- **Mexico**: `MEX_mission_cedillos_rebellion` timeout → `mexico.1`; Cristiada / second-revolution missions → `mexico.28` / `mexico.30`.
- **Australia**: `on_daily_AST` veterans revolt; `AST_veterans_revolt` mission timeout; TAOG paths that call `AST_instigate_civil_war_in_target` on AST itself.
- **Greece**: BFTB events that `start_civil_war` (`bftb_greece.105` via `bftb_greece.100` else_if + weekly retry, `.218` from `.207.b` Pattern B — not the "start a war in Turkey" options unless TUR is the target slot).
- **Poland**: peasant-strike / sanation mission timeouts and `POL_scripted_effects` civil-war effects.
- **Baltic**: LIT/LAT/EST decisions and NSB events that start a war in ROOT (and LIT events that start one in POL — gate the actor, count the target). `EST_vaps_down_effect` (same pattern as Iron Wolf). `EST_events.7` trigger + weekly retry. `LAT_events.8` (both options war; mission `available` + event trigger). `LIT_events.10` / `EST_events.9` Pattern B.
- **Persia**: `PER_revolution_events.1` (event trigger + weekly retry) and ignition on `PER_revive_old_ways`; `PER_civil_war_imminent` mission delay.
- **Italy**: BoP `ITA_grand_council_total_control_range` → `BBA_italy_civil_war.1` (event trigger + weekly retry). Overlays use `sandbox_civil_war_ai_allowed()` (`= yes`), not `scripted_trigger = no`.
- **Ethiopia**: BoP total-control ranges → `BBA_ethiopia_balance_of_power_events.01`; weekly retry while the range is still live.
- **Siam**: `siam.8` (Songsuradet, delayed from `siam.7`); `SIA_war_fervor_coup` mission.
- **Soviets**: ignition focuses `SOV_left_opposition_coup` / `SOV_coup_detat` / `SOV_the_hands_do`, plus the events they queue.
- **Lithuania**: `LIT_iron_wolf_partisans` / `LIT_iron_wolf_down_effect` (Iron Wolf idea tick at bad_4). `EST_vaps_down_effect` is the same family.
- **Elections**: `election.11.b` / `election.12.b` — Pattern B.
- **UK/dominions**: ENG decisions that `start_civil_war` on CAN/SAF/AST/NZL.

If unsure whether a `random_list` can skip the war, still overlay: the cap only delays the AI, it does not delete the reward.

## Honor, Tyranny, Rivals

No Honor change when a civil war starts. The winner still rolls Honor/Tyranny on `on_civil_war_end` as today.

Rivals: `on_civil_war_end` already re-rolls the winner's personal rival. No extra rule. A civil-war opponent is not auto-added as a rival (they are at war; `$is_rival_of()` already treats that as rivalry for gating).

## Implementation notes

- Counter and `seen[]` live in global scope. `seen[]` is a temp rebuild, not a persistent list of old wars. Dedup with `every_country_with_original_tag` / `original_tag_to_check = THIS` — do not bind a loop variable that compiles `THIS` to the weekly ROOT.
- `sandbox_civil_war_cap_reached` is a scripted trigger so focus files do not read the variable with a raw `compare`. Vanilla overlay `limit` / `trigger` blocks use `sandbox_civil_war_ai_allowed()` (`NOT` of `sandbox_civil_war_ai_blocked`). Do not write `sandbox_civil_war_ai_blocked = no`: custom `scripted_trigger = no` does not reliably invert.
- `$ai_civil_war_ignition_modifier` must **not** fold `factor(0)` for the cap into the same block as `factor(0.25)`: if the cap trigger fails, the whole modifier is skipped and the 0.25 would vanish. Two modifiers, as in the snippet above.
- `$ai_sandbox_modifier()` stays on those focuses. Order: sandbox 40, then 0.25, then cap, then party/Tyranny as today.
- Rebuild the counter on `on_weekly`, `on_civil_war_end`, and civil-war `on_declare_war`. Do not wait a week after Spain ends to open a slot.
- `original_tag` of a rebel is usually the parent's. If a dynamic `Dxx` tag ever shows `has_civil_war` with its own original_tag, it counts as its own slot; accept that.
- Empty `t*` in `#sandbox` pulses often print the pulse ROOT (HAI) when the array slot is empty. Trust `cw=`, not unique `t*` tags.
- Compile after tagging `.include` files (`compile-after-hsl` rule), including `events/` and `common/decisions/` overlays.

## How to read `game.log`

First line is the version (`#sandbox Mode Overhaul v0.1.2`). Next is `sandbox_start historical=0` or `historical=1`.

| Token | When | What to read |
| --- | --- | --- |
| `cw_pulse` | weekly, HAI | Census. Use `cw=` and `cap=`. The `N->N` arrow is the post-rebuild snapshot, not a weekly delta. Ignore `t*` for identity. |
| `cw_count` | counter actually changed | Same fields; the arrow *is* the delta. |
| `cw_declare` | civil-war `on_declare_war` | Slot taken. Arrow should be `N->N+1` (Spain is 1, not SPR+SPA). `ai=0` if **either** ROOT or FROM is human (ROOT is often a Dxx rebel). `other=` is the other side — use that, not Dxx, to name the war. |
| `cw_end` | `on_civil_war_end` | Slot freed the same day. Then a waiting fuse may fire that day or within a week. |
| `cw_ignition` / `cw_root` | focus `completion_reward` | `ai=0` is the player. Root has no cap; ignition must not complete while `cap=1` for an AI. |
| `cw_defer` | Pattern C skip this week | Tag + fuse id (`spain`, mission id, `BBA_italy_civil_war.1`, `on_daily_AST`). Proves the AI is waiting, not that vanilla has not rolled yet. |
| `cw_event` | fuse actually fired | `spain.1` / `spain.10`, `election.11.b` / `12.b`, ITA retry. `ai=` is THIS (the country running the event), not a rebel. |

**Fail the cap** if any `cw_pulse` / `cw_count` has `cw=` **greater than 3**, or an AI (`ai=1`) `cw_declare` whose arrow is `3->4`. A `2->3` line with `cap=1` is the third war, not a fail. A player (`ai=0`) may push `cw` above 3; that is allowed.

**Name an ungated fuse:** an AI `cw_declare` that raises the count with no `cw_ignition`, `cw_event`, or `cw_defer` for that original_tag in the days before it. v0.1.1 playtest extras (AST, GRE, MEX, LIT, PER, POL, ITA) must now show `cw_defer` or `cw_event` first. A new extra without those tokens is a hole (NSB events, `bftb_greece.105` from `.100`, `bftb_greece.218`).

**Silent by design:** Pattern B skip (`ai_chance` 0) and Pattern D (`ai_will_do` 0) do not log. Prove them by the fail rule above, not by a defer line.

Historical: after `sandbox_start historical=1` the rest of the log must not contain `cw_`. Overlay files still exist; their gates require sandbox mode, so they are no-ops.

## Acceptance checklist

Log-first. Observer sandbox unless the item says human or aiview. Tick only when the grep holds (compound items split so a partial pass is visible).

- [x] First `#sandbox` line is the current version; next is `sandbox_start historical=0`.
- [x] Spain 1936 with `cw<3`: `cw_event spain.1` / `spain.10` / `lar_spain.2` then `cw_count` whose arrow is `N->N+1` (not +2 for SPA/SPB).
- [ ] AI Spain while `cap=1` and no SCW yet: weekly `cw_defer spain` (and `cw_defer SPA_military_plot_nationalists` / `SPR_military_plot_republicans` if LaR missions are already ticking). No `cw_event spain.1` until a `cw_end` drops `cap` to 0.
- [ ] Human SPR at `cap=1`: no `cw_defer spain`; `cw_event spain.1` with `ai=0`; `cw_declare` `ai=0`.
- [x] After Spain, a second and a third AI war may start (`cw=` 2 then 3) from focus (`cw_ignition`), event (`cw_event`), or mission (`cw_defer` then `cw_declare`).
- [x] No AI `cw_declare` with arrow `3->4` or `cw=` 4 on a pulse. v0.1.1 hit 8 via event/mission after `cap=1`; that must not recur through 1938.
- [ ] Capped ITA BoP: `cw_defer BBA_italy_civil_war.1` weekly while the range is active; after `cw_end`, `cw_event BBA_italy_civil_war.1` (same week or next).
- [x] Capped Cedillo / peasants / veterans with the mission already ticking: `cw_defer MEX_mission_cedillos_rebellion` (or `POL_peasants_strike` / `AST_veterans_revolt` / `on_daily_AST`); after `cw_end`, the timeout may fire within a week (no more defer, then `cw_declare`).
- [ ] `cw_root USA_america_first` may appear while `cap=1`. `cw_ignition USA_ally_with_the_silver_shirts` / `USA_union_representation_act` must not appear for an AI (`ai=1`) while `cap=1`.
- [ ] Human USA ignition or human Mexico Cedillo timeout at `cap=1`: `cw_ignition` / `cw_declare` with `ai=0`; no `cw_defer` from that player tag.
- [ ] Historical: `sandbox_start historical=1`, then no `cw_` lines. Vanilla Spain 1936 still happens in-game.
- [ ] aiview (in-game, not the log) on an ignition focus, cap free: sandbox 40 × 0.25 = 10, times party/Tyranny. Cap reached: 0.

## Out of scope for this iteration

- Rewriting Spain, Cedillo, or any `start_civil_war` payload (states, ideology, OOBs).
- Player decisions "start / join a civil war" besides applying the same AI gate as other decisions.
- Spy coup operations (`00_operations.txt`).
- Stability-crisis civil wars (`stability.3`) unless a playtest shows they cluster; then use Pattern C on that mission.
- News events / notifications about the cap.
- A game rule for the cap (3 vs 2). Hard-code 3; promote to a rule only if testers want it tighter.

## Second iteration (not blocking)

- If the 1936 cluster is still too hot because many AIs *finish* the branch the week Spain starts: lower root 0.25, or delay ignition with `days = 30` only when the cap is reached (hidden event) — that second option is a content change, not a weight change, and needs a separate pass.
- Reserve a slot for Spain so 1936 always fires even if two others went first — only if testers want Spain guaranteed rather than "up to three including Spain".
- Count "player's civil war" toward the cap or not (currently it does, which is what we want: the player's Spanish playthrough still occupies a slot for the AI).
- `stability.3` if wartime crises start clustering.
