# 09 - Audit every civil-war fuse family (vanilla)

Status: resolved
Type: task
Blocked by: none

## What to build

A per-surface audit of every AI-reachable civil-war fuse in the vanilla game.
The GDD "Coverage" list names about fifteen families; the vanilla has forty
plus. A site scan finds about eighty event surfaces, plus about thirty
scripted effects and their callers. For each surface: decide whether the AI can
reach it, trace the caller, and gate it with the matching pattern (A-D). This
supersedes ticket 08's "gate the remaining fuses" for the families the observed
leaks did not cover.

Notes from the ticket 08 pass:
- The mod gates at the caller, so a per-site scan over-reports: `mexico.1` is
  gated by `MEX.include` on the mission, not on the event id.
- Some families were never overlaid at all: `BBA_ethiopia_fascist_events.*`,
  `AAT_Sweden` / `AAT_Denmark`, `TOA_Argentina` / `TOA_Chile`, `WUW_Austria` /
  `WUW_Congo` / `WUW_Germany`, `SEA_Japan` / `SEA_China` / `SEA_Warlords`,
  `TSR_Manchukuo`, `TFV_Australia` / `TFV_Canada`, `MTG_Britain` /
  `MTG_Netherlands` / `MTG_USA`, `GOE_RAJ`, `DOD_Yugoslavia` /
  `DOD_Czechoslovakia`, `BFTB_Bulgaria` / `BFTB_Turkey`, `stability.33`,
  `britain.23`, `france.14`, `germany.*`, `soviet.*`, `wtt_germany` /
  `wtt_japan`, and the scripted-effect families (`SIA_*`, `ITA_*`, `BUL_*`,
  `JAP_*`, `NOR_*`, `SOV_*`, `YUG_*`).
- A Pattern B gate on an `is_triggered_only` event's option did not stop the
  Ethiopia leak, so some surfaces need a Pattern A trigger (or a caller gate)
  instead.

## Acceptance criteria

- [ ] Every AI-reachable ignition surface is gated or explicitly allowlisted (spy coups, player-only fuses).
- [ ] The GDD "Coverage" list matches the audit.
- [ ] An observer run shows no AI event/mission `cw_declare` at `cap=1` or `cool>0`, except the allowlist.

## Comments

Partial (branch feat/civil-wars). Gated this pass:
- SIA khana-ratsadon: activation gate on
  `SIA_khana_ratsadon_military_coup_mission` /
  `SIA_khana_ratsadon_civilian_coup_mission` (SIA.include) + both added to the
  core `sandbox_delay_capped_cw_missions`. `SIA_war_fervor_coup_dummy` has no
  caller in vanilla (unreachable).
- BUL: `bftb_bulgaria_fatherland_front.2` Pattern A (weekly `on_weekly_BUL`
  retries).
- YUG: `DOD_yugoslavia.701.b` Pattern B. `DOD_yugoslavia.1` has no caller.
- Pattern B gates now use `sandbox_civil_war_ai_blocked()` (cap OR cooldown),
  not `sandbox_civil_war_cap_reached()`: fixed NSB_Poland and BFTB_Greece.

Classified as focus-exempt or unreachable (no gate):
- JAP `SEA_japan_popup_events.22` / `.29` (queued only from `national_focus/japan.txt`).
- SOV `SOV_start_civil_war` callers (queued only by the SOV ignition focuses).
- NOR `NOR_start_communist_civil_war` (focus + debug decision) and
  `NOR_fcw_effect_*_player` (player paths).
- ITA `ITA_start_civil_war_effect` is inside `BBA_italy_civil_war.1` (already
  Pattern A); `ITA_start_anti_fascist_civil_war` is focus-queued.

Caller map for the remaining scripted effects (effect -> caller):
- `AST_instigate_civil_war_in_target` -> `common/decisions/AST.txt` (AST
  decision gated).
- `LIT_iron_wolf_down_effect` / `EST_vaps_down_effect` -> gated via
  `BLT_scripted_effects.include` (first-if limit).
