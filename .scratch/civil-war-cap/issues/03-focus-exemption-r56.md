# 03 - Focus exemption: drop the ignition cap modifier (r56)

Status: resolved
Type: task
Blocked by: 01

## What to build

Same as the vanilla ticket, for `_sandbox-r56`: remove the `factor(0)` /
`sandbox_civil_war_cap_reached()` modifier from the `ai_will_do` of every
civil-war ignition focus (75 sites across `common/national_focus/*.include`).
Keep `$ai_civil_war_ignition_modifier()` (0.25). Leave the event/decision/BoP
overlays untouched.

## Acceptance criteria

- [ ] No `sandbox_civil_war_cap_reached` remains under r56 `common/national_focus/`.
- [ ] In aiview, an ignition focus shows weight 10 at any cap.
- [ ] In an observer session, a focus ignition starts while a capped war runs.
- [ ] The mod compiles.

## Answer

Removed the factor(0) / sandbox_civil_war_cap_reached() modifier from 75
ignition focus sites in 45 files; an ignition focus keeps only the 0.25 weight.
r56 128834c. The mod compiles. Not observed yet (observer deferred).
