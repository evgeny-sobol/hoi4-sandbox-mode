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
(aggressor, targets, ideology gate, ladder calendar). An arc is data; the
scenario is the session's pick of it. Each arc is described by its **arc spec**.
_Avoid_: branch, path, story, plot

**Arc spec**:
The TOML file that records an arc's design decisions: aggressor, target
variants, ordered focus paths, ladder months, joiners, optional ideology gate,
and notes. Decisions live here; scripted events and effects stay in the HSL
catalog. Tooling derives the catalog, the focus diagrams, the boost closure and
the telemetry labels from the specs. One spec per arc per mod.
_Avoid_: config, manifest, data file

**Path**:
One ordered sequence of key focuses inside an arc's spec, from a branch entry
to a war leaf. An arc has one or more paths; each path declares the target
variants it serves (a missing field means shared). The director boosts each
path's foci plus their prerequisite closure only while one of its variants
runs; shared focuses stay boosted whenever the aggressor is live. The last
focus of the live path is the peak gate: AI ultimatums wait for it. Put
rarely-bypassed focuses last: a bypassed tail stalls the arc to the peak
fallback.
_Avoid_: branch, chain, route

**ready / draft** (arc status):
An arc spec's `status`. `ready` means the arc is in the shipped pool; `draft`
means it is authored but not in the pool. `number` (the director's
`sandbox_scenario` id) is written when the arc has code, in either status.
_Avoid_: implemented, planned, coded

**Target variant**:
The arc's chosen target set, one of the spec's `targets` keys, rolled evenly at
pick and fixed for the session. Variant A is the historical default; later
variants are catalog alts; a single-variant arc always uses A.
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
The peak-phase mechanism that invites the top-2 scored outsiders to the
aggressor's side. One shared scorer, per-arc filters (see Join filter); no
faction forms.
_Avoid_: recruitment, alliance, ally system, bloc

**Join filter**:
A per-arc condition on a join lever's candidate pool, declared in the spec's
`require` list: `same_ideology` (candidate and aggressor share a government
group) or `same_continent` (their capitals are on one continent). A filter
narrows the pool; the scorer ranks what remains.
_Avoid_: join gate, join condition, constraint

**Content-portable arc**:
An arc whose key focuses and targets exist in the target mod without
substitution and without a DLC gate. Portability is a per-mod property: an arc
can be portable in one mod and not another.
_Avoid_: compatible, supported, available