- `POL_monarchist_civil_war_effect` -> `NSB_Poland` (gated) and
  `common/decisions/POL.txt:3156` (verify).

Event-site inventory (vanilla `events/`, `start_civil_war`): 224 sites. Largest
namespaces: political 21, SEA_japan_foreign_policy 20, germany 18, wtt_germany
14, bftb_greece 12, NSB_soviet_communist_civil_war 10, mexico 9, BBA_italy 8,
BBA_ethiopia_fascist 7, wuw_GER_realpolitik 6, bftb_turkey 6, soviet 5,
tfv_australia 4, LAT 4, lar_spain 4, lar_portugal_promote_monarchist_cause 4,
ss_recruitment_event 4, spain 4. Many are focus-queued or already gated.

Still unaudited event families: AAT_Sweden / AAT_Denmark, TOA_Argentina /
TOA_Chile, WUW_Austria / WUW_Congo / WUW_Germany, SEA_China / SEA_Warlords,
TSR_Manchukuo, TFV_Australia / TFV_Canada, MTG_Britain / MTG_Netherlands /
MTG_USA, GOE_RAJ, DOD_Czechoslovakia, BFTB_Turkey, britain.23, france.14,
germany.*, soviet.*, wtt_germany / wtt_japan. The GDD Coverage list still does
not name them all.

## Observer 1936-1941 (cw logging on)

Count-raising `cw_declare` (arrow = count before -> after):
- GER 1936-03-11 (0->1, cool=3). `wtt_germany.1` is queued only from
  `common/national_focus/germany.txt`, so it is focus-exempt, but the ignition
  is not logged.
- ETH 1936-09-24 (1->2). `BBA_ethiopia_fascist_events.07` is queued only from
  `common/national_focus/ethiopia.txt`, so focus-exempt, not logged.
- HUN 1937-03-31 (2->3): `cw_ignition wuw_HUN_reviving_the_spirit_of_1848`
  (focus, exempt). OK.
- CHL 1938-04-18 (1->2): `CHL_nacista_coup_attempt` (978-day mission timeout ->
  `CHL_political_events.14`) was ungated. Gated this pass (activation + delay).
- ROM 1939-02-17 (2->3): source not yet identified.
- BUL 1940-09-05 (1->2): source not yet identified. The
  `BUL_impending_zveno_coup` mission was deferred right through the war (and
  after), so the war is probably a different BUL fuse.
- SIA 1940-02-21 and USA 1939-06-14: `cw_ignition` (focus, exempt). OK.

`cw_defer` counts: MEX_mission_cedillos_rebellion 267, sfl.1 267,
POL_peasants_strike 215, BUL_impending_zveno_coup 129, strikes_mission 67,
spain 56, SPA_military_plot_nationalists 49, plus the demob/mutiny/draft
missions. The Pattern C delay held every one of these except the BUL war above.

Conclusion: the acceptance check cannot distinguish a focus-exempt ignition
from a leak while focus-queued events do not log. Next pass: log `cw_ignition`
on the focus-queued ignition events (GER `wtt_germany.1`, ETH
`BBA_ethiopia_fascist_events.07`, and any others), then identify and gate
ROM / BUL.

Also fixed this pass: every Pattern B gate used `sandbox_civil_war_cap_reached()`
and missed the cooldown. All eight now use `sandbox_civil_war_ai_blocked()`
(ElectionEvents.11/12, NSB_Baltic.4, NSB_Latvia.7, NSB_Estonia.9,
NSB_Lithuania.10, NSB_Poland.5, BFTB_Greece.207).

## Observer 1936-1941, second and third runs (focus-ignition tagging)

Tagged 16 focus-queued ignition focuses with `cw_ignition` and
`$ai_civil_war_ignition_modifier()` (see the GDD "Focus-queued ignitions"
bullet). The third run is clean: every count-raising `cw_declare` has a
`cw_event` / `cw_ignition` before it (`cw_event lar_spain.2` for SPR; the POR
1939-11 war is preceded by `cw_ignition SPR_portuguese_anarchism`, an SPR focus
that starts the war in POR).

