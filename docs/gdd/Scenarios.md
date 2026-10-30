# Scenarios

A sandbox-only director that gives every session a crisis to live through: at
startup it picks one **arc** (a plausible 1930s conflict), rolls its target
variant, seeds the aggressor against its targets, and runs a three-rung ladder
that pushes the AI toward war. The player either gets drawn in or watches the
world burn. The system is designed to reuse the other sandbox mechanics (Honor,
Tyranny, Rivals, Civil Wars, National Focuses) rather than add new ones.

This is the vanilla mod. The Rt56 overlay (`_sandbox-r56`) shares the engine
and most documentation; this file describes what is specific to vanilla.

## Design goals

1. Make sessions alarming: an arc must, on a random draw, drive a major war.
2. Leave the player free: the director pushes AI, not the human; the player can
   join, meddle, or sit it out.
3. No new PM-level systems: reuse existing modifiers and hooks.
4. Stay legible: every mechanism logs to `game.log` under `#sandbox` for
   observer sessions.

## Selection

One arc per session, chosen at startup: pinned by a game rule or rolled at
random over the arcs whose aggressor exists. Arc ids are fixed per major
(1 GER, 2 ITA, 3 JAP, 4 SOV, 5 FRA, 6 ENG); the USA arc is an authored draft
without a `number`, so the builder emits no code for it and it cannot be picked.
The pick rolls the target variant evenly (`targets` keys `a`, `b`, ...; a
single-variant arc uses `a`, and the index - not the letter - is what
`sandbox_target_variant` holds) and logs `sc_pick` plus `sc_variant`.

### Pool and selection

`sandbox_pick_scenario()` (HAI scope, `on_startup`) first calls the six generated `gen_<arc>_scenario_pin()` functions, each of which asks its own `sandbox_scenario_pin_is_<arc>()` trigger (a raw `has_game_rule: { rule = sandbox_scenario option = ... }`) and sets `global.sandbox_scenario_pin = 1` on a match. Game-rule option ids are not l10n keys and need no localisation entry; the `sandbox_nazi_germany` option id is the only one with a `sandbox_` prefix, the rest are bare arc keys.

- If the pin is unset (`0`), the pick is a **uniform roll over eligible arcs**, not a scan in id order: each arc appends its id to `eligible[]` when its aggressor exists, then `roll = randi(0, eligible[].size() - 1)`. An empty pool sets `sandbox_scenario = 0` (no arc).
- A derail repicks the same way over the never-derailed arcs (`sandbox_scenario_maybe_repick()`); a derailed arc never re-enters the pool in the same session.
- Target variants are rolled evenly at pick (`randi(0, key_count - 1)` in the generated `roll_variant`) and remain fixed for the session. Every arc's roll function runs, so a repick re-rolls the variant.
- After the roll the pick clears the four counters (`arc_months`, `peak_months`, `civil_war_months`, `hold_months`), sets the targets, seeds the actors, logs `sc_pick` and `sc_variant`, and logs `sc_phase smolder`.

### Excluded majors

- **HUN**: the Habsburg restoration arc is out of scope for this pool by user
  decision; its vanilla focuses do exist should it be added later.
- **USA**: the fascist-America arc is authored as a spec (`draft`, no `number`)
  and is parked. Removing it from the code (commit `3a48253`) deleted its events
  file, its pin game-rule option and its pin trigger, so arc id 7 is no longer
  dispatchable; `sandbox_scenario_maybe_repick()` still tests
  `country_exists(USA) and 7 not in ...`, which is harmless because
  `sandbox_set_targets()`,
  `sandbox_seed_actors()` and the tick dispatcher have no id-7 branch. The spec
  stays for when the regime-flip design is reworked.

## Arc schema

Each arc is described by one TOML **arc spec** in `docs/scenarios/<id>.toml` or
`docs/scenarios/<aggressor>_<id>.toml` (one per arc per mod). Shared tooling
(`core/tools/build_scenario_catalog.py`) reads the specs and derives the
catalog (`docs/gdd/Scenarios Catalog.md`), the per-arc Mermaid diagrams, the
focus-boost and suppress splices, the expected telemetry labels, and the
per-arc generated HSL mechanics (`common/scripted_effects/99_sandbox_scenarios_gen.hsl`:
target seeding, seed actors, variant roll, ladder tick, s7 telemetry, derail
arms, joiner selection, and pick/pin helpers; see ADR-0003 and ADR-0005).
Scripted events and `fire_*` effects stay hand-written in the HSL catalog.

