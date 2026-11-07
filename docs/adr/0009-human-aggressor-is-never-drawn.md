# A human aggressor is never drawn

Status: accepted

## Context

`docs/gdd/Scenarios.md` design goal 2 states the director pushes AI, not the
human: "the player can join, meddle, or sit it out". Selection eligibility has
never enforced it. All six generated `gen_<arc>_scenario_eligible()` functions
test `country_exists(<aggressor>)` and nothing else, in both the initial pick and
`sandbox_scenario_maybe_repick()`. A human-controlled major therefore enters the
pool at equal weight with the AI majors, and one arc in six can land on the
player's own country.

A 1936-1941 Rt56 session hit exactly that: arc 5 (`napoleonic_france`) was drawn
with `pin=0` while the human was playing France. The arc ran its full ladder -
crises at 1937.03, peak at 1938.07, `peak_timeout` at 1939.07 - and produced no
war, because the director has no lever on a human beyond issuing wargoals the
human may ignore. FRA held wargoals on HOL and LUX for eleven consecutive months.

The code was not uniformly accidental. `render_peak_gate()` in
`core/tools/build_scenario_catalog.py` emits a dedicated arm for the case:

```
elif <aggressor>->is_ai(no):
  global.&sandbox_scenario_phase = 2
  <arc>_fire_peak()
```

so a human aggressor advances to peak on schedule rather than waiting on a focus
tail it will never complete. That is deliberate half-support - peak was made to
work for a human aggressor, but nothing else was - and it is unmaintainable in
that state: no spec asks for a human-played arc, and no session can exercise the
arms that would follow peak.

The question came up in triage of the playtest audit; three options were on the
table.

## Decision

Exclude the human player's country from the arc pool, at both the initial pick
and the repick. Remove the human-aggressor arm from `render_peak_gate()`, leaving
the peak rung gated on the completed path tail and the
`peak_at_month + 12` fallback.

- The predicate is the same in both places: `country_exists(<aggr>)` plus "the
  aggressor is not a human". One helper, called from the eligibility functions
  and from the repick pool.
- An all-human-majors start yields an empty pool, which already has defined
  behaviour: `sandbox_scenario = 0`, no arc. It now becomes reachable.
- Being a declared *target* of an AI aggressor stays supported. That is the
  intended pressure direction and the whole point of joining and meddling.

## Considered Options

- **Keep the human arm and support a human aggressor properly (rejected).** Would
  need a real lever - pressure the human cannot ignore, or an explicit opt-out -
  which the director does not have and which no spec requests. Half-support that
  cannot be tested is worse than an honest exclusion.
- **Exclude only when the human is not also a declared target (rejected).** Still
  allows the observed failure: FRA was the aggressor with HOL/LUX as targets, so
  the human was not a target and would still have been drawn.
- **Warn and continue (rejected).** Logging a warning while the arc is
  undriveable leaves the session broken, only more legibly.

## Consequences

- One arc in the pool can be unavailable in a given session, dependably: the
  1-in-6 chance of an undriveable arc becomes 0, and the remaining pool rolls
  with equal weights over what is left.
- The `is_ai(no)` peak arm disappears from all six arcs in both mods. The peak
  rung becomes a two-arm gate (completed tail, then the 12-month fallback),
  which is also what the GDD now documents.
- `docs/gdd/Scenarios.md` "Peak" loses the human arm from its numbered list of
  gates. The `render_peak_gate()` docstring loses the phrase about human
  aggressors proceeding on schedule.
- If a human-played aggressor is ever wanted, it comes back as a designed mode
  with its own spec, a lever and a session log to verify against - not by
  re-adding a gate arm.
- Multiplayer is unaffected in kind: every human country is excluded, so a
  session whose majors are all human plays without a director rather than with a
  stalled one.