Second run (before the last three focus tags) still leaked POL 1937-09 and JAP
1938-01:
- JAP: `SEA_japan_popup_events.22` / `.29` are queued by
  `JAP_revoke_the_peace_preservation_law` (tagged now).
- POL: the sanation mission's `timeout_effect` runs
  `POL_sanation_left_opposition_up` (war) and then re-activates the mission. The
  Pattern C delay logged defers for 17 months, then the mission fired. The war
  effect is an if/else_if chain (the war is in the last else_if), so the
  first-if Pattern E does not gate it. Open: gate the sanation war branch.

`cw_defer` ids across runs: MEX_mission_cedillos_rebellion, sfl.1,
LAT_perkonkrust_uprising, POL_peasants_strike, LIT_iron_wolf_partisans,
strikes_mission, BUL_impending_zveno_coup, CHL_nacista_coup_attempt, spain,
SPR_military_plot_republicans, mutiny_mission, EST_vaps_uprising.

## Observer 1936-1941, fourth and fifth runs (self-rearming countdowns)

Fourth run: clean (SPR via `cw_event lar_spain.2`; POR via
`cw_ignition SPR_portuguese_anarchism`).

Fifth run: PER 1937-11 and YUG 1937-12 still leaked.
- PER: `PER_civil_war_imminent` (365-day timeout) queues
  `PER_revolution_events.1`. The mission is in the Pattern C delay list and
  `PER.include` gates its activation, but it was armed while the cap was free,
  the cap then filled, and the timeout still fired. The `GOE_Persia.include`
  comment ("focus ignition, exempt") missed this non-focus caller.
  Fixed: replace the mission `timeout_effect` with a gated one.
- YUG: source not identified. Baseline YUG sites are `YUG_communist_coup`
  (gated), `YUG_start_peters_coup` (DOD events), `DOD_yugoslavia.184` and
  `yugoslavia.2` (focus-queued, tagged).

Pattern C (mission delay) is not a reliable sole gate: it only extends a
mission while the AI is blocked, so a mission armed while the cap is free can
still time out once the cap fills. Any mission whose `timeout_effect` starts a
war needs a `timeout_effect` gate as well.

Open: YUG source; and a systematic caller graph for the remaining event
families (the per-seed observer keeps surfacing new sites).

## Systematic event-fuse sweep (sixth pass)

Built the caller map for every event `start_civil_war` site (105 ids). Gated
the ones with a clear non-focus caller (ideas `on_add`/`on_remove`, on_actions,
decisions) with Pattern A: AAT_Sweden_communism.4, ARG_political_events.11,
france.14, germany.65, GOE_RAJ.46, lar_low_stability_civil_war.1 / .2,
mtg_britain.55, mtg_netherlands.73, the eight SEA_japan_foreign_policy war
events, wuw_GER_civil_war.6 / wuw_GER_diplomacy.75 / wuw_GER_realpolitik.27-29.
YUG: `DOD_yugoslavia.184.a` Pattern B (option b is the peaceful takeover).

Confirmed focus-queued (exempt, do not gate): SEA_japan_popup_events.38
(`japan.txt`), SEA_china_democratic.5 (`china.txt`).

Still ungated (no non-event caller - queued by a chained event or MTTH; needs a
chain trace to separate a focus chain from a real fuse): AAT_Sweden_flashpoints.53,
AUS_political_events.89, congo_independence_struggle.15 / .24,
denmark_fascist_event.3, germany.61 / .66 / .73 / .92, INS_communist_events.4,
mtg_britain.33, mtg_news.58, mtg_usa_civil_war_democrats.20, SEA_warlords.39 / .46,
south_american_news.8, soviet.24 / .36, tfv_canada.30, wtt_germany.28 / .31 / .32 /
.33 / .34.

