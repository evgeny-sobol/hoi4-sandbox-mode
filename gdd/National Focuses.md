
# Common blocks

## `ai_will_do`

### Basic modifiers

**Each** national focus:
```
    ai_will_do:
      +modifier:
        $ai_sandbox_modifier()
```

Each **root** in national focuses tree:
```
      +modifier:
        $root_modifier()
```

**Mutually exclusive** focuses that:
- are actually available at the same time (`N` is that concurrent count, not the size of the `mutually_exclusive` list)
- are **optional** (doctrine, MIC, "improve fighters vs bombers") rather than a political or story beat
- are not already partitioned by party-popularity weights
- are not already partitioned by Tyranny factors (a "repression vs. reform" fork)
- are not already gated by a party-popularity `available` check of `> 0.5`
- are not already gated by conflicting `has_government` checks (different ruling ideologies cannot appear at once)
- **none** of the concurrent options has `FOCUS_FILTER_POLITICAL` or `FOCUS_FILTER_POLITICAL_CHARACTER` in `search_filters` (if any sibling has either filter, drop `$crossroad_modifier` from the whole exclusive group — e.g. `GER_heed_von_neuraths_concerns` / `GER_reorganize_the_wehrmacht`)
```
      +modifier:
        $crossroad_modifier(N)
```

`$ai_sandbox_modifier()` is `factor(0)` **and** `add(40)` in the **same** `modifier` block. Do not split them across modifiers: the engine multiplies every `factor` into the final weight, so a standalone `factor(0)` leaves the focus at 0 in aiview even after a later `add(40)` fires. To gate a root on a completed political focus, put `factor(0)` + `add(N)` in one modifier with that `has_completed_focus` trigger, and a separate `factor(0)` only in the complementary `NOT` case.

### Party-popularity modifiers

Weight a focus by `mtth:democracy_factor`, `mtth:monarchy_factor`, `mtth:communism_factor`, and/or `mtth:fascism_factor` when the AI's choice is a **political path**: the options stand for different ruling ideologies or party constituencies.

Do **not** use these factors for doctrine, MIC, or pure diplomacy forks.

If `available` already requires a party above 50% (`democratic > 0.5`, `neutrality > 0.5`, `communism > 0.5`, or `fascism > 0.5`), skip both `$crossroad_modifier` and the party-popularity factor: the game has already filtered the choice.

The same applies when exclusive options require different ruling ideologies (`has_government`): they are never concurrent, so `$crossroad_modifier` is unnecessary, and a party-popularity factor for that same ideology adds nothing.

**Unconstitutional** government-change focuses ("seize power", "ban the party", "suspend elections", coups) get `$ai_high_tyranny_tilt()` from "Domestic-politics modifiers" so despots prefer the coup and liberals wait for the ballot. The intended Authoritarian bypass of the popularity gate (`gdd/Tyranny System.md`, "Gating focuses by band") is **deferred**: the popularity checks live in vanilla `available` blocks, and an include can only append conditions to an existing block, not wrap a vanilla condition in an `OR`. Do not try to emulate it with `+available:`; wait for a replace capability in the compiler.

Assign each option the parties that support it.

Scale the shares so the exclusive set sums to `N` (each option averages the weight of a singleton). Drop `$crossroad_modifier`.

**Disjoint** party sets (no party supports more than one option): sum of supporting factors, times `N`:

```
      +modifier:
        f = (mtth:democracy_factor + mtth:communism_factor) * 2
        factor(f)
        is_sandbox_mode_on()
```

```
      +modifier:
        f = (mtth:monarchy_factor + mtth:fascism_factor) * 2
        factor(f)
        is_sandbox_mode_on()
```

**Overlapping** party sets (the same party supports more than one option): supporting parties in the numerator; in the denominator count each party once per option that claims it; multiply by `N`:

```
      +modifier:
        f = (mtth:democracy_factor + mtth:communism_factor) /
          (mtth:democracy_factor + 2 * mtth:monarchy_factor + mtth:communism_factor + mtth:fascism_factor) * 3
        factor(f)
        is_sandbox_mode_on()
```

