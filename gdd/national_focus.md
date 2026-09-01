
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

Each **mutually exclusive** focuses:
```
      +modifier:
        $crossroad_modifier(N)
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
      +modifier:
        $ai_war_support_modifier()
      +modifier:
        $ai_antagonism_modifier($TAG)
```

**Antagonism** with *multiple* countries:
```
      +modifier:
        $war_support_modifier()
      +modifier:
        antagonism = 1 - ($opinion_factor($TAG1) + $opinion_factor($TAG2)) / 2
        factor(antagonism)
        is_sandbox_mode_on()
```

### Military-industrial complex modifiers

```
      +modifier:
        $ai_mic_modifier()
```
