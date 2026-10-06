# 34 - Ultimatum refusal gives no casus belli, so ignition waits on the gate

Status: resolved
Type: bug
Blocked by: none

## What to build

A refused soviet_west ultimatum must give the aggressor a casus belli, so the
arc ignites from the peak content instead of depending on whether the AI
happens to declare war later.

## Problem

The `soviet_west` ultimatum events (`sandbox_soviet_west.2/.3/.5`, option `_b`)
only added war support and rivalry on a refusal. With no wargoal, ignition
relied entirely on the AI's own war decision after the peak.

The 2026-10-05 pinned variant-B run peaked at `t=36` (the baltic gate
`SOV_demand_eastern_poland` is unreachable before then - see the diagnosis
below) and then stalled to `peak_timeout` at `t=48` without igniting:

```
1939.1  ROM sc_crisis soviet_west_ult_3_defy  sc=4 phase=2 t=36
1940.1  HAI sc_derail peak_timeout            sc=4 phase=3 t=48
```

Variant A happened to declare war on its own (`sc_ignite` at `t=42`), so the
outcome was variant- and run-dependent.

## Diagnosis: why the gate never completes by the peak month

`SOV_baltic_security` is gated by the vanilla paranoia system:

```
available = { OR = { NOT = { has_country_flag = SOV_paranoia_system_active_flag } } is_subject = no }
```

The flag clears only via `SOV_remove_paranoia_effect`, called by the purge
focus `SOV_the_bloc_of_rights_and_trotskyites`. In the observer run SOV
completed `SOV_the_comintern` at `t=6` but `SOV_baltic_security` only at
`t=32` - a 26-month wait for the purge branch to clear paranoia. So the whole
baltic chain (both variants) opens around `t=30+`, the `peak_at_month = 24`
gate always falls through to the `t=36` fallback, and ignition must come from
the peak content, not the gate.

## Fix

The three defy options now give the aggressor a casus belli:

```
SOV:
  $create_wargoal(PREV, topple_government)
```

`topple_government` matches the ideological ultimatum and the vanilla SOV
decision pattern (the type's `allowed = always no` bars the justify UI, not an
effect-driven `create_wargoal`).

## Acceptance

- [x] A refused soviet_west ultimatum creates a wargoal for SOV on the
      defying target.
- [x] The arc ignites from the peak content without waiting on the gate: a
      pinned variant-B run ignites on the peak tick.
- [x] `error.log` has zero scenario lines; the mod compiles clean.

## Verification: PASSED (pinned observer run, 2026-10-05)

Pinned variant B (variant forced for coverage, reverted), 1936.1-1940.1:

```
1939.1  ROM sc_target open                        sc=4 phase=2 pin=1 t=36
1939.1  ROM sc_crisis soviet_west_ult_3_defy      sc=4 phase=2 pin=1 t=36
1939.1  SOV sc_ignite soviet_west_war             sc=4 phase=3 pin=1 t=36
1939.1  SOV sc_success soviet_west_war            sc=4 phase=3 pin=1 t=36
1939.1  SOV sc_end soviet_west_war                sc=4 phase=3 pin=1 t=36
```

Ignition lands on the same tick as the peak, where the pre-fix run timed out.

## Out of scope

- Clearing the vanilla paranoia flag at pick (option (a) in the round): not
  taken; the gate stays decorative and the peak uses the fallback by design.
- The variant-A path, which already ignited.
