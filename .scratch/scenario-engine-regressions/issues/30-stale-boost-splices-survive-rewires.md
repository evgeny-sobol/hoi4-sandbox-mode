# 30 - Stale focus-boost splices survive an arc rewire

Status: ready-for-agent
Type: bug
Blocked by: none

## What to build

The scenario builder must prune a focus-boost splice that no longer belongs to
any arc's boost plan. Today `build_scenario_catalog.py` only prunes when
`strict` is true, and `strict` is permanently false in `_sandbox` because the
disabled arcs 5-6 sit in the code dispatcher without specs, so the splice runs
additive-only forever and retired arcs leave their boosts behind.

## Problem

Three rewires retired arcs and moved their slots, but the old boosts stayed in
the `.include` files because `apply` never removed them (20 in `_sandbox`):

- the old `axis` path left 2 `GER_*` boosts (`GER_befriend_czechoslovakia`,
  `GER_danzig_for_slovakia`).
- `sov_south` (retired from slot 2) left `SOV_middle_east_diplomacy`,
  `SOV_support_afghan_ideology`, `SOV_preemptive_invasion_of_iran` boosted.
- `italian` (retired from slot 4) left 11 `ITA_*` boosts.
- the old slot-3 targets left 4 `JAP_*` boosts.

`apply_splice_file(..., remove_stale=strict)` and
`coverage()` returns `strict = spec_numbers == code and not errors`; with coded
arcs `{1..6}` and specs `{1,2,3,4}` the flag is always false, so the
out-of-plan branch `continue`s and `--check` prints a note instead of failing.

Consequence in the 2026-10-04 session (`sc=4 soviet_west`, variant A): the new
path focus `SOV_baltic_security` and the stale `SOV_middle_east_diplomacy`
carried the same plain x5 boost, so the fork the director meant to force was a
coin flip. The AI took the Middle East fork, never completed
`SOV_control_scandinavia`, the peak gate fell through to the `>= 36` fallback,
and the arc died on `peak_timeout`.

## Acceptance

- [ ] `apply_splice_file` removes a canonical out-of-plan boost (and its
      `sc_focus` block, issue 31) unconditionally; `remove_stale` is no longer
      a migration escape.
- [ ] `--check` exits 1 on an out-of-plan boost for both mods.
- [ ] After a build, `common/national_focus/*.include` in `_sandbox` carry no
      boost outside the spec plans (the 20 stale splices are gone).
- [ ] `test_build_scenario_catalog.py` covers apply-time removal of a stray
      canonical boost; the old additive-migration test is retired.
- [ ] Both mods recompile clean; no new `error.log` lines from scenario files.

## Out of scope

- The disabled arcs 5-6: they keep their hand content and stay spec-less; the
  fix removes the migration mode, not the arcs.
- `_sandbox-r56`: it has no scenario specs yet, so pruning there would strip
  its whole catalog (see issue 28).
