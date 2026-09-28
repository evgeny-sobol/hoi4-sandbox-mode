# 05 - Move the boost splicer into core and drive it from paths

Status: resolved
Type: task
Blocked by: 02

## What to build

One shared focus-boost splicer in core, taking a mod directory as its argument
the way the other core tools do, replacing the per-mod hardcoded focus lists.
It applies the director's focus boost to each path's key focuses and to their
whole prerequisite closure, so a boost behind an unboosted fork is impossible.
On a mutually exclusive fork it boosts the side that leads to the next focus of
the path, and both sides when the path does not favour one. The splice is
idempotent, and the check fails when the focus files on disk do not match the
specs.

## Acceptance criteria

- [ ] The splicer lives in core and runs against a mod directory argument; the
      old per-mod hardcoded lists are gone.
- [ ] Every key focus and every prerequisite ancestor on its path carries the
      boost.
- [ ] A fork boosts the path-leading side; a fork with no path preference
      boosts both sides.
- [ ] Running the splice twice changes nothing the second time.
- [ ] `--check` fails when a focus file's boost set differs from the specs.
- [ ] The vanilla `axis_expansion` spec produces the expected boost set.

## Out of scope

- Changing the boost macro itself or the war-focus weighting.

## Verification: PASSED (tests + live build + compile)

- One core splicer (`core/tools/build_scenario_catalog.py`, `<mod_dir>`
  argument); `add_vanilla_focus_boosts.py`, `boost_focus_ancestors.py` and
  `build_scenario_graphs.py` deleted (superseded; history kept in git).
- Live axis run: 14 boosted focuses in `germany.include`; the Q38 fork trim
  removed exactly the two fork-losing sides (`GER_befriend_czechoslovakia`,
  `GER_danzig_for_slovakia`); all 6 keys stay boosted.
- `test_fork_prefers_path_side`, idempotency (`test_splice_converges_and_idempotent`)
  and unexpected-boost detection (`test_unexpected_boost_detected`) green.
- Full HSL recompile clean; compiled `germany.txt` confirms the trim.
