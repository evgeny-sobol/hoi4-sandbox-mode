# Tyranny

Tyranny is a per-regime measure of how concentrated and repressive the ruler's power is: how much the country is governed by coercion rather than consent.

Tyranny is a trade-off, not a good/bad scale. High Tyranny buys control (party drift defence, political power, a firm grip during war) at the price of openness (research, trade, resistance in occupied land). Low Tyranny is the mirror image: open and productive, but easy to destabilise from outside.

Tyranny is **not**:
- Honor (keeping promises to other countries; see `gdd/Honor System.md`). The two are orthogonal: a liberal democracy can be treacherous, a despot can be a man of his word.
- Ideology. Ideology sets where Tyranny naturally settles, but every government can be pushed far from its home value.
- Rivalry (whom we want to fight; see `gdd/Rivals System.md`). The only link runs the other way: an Authoritarian or Despotic ruler's personal rivalry (`rivals[0]`) grows +1 per month faster, a Libertarian or Liberal ruler's −1 slower.

Sandbox-only: every rule below runs under `is_sandbox_mode_on()`.

## Scale and bands

`tyranny` is a country variable in `[-100.0, 100.0]`, clamped by `$add_tyranny()` in `common/macros.hml`.

Bands (same thresholds as Honor):
- `< -75` Libertarian (`libertarian_leader`)
- `< -25` Liberal (`liberal_leader`)
- `< 25` Moderate (`moderate_leader`, no modifiers)
- `< 75` Authoritarian (`authoritarian_leader`)
- `>= 75` Despotic (`despotic_leader`)

Initial value for a fresh sandbox leader: `randi(min_tyranny, max_tyranny)` from the government/leader-ideology table in `initialize_new_country_leader()` (`common/scripted_effects/99_sandbox_scripted_effects.hsl`). The table is kept as is.

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

computed in the same function that rolls the initial value, from the same table (e.g. liberal democracy `(-100 + -80) / 2 = -90`, fascism `90`, centrist neutrality `-25`). Recomputed on every ruling-party change.

## Band effects (leader traits)

One trait per band, swapped by `update_country_leader_traits()` exactly like the Honor traits. Modifiers:

- **Libertarian**: `research_speed_factor +0.05`, `trade_opinion_factor +0.10`, `drift_defence_factor -0.25`, `political_power_factor -0.10`, `foreign_subversive_activites +0.25` (vanilla spelling).
- **Liberal**: `research_speed_factor +0.02`, `trade_opinion_factor +0.05`, `drift_defence_factor -0.10`.
- **Moderate**: none.
- **Authoritarian**: `drift_defence_factor +0.10`, `political_power_factor +0.05`, `research_speed_factor -0.02`, `trade_opinion_factor -0.05`.
- **Despotic**: `drift_defence_factor +0.25`, `political_power_factor +0.10`, `research_speed_factor -0.05`, `trade_opinion_factor -0.10`, `resistance_growth +0.10`.

Intent: a despot keeps the ruling party in power by force and pushes decisions through faster, but pays in science, trade, and resistance in occupied territory. A libertarian is open and productive, but the party system is easy to shake from abroad.

## Changes from national focuses (main source)

Vanilla focus trees are tagged with `$add_tyranny(±X)` in `completion_reward`. Classification guide:

- **+20**: purges; secret police; one-party state; abolishing elections or the constitution; martial law; banning parties; arresting the opposition.
- **+10**: censorship and propaganda; militarisation of society; personality cult; centralisation; suppressing regional autonomy.
- **+5**: expanded executive powers; curbing unions; loyalist appointments.
- **−5**: coalition government; partial amnesty; relaxing censorship.
- **−10**: free elections; civil rights; press freedom; legalising parties; regional autonomy.
- **−20**: new democratic constitution; dissolving the secret police; decentralisation; general amnesty.

Calibration anchors:
- A democracy at −75 needs five +20 focuses to become Authoritarian.
- A single +20 focus is erased by drift in about 7 years (see below), so one-off focuses leave a visible but temporary mark; a lasting shift needs a sustained path or a change of government.

Focuses that already change the ruling party (e.g. a fascist coup path) do not need a Tyranny reward: the leader-change rule below handles the jump.

## Systemic sources

### War: +0.25 per month, +0.50 if core territory is occupied

Any war (`has_war()`) adds `+0.25` per month (emergency powers). If at least one core state is controlled by an enemy, the rate is `+0.50` instead (siege mentality). Offensive and defensive wars are treated the same.

This **replaces** the current `update_tyranny_gain_monthly_factor()` (offensive −0.25 / defensive +0.25), whose sign contradicts the model: an aggressive war must not liberalise the aggressor.

### Low stability: +0.25 per month

