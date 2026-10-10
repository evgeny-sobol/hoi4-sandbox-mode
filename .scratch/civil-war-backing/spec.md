# Civil-war backing

Status: resolved
Type: spec

## Context

Every civil war that runs in the world is currently a two-sided fight nobody
else reacts to. The goal is that major powers take a side: a major backs the
side whose ruling ideology matches its own.

Example: a civil war in Poland splits it into a neutral (monarchist) side and
a democratic side. Neutral (monarchist) Japan backs the neutral side, while
democratic USA, UK and France back the democratic side.

This document records the design agreed in a grilling session. No code is
written yet.

## Vocabulary

Canonical terms, to be added to `CONTEXT.md` at implementation time (in both
mods):

- **Civil-war backing** - the rule that a major backs one side of a civil war.
- **Backer** - a major that backs a side.
- **Kin side** - the civil-war side whose ruling ideology matches the backer.
- **Rival side** - the other side of the same war.
- **Major power** - any country where the engine's `is_major = yes` holds, so
  Rt56 `set_major` grants (e.g. China later) count.

Avoid **Support** (collides with the scenario join lever), **Intervention**,
and **Ignition** (already overloaded). Do not reuse the existing **Join
lever** / **Join filter** terms, which belong to the scenario director.

## Rule

For each ongoing civil war, every major whose ruling ideology equals one
side's ruling ideology backs that side.

- Ideology is the government group: `democratic`, `fascism`, `communism` or
  `neutrality` (tested with `has_government`); sub-ideologies are not
  distinguished.
- All matching majors back; there is no per-major limit.
- No proximity or access requirement (Japan can back Poland).
- A major's own civil war is not a backing: it is a participant.
- A major does not back a war when it is at war with the war's
  `original_tag`, or when it is itself in a civil war or near collapse.
- Backing is AI-only; a player-controlled major is never forced.

## Trigger

There is no `on_civil_war_start`. Backing runs from the existing weekly
census (`on_weekly` in the HAI scope, alongside
`update_sandbox_civil_war_count()`). This yields the intended ~one-week delay
and catches wars that the declaration hook misses.

## What backing does

Applied once, when the war is first seen, and held until the war ends. The
only re-evaluation is a backer's own government change (see Out of scope):

- Opinion: a positive modifier toward the kin side and a negative modifier
  toward the rival side. Quarrels between backers are left to the existing
  Rivals system.
- `give_military_access` to the kin side.
- Equipment: `send_equipment` to the kin side, repeated monthly while the war
  runs, the amount scaled by the backer's strength with a fixed floor.
- AI nudges: `send_lend_lease_desire` toward the kin side, and
  `send_volunteers_desire` where the engine rule already allows volunteers
  (fascism, communism). No `can_send_volunteers` rule override is granted.

## Engine constraints

- There is no `send_volunteers` or expeditionary-force effect. Volunteers are
  rule + AI-desire driven and cannot be forced; expeditionary forces are not
  scriptable at all.
- Democratic and neutrality governments have `can_send_volunteers = no`, so
  their backing stays materiel/diplomatic unless a rule override is added
  (deliberately not done).
- Equipment, opinion, military access, guarantees and AI strategies are all
  available as effects.

## Telemetry

A new `cw_support` log token, in the style of the existing `cw_*` tokens,
records which backer backed which side. Backing is otherwise silent; no
player-facing events.

## Out of scope (deferred)

- Backers joining the war; escalation stays with the existing Rivals and
  wargoal systems.
- Expeditionary forces (not scriptable).

Implemented after the original design: re-evaluating backing when a backer's
government changes mid-war (`issues/04-government-change-reevaluation.md`).
A backer that changes ruling ideology drops a kin side it no longer matches
(logging `cw_withdraw`) and backs the newly matching side. This is the one
exception to the frozen choice above.

## Scope of change

Shared logic in `sandbox-mod-core`; per-mod major weighting where the mods
differ. Reaches both `_sandbox` and `_sandbox-r56` through the submodule.