A focus that only **tilts** toward a party, without partitioning a fork, uses a boost instead of a share. Do not add `$crossroad_modifier` on the same exclusive set: `1 + factor` already sits at singleton weight or above.

```
      +modifier:
        f = 1 + mtth:communism_factor
        factor(f)
        is_sandbox_mode_on()
```

### Diplomacy modifiers

**Cooperation** with *single* country (for focuses leading to alliances). Rivals (`gdd/Rivals System.md`) block cooperation: the `available` gate uses `$not_rival_of_PREV($TAG)` — `$is_rival_of()` (at war, or either side lists the other in `rivals[]`) wrapped in the `country_exists` guard so tag aliases are safe — and the AI weight is zeroed when the target is in our `rivals[]`. The rival opinion modifiers (−20/−10) already lower `$ai_cooperation_modifier`, so no extra rivalry factor is needed here.
```
    available:
      $not_rival_of_PREV($TAG)
    ai_will_do:
      +modifier:
        $ai_cooperation_modifier($TAG)
      +modifier:
        factor(0)
        $TAG in rivals[]
        is_sandbox_mode_on()
```
Use `+available:` if the vanilla focus has no `available` block.

**Cooperation** with *two* countries:
```
    available:
      $not_rival_of_PREV($TAG1)
      $not_rival_of_PREV($TAG2)
    ai_will_do:
      +modifier:
        cooperation = 1 + ($opinion_factor($TAG1) + $opinion_factor($TAG2)) / 2
        factor(cooperation)
        is_sandbox_mode_on()
      +modifier:
        factor(0)
        or:
          $TAG1 in rivals[]
          $TAG2 in rivals[]
        is_sandbox_mode_on()
```

**Cooperation** with *three or more* countries (faction-building invitations such as `USA_hemisphere_defense`, `ITA_south_american_alliances`, `GER_safeguard_the_baltic`, `SOV_our_slavic_commitments`): **no** rival gate and **no** `factor(0)`. National rivals are picked from neighbours and the same continent, so with many invitees one of them is almost always a rival and a gate would lock the focus for the player and the AI alike. Keep only the averaged cooperation factor; the rival opinion modifiers pull it down, and the rival's own AI declines the alliance (`alliance −200`).
```
    ai_will_do:
      +modifier:
        cooperation = 1 + ($opinion_factor($TAG1) + $opinion_factor($TAG2) +
          $opinion_factor($TAG3)) / 3
        factor(cooperation)
        is_sandbox_mode_on()
```

Focuses that lead to war against a **friend** (ally, guarantor, or non-aggression-pact partner; `$is_friend_of()`) are **betrayal focuses**. Never gate them with `is_honored_leader(no)` directly: it ignores the Honor tiers. Two macros in `macros.hml` carry the AI side (`gdd/Honor System.md`, "AI weighting"); the factor is `clamp((25 - honor) / 125, 0, 1)`, so a Treacherous AI betrays at full weight and an Inglorious AI near 25 almost never does. A focus whose targets are not friends is unaffected because the trigger fails and the modifier does not apply:

```
macro ai_betrayal_modifier():
  betrayal = clamp((25 - honor) / 125, 0, 1)
  factor(betrayal)
  is_sandbox_mode_on()

macro ai_betrayal_modifier_vs(_tag_):
  $ai_betrayal_modifier()
  country_exists(_tag_)
  _tag_->is_friend_of_PREV()
```

The Honor penalty itself is never written in the focus block. Vanilla focuses remove pacts with their own `diplomatic_relation`, which the include cannot replace; the −50 is charged by `on_declare_war` through the weekly snapshot and the 6-month dropped-obligation window (`gdd/Honor System.md`, "Honor losses"). Only sandbox-authored focuses that remove a pact use `$break_non_aggression_pact_with($TAG)`, which applies `$add_honor(-50)` directly. Wars on guaranteed countries and faction exits are likewise charged by on_actions.

