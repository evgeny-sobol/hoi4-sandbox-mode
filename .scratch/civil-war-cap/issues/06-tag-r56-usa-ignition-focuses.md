# 06 - Tag the r56 USA ignition focuses

Status: resolved
Type: task
Blocked by: none

## What to build

In r56, the USA focuses that fire `mtg_usa_civil_war_fascists` /
`mtg_usa_civil_war_democrats` are not tagged as ignition focuses, so they keep
the normal weight (40) instead of the rare 0.25. Add
`$ai_civil_war_ignition_modifier()` to their `ai_will_do`. Do not add a cap
modifier: a focus ignition is exempt.

## Acceptance criteria

- [ ] Those USA focuses carry `$ai_civil_war_ignition_modifier()` and no cap modifier.
- [ ] aiview shows 0.25 (x40 = 10).
- [ ] The mod compiles.

## Answer

Tagged USA_union_representation_act and USA_ally_with_the_silver_shirts with
$ai_civil_war_ignition_modifier() (0.25); both already logged cw_ignition.
r56 128834c.