Which functions the builder actually emits per arc is what a spec's fields
turn on: `set_targets`, `seed`, `roll_variant`, `log_variant`, `pick_log`,
`pin`, `eligible`, `telemetry` and `derail` always; `tick` only when the
`[ladder]` content pair is present (an arc without `crises_func` / `peak_func`
has no generated rung branch); `sandbox_select_<id>_joiners` only when a
`[joiners]` table exists. The dispatchers in the mod catalog
(`sandbox_set_targets`, `sandbox_seed_actors`, `sandbox_scenario_tick`,
`sandbox_scenario_maybe_repick`, `sandbox_log_scenario_success`,
`sandbox_scenario_check_*`) call the generated functions by number, so a
missing `number` removes the arc from the dispatcher as well.

The catalog regenerates together with the splices; `--check` compares the
committed catalog and the `.include` splices against the specs. It also
compares each spec's mtime against its aggressor's focus-graph snapshot
(`docs/gdd/National Focuses/<stem>.md`), so running it without first
re-exporting the graphs via `.scratch/scripts/export_focus_graphs.py` fails
with `stale focus graph` rather than reading a stale prerequisite map.

```toml
id = "nazi_germany_scenario" # slug; identity (matches <id>.toml or <aggressor>_<id>.toml)
number = 1                   # the director's arc id; written when the arc has code
status = "ready"             # ready (in the shipped pool) | draft (authored, not selected)
aggressor = "GER"            # a single tag
key = "nazi_germany"         # short slug for the pin trigger and pick label; optional

targets = { a = ["CZE", "POL"], b = ["FRA", "ENG"] }  # target variants, rolled evenly
suppress = ["GER_austria_first"]  # optional: focus ids the AI must not pick while the arc is live

[ladder]                    # months from arc start
crises_at_month = 12
peak_at_month = 24
# Content rungs (optional pair): hand-written functions the tick calls.
# Both or neither; absent means the arc has no generated tick branch yet.
crises_func = "sandbox_fire_nazi_germany_crises"
peak_func = "sandbox_fire_nazi_germany_peak"

[joiners]                   # shared scorer + optional candidate-pool filters
select = "top_n_by_scorer"
n = 2
invite_event = "sandbox_nazi_germany.4"
require = ["same_ideology", "same_continent"]  # optional subset of {"same_ideology", "same_continent"}

[gate]                      # optional; absent means no gate
# Derail pair (optional): park the arc when the aggressor is off ideology.
ideology = "fascism"
at_phase = "crises"
# Hold set (optional, all three together): freeze the arc clock while the
# aggressor is not yet on hold_ideology, then run the ladder; if it never
# changes, park the arc after hold_max_months months with hold_reason.
hold_ideology = "neutrality"
hold_max_months = 30
hold_reason = "no_regime_change"

# Ordered focus paths: each table runs from a branch entry to a war leaf and
# declares the variants it serves (absent means shared across all variants).
[[paths]]
focuses = ["GER_remilitarize_the_rhineland", "GER_anschluss", "GER_demand_sudetenland"]

# Optional `after`: gate this path's boost on the listed focuses being done, so
# a later stage waits for an earlier path. Shared ancestors stay ungated.
[[paths]]
after = ["GER_anschluss"]
focuses = ["GER_austria_first"]

notes = """
Free rationale prose, printed into the catalog beside the arc.
"""
```

