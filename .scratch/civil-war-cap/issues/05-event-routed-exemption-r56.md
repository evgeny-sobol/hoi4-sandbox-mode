# 05 - Focus exemption for event-routed ignitions (r56)

Status: resolved
Type: task
Blocked by: 01

## What to build

Same as the vanilla ticket, for `_sandbox-r56`: remove the overlay from
`lithuania.16` / `lithuania.109` and `portugal.44` / `portugal.45`, which are reachable only from
their ignition focuses. Do NOT remove the overlay from the NSB Soviet
war-starters in r56: the `on_daily_SOV` fuse shares them with the focus, so
those three focus ignitions stay capped (a known gap).

## Acceptance criteria

- [ ] `LIT_launch_the_revolution` and the POR ignition focuses can start their war while the cap is reached.
- [ ] The r56 NSB overlay is unchanged.
- [ ] The mod compiles.

## Answer

Un-overlaid the focus-queued events lithuania.16 / lithuania.109 and
portugal.44 / portugal.45 (a focus ignition is exempt); the r56 NSB overlay is
unchanged. r56 128834c.
