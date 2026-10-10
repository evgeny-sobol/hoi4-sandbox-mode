# 04 - Focus exemption for event-routed ignitions (vanilla)

Status: resolved
Type: task
Blocked by: 01

## What to build

Some ignition focuses reach `start_civil_war` through an event that the cap
overlay already gates, so removing the focus modifier is not enough. Remove the
overlay from the events reachable only from an ignition focus:
`PER_revolution_events.1`, and the vanilla NSB Soviet war-starters
`.001` / `.003` / `fascist.001` (their only AI path is the focus; the non-focus
`on_daily` path is player-only). Leave every other overlay as is.

## Acceptance criteria

- [ ] `PER_revive_old_ways` and the SOV ignition focuses can start their war while the cap is reached.
- [ ] No non-focus AI fuse for those events is left ungated.
- [ ] The mod compiles.

## Answer

Removed the cap overlay from `PER_revolution_events.1` and the SOV NSB
war-starters (`.001` / `.003` / `fascist.001`). Both `.include` files now carry
no overlay and the generated `.txt` are the vanilla bodies. mod 7ec2761.