Top-level keys come before `[table]` headers: in TOML everything after a
header belongs to that table. `id` must match the file stem (`<id>` or
`<aggressor>_<id>`); `number` is unique and must match the code dispatcher; a
`ready` arc requires a `number` (a spec without a `number` is authoring-only:
it prints in the catalog, while boosts, suppress, labels and generated HSL are
skipped). Every key focus must exist in the aggressor's focus graph. The ladder
content functions come as an optional pair (`crises_func` + `peak_func` naming
the hand-written rung functions); absent means no generated tick branch. The
optional `key` names the pin trigger suffix and pick label; absent means no
generated pick data. `joiners` requires `select = "top_n_by_scorer"`, positive
integer `n`, and non-empty `invite_event`, plus optional `require` filters
(`"same_ideology"`, `"same_continent"`). Every variant holds 1-4 targets (the
derail arms cover that range). Every `targets` key is covered by at least one
path; every listed `variants` entry is a `targets` key. Boosts follow the live
variant: shared focuses stay boosted whenever the aggressor is live,
path-specific focuses only while their variant runs, and an entry's optional
`after` holds its boost back until every listed focus is completed (shared
ancestors of a gated path stay ungated). The peak rung waits for the AI to
complete the last focus of the live path (humans proceed on schedule), with a
fallback twelve months past the peak month; put rarely-bypassed focuses last,
since a bypassed tail stalls to the fallback. The optional `suppress` list
closes focuses for the AI while the aggressor is live
(`$ai_scenario_focus_suppress()`, factor 0); a suppressed id must exist in the
graph and must not be a key focus, so suppressing a fork forces the AI onto a
sibling (issue 33: the SOV purge-opposition forks, leaving `the_centre`). There
is no `type`, `block` or `content_refs` field. The optional `gate` table either
holds the arc until a regime flip (the `hold_*` trio) or carries the derail
pair (`ideology`/`at_phase`); the hold freezes `arc_months` at zero while the
aggressor is off `hold_ideology` and parks the arc with `hold_reason` once
`hold_max_months` held months pass, so a ladder whose premise is a regime
change never fires into the old regime. A hold needs the ladder content pair
(its tick is where the rungs live). The builder validates `gate.at_phase` as a
string but does not consume it: the generated derail arm only uses the
`hold_*` trio, and the `ideology`/`at_phase` pair is implemented by the generic
`$sandbox_check_flip_gate1/2` / `$sandbox_check_flip_gate_inv` macros in
`common/macros.hml`, which no shipped arc calls. A spec that relies on the pair
is authoring-only until a mod's catalog adds that call.

## Ladder

The rungs are arc-relative: every arc counts `sandbox_scenario_arc_months` from
its own pick (a repick resets the clock to 0), and each spec sets its own
thresholds in `[ladder]`.

| Rung | Phase | Fires at (`crises_at_month` / `peak_at_month`) | Releases |
|---|---|---|---|
| smolder | 0 | month 0 | seed only |
| crises | 1 | 12 (GER, ITA, JAP), 10 (ENG), 14 (FRA), 16 (SOV) | crisis events (claims, incidents) |
| peak | 2 | 24 (GER, ITA, JAP), 20 (ENG), 30 (FRA), 32 (SOV) | ultimatums to targets, join offers |

There is no single template calendar: the values above are what the six shipped
specs declare. GER / ITA / JAP sit on the original 12-and-24 template; ENG runs
a compressed 10/20, FRA 14/30 and SOV 16/32. The cartesian calendar in
364-day months (36.1.1 / 37.1.1 / 38.1.1) is the same for a 12/24 arc.

**Peak gating.** The peak rung does not simply fire at `peak_at_month`. The
builder (`render_peak_gate()` in `core/tools/build_scenario_catalog.py`) emits
three arms per target variant, using that variant's own `peak_at_month`:

1. the AI completed the **last focus of the live path** (`path_tail()`, the focus
   last listed in the *first* `paths` entry whose `variants` names the live
   variant) - fires now;
2. the aggressor is a human (`<aggr>->is_ai(no)`) - fires on schedule;
3. the fallback: `arc_months >= peak_at_month + 12` - fires even if the tail was
   bypassed.

A bypassed tail therefore stalls the arc to the fallback, which is why the
`docs/gdd/Scenarios Catalog.md` guidance is to put rarely-bypassed focuses last.
The peak counter (`sandbox_scenario_peak_months`) then runs for 12 months before
`peak_timeout` derails the arc (see "Lifecycle").

## Levers

**Rivals and antagonism**: the director seeds each aggressor-target pair as a
national rival at 65 (`$sandbox_seed_rival(PREV, 65)` inside
`sandbox_seed_from_targets()`, which also writes `scenario_enemies[]` on **both**
sides so ignition is direction-agnostic). Rivalry is then injected through the
hand-written crisis and ultimatum events: the crisis option adds `+10` to a
named target, and each defied ultimatum adds `+15` to the defying target
(`$sandbox_add_rivalry_vs`). Rivalry is the main lever; no new AI code.

