# 09 - Audit every civil-war fuse family (vanilla)

Status: ready-for-agent
Type: task
Blocked by: none

## What to build

A per-surface audit of every AI-reachable civil-war fuse in the vanilla game.
The GDD "Coverage" list names about fifteen families; the vanilla has forty
plus. A site scan finds about eighty event surfaces, plus about thirty
scripted effects and their callers. For each surface: decide whether the AI can
reach it, trace the caller, and gate it with the matching pattern (A-D). This
supersedes ticket 08's "gate the remaining fuses" for the families the observed
leaks did not cover.

Notes from the ticket 08 pass:
- The mod gates at the caller, so a per-site scan over-reports: `mexico.1` is
  gated by `MEX.include` on the mission, not on the event id.
- Some families were never overlaid at all: `BBA_ethiopia_fascist_events.*`,
  `AAT_Sweden` / `AAT_Denmark`, `TOA_Argentina` / `TOA_Chile`, `WUW_Austria` /
  `WUW_Congo` / `WUW_Germany`, `SEA_Japan` / `SEA_China` / `SEA_Warlords`,
  `TSR_Manchukuo`, `TFV_Australia` / `TFV_Canada`, `MTG_Britain` /
  `MTG_Netherlands` / `MTG_USA`, `GOE_RAJ`, `DOD_Yugoslavia` /
  `DOD_Czechoslovakia`, `BFTB_Bulgaria` / `BFTB_Turkey`, `stability.33`,
  `britain.23`, `france.14`, `germany.*`, `soviet.*`, `wtt_germany` /
  `wtt_japan`, and the scripted-effect families (`SIA_*`, `ITA_*`, `BUL_*`,
  `JAP_*`, `NOR_*`, `SOV_*`, `YUG_*`).
- A Pattern B gate on an `is_triggered_only` event's option did not stop the
  Ethiopia leak, so some surfaces need a Pattern A trigger (or a caller gate)
  instead.

## Acceptance criteria

- [ ] Every AI-reachable ignition surface is gated or explicitly allowlisted (spy coups, player-only fuses).
- [ ] The GDD "Coverage" list matches the audit.
- [ ] An observer run shows no AI event/mission `cw_declare` at `cap=1` or `cool>0`, except the allowlist.
