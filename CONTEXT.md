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
variants it serves (a missing field means shared) and an optional `after` focus
list that holds the path's boost until those focuses are completed. The director
boosts each path's foci plus their prerequisite closure only while one of its
variants runs; shared focuses stay boosted whenever the aggressor is live. The
last focus of the live path is the peak gate: AI ultimatums wait for it. Put
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
The peak-phase mechanism that invites the top-N scored outsiders (`joiners.n`,
default 2) to the aggressor's side. One shared scorer, per-arc filters (see
Join filter); no faction forms.
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

**Character**:
A person record: name, portraits, and one or more roles.
_Avoid_: advisor (a role, not the person)

**Advisor**:
A hireable role of a character in a slot (political advisor, army chief):
the player or AI spends political power to hire it. Hiring is gated by
`available` (hard gate) and weighted for the AI by `ai_will_do`.
_Avoid_: character, minister

**Opinion**:
The engine-tracked country-to-country total: individual modifiers add into
it and the clamp cuts the sum, [-100, 100] in vanilla and [-200, 200]
in Rt56.
_Avoid_: rivalry, relation

**Rivalry**:
The mod's own 0-100 per-slot intensity toward a declared rival; it feeds
opinion through fixed modifiers and never reads it.
_Avoid_: opinion, hostility

**Economic posture**:
The economic-diplomacy behaviour a country derives from its attitude towards
another country. Two axes, and every act reads exactly one: hostility (Rivalry
bands Cold / Rival / Feud) and sympathy (the country's own Opinion of the
target, thresholds as fractions of the opinion scale). The axes never mix
arithmetically.
_Avoid_: stance, relation, trade policy

**Embargo**:
A persistent hostile act; the engine effects `send_embargo` and `break_embargo`
(By Blood Alone). The mod tracks its own embargoes in a bounded ledger, because
the engine's queries are per country.
_Avoid_: sanction (no such engine concept), blockade

**Licensed production**:
Engine licensing: a country lets another produce its equipment. The mod steers
who grants a licence; it cannot make an AI ask for one.
_Avoid_: licence deal, patent

**Equipment purchase**:
Buying and selling on the engine's international equipment market (Arms Against
Tyranny).
_Avoid_: arms trade, arms sale

**Trade agreement**:
The market relationship the engine creates (market access plus purchase
contracts), which posture biases. Not a diplomatic action of our own.
_Avoid_: trade deal, pact (that is a non-aggression pact)

**Civil-war backing**:
The rule that a major power backs one side of every ongoing civil war: the
side whose ruling government matches the major's own.
_Avoid_: support (the scenario join lever), intervention

**Backer**:
A major power that backs a side of a civil war. Backing is AI-only.
_Avoid_: patron, sponsor

**Kin side**:
The civil-war side whose ruling government matches the backer's. The backer
gives it opinion, military access, equipment and AI pressure.
_Avoid_: ally side, friendly side

**Rival side**:
The other side of the same civil war; the backer gives it a negative opinion
modifier.
_Avoid_: enemy side, opposing side

**Major power**:
Any country where the engine's `is_major = yes` holds, so Rt56 `set_major`
grants (e.g. China later) count.
_Avoid_: great power, big country (a major is not a world power)

**Civil-war cap**:
The limit of one concurrent civil war for the AI: while one war runs, the AI
starts no new event/mission ignition. A focus ignition is exempt, but a
running focus ignition still occupies the slot.
_Avoid_: limit, threshold

**Focus ignition**:
A civil war that starts from a national-focus completion reward, directly or
through a script the focus always calls. Exempt from the civil-war cap and
its cooldown.
_Avoid_: ignition (that is the scenario term), focus war

**Event/mission ignition**:
A civil war that starts from a non-focus script (event, mission, decision,
on_action, balance of power). Subject to the civil-war cap.
_Avoid_: scripted war, event war

**Civil-war cooldown**:
The random wait of 0 to 12 months after a capped civil war ends, before the
AI may start another event/mission ignition. A focus ignition ignores it.
_Avoid_: delay, pause

**Civil-war fuse**:
A script that can start a civil war for a country: a focus reward, an event, a
mission timeout, a decision, an on_action, or a balance of power. A focus fuse
is a focus ignition (exempt from the cap); every other fuse is an event/mission
ignition (capped).
_Avoid_: trigger, source, spark

**Ignition overlay**:
The mod's gate on a civil-war fuse: a `sandbox_civil_war_ai_allowed()` check
added to the fuse, so a capped AI defers it instead of losing it.
_Avoid_: block, filter, patch
