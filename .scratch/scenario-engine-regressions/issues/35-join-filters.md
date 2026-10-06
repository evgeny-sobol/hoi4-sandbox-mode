# 35 - Join filters (same ideology / same continent)

Status: resolved
Type: feature
Blocked by: none

## What to build

Let a scenario arc narrow its join-lever candidate pool with optional filters,
composed from the spec, without a scorer per combination.

## Decision

`docs/adr/0005-join-filters-via-one-flagged-scorer.md`: one shared
`scenario_join_scorer` reads per-call filter flags; the builder generates
`sandbox_select_<key>_joiners()` from the spec, so `[joiners] select/n/require`
stops being decorative.

## What changed

- `has_same_ideology_as_FROM` trigger (mirror of `_PREV`).
- `scenario_join_scorer` gates on `global.scenario_join_same_ideology` /
  `global.scenario_join_same_continent`.
- Spec `[joiners]` gains `invite_event` (required) and `require`
  (subset of `same_ideology`, `same_continent`); `select` stays
  `top_n_by_scorer`; `n` is honoured.
- Builder emits `sandbox_select_<key>_joiners()` (flags set from `require`,
  top-n invites, flags cleared); the four spec'd arcs dropped their
  hand-written bodies.
- N/single-variant tooling: `expected_labels` iterates the spec's variant keys;
  `extract_arc_hooks.py` emits numeric variant indices and accepts any count.

## Verification: PASSED (builder + compile + observer)

- 40/40 builder tests; `--check` in sync; shared guards green; both mods
  recompile clean.
- Observer run (pinned `napoleonic_france`, `require = [same_ideology,
  same_continent]`): join offers went to `ROM` and `POR` - same continent as
  FRA and a matching government group; no distant candidate was offered.

## Out of scope

- Changing the scorer's strength/goodwill staircases.
