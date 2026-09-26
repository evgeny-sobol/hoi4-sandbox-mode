# 14 - A declared target's tag can stop matching, and telemetry and derail disagree

Status: ready-for-agent
Type: bug
Blocked by: none

## What to build

One shared notion of "the declared target still exists", so the peak telemetry
and the derail arm never disagree about it. Today the telemetry logs a tag the arc never declared,
and the derail arm keyed to the declared tag stays silent, so an arc keeps running against a target
the engine may no longer see.

## Problem

The `axis` arc seeds `POL` as its second target and later logs a different tag for the same slot,
while the derail arm keyed to `POL` never fires.

Evidence, `_sandbox-r56` session (152 telemetry lines, 1936.1 - 1938.2):

```
1936.1   GER sc_seed t0=CZE t1=POL            # the declared pair
1938.1   CZE sc_target subject                # first target neutralized
1938.1   D09 sc_target open                   # second target logs a tag the arc never declared
1938.2   GER sc_ignite axis_war               # arc ignites instead of derailing
```

`sc_power` shows the identity change over time - `POL` is sampled through December 1937, then
`D09` takes its place in January 1938:

```
1937.12  POL sc_power div=17 fab=7            # last month POL is sampled
1938.1   D09 sc_power div=34 fab=27           # next month a different tag fills the slot
```

The session log also records two countries joining an array around that window ("Kingdom of Poland
was added to array", "Polish Peasant Union was added to array"), which is the shape of a Polish
civil war splitting the tag.

Two mechanisms read the target differently:

- The peak telemetry guards each target with `country_exists(<declared tag>)` and then logs
  `[THIS.GetTag]` from inside that scope. If the tag no longer resolves to the declared country,
  the logged tag and the declared tag diverge.
- The derail arm (`sandbox_check_targets_derail2` and siblings) decides "gone" purely on
  `not country_exists(<declared tag>)`, and "neutralized" on subject-of-aggressor or
  in-faction-with-aggressor.

So the same slot can read as alive to one and dead to the other. In this session the arc neither
derailed nor reported the declared target: it logged an undeclared tag and went on to ignite.

The same shape was seen earlier as `D04` in another session, so this is not a one-off.

## Why it matters

Every acceptance read of an arc keys off the declared pair: `sc_seed` names it, `sc_target` is
supposed to report on it, and the derail arm is supposed to end the arc when it can no longer
fight. When the logged tag drifts, the log cannot be trusted to answer "what happened to this
arc's targets", and an arc can run against a target the engine no longer considers declared.

## Acceptance

- [ ] A target that no longer resolves to its declared country logs `<declared tag>_gone` (the
      existing convention for a dead target), never a different live tag.
- [ ] The derail arm and the peak telemetry use the same test for "the declared target is gone",
      so they cannot disagree in the same tick.
- [ ] A session where a declared target's tag changes (civil war, annexation, re-tag) produces a
      `sc_derail`/`sc_end` pair or a `<tag>_gone` line, not a silently substituted tag.
- [ ] No new `error.log` lines attributable to scenario files; HSL compile clean in both mods.

## Out of scope

- The `sc_goal` silence while the aggressor was actively justifying; that is issue 16.
- The sampling cadence of the s7 package; that is issue 15.
- The eligibility rules that pick the targets in the first place.