**Antagonism** with *single* country (for focus leading to wars). `can_PREV_get_wargoal_on_THIS` is Honor-tiered (see `gdd/Honor System.md`): a NAP requires Inglorious or worse, a guarantee Dishonorable or worse, a faction ally Treacherous; a non-friend is always allowed.
```
    available:
      $TAG->can_PREV_get_wargoal_on_THIS()
    ai_will_do:
      +modifier:
        $ai_war_support_modifier()
      +modifier:
        $ai_antagonism_modifier($TAG)
      +modifier:
        $ai_rivalry_modifier($TAG)
      +modifier:
        $ai_betrayal_modifier_vs($TAG)
```
Use `+available:` if the vanilla focus has no `available` block.

`$ai_rivalry_modifier($TAG)` (`gdd/Rivals System.md`, "National focuses") is `factor(1 + rivalry_vs / 50)`, where `rivalry_vs` is the highest `rivalry` among our slots holding `TAG` (0 for a non-rival): ×1 for a stranger, ×2 for a rival at 50, ×3 at Feud. It sits beside, not instead of, `$ai_antagonism_modifier`: the rival opinion modifiers already raise antagonism, the rivalry factor adds the intensity that opinion cannot express.

**Antagonism** with *multiple* countries:
```
    available:
      $TAG1->can_PREV_get_wargoal_on_THIS()
      $TAG2->can_PREV_get_wargoal_on_THIS()
    ai_will_do:
      +modifier:
        $ai_war_support_modifier()
      +modifier:
        antagonism = 1 - ($opinion_factor($TAG1) + $opinion_factor($TAG2)) / 2
        factor(antagonism)
        is_sandbox_mode_on()
      +modifier:
        $ai_rivalry_modifier_max($TAG1, $TAG2)
      +modifier:
        $ai_betrayal_modifier()
        or:
          $TAG1->is_friend_of_PREV()
          $TAG2->is_friend_of_PREV()
```
Use `+available:` if the vanilla focus has no `available` block. `$ai_rivalry_modifier_max` takes the highest `rivalry` over both targets, so a focus against one rival and one stranger weighs like a focus against the rival alone.

**Antagonism** with *three or more* countries: the macros are fixed-arity, so spell the same modifier out with one `$rivalry_vs_into($TAG)` line per target (the macro only raises `rivalry_vs`, so the lines compose):
```
      +modifier:
        rivalry_vs = 0
        $rivalry_vs_into($TAG1)
        $rivalry_vs_into($TAG2)
        $rivalry_vs_into($TAG3)
        f = 1 + rivalry_vs / 50
        factor(f)
        is_sandbox_mode_on()
```
Every `$ai_antagonism_modifier` and every multi-target `antagonism = …` block must have a rivalry modifier next to it, shared trees (`*_shared`, `*_joint`, `TSR_*`) included.

**Antagonism** with *owners of listed states* (the countries are not fixed tags). Weekly `update_<TAG>_national_focuses()` stores **one owner per state** (the same country may appear more than once, so the focus tooltip names every state owner). The AI factor averages unique other-country owners only. Then the focus uses those slots like `SOV_the_rightful_heir_to_the_empire` / `GER_demand_slovenia`:

```
    available:
      var:focus_targets[0]->can_PREV_get_wargoal_on_THIS()
      var:focus_targets[1]->can_PREV_get_wargoal_on_THIS()
    ai_will_do:
      +modifier:
        $ai_war_support_modifier()
      +modifier:
        factor(focus_antagonism)
        is_sandbox_mode_on()
      +modifier:
        $ai_betrayal_modifier()
        any_other_country:
          THIS in ROOT.focus_targets[]
          is_friend_of_ROOT()
```

If there is only one possible owner, a single `var:focus_targets[0]->can_PREV_get_wargoal_on_THIS()` is enough. Use `+available:` if the vanilla focus has no `available` block. State-owner focuses take rivalry into account through opinion only; a rivalry factor over dynamic targets is a follow-up (`gdd/Rivals System.md`, "Out of scope").

