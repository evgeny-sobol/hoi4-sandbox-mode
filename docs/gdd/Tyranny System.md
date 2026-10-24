# Tyranny

Tyranny is a per-regime measure of how concentrated and repressive the ruler's power is: how much the country is governed by coercion rather than consent.

Tyranny is a trade-off, not a good/bad scale. High Tyranny buys control (party drift defence, political power, a firm grip during war) at the price of openness (research, trade, resistance in occupied land). Low Tyranny is the mirror image: open and productive, but easy to destabilise from outside.

Tyranny is **not**:
- Honor (keeping promises to other countries; see `docs/gdd/Honor System.md`). The two are orthogonal: a liberal democracy can be treacherous, a despot can be a man of his word.
- Ideology. Ideology sets where Tyranny naturally settles, but every government can be pushed far from its home value.
- Rivalry (whom we want to fight; see `docs/gdd/Rivals System.md`). The only link runs the other way: an Authoritarian or Despotic ruler's personal rivalry (`rivals[0]`) grows +1 per month faster, a Libertarian or Liberal ruler's -1 slower.

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`.

## Scale and bands

`tyranny` is a country variable in `[-100.0, 100.0]`, clamped by `$add_tyranny()` in `common/macros.hml`.

Bands (same thresholds as Honor):
- `< -75` Libertarian (`libertarian_leader`)
- `< -25` Liberal (`liberal_leader`)
- `< 25` Moderate (`moderate_leader`, no modifiers)
- `< 75` Authoritarian (`authoritarian_leader`)
- `>= 75` Despotic (`despotic_leader`)

Initial value for a fresh sandbox leader: `randi(min_tyranny, max_tyranny)` from the government/leader-ideology table in `initialize_new_country_leader()` (`core/common/scripted_effects/99_sandbox_scripted_effects.hsl`); `min_tyranny` / `max_tyranny` / `tyranny_home` are set by `set_tyranny_range_from_government()` just before the roll.

## Design goals

1. National focuses are the main lever: repressive and liberal focuses in the vanilla trees move Tyranny in discrete steps.
2. Institutions have inertia: Tyranny drifts back toward the ideology's home value, so a one-off focus leaves a mark that fades over years unless the path is continued.
3. War and crisis push every regime toward control.
4. Bands change what a leader can do domestically (mirror of Honor gating foreign betrayal) and how the AI weighs repressive vs. liberal focus paths.

## Home value

Every government has a natural Tyranny level, `tyranny_home`, equal to the midpoint of its initialisation range:

```
tyranny_home = (min_tyranny + max_tyranny) / 2
```

`set_tyranny_range_from_government()` computes the range from the government group plus a leader-ideology offset. It is recomputed on every ruling-party change, on every civil-war victory, and by `reset_tyranny_for_new_ruler()`. The implemented table:

| Government group | Leader ideology | min..max | home |
|---|---|---|---|
| `democratic` | `liberalism`, `socialism` | -100..-80 | -90 |
| `democratic` | `conservatism`, `populism` | -75..-25 | -50 |
| `democratic` | (none of the above) | -100..-50 | -75 |
| `neutrality` | `anarchism` | -75..-25 | -50 |
| `neutrality` | `moderatism`, `centrism` | -50..0 | -25 |
| `neutrality` | `despotism`, `oligarchism` | 0..50 | 25 |
| `neutrality` | `japan_militarism_ideology` | 50..100 | 75 |
| `neutrality` | (none of the above) | -25..25 | 0 |
| `communism` | `anarchist_communism`, `buddhist_socialism` | -75..-25 | -50 |
| `communism` | `marxism`, `leninism` | 0..50 | 25 |
| `communism` | `stalinism`, `anti_revisionism` | 80..100 | 90 |
| `communism` | (none of the above) | 50..100 | 75 |
| `fascism` | any | 80..100 | 90 |

The last row of each group is the fall-through: `fascism` has no ideology sub-branch at all, so every fascist government rolls 80..100 and homes at 90. `set_tyranny_range_from_government()` leaves `min_tyranny` / `max_tyranny` as country variables, so any effect that needs the range again (the leader-change reroll) simply calls it before rolling.

## Programmatic surface

Same discipline as Honor: `$add_tyranny()` in `common/macros.hml` is the only writer, and it clamps, swaps the band trait through `update_country_leader_traits()`, logs `tyranny_*` lines under the `sandbox_log_tyranny` gate, and carries the `LocKey_tyranny_change_tt` tooltip. Do not write `&tyranny` directly outside `initialize_new_country_leader()`, `inherit_tyranny_on_ruling_party_change()` and `reset_tyranny_for_new_ruler()`.

- `set_tyranny_range_from_government()`: the table above; sets `min_tyranny`, `max_tyranny`, `tyranny_home`.
- `initialize_new_country_leader()`: rolls `tyranny = clamp(randi(min, max), -100, 100)`, sets `prev_tyranny = 999`, logs `tyranny_init`.
- `inherit_tyranny_on_ruling_party_change()`: `span = max_tyranny - min_tyranny`, `roll = randi(0, span)`, `roll += min_tyranny`, then `tyranny = clamp(0.5*old + 0.5*roll, -100, 100)`. The span and the half-sums go through temps because the engine rejects a bare arithmetic expression as a `randi` argument and inside `clamp(...)` with variables.
- `reset_tyranny_for_new_ruler()`: re-runs the range, then a full `randi(min, max)`; logs `tyranny_civil_war`.
- `update_tyranny_gain_monthly_factor()`: writes `tyranny_war_rate`, `tyranny_stability_rate` and the summed `tyranny_gain_monthly_factor`, and logs `tyranny_factor_change` when the previous week's factor differs (`prev_tyranny_gain_monthly_factor`).
- `remove_tyranny_leader_traits()` / `remove_honor_leader_traits()`: used by `initialize_new_country_leader()`, because civil-war copies can already carry the parent's traits.

## Band effects (leader traits)

One trait per band, swapped by `update_country_leader_traits()` exactly like the Honor traits. Modifiers:

- **Libertarian**: `research_speed_factor +0.05`, `trade_opinion_factor +0.10`, `drift_defence_factor -0.25`, `political_power_factor -0.10`, `foreign_subversive_activites +0.15` (vanilla spelling).
- **Liberal**: `research_speed_factor +0.02`, `trade_opinion_factor +0.05`, `drift_defence_factor -0.10`.
- **Moderate**: none.
- **Authoritarian**: `drift_defence_factor +0.10`, `political_power_factor +0.05`, `research_speed_factor -0.02`, `trade_opinion_factor -0.05`.
- **Despotic**: `drift_defence_factor +0.25`, `political_power_factor +0.10`, `research_speed_factor -0.05`, `trade_opinion_factor -0.10`, `resistance_growth +0.03`.

Intent: a despot keeps the ruling party in power by force and pushes decisions through faster, but pays in science, trade, and resistance in occupied territory. A libertarian is open and productive, but the party system is easy to shake from abroad.

## Changes from national focuses (main source)

Vanilla focus trees are tagged with `$add_tyranny(+/-X)` in `completion_reward`. Classification guide:

- **+20**: purges; secret police; one-party state; abolishing elections or the constitution; martial law; banning parties; arresting the opposition.
- **+10**: censorship and propaganda; militarisation of society; personality cult; centralisation; suppressing regional autonomy.
- **+5**: expanded executive powers; curbing unions; loyalist appointments.
- **-5**: coalition government; partial amnesty; relaxing censorship.
- **-10**: free elections; civil rights; press freedom; legalising parties; regional autonomy.
- **-20**: new democratic constitution; dissolving the secret police; decentralisation; general amnesty.

Calibration anchors:
- A democracy at -75 needs five +20 focuses to become Authoritarian.
- A single +20 focus is erased by drift in about 7 years (see below), so one-off focuses leave a visible but temporary mark; a lasting shift needs a sustained path or a change of government.

Which focuses in a tree carry a Tyranny reward is an authoring decision recorded in `completion_reward`; the numbers above are the full classification. The live distribution is not pinned here on purpose: it moves with every content pass, so read it from the tree (`grep -o '\$add_tyranny(...)' common/national_focus/*.include`), not from this document. The skew toward the repressive classes is the evidence behind the "Liberal focus coverage" item under "Second iteration".

Focuses that already change the ruling party (e.g. a fascist coup path) do not need a Tyranny reward: the leader-change rule below handles the jump.

## Systemic sources

### War: +0.25 per month, +0.50 if core territory is occupied

Any war (`has_war()`) adds `+0.25` per month (emergency powers). If at least one **owned core state is not controlled by us** the rate is `+0.50` instead (siege mentality). Offensive and defensive wars are treated the same.

This **replaced** the older `update_tyranny_gain_monthly_factor()` (offensive -0.25 / defensive +0.25), whose sign contradicted the model: an aggressive war must not liberalise the aggressor. The shipped body writes the two components into `tyranny_war_rate` and `tyranny_stability_rate` and stores the sum in `tyranny_gain_monthly_factor`, so the census can report the three numbers separately.

### Low stability: +0.25 per month

While stability is below `0.25` (`$compare(has_stability, "<", 0.25)`), the regime clamps down. `$compare` / `$has_stability` are the `hsd` stdlib macros over engine infix triggers (`hsl/macros/stdlib.hml`): HSL's own `a < b` always compiles to `check_variable`, which is wrong for `has_stability`, so the macro emits the raw infix form. Stacks with the war rate. The check reads the current value each week, so the term disappears the week stability recovers to 25% or more.

### Elections: -5

`on_new_term_election`: `$add_tyranny(-5, tyranny_election)`. The renewed mandate loosens the grip. Fires only for countries that hold elections, so democracies get a periodic downward nudge in addition to drift.

### Civil war and coup

No separate bonus. The new regime is rerolled by the leader-change rule below.

## Drift toward home

Every month Tyranny moves **0.25 toward `tyranny_home`**, in addition to the systemic sources:

```
drift = clamp(tyranny_home - tyranny, -0.25, 0.25)
tyranny_gain_monthly_factor = war_rate + stability_rate + drift
```

The sum is applied by `$add_tyranny(tyranny_gain_monthly_factor)` in `on_monthly`; the factor itself is recomputed weekly, so a war that ends mid-month stops contributing on the next week's number.

Consequences to preserve when tuning:
- Institutions gravitate to the norm of their ideology; a despotic democracy survives only while something keeps pushing it (war, focuses), and a liberalised fascist state rolls back without continued reform.
- Drift and war stack: a democracy in a long war with occupied cores still climbs at `0.50 - 0.25 = +0.25` net per month.
- At home value with no war and stable government, Tyranny is flat.

The tooltip `LocKey_honor_tt` displays `tyranny_gain_monthly_factor` beside `honor_gain_monthly_factor`; both show the combined value, formatted with `|.2=+` so the sign always reads.

## Leader change

Tyranny is a property of the regime more than of the person, so inertia is stronger than for Honor.

- Peaceful ruling-party change (`on_ruling_party_change`): `tyranny = 0.5 * tyranny + 0.5 * randi(min, max)` using the new government's row of the table; `tyranny_home` is recomputed. Institutions persist, ideology changes direction.
- Civil-war victory (`on_civil_war_end`, ROOT = winner): full `randi(min, max)` for the new government. The old apparatus is gone.
- Rebel tags and coup regimes are new countries: they are initialised lazily by the weekly `sandbox_initialized` guard (see `docs/gdd/Honor System.md`, "Leader change") and roll like a startup country. `on_coup_succeeded` is not used because its ROOT is the country the coup was staged against.

Then `update_country_leader_traits()` runs, and `reroll_leader_rival()` gives the new ruler a fresh personal rival (`docs/gdd/Rivals System.md`, "Ruler change"). `on_government_change` re-runs `update_country_leader_traits()` alone, because a government change that is not a ruling-party change must not reroll either axis.

## Gating focuses by band

Honor lets a leader betray neighbours; Tyranny lets a leader trample the country's own constitution.

- **Liberal or lower** (`tyranny < -25`): purge and secret-police focuses (the `+20` class) are unavailable. Shipped: `is_liberal_leader(no)` (Liberal or Libertarian, inverted) appended to `available` on the tagged focuses, e.g. `focus[id = AUS_strengthen_the_cabinet] { available: is_liberal_leader(no) }` in `common/national_focus/austria.include`.
- **Authoritarian or higher** (`tyranny >= 25`) - **deferred, blocked by tooling.** The intent is that unconstitutional government-change focuses ("seize power", "ban the party", "suspend elections") become available without the party-popularity `> 0.5` requirement that gates political paths. Those requirements live in vanilla `available` blocks, and the `.include` delta system can only *append* conditions to an existing block (AND); it cannot wrap or replace a vanilla condition in an `OR`. Until the compiler supports replacing a condition, this rule is expressed only through the AI tilt below (despots prefer the coup path when it is open to them). The trigger `is_authoritarian_leader` and its tooltips exist and are ready for the gate.
- Despotic gets no extra permissions; its distinction is in modifiers and AI weight.

Implementation: scripted triggers `is_authoritarian_leader` (Authoritarian or Despotic) / `is_liberal_leader` (Liberal or Libertarian) with `custom_override_tooltip` and `LocKey_is_*_leader_tt` / `_tt_NOT` in the style of `is_honored_leader`. The `available` append is the only shape the include DSL supports: `+available:` adds a sibling condition, which ANDs with the vanilla block.

## AI weighting

The existing mtth factors in `common/mtth/99_sandbox_factors_mtth.hsl` are used with the patterns of `docs/gdd/National Focuses.md`:

- Fork "repression vs. reform" (both options mutually exclusive **with each other**): partition shares with `$ai_high_tyranny_fork()` / `$ai_low_tyranny_fork()` (`0.5 + factor`, so a Moderate AI keeps a weight) and drop `$crossroad_modifier`; a middle option takes `$ai_medium_tyranny_fork()`. Only genuine Tyranny forks qualify; a liberal focus whose exclusive sibling is an *ideological* choice (e.g. `GER_reestablish_free_elections` vs `GER_revive_the_kaiserreich`) keeps the tilt and the party-popularity partition. Identified so far: `SIA_an_absolute_monarchy` / `SIA_a_constitutional_monarchy`, `POL_codify_national_unity` / `POL_draft_a_new_constitution`.
- A single repressive focus without a fork: `$ai_high_tyranny_tilt()` (`1 + mtth:high_tyranny_factor`); a single liberal focus: `$ai_low_tyranny_tilt()`.
- Unconstitutional government-change focuses: `$ai_high_tyranny_tilt()`, so despots stage coups and liberals go through elections.

The factors in `common/mtth/99_sandbox_factors_mtth.hsl` are aligned with the bands and are read through the macros of `docs/gdd/National Focuses.md`:

- `high_tyranny_factor` = `clamp((tyranny - 25) / 50, 0.0, 1.0)`: 0 at 25, 0.5 at 50, 1 at 75 and above.
- `low_tyranny_factor` = `clamp((-25 - tyranny) / 50, 0.0, 1.0)`: 0 at -25, 0.5 at -50, 1 at -75 and below.
- `medium_tyranny_factor` = `clamp(1 - (abs(tyranny) - 25) / 50, 0.0, 1.0)`: 1 inside `[-25, 25]`, 0.5 at `+/-50`, 0 at `+/-75`.

All three are `base(0)` plus one `is_sandbox_mode_on()` modifier, so outside sandbox mode they read 0. The `abs()` call is the engine's own function, not a macro.

## Implementation notes

Hooks (from vanilla `common/on_actions/00_on_actions.txt`):
- `on_new_term_election`: ROOT = country holding the election; `$add_tyranny(-5, tyranny_election)`.
- `on_ruling_party_change`: `inherit_honor_on_ruling_party_change()`, which calls `inherit_tyranny_on_ruling_party_change()` after the Honor roll.
- `on_civil_war_end` (ROOT winner, FROM loser): `reset_honor_for_new_ruler()`, which calls `reset_tyranny_for_new_ruler()`.
- `on_weekly`: `update_tyranny_gain_monthly_factor()` recomputes the factor; `update_country_leader_traits()` re-applies band traits; the `sandbox_initialized` guard lazily initialises late-created countries.
- `on_monthly`: `$add_tyranny(tyranny_gain_monthly_factor)` applies the factor.
- `on_government_change`: `update_country_leader_traits()` only (a government change that is not a ruling-party change does not reroll Tyranny).
- Not used: `on_coup_succeeded` (ROOT is the coup victim; the new regime is a new tag caught by the weekly initialisation guard).

Shipped changes to the shared effects file (`core/common/scripted_effects/99_sandbox_scripted_effects.hsl`):
- `update_country_leader_traits()` handles both systems in one body: an `if honor != prev_honor` branch and a parallel `if tyranny != prev_tyranny` branch guarded the same way, each swapping the five traits of its system and calling its own band logger.
- `update_tyranny_gain_monthly_factor()` is the war rate + stability rate + drift sum described above.
- `initialize_new_country_leader()` calls `set_tyranny_range_from_government()` (which also stores `tyranny_home`) and rerolls the leader's personal rival.
- `LocKey_honor_tt` formats both axes with `|.2=+`, so a positive Tyranny reads as "more repressive" and a positive Honor as "more honorable".

All Tyranny changes go through `$add_tyranny()` so that traits and tooltips stay consistent. Do not write `&tyranny` directly outside `initialize_new_country_leader()`, `inherit_tyranny_on_ruling_party_change()` and `reset_tyranny_for_new_ruler()`.

## Acceptance checklist

Log-first (the `sandbox_log_tyranny` gate), plus the monthly census line. A box may be ticked because the code pins the number (marked "code-verified") or because a run showed it.

- [x] A liberal democracy starts in `[-100, -80]`, `tyranny_home = -90`, trait Libertarian; other countries see no opinion change (opinion is out of scope for this iteration).
- [x] A fascist state at 90, at peace, stable: monthly factor 0.00.
- [ ] A democracy at -90 (its home value, so drift is 0) enters a war: factor `+0.25`; after an enemy occupies a core state the factor is `+0.50`. Once it has climbed to -70 with cores still occupied, drift kicks in and the factor is `+0.50 - 0.25 = +0.25`.
- [ ] A country at -70 with `tyranny_home = -90`, no war, stability 60%: factor `-0.25`, reaches -90 in 80 months and then stays flat.
- [x] Completing a +20 focus shows "Tyranny +20" in the focus tooltip, moves the value by exactly 20 (clamped), and swaps the trait if a band boundary is crossed.
- [x] Stability drops below 25% in peacetime: factor gains `+0.25`; it disappears the week stability recovers to 25% or more.
- [x] A democracy holds an election: -5 applied once, tooltip visible in the election event chain if one is shown.
- [x] Peaceful party change from democracy (-80) to fascism: new value is `0.5 * (-80) + 0.5 * randi(80, 100)`, i.e. in `[0, 10]`, trait Moderate, `tyranny_home = 90`, then climbs at 0.25 per month toward 90.
- [x] A fascist rebel tag created by a coup or civil war has, by the end of its first week, a value in `[80, 100]` and the Despotic trait; the country it split from keeps its own values.
- [ ] (Deferred with the Authoritarian gate) A leader at 30 can take a "seize power" focus with ruling party at 35% popularity; a leader at 20 cannot until popularity exceeds 50%.
- [ ] A leader at -30 cannot take a purge focus; at -20 the focus is available.
- [ ] In the `SIA_an_absolute_monarchy` / `SIA_a_constitutional_monarchy` fork a Despotic AI weighs the options 1.5 : 0.5, a Libertarian AI 0.5 : 1.5, a Moderate AI 0.5 : 0.5; no `$crossroad_modifier` is applied on top.
- [x] With the aligned breakpoints, `high_tyranny_factor` is 0 at 25, 0.5 at 50, 1 at 75; `low_tyranny_factor` mirrors it; `medium_tyranny_factor` is 1 at 0, 0.5 at +/-50, 0 at +/-75. Code-verified: those are the exact `clamp(...)` bodies in `common/mtth/99_sandbox_factors_mtth.hsl`.

## Second iteration (not blocking)

- **Liberal focus coverage.** The tagging pass is skewed toward repression: the `+20` and `+10` classes dominate the tree, `-10` is the only well-used liberal class, `-20` appears a handful of times, and the `+5` class is unused. Democracies can therefore move down only through drift and elections. A content pass over the vanilla trees for elections, constitutions, civil rights, press freedom, amnesties, and autonomy focuses is needed to tag the liberal side, and the `+5` / `-5` classes should be used for the softer items in the classification table.
- **Authoritarian gate** once the include system can replace a vanilla condition (see "Gating focuses by band").
- Opinion by band distance between two countries: same band +5, one band apart 0, two apart -5, three apart -10, opposite extremes -20. Gives democracies and despotisms a natural mutual dislike independent of ideology.
- Linking Tyranny to laws (total mobilisation, universal conscription) through `on_idea_added`, if that hook is confirmed to exist.

## Out of scope for this iteration

- Opinion, trade, or intel effects beyond the trait modifiers listed above.
- Tyranny effects on subjects or overlords.
- Player-facing decisions to raise or lower Tyranny outside focus trees.
- Historical-mode behaviour: everything here is sandbox-only.
