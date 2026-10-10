# 02 - Focus exemption: drop the ignition cap modifier (vanilla)

Status: resolved
Type: task
Blocked by: 01

## What to build

Remove the `factor(0)` / `sandbox_civil_war_cap_reached()` modifier from the
`ai_will_do` of every civil-war ignition focus in `_sandbox` (53 sites across
`common/national_focus/*.include`). Keep `$ai_civil_war_ignition_modifier()`
(0.25). Leave the event/decision/BoP overlays untouched: those are event/mission
ignitions and stay capped. A focus ignition is then exempt from the cap and the
cooldown, while a running focus ignition still occupies the slot.

## Acceptance criteria

- [ ] No `sandbox_civil_war_cap_reached` remains under `_sandbox` `common/national_focus/`.
- [ ] In aiview, an ignition focus shows weight 10 at any cap (sandbox 40 x 0.25).
- [ ] In an observer session, a focus ignition starts while a capped war runs.
- [ ] The mod compiles.

## Answer

Removed the `factor(0)` / `sandbox_civil_war_cap_reached()` modifier from 53
ignition focus sites in 27 files; an ignition focus keeps only the 0.25 weight.
mod 396d6f8. Observer: `cw_ignition TUR_restack_the_officer_corps` fired at
`cap=1` (1941-07-24).
