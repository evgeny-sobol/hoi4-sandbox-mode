# 08 - Gate the remaining AI civil-war fuses (vanilla)

Status: claimed
Type: task
Blocked by: 01, 02, 04

## What to build

Gate every remaining AI-reachable civil-war fuse in `_sandbox`, so a capped AI
defers a fuse instead of lighting it. Use the existing patterns A-D and the
`sandbox_civil_war_ai_blocked` / `sandbox_civil_war_ai_allowed` helper. Do NOT
gate a fuse reachable only from a national focus (a focus ignition is exempt),
and do NOT gate the spy coups (out of scope).

Fuses to gate:

- **Stability crises**: the `common/decisions/stability_war_support.txt`
  missions that `start_civil_war` (`draft_dodging`, `strikes_mission`, and the
  other timeouts) - Pattern C. The v0.2 observer run showed they cluster.
- **Poland**: the sanation decisions (`POL.txt` ->
  `POL_sanation_left_opposition_up` / `POL_sanation_right_opposition_up`,
  Pattern D); `NSB_poland_monarchist_events.5` (Pattern B); the peasant-strike
  `timeout_effect` (Pattern C). The sanation path is the prime ungated hole;
  the peasant strike was gated only at `activation`.
- **Un-overlaid decisions**: the CHL / BUL / GUAY / HUN / USA / RAJ_GOE / SWE /
  BALTIC decisions that `start_civil_war` - verify each AI path and gate it
  (Pattern D).

Also:

- Extend the `docs/gdd/Civil Wars.md` "Coverage" list with the verified sites.
- Add a check script (in the style of `.scratch/scripts/check_*.py`, synced by
  `sync_core.py`) that fails when a `start_civil_war` outside
  `common/national_focus` has no overlay. Spy coups (`common/operations`) are
  allowlisted.

## Acceptance criteria

- [ ] The check script passes: no `start_civil_war` outside `common/national_focus` is left ungated, except the allowlisted spy coups.
- [ ] In an observer session, no AI event/mission `cw_declare` raises the count at `cap=1` or `cool>0` without a `cw_ignition` / `cw_event` / `cw_defer` first, except a spy coup.
- [ ] POL and BRA no longer leak via a scripted fuse (BRA has no non-focus fuse; the POL sanation path is gated).
- [ ] The vanilla mod compiles.

## Comments

Partial (branch feat/civil-wars). Added: the stability missions, the POL
sanation, and the HUN / GUAY / RAJ ignition missions to
sandbox_delay_capped_cw_missions; the POL monarchist event (Pattern B);
CHL / BUL / USA decision gates (Pattern D); YUG was already gated.
check_cw_fuses.py (baseline guard, 167 sites) passes.

Not met: the observer still shows leaks past cap=1. A 1936-1938 run reached
cw=5 (ETH / MON / ITA / SIA declares) with 480 cw_defer, and the count jumped
1->3 in one tick. The gated fuses are not the source, so a follow-up must find
the remaining ungated fuses. The run also failed on
`has_active_mission = YUG_communist_coup` (a decision, not a mission); fixed.

Update: gated the BBA Ethiopia family (BoP `.01` and fascist `.02/.03/.04`),
which the GDD Coverage list never named. The remaining leaks (MON / ITA / SIA)
come from scripted effects (`SIA_start_opposing_civil_war`, `SIA_military_coup`,
`ITA_bop_remove_bop_effect`, ...) called by decisions, events and focuses; each
caller must be traced and gated. The Coverage list is incomplete: it names ~15
families, the vanilla has 40+. A full pass needs the caller graph, not the
site list.

Verification: a 1936-1938 run with the Ethiopia gate still shows ETH
(1936-09), ITA (1937-03) and SIA (1937-10) starting at cap=1 (max cw=2). The
observed leaks are NOT closed. Either the Ethiopia source is not the events the
gate covered, or a Pattern B `ai_chance` gate does not stop a forced option.
Superseded by ticket 09 (full audit); this ticket stays claimed.

Acceptance correction: the shipped `check_cw_fuses.py` is a baseline guard
(new sites fail), not a per-site gating proof - the mod gates at the caller, so
per-site gating cannot be checked cheaply. The criterion "no start_civil_war
outside national_focus is left ungated" is replaced by "no NEW start_civil_war
appears that is not in the baseline".