While `has_stability < 0.25`, the regime clamps down. Stacks with the war rate.

### Elections: −5

`on_new_term_election`: the renewed mandate loosens the grip. Fires only for countries that hold elections, so democracies get a periodic downward nudge in addition to drift.

### Civil war and coup

No separate bonus. The new regime is rerolled by the leader-change rule below.

## Drift toward home

Every month Tyranny moves **0.25 toward `tyranny_home`**, in addition to the systemic sources:

```
drift = clamp(tyranny_home - tyranny, -0.25, 0.25)
tyranny_gain_monthly_factor = war_rate + stability_rate + drift
```

Consequences to preserve when tuning:
- Institutions gravitate to the norm of their ideology; a despotic democracy survives only while something keeps pushing it (war, focuses), and a liberalised fascist state rolls back without continued reform.
- Drift and war stack: a democracy in a long war with occupied cores still climbs at `0.50 − 0.25 = +0.25` net per month.
- At home value with no war and stable government, Tyranny is flat.

The tooltip `LocKey_honor_tt` already displays `tyranny_gain_monthly_factor`; it must show the combined value.

## Leader change

Tyranny is a property of the regime more than of the person, so inertia is stronger than for Honor.

- Peaceful ruling-party change (`on_ruling_party_change`): `tyranny = 0.5 * tyranny + 0.5 * randi(min, max)` using the new government's row of the table; `tyranny_home` is recomputed. Institutions persist, ideology changes direction.
- Civil-war victory (`on_civil_war_end`, ROOT = winner): full `randi(min, max)` for the new government. The old apparatus is gone.
- Rebel tags and coup regimes are new countries: they are initialised lazily by the weekly `sandbox_initialized` guard (see `gdd/Honor System.md`, "Leader change") and roll like a startup country. `on_coup_succeeded` is not used because its ROOT is the country the coup was staged against.

Then `update_country_leader_traits()` runs as today.

## Gating focuses by band

Honor lets a leader betray neighbours; Tyranny lets a leader trample the country's own constitution.

- **Liberal or lower** (`tyranny < -25`): purge and secret-police focuses (the `+20` class) are unavailable. Implemented: `is_liberal_leader(no)` in `available`.
- **Authoritarian or higher** (`tyranny >= 25`) — **deferred, blocked by tooling.** The intent is that unconstitutional government-change focuses ("seize power", "ban the party", "suspend elections") become available without the party-popularity `> 0.5` requirement that gates political paths. Those requirements live in vanilla `available` blocks, and the `.include` delta system can only *append* conditions to an existing block (AND); it cannot wrap or replace a vanilla condition in an `OR`. Until the compiler supports replacing a condition, this rule is expressed only through the AI tilt below (despots prefer the coup path when it is open to them). The trigger `is_authoritarian_leader` and its tooltips exist and are ready for the gate.
- Despotic gets no extra permissions; its distinction is in modifiers and AI weight.

Implementation: scripted triggers `is_authoritarian_leader` / `is_liberal_leader` with `custom_override_tooltip` in the style of `is_honored_leader`.

## AI weighting

The existing mtth factors in `common/mtth/99_sandbox_factors_mtth.hsl` are used with the patterns of `gdd/National Focuses.md`:

- Fork "repression vs. reform" (both options mutually exclusive **with each other**): partition shares with `$ai_high_tyranny_fork()` / `$ai_low_tyranny_fork()` (`0.5 + factor`, so a Moderate AI keeps a weight) and drop `$crossroad_modifier`; a middle option takes `$ai_medium_tyranny_fork()`. Only genuine Tyranny forks qualify; a liberal focus whose exclusive sibling is an *ideological* choice (e.g. `GER_reestablish_free_elections` vs `GER_revive_the_kaiserreich`) keeps the tilt and the party-popularity partition. Identified so far: `SIA_an_absolute_monarchy` / `SIA_a_constitutional_monarchy`, `POL_codify_national_unity` / `POL_draft_a_new_constitution`.
- A single repressive focus without a fork: `$ai_high_tyranny_tilt()` (`1 + mtth:high_tyranny_factor`); a single liberal focus: `$ai_low_tyranny_tilt()`.
- Unconstitutional government-change focuses: `$ai_high_tyranny_tilt()`, so despots stage coups and liberals go through elections.

Align the factor breakpoints with the bands (currently zero at ±34, peak at ±100):
- `low_tyranny_factor`: 1 at `tyranny <= -75`, linear to 0 at `tyranny >= -25`.
- `high_tyranny_factor`: 1 at `tyranny >= 75`, linear to 0 at `tyranny <= 25`.
- `medium_tyranny_factor`: 1 inside `[-25, 25]`, linear to 0 at `±75`.

## Implementation notes