**Focus weights**: `$ai_scenario_focus_boost()` (x5, live aggressor only) is
spliced onto the arc's war focuses and the transitive ancestor closure of their
prerequisites, so the AI actually walks the war branch (the s10 lesson: a boost
behind an unboosted fork is dead). `boost_set()` in the builder computes the
closure and drops a mutually exclusive sibling when exactly one side of a fork
is a key focus. Which focuses each arc boosts is drawn per arc in
`docs/gdd/Scenarios Catalog.md`. Three more forms ride beside it:
`$ai_scenario_focus_boost_variant(N)` when a focus belongs only to specific
target variants, `$ai_scenario_focus_gate_after(FOCUS_ID)` with `factor(5)` when
the spec's path entry declares `after`, and `$ai_scenario_focus_suppress()`
(factor 0) for the spec's `suppress` list, so a wrong fork cannot win the AI's
pick even before the boost applies. Every boosted focus also gets
`$sandbox_log_sc_focus(FOCUS_ID)` in its completion reward, which is the only
evidence that the AI is actually walking the path.

**Join levers**: at peak the top `n` highest-scoring outsiders
(`scenario_join_scorer`, filtered by optional `joiners.require` flags; see
ADR-0005) get a bloc invitation (`joiners.invite_event`). The scored pool is
`global.countries`; the scorer's gates (score `factor(0)`) are self, human,
civil war, at war with the aggressor, in the aggressor's own faction, subject
ties either way, enemy ideology with the aggressor, and the two `require`
filters. It scores divisions, industry (`scenario_join_industry`, snapshotted by
`sandbox_snapshot_join_industry()` before the sort), and the candidate's opinion
of the aggressor in three staircases, maxima 60/60/60. Accepting the invitation
gives mutual military access and the `scenario_ally` opinion modifier
(+40 vanilla / +80 Rt56) and logs `sc_join`; a joiner leaves its old faction
first with `sandbox_honor_skip_leave_faction` set, so the exit is Honor-free.
No faction is formed.

**Ultimatum casus belli**: a refused peak ultimatum must give the aggressor a
wargoal (`$create_wargoal(PREV, topple_government)` from the `hsd` stdlib
macro), or ignition waits on the AI's own war decision and can miss the
`peak_timeout`. Shipped coverage: the defied option of every ultimatum in
`napoleonic_france` (3), `soviet_west` (3) and `monarchical_great_britain` (2)
carries it. The `nazi_germany`, `fascist_italy` and `militarist_japan` arcs do
not: their defied options only add war support and rivalry, so those arcs still
depend on the AI justifying on its own. That gap is what the acceptance runs
below observed.

## Lifecycle

The `sandbox_scenario_phase` value is `0` smolder, `1` crises, `2` peak, `3`
ended. `sandbox_scenario_tick()` runs monthly and, unless the arc is already
parked, increments `sandbox_scenario_arc_months` and then calls two ignition and
derail checks before the per-arc tick functions.

