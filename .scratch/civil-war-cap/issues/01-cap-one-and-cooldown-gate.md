# 01 - Cap one and the cooldown gate

Status: resolved
Type: task
Blocked by: none

## What to build

The AI civil-war cap drops from three concurrent wars to one, and the freed
slot is held behind a random cooldown. `sandbox_civil_war_cap_reached` fires at
`sandbox_civil_war_count >= 1`. A new global `sandbox_civil_war_cooldown_until`
holds `months_elapsed + roll`, where `roll` is a uniform integer 0..12; it is
rolled at session start and every time `sandbox_civil_war_count` drops to 0. A
new scripted trigger `sandbox_civil_war_cooldown_active` is true while
`months_elapsed < sandbox_civil_war_cooldown_until`. `sandbox_civil_war_ai_blocked`
becomes `is_ai` and (`sandbox_civil_war_cap_reached` OR
`sandbox_civil_war_cooldown_active`). The `cw_` log lines carry a `cool=` field
(months left, 0 = inactive). The existing event/mission overlays need no change
beyond the shared `sandbox_civil_war_ai_blocked` helper.

## Acceptance criteria

- [ ] In an observer session, an AI event/mission ignition does not start while another civil war runs.
- [ ] After a capped civil war ends, the next event/mission ignition waits 0..12 months; the value differs across slot-free events.
- [ ] `cw_` lines show `cool=` with the months left, and 0 when inactive.
- [ ] The player is unrestricted (no cap, no cooldown).
- [ ] Both mods compile.

## Answer

Implemented. `sandbox_civil_war_cap_reached` is `count >= 1`. New global
`sandbox_civil_war_cooldown_until` = `months_elapsed + randi(0, 12)`, rolled at
session start and when the count drops to 0. New trigger
`sandbox_civil_war_cooldown_active`. `sandbox_civil_war_ai_blocked` = `is_ai`
and (cap OR cooldown). `cw_` lines carry `cool=`. core ca5f79a, mods 5d51244 /
278d790. Observer: the cap blocked 373 event/mission fuses in 1936-38; the
cooldown rolled 5 months when SPR ended (1939-06-11, `cool=5`) and the next war
waited to 1939-11-05.