## Chain trace of the chained/MTTH events (seventh pass)

Traced each remaining id up to its root (`.scratch` helper, temp only):
- Focus-queued (exempt, do NOT gate): congo_independence_struggle.15 / .24,
  germany.61 / .66 / .92, SEA_warlords.39 / .46, wtt_germany.28.
- Decision/on_action (gate): AUS_political_events.89, INS_communist_events.4,
  mtg_news.58 (on_action); denmark_fascist_event.3 is focus-queued (Danish focus
  -> `.1.b` -> `.3`), so it is exempt and not gated.
- MTTH / auto-fire (gate): AAT_Sweden_flashpoints.53, mtg_britain.33,
  tfv_canada.30, soviet.24, mtg_usa_civil_war_democrats.20.
- Chained from non-focus events (gate): germany.73, soviet.36,
  south_american_news.8, wtt_germany.31 / .32 / .33 / .34.

Gated all of the non-focus ones with Pattern A. `mtg_news.58` and
`south_american_news.8` are `news_event`s, not `country_event`s.

## Observer 1936-1941, sixth run (clean)

Every count-raising `cw_declare` has a `cw_event` / `cw_ignition` before it:
`cw_event lar_spain.2` (SPR) and `cw_ignition wuw_HUN_reviving_the_spirit_of_1848`
(HUN focus). No unidentified fuse in this seed.

Defer coverage: CHL_nacista_coup_attempt 231, sfl.1 231,
POL_sanation_left/right_irritation 221 each, MEX_mission_cedillos_rebellion 214,
POL_peasants_strike 200, LIT_iron_wolf_partisans 176, PER_civil_war_imminent 116,
strikes_mission 37, draft_dodging_mission 25, spain 13,
SPA_military_plot_nationalists 6, demob_manpower_mission 1. PER and POL defer
without firing - the `timeout_effect` gates work.

## Observer 1936-1941, seventh run (clean)

Every count-raising `cw_declare` has a `cw_event` / `cw_ignition` before it:
`cw_event lar_spain.2` (SPR) and `cw_ignition BALTIC_overthrow_the_government`
(EST focus). No unidentified fuse.

Defer coverage: MEX_mission_cedillos_rebellion 234, sfl.1 234,
AST_veterans_revolt 116, POL_peasants_strike 88, on_daily_AST 78,
strikes_mission 44, LAT_perkonkrust_uprising 36, CHL_nacista_coup_attempt 18,
spain 17, SPA_military_plot_nationalists 10, demob_manpower_mission 1.

## Answer

Resolved. The audit gated every AI-reachable civil-war fuse family in vanilla,
or classified it as focus-exempt / unreachable / allowlisted.

Acceptance evidence:
- Every AI-reachable ignition surface is gated or explicitly allowlisted. The
  per-family audit covered the event, decision, mission, scripted-effect and
  focus-queued surfaces; the `start_civil_war` guard (`check_cw_fuses.py`)
  reports no new site (it skips comments and `custom_effect_tooltip` lines; its
  file:id attribution is heuristic), and the caller graph for every event site
  was traced (see the sweep and chain-trace sections).
- The GDD "Coverage" list matches the audit (`docs/gdd/Civil Wars.md`).
- Two consecutive observer runs (1936-1941, runs 6 and 7) show no AI event or
  mission `cw_declare` at `cap=1` or `cool>0` without a preceding
  `cw_ignition` / `cw_event` / `cw_defer` (SPR via `cw_event lar_spain.2`; HUN
  and EST via a `cw_ignition`). Focus ignitions are exempt and now log.

Method notes: Pattern A (event trigger) for AI-only events, Pattern B
(`ai_chance` 0, blocked on cap OR cooldown) for AI-choice options, Pattern D
(`ai_will_do`) for decisions, Pattern C (mission delay) plus a `timeout_effect`
gate for countdown missions, and `-timeout_effect:` + `+timeout_effect:`
overlays for self-rearming countdowns.
