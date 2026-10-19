# 01 - Posture model and shared macros

Status: resolved
Type: task
Blocked by: none

## What to build

The two-axis model as reusable macros in `sandbox-mod-core/common/macros.hml`,
so every act reads the same bands instead of re-deriving them.

- `$rivalry_vs_into()` already reduces the three slots to the highest intensity
  for a tag; add the band predicates on top of it: Cold (below 25), Rival (25
  and above), Feud (75 and above), plus one veto macro ("Rival or above")
  that every positive act must call, so no act can forget the rule.
- `$opinion_good(_tag_)`: `has_opinion = { target = _tag_ value = <scale/2> }`
  built from `$sandbox_opinion_scale()` (100 vanilla, 200 Rt56). No literal 50
  or 100 anywhere near opinion.
- The shields that keep the sweep honest: a helper for "no hostile act against
  a country we are allied with, in a faction with, or have a pact with", and a
  helper for "the target still exists", both usable from trigger and effect
  context.
- Nothing else. No acts, no sweep, no market entries: those are issues 02-05.

Respect the existing split in `macros.hml`: trigger-only macros stay
trigger-only (`enable` blocks run in trigger context, temps plus `if`), effects
stay effects. `$add_rivalry` is the model for the comment style and for why
array elements are read into temps before math.

## Acceptance criteria

- [ ] Bands derive from `rivalry[]` only; opinion never produces or removes a
      band.
- [ ] The veto macro is the only hostility check used by positive acts.
- [ ] The opinion threshold is expressed through `$sandbox_opinion_scale()`;
      a grep of the new code finds no literal 50 or 100 beside opinion.
- [ ] Macros compile in both mods and produce no `Invalid Scope` lines when a
      slot holds a country that ceased to exist mid-month.
- [ ] The macros are documented in the `docs/gdd/Economic Posture.md` "Where it
      lives" list.

## Out of scope

- The acts themselves (02-05), the sweep (03) and telemetry (each act logs its
  own line).
- Any change to how `rivals[]` is selected or how `rivalry[]` moves: this issue
  only reads them.

Implemented. Macros in `sandbox-mod-core/common/macros.hml`:
`$is_rivalry_at_least`, `$is_rival_or_above`, `$is_feud`, `$is_cold_band`,
`$opinion_good` (built from `$sandbox_opinion_scale()`), `$target_still_exists`,
`$can_act_hostile_towards`, the ledger readers `$is_embargoed_by_us` /
`$embargo_cooldown_holds`, and the `sandbox_log_economic` gate. The bands read
`rivalry[]` only; the predicates are plain trigger expressions rather than temp
writers, so one form serves `enable`, `limit` and `available` alike (a temp
writer would be rejected in the strict trigger contexts). The GDD's "Where it
lives" list names the macros. Both mods compile; `Invalid Scope` on a dead slot
can only be observed in a session, which issue 08 carries.