**Ignition**: any war between declared scenario enemies, in either direction,
detected at declaration (`on_declare_war` -> `sandbox_scenario_ignite()`, which
only tests that `FROM` is in `scenario_enemies[]`) or by the monthly ongoing-war
sweep (`sandbox_scenario_check_ignite_by_war()` -> `sandbox_ignite_if_at_war()`,
which walks target slots 0-3 in the aggressor's scope). Ignition sets the phase
to 3 and logs `sc_ignite` + `sc_success` + `sc_end` with an `<arc>_war` label.

**Derail** parks a dead arc at phase 3. `sandbox_scenario_check_derail()` first
runs `sandbox_scenario_check_civil_war_derail()` (12 consecutive months of
`sandbox_scenario_civil_war_months`, reason `aggressor_civil_war`), then
`$sandbox_check_peak_timeout()` (12 consecutive months at phase 2, reason
`peak_timeout`), then the per-arc generated derail arm. The generated arms cover
the aggressor no longer existing (`<agg>_gone`), the aggressor having capitulated
(`<agg>_capitulated`), and two target arms per variant:
`targets_gone` when no declared target exists, and `targets_neutralized` when
every target is gone, a subject of the aggressor, or in its faction. A spec's
`gate` table adds one more: the `hold_*` trio parks the arc with `hold_reason`
after `hold_max_months` months off the required ideology, and the
`ideology`/`at_phase` pair (via `$sandbox_check_flip_gate1/2` and
`$sandbox_check_flip_gate_inv`) parks it when the aggressor is on the wrong
ideology at the given phase. No shipped spec uses the flip pair today; the
generic macros are ready for it.

When the phase crosses from `< 3` to `3`, `sandbox_scenario_maybe_repick()` runs.
On a random session it appends the arc to `global.sandbox_derailed_arcs[]`,
clears every country's `scenario_enemies[]`, and rolls a fresh arc over the
eligible, never-derailed ids 1-7 (equal weights, like the initial pick; ids 1-6
ship, 7 is the USA draft and is never eligible in practice). Nothing eligible
logs `sc_repick none_eligible` plus a `sc_repick_detail` line naming the
`country_exists` flags. Pinned sessions (`sandbox_scenario_pin == 1`) go quiet:
the phase stays 3 and nothing is repicked.

## Hooks and telemetry

All hooks live in the core skeleton `core/common/on_actions/99_sandbox_core_on_actions.hsl`, copied into each mod as the generated `common/on_actions/99_sandbox_on_actions.hsl`; per-arc tail hooks are generated into `common/scripted_effects/99_sandbox_arc_hooks.hsl` by `tools/extract_arc_hooks.py`.

- Tick: `on_startup` (selection, in HAI scope, **after** the country init loop so `months_elapsed` and `tyranny_home` are set before `sc_pick`) plus `on_monthly`.
- Monthly host chain: `on_monthly` runs per country, so the tick fires in exactly one host per month. HAI is primary; if HAI does not exist the chain falls through GER, SOV, JAP, ITA, ENG, USA, and finally `sandbox_arc_tick_hosts()` (the per-mod fallback, `pass` in vanilla, FRA-then-HUN in Rt56). The same HAI host also runs `sandbox_civil_war_cooldown_tick()` and `sandbox_cw_backing_monthly()`.
- Weekly: `sandbox_arc_on_weekly()` (`pass` in vanilla) for extra fuse retries.
- Reactions: `on_declare_war` (`sandbox_scenario_ignite()`), `on_wargoal_expire` (`sandbox_arc_wargoal_expire_hook()`, gated on `sandbox_scenario_phase < 3`). The scenario director has **no** `on_annex` / `on_capitulation` / `on_join_allies` / `on_join_faction` hooks: derail detection is entirely monthly (`sandbox_scenario_check_derail()`), and the join lever is tracked by the invitation event's own `sc_join` line, not by a faction hook (no faction is formed).
- Telemetry: `sc_pick`, `sc_variant`, `sc_seed`, `sc_phase`, `sc_crisis`, `sc_target`, `sc_power`, `sc_goal`, `sc_justify`, `sc_goal_end`, `sc_focus`, `sc_offer`, `sc_ignite`, `sc_success`, `sc_join`, `sc_end`, `sc_derail`, `sc_repick`. Per-actor lines are gated on `is_scenario_actor` (aggressor or a declared target), so an unrelated country's focus does not pollute the arc.

The `#sandbox` gate is `sandbox_log_scenarios`, raised by default in `on_startup` (it is the only system whose log gate is up out of the box). `sc_crisis` and `sc_join` are emitted from the arc events in `events/`, everything else from the effect files.

### Sampling cadence

A recurring state is sampled on a schedule; a transition is logged when it
happens. The s7 diagnostic package follows this rule:

| Line | Cadence |
| --- | --- |
| `sc_power` | monthly per live actor |
| `sc_goal` | monthly per declared pair with a held wargoal or an active justification |
| `sc_justify` | monthly per declared pair with an active justification |
| `sc_goal_end` | on wargoal expiry (transition) |

`sc_justify` used to ride the daily justification pulse (one line per day per
justification); since issue 15 it is a monthly sample like the rest of s7, so
a long justification costs lines per month, not per day.

### Telemetry label convention

`sc_goal` and `sc_justify` carry one label per aggressor/target pair, always
`<aggressor>_on_<target>` in **lowercase** (`ger_on_cze`, `ita_on_eng`). Both
label sets are generated from the arc specs into `99_sandbox_scenarios_gen.hsl`
and checked by `build_scenario_catalog.py --check`, so `sc_goal` and
`sc_justify` cannot drift apart.

- `sc_goal` logs wargoals in **both** directions, so it also holds
  `<target>_on_<aggressor>` labels (`cze_on_ger`); `sc_justify` only covers the
  aggressor's justifications.
- Every target tag in a label must be a real tag the arc seeds
  (`sandbox_set_targets`). Romania is `ROM`, never `ROU`.

### Join lever

The lever sends `sc_offer` to the top-N pool candidates (`joiners.n`, default 2). Accepting is
Honor-free (`sandbox_honor_skip_leave_faction`), grants **mutual military
access** with the aggressor and the `scenario_ally` opinion modifier (+40
vanilla / +80 Rt56), and logs `sc_join`. **No faction is formed.** Making the
aggressor a faction leader locks it out of its own war focuses, several of which
require `is_in_faction = no` (`ITA_pact_of_steel`, `ITA_italy_first`,
`GER_integrate_czechoslovakia`, `JAP_sea_pressure_siam`); an observer session
showed Italy reaching `ITA_foreign_affairs` and then stalling for six years,
unable to open the `italian_irredentism` path to war.

The invitation event's own trigger re-checks `is_ai(yes)` and
`not is_in_faction_with(<aggressor>)`, so a candidate that joined the
aggressor's faction between the sort and the event simply gets no invitation.

## Acceptance checklist

Log-first. Observer sandbox. Tick only when the grep holds.

- [ ] Startup: exactly one `sc_pick` naming one pool arc, plus one `sc_variant`.
- [ ] Ladder phases logged on schedule: `sc_phase smolder`, `crises`, `peak`.
- [ ] At peak each target logs one `sc_target` status line.
- [ ] Ignition: `sc_ignite` + `sc_success` + `sc_end` when a war fires between
  declared enemies (direct or ongoing).
- [ ] Derail: `sc_derail` + `sc_end` with a reason; random repicks.
- [ ] No `error.log` lines attributable to scenario files.

Observer note (first vanilla session, `italian` / variant a / YUG+GRE): phases
ran on schedule, the chosen variant was honoured, and the join lever fired
(`sc_offer` -> `sc_join`). The arc then hung at peak for a full year with no
`sc_ignite`, `sc_success` or `sc_derail`: both ultimatums were defied and the
defy option only adds war support, so ignition depends on the AI justifying on
its own. The betrayal exemption (F1) and the `sc_justify` / `sc_goal_end` /
`sc_focus` telemetry were missing from the vanilla port and are now wired. The
resulting gap - a peak that outlives the ladder undetected - is now closed by
`$sandbox_check_peak_timeout()` (12 months at phase 2 derails with
`peak_timeout`).

Observer note (second vanilla session, `japanese` / variant a / CHI+PHI): the
new `sc_focus` telemetry showed Japan completing **zero** war focuses over four
years while the arc sat at peak. Cause: the port boosted only the war leafs and
one or two roots, so nearly every leaf sat behind an unboosted prerequisite
(the ideological fork `JAP_sea_purge_the_kodoha_faction` XOR
`JAP_revere_the_emperor_destroy_the_traitors` for Japan, the Africa path for
Italy, `reorganize_the_wehrmacht` for Germany, `the_comintern` for the USSR,
`no_further_appeasement` for Britain, `intervention_in_asia` for the USA). The
AI never commits to the gate, so the leaf is never *available* and the boost on
it does nothing. The ancestor closure is now computed by `boost_set()` in
`core/tools/build_scenario_catalog.py` and spliced by the same generator that
emits the boost, and `sc_focus` logging was extended to match, so a dead gate is
visible in the log rather than silent. The standalone `boost_focus_ancestors.py`
helper no longer exists in this tree.

Observer note (third vanilla session, `japanese` -> `axis` repick): the peak
timeout worked as designed. Japan held at peak from 1938.1, both ultimatums were
submitted, the join lever fired (GER and SOV joined), and on 1939.1 the arc
derailed with `sc_derail peak_timeout` and repicked to `axis`. The axis arc then
compressed its ladder (crises and peak on consecutive ticks) and reached peak
with CZE/POL ultimatums and JAP/HUN joiners within a month. `sc_focus` showed
zero lines: the gate `is_scenario_actor` called the aggressor branch without
parentheses, so the compiler dropped it and only targets could log; fixed.

l10n note: `99_sandbox_l_english.yml` must stay UTF-8 **with BOM**. HOI4
silently drops a localisation file without it, and every string falls back to
its raw key (the leader-personality tooltip is the tell). The event-key
generator writes with `utf-8-sig` for this reason. Separately, every key the
engine points at must exist: the `scenario_ally` opinion modifier was missing
and surfaced as a raw key in the diplomacy tooltip. Game-rule
`option = sandbox_<arc>` ids are not l10n keys and need no entry.

## Out of scope for this iteration

- Flip and imperial arcs (DLC-gated focus branches in vanilla; they live in the
  Rt56 overlay).
- The full 28-arc catalog: only the content-portable subset ships here (six
  arcs plus the USA draft).
- Player-facing scenario UI beyond the pinning game rule.
- Concurrent arcs.
- Scenario behaviour in historical mode: sandbox-only.
