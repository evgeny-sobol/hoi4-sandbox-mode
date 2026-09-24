# 10 - Repick is deterministic (`eligible[0]`), not random

Status: needs-triage
Type: bug
Blocked by: none

## Problem

`docs/gdd/Scenarios.md:117` (Acceptance checklist) expects "random repicks", but
`sandbox_scenario_maybe_repick` takes the **first** eligible arc instead of rolling:

`common/scripted_effects/99_sandbox_scenarios.hsl:168-171`:

```hsl
 168:     if eligible[].size() == 0:
 169:       $sandbox_log_sc(sc_repick, none_eligible)
 170:     else:
 171:       global.&sandbox_scenario = eligible[0]   # <- always the lowest-numbered arc
```

Contrast with the initial pick, which does roll:

```hsl
 113:       eligible_max = eligible[].size() - 1
 114:       roll = randi(0, eligible_max)
 115:       global.&sandbox_scenario = eligible[roll]
```

## Session evidence

Both repicks in the session went to the lowest-numbered remaining arc, in order:

```
HAI sc_repick axis     sc=1 t=36   # sov_south derailed, eligible [1,3,4,5,6]
HAI sc_repick japanese sc=3 t=49   # axis derailed,      eligible [3,4,5,6]
```

`docs/gdd/Scenarios.md:142-145` records the same pattern in an earlier observer session
(`japanese` -> `axis` repick), so this is reproducible, not a one-off.

## Impact

Once the first arc derails, every later arc in the session is drawn in ascending id order, so a
long session walks `axis`, `japanese`, `italian`, ... deterministically instead of sampling. That
biases what an acceptance run exercises (and the arc order is correlated with the aggressor's
strength and start position).

## Suggested fix

Mirror the initial pick: `roll = randi(0, eligible[].size() - 1)` then
`global.&sandbox_scenario = eligible[roll]`.

## Comments
