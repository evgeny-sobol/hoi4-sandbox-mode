# Scenarios

A sandbox-only director that gives every session a crisis to live through: at
startup it picks one **arc** (a plausible 1930s conflict), rolls its target
variant, seeds the aggressor against its targets, and runs a three-rung ladder
that pushes the AI toward war. The player either gets drawn in or watches the
world burn. The system is designed to reuse the other sandbox mechanics (Honor,
Tyranny, Rivals, Civil Wars, National Focuses) rather than add new ones.

This is the vanilla mod. The Rt56 overlay (`_sandbox-r56`) shares the engine
and most documentation; this file describes what is specific to vanilla.

## Design goals

1. Make sessions alarming: an arc must, on a random draw, drive a major war.
2. Leave the player free: the director pushes AI, not the human; the player can
   join, meddle, or sit it out.
3. No new PM-level systems: reuse existing modifiers and hooks.
4. Stay legible: every mechanism logs to `game.log` under `#sandbox` for
   observer sessions.

## Selection

One arc per session, chosen at startup: pinned by a game rule or rolled at
random over the arcs whose aggressor exists. Arc ids are fixed per major
(1 GER, 2 SOV, 3 JAP, 4 ITA, 5 ENG, 6 USA); id 7 is a documented gap (France is
not content-portable; see `docs/gdd/Scenarios Catalog.md`). The pick rolls the
A/B target variant 50/50 and logs `sc_pick` plus `sc_variant`.

## Arc schema

```
sandbox_scenario_<id>:
  aggressor: GER            # a single tag
  type: historical          # every vanilla arc; no flip gate
  targets:
    a: [CZE, POL]           # variant A (historical default)
    b: [FRA, ENG]           # variant B (alt)
  joiners: open_pool_top2   # shared scorer, no per-arc parameters
  ladder: template          # smolder / crises / peak
  block: axis               # faction name if one forms
  content_refs: ...         # per-mod focus/event ids
```

## Ladder

| Rung | Fires at | Releases |
|---|---|---|
| smolder | month 0 | seed only |
| crises | month 12 | crisis events (claims, incidents) |
| peak | month 24 | ultimatums to targets, join offers |

The template calendar (smolder 36.1.1 / crises 37.1.1 / peak 38.1.1) is what
vanilla arcs use; later arcs may shift the rungs.

## Levers

**Rivals and antagonism**: the director seeds each aggressor-target pair as a
national rival at 65 and injects rivalry at the crises phase, so the existing
AI weights push war planning. Rivalry is the main lever; no new AI code.

**Focus weights**: `$ai_scenario_focus_boost()` (x5, live aggressor only) is
spliced onto the arc's war focuses and their branch roots, so the AI actually
walks the war branch (the s10 lesson: a boost behind an unboosted fork is dead).
Which focuses each arc boosts is drawn per arc in
`docs/gdd/Scenarios Catalog.md`.

**Join levers**: at peak the two highest-scoring outsiders (`scenario_join_scorer`)
get a bloc invitation. The scorer gates on ideology and hostility and scores
strength plus goodwill; a joiner leaves its old faction first (no Honor charge).

## Lifecycle

The arc ends at **ignition**: any war between declared scenario enemies, in
either direction, detected at declaration or by the monthly ongoing-war sweep.
Ignition logs `sc_ignite` + `sc_success` + `sc_end`.

**Derail** parks a dead arc at phase 3: the aggressor is gone, capitulated, or
has been in a protracted civil war (12 months); or no viable target remains.
On random a derail repicks; pinned sessions go quiet.

## Hooks and telemetry

- Tick: `on_startup` (selection) plus `on_weekly` / `on_monthly`. `on_monthly`
  runs per country, so the ladder tick fires in exactly one host per month: HAI
  is the primary host with a fallback chain through the majors.
- Reactions: `on_declare_war` (ignition), `on_annex` / `on_capitulation`
  (derail), `on_join_allies` / `on_join_faction` (joiner tracking).
- Telemetry: `sc_pick`, `sc_variant`, `sc_seed`, `sc_phase`, `sc_crisis`,
  `sc_target`, `sc_power`, `sc_goal`, `sc_justify`, `sc_goal_end`, `sc_focus`,
  `sc_offer`, `sc_ignite`, `sc_success`, `sc_join`, `sc_end`, `sc_derail`,
  `sc_repick`.

## Acceptance checklist

Log-first. Observer sandbox. Tick only when the grep holds.

- [ ] Startup: exactly one `sc_pick` naming one pool arc, plus one `sc_variant`.
- [ ] Ladder phases logged on schedule: `sc_phase smolder`, `crises`, `peak`.
- [ ] At peak each target logs one `sc_target` status line.
- [ ] Ignition: `sc_ignite` + `sc_success` + `sc_end` when a war fires between
  declared enemies (direct or ongoing).
- [ ] Derail: `sc_derail` + `sc_end` with a reason; random repicks.
- [ ] No `error.log` lines attributable to scenario files.

## Out of scope for this iteration

- Flip and imperial arcs (DLC-gated focus branches in vanilla; they live in the
  Rt56 overlay).
- The full 28-arc catalog: only the content-portable subset ships here.
- Player-facing scenario UI beyond the pinning game rule.
- Concurrent arcs.
- Scenario behaviour in historical mode: sandbox-only.