**Antagonism** with a *tag alias*. Some tags used by vanilla focus trees are not countries but aliases from `common/country_tag_aliases/tag_aliases.txt` (`SPA`, `SPB`, `SPC`, `SPD`, `VIC`, `SOU`, `SOB`, `SOS`, `SOT`, `SOP`, `BUF`, `BUZ`, `FGR`, `FNO`, `MOT`, `RDS`, `RSI`, `SB1`–`SB4`). An alias resolves to a country only while its trigger holds (e.g. `SOS` is the Stalinist half of a Soviet civil war); otherwise it is `None`, and entering it as a scope (`$SOS->…`) logs `Invalid Scope` in `error.log` every time the block is evaluated. Ordinary tags are safe even when the country does not exist on the map. For aliases, never enter the scope unguarded:
```
    available:
      $can_get_wargoal_on($ALIAS)         # OR: NOT country_exists / ALIAS->can_PREV_get_wargoal_on_THIS
    ai_will_do:
      +modifier:
        $ai_betrayal_modifier_vs($ALIAS)  # already checks country_exists before the scope
      +modifier:
        $ai_betrayal_modifier()
        or:
          $TAG1->is_friend_of_PREV()
          and:
            country_exists($ALIAS)
            $ALIAS->is_friend_of_PREV()
```
Value forms (`$opinion_factor($ALIAS)`, `has_war_with = ALIAS`) do not enter the scope and need no guard. Trigger blocks evaluate in order and stop at the first failing (`and`) or passing (`or`) trigger, so `country_exists` must come **before** the scope.

### Domestic-politics modifiers (Tyranny)

Repressive and liberal focuses are tagged with `$add_tyranny(±X)` in `completion_reward` according to the classification in `gdd/Tyranny System.md` ("Changes from national focuses"); the gates and weights below are the focus-side counterpart. The mtth factors `low_tyranny_factor`, `medium_tyranny_factor`, and `high_tyranny_factor` peak in the Libertarian / Moderate / Despotic bands and reach zero one band away.

**Gate**: purge and secret-police focuses (the `+20` class) are unavailable to Liberal-or-lower leaders (`gdd/Tyranny System.md`, "Gating focuses by band"):

```
    available:
      +is_liberal_leader(no)
```

The Authoritarian bypass for unconstitutional government-change focuses is deferred (see "Party-popularity modifiers"); such focuses get only the tilt below.

**Fork** "repression vs. reform": both options are mutually exclusive *with each other* and differ in repressiveness rather than ideology (`SIA_an_absolute_monarchy` / `SIA_a_constitutional_monarchy`, `POL_codify_national_unity` / `POL_draft_a_new_constitution`). Drop `$crossroad_modifier`. Do **not** multiply by `N` the way party-popularity shares do: between −25 and 25 both outer factors are 0, so a Moderate AI would have no weight at all; the `0.5 +` inside the macros keeps the fork open (Despotic 1.5 : 0.5, Moderate 0.5 : 0.5).

```
      +modifier:
        $ai_high_tyranny_fork()
```

```
      +modifier:
        $ai_low_tyranny_fork()
```

With a third, middle-of-the-road option give it `$ai_medium_tyranny_fork()` (bare `mtth:medium_tyranny_factor`; some factor is then always non-zero, so the `0.5 +` variants are not needed and the outer options use the bare factors).

A liberal focus whose exclusive sibling is an **ideological** choice (`GER_reestablish_free_elections` vs `GER_revive_the_kaiserreich`, `PER_free_elections` vs `PER_islamic_restoration`) is not a Tyranny fork: keep the party-popularity partition and use a tilt.

**Tilt**: a single repressive focus without a fork, or an unconstitutional government-change focus:

```
      +modifier:
        $ai_high_tyranny_tilt()
```

A single liberal focus uses `$ai_low_tyranny_tilt()`. The macros are `1 + mtth:high_tyranny_factor` / `1 + mtth:low_tyranny_factor`.

Do **not** combine Tyranny factors with party-popularity factors on the same fork unless the options differ in both ideology and repressiveness; in that case multiply the two shares.

### Military-industrial complex modifiers

```
      +modifier:
        $ai_mic_modifier()
```