Hooks (from vanilla `common/on_actions/00_on_actions.txt`; verify scopes marked "check"):
- `on_new_term_election`: ROOT = country holding the election.
- `on_ruling_party_change`, `on_civil_war_end` (ROOT winner, FROM loser).
- `on_weekly` for recomputing the monthly factor and for lazy initialisation of late-created countries, `on_monthly` for applying the factor (existing).
- Not used: `on_coup_succeeded` (ROOT is the coup victim; the new regime is a new tag and is caught by the weekly initialisation guard).

Changes to existing code:
- `update_country_leader_traits()` currently handles only Honor traits although `$add_tyranny` calls it. Add a parallel branch guarded by `tyranny != prev_tyranny` that swaps the five Tyranny traits.
- `update_tyranny_gain_monthly_factor()` is rewritten to war rate + stability rate + drift.
- `initialize_new_country_leader()` additionally stores `tyranny_home`; the same table must be reusable for the leader-change reroll (extract the range computation into its own effect).
- Tooltip `LocKey_honor_tt` formats Tyranny with `|.2-` and Honor with `|.2+`; unify so that a positive sign reads as "more repressive" for Tyranny as well.

All Tyranny changes go through `$add_tyranny()` so that traits and tooltips stay consistent. Do not write `&tyranny` directly outside initialisation and the leader-change rule.

## Acceptance checklist

- A liberal democracy starts in `[-100, -80]`, `tyranny_home = -90`, trait Libertarian; other countries see no opinion change (opinion is out of scope for this iteration).
- A fascist state at 90, at peace, stable: monthly factor 0.00.
- A democracy at −90 (its home value, so drift is 0) enters a war: factor `+0.25`; after an enemy occupies a core state the factor is `+0.50`. Once it has climbed to −70 with cores still occupied, drift kicks in and the factor is `+0.50 − 0.25 = +0.25`.
- A country at −70 with `tyranny_home = -90`, no war, stability 60%: factor `−0.25`, reaches −90 in 80 months and then stays flat.
- Completing a +20 focus shows "Tyranny +20" in the focus tooltip, moves the value by exactly 20 (clamped), and swaps the trait if a band boundary is crossed.
- Stability drops below 25% in peacetime: factor gains `+0.25`; it disappears the week stability recovers to 25% or more.
- A democracy holds an election: −5 applied once, tooltip visible in the election event chain if one is shown.
- Peaceful party change from democracy (−80) to fascism: new value is `0.5 · (−80) + 0.5 · randi(80, 100)`, i.e. in `[0, 10]`, trait Moderate, `tyranny_home = 90`, then climbs at 0.25 per month toward 90.
- A fascist rebel tag created by a coup or civil war has, by the end of its first week, a value in `[80, 100]` and the Despotic trait; the country it split from keeps its own values.
- (Deferred with the Authoritarian gate) A leader at 30 can take a "seize power" focus with ruling party at 35% popularity; a leader at 20 cannot until popularity exceeds 50%.
- A leader at −30 cannot take a purge focus; at −20 the focus is available.
- In the `SIA_an_absolute_monarchy` / `SIA_a_constitutional_monarchy` fork a Despotic AI weighs the options 1.5 : 0.5, a Libertarian AI 0.5 : 1.5, a Moderate AI 0.5 : 0.5; no `$crossroad_modifier` is applied on top.
- With the aligned breakpoints, `high_tyranny_factor` is 0 at 25, 0.5 at 50, 1 at 75; `low_tyranny_factor` mirrors it; `medium_tyranny_factor` is 1 at 0, 0.5 at ±50, 0 at ±75.

## Second iteration (not blocking)

- **Liberal focus coverage.** The first tagging pass is skewed toward repression (+20 ×37, +10 ×41 against −10 ×16, −20 ×5, −5 ×1; the ±5 classes are almost unused). Democracies can therefore move down only through drift and elections. A content pass over the vanilla trees for elections, constitutions, civil rights, press freedom, amnesties, and autonomy focuses is needed to tag the liberal side, and the `+5` / `−5` classes should be used for the softer items in the classification table.
- **Authoritarian gate** once the include system can replace a vanilla condition (see "Gating focuses by band").
- Opinion by band distance between two countries: same band +5, one band apart 0, two apart −5, three apart −10, opposite extremes −20. Gives democracies and despotisms a natural mutual dislike independent of ideology.
- Linking Tyranny to laws (total mobilisation, universal conscription) through `on_idea_added`, if that hook is confirmed to exist.

## Out of scope for this iteration

- Opinion, trade, or intel effects beyond the trait modifiers listed above.
- Tyranny effects on subjects or overlords.
- Player-facing decisions to raise or lower Tyranny outside focus trees.
- Historical-mode behaviour: everything here is sandbox-only.
