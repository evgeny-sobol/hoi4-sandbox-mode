# Sandbox Mode Overhaul (vanilla)

A sandbox-only overhaul of vanilla Hearts of Iron IV: it strips the historical
AI engine and rebuilds it from player- and AI-facing systems (Honor, Tyranny,
Rivals, Civil Wars, National Focuses), of which the scenario director is the
war-driving one. This file is the shared vocabulary; it is not a spec.

## Language

**Scenario**:
The session-level choice the director makes once at startup: exactly one arc
runs per session (pinned by a game rule or rolled at random).
_Avoid_: mode, campaign, playthrough

**Arc**:
A catalog entry: one plausible 1930s conflict the aggressor drives toward
(aggressor, targets, ideology gate, ladder calendar, bloc). An arc is data;
the scenario is the session's pick of it.
_Avoid_: branch, path, story, plot

**Target variant**:
The arc's chosen target set, A or B, rolled 50/50 at pick and fixed for the
session. Variant A is the historical default; variant B is the catalog alt.
_Avoid_: target set, option, side

**Aggressor**:
The arc's driving country, the one the director seeds, boosts and gates. Its
tag is passed explicitly into derail/gate checks, never read from scope.
_Avoid_: attacker, actor, protagonist

**Ladder**:
The three-rung calendar every arc runs: smolder, crises, peak. Each rung fires
once at a month threshold and releases that phase's content.
_Avoid_: timeline, schedule, progression

**Crisis**:
Scripted content released by a ladder rung (claims, border incidents,
ultimatums). The only scenario content the player sees; it never names the arc.
_Avoid_: event chain, incident chain (an incident is one crisis beat)

**Derail**:
Parking a dead arc at phase 3 (ended): the aggressor is gone, capitulated,
off-ideology, in a protracted civil war, or no viable target remains. On random
sessions a derail repicks; pinned sessions go quiet.
_Avoid_: abort, cancel, fail, end (an arc "ends" by ignition instead)

**Ignition**:
The arc's success: any war between declared scenario enemies, in either
direction, detected at declaration or by the monthly ongoing-war sweep.
_Avoid_: trigger, success (success is logged separately as `sc_success`)

**Join lever**:
The peak-phase mechanism that invites the top-2 scored outsiders into the
aggressor's bloc. One shared scorer, no per-arc parameters.
_Avoid_: recruitment, alliance, ally system

**Content-portable arc**:
An arc whose key focuses and targets exist in the target mod without
substitution and without a DLC gate. Portability is a per-mod property: an arc
can be portable in one mod and not another.
_Avoid_: compatible, supported, available
