
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
- are not already partitioned by disjoint party-popularity weights
- are not already gated by a party-popularity `available` check of `> 0.5`
- are not already gated by conflicting `has_government` checks (different ruling ideologies cannot appear at once)
```
      +modifier:
        $crossroad_modifier(N)
```

### Party-popularity modifiers

Weight a focus by `mtth:democracy_factor`, `mtth:monarchy_factor`, `mtth:communism_factor`, and/or `mtth:fascism_factor` when the AI's choice is a **political path**: the options stand for different ruling ideologies or party constituencies.

Do **not** use these factors for doctrine, MIC, or pure diplomacy forks.

If `available` already requires a party above 50% (`democratic > 0.5`, `neutrality > 0.5`, `communism > 0.5`, or `fascism > 0.5`), skip both `$crossroad_modifier` and the party-popularity factor: the game has already filtered the choice.

The same applies when exclusive options require different ruling ideologies (`has_government`): they are never concurrent, so `$crossroad_modifier` is unnecessary, and a party-popularity factor for that same ideology adds nothing.

Assign each option the parties that support it.

**Disjoint** party sets (no party supports more than one option): drop `$crossroad_modifier`. Use the sum of the supporting factors (they already add up across the set):

```
      +modifier:
        f = mtth:democracy_factor + mtth:communism_factor
        factor(f)
        is_sandbox_mode_on()
```

```
      +modifier:
        f = mtth:monarchy_factor + mtth:fascism_factor
        factor(f)
        is_sandbox_mode_on()
```

**Overlapping** party sets (the same party supports more than one option): keep `$crossroad_modifier(N)`. Put supporting parties in the numerator; in the denominator count each party once per option that claims it. Multiply by `N` so the shares remain the relative weights after `1/N`:

```
      +modifier:
        $crossroad_modifier(3)
      +modifier:
        f = (mtth:democracy_factor + mtth:communism_factor) /
          (mtth:democracy_factor + 2 * mtth:monarchy_factor + mtth:communism_factor + mtth:fascism_factor) * 3
        factor(f)
        is_sandbox_mode_on()
```

A focus that only **tilts** toward a party, without partitioning a fork, uses a boost instead of a share:

```
      +modifier:
        f = 1 + mtth:communism_factor
        factor(f)
        is_sandbox_mode_on()
```

### Diplomacy modifiers

**Cooperation** with *single* country (for focuses leading to alliances):
```
      +modifier:
        $ai_cooperation_modifier($TAG)
```

**Cooperation** with *multiple* countries:
```
      +modifier:
        cooperation = 1 + ($opinion_factor($TAG1) + $opinion_factor($TAG2)) / 2
        factor(cooperation)
        is_sandbox_mode_on()
```

**Antagonism** with *single* country (for focus leading to wars):
```
    available:
      $TAG->can_PREV_get_wargoal_on_THIS()
    ai_will_do:
      +modifier:
        $ai_war_support_modifier()
      +modifier:
        $ai_antagonism_modifier($TAG)
```
Use `+available:` if the vanilla focus has no `available` block.

**Antagonism** with *multiple* countries:
```
    available:
      +or:
        is_honored_leader(no)
        and:
          $TAG1->is_friend_of_PREV(no)
          $TAG2->is_friend_of_PREV(no)
    ai_will_do:
      +modifier:
        $ai_war_support_modifier()
      +modifier:
        antagonism = 1 - ($opinion_factor($TAG1) + $opinion_factor($TAG2)) / 2
        factor(antagonism)
        is_sandbox_mode_on()
```
Use `+available:` / `or:` if the vanilla focus has no `available` block.

**Antagonism** with *owners of listed states* (the countries are not fixed tags). Weekly `update_<TAG>_national_focuses()` stores **one owner per state** (the same country may appear more than once, so the focus tooltip names every state owner). The AI factor averages unique other-country owners only. Then the focus uses those slots like `SOV_the_rightful_heir_to_the_empire` / `GER_demand_slovenia`:

```
    available:
      +or:
        is_honored_leader(no)
        and:
          var:focus_targets[0]->is_friend_of_PREV(no)
          var:focus_targets[1]->is_friend_of_PREV(no)
    ai_will_do:
      +modifier:
        $ai_war_support_modifier()
      +modifier:
        factor(focus_antagonism)
        is_sandbox_mode_on()
```

If there is only one possible owner, use `var:focus_targets[0]->can_PREV_get_wargoal_on_THIS()` instead of the honored-leader OR. Use `+available:` / `or:` if the vanilla focus has no `available` block.

### Military-industrial complex modifiers

```
      +modifier:
        $ai_mic_modifier()
```
