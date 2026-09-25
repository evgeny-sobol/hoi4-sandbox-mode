# 05 - Normalize r56 telemetry labels

Status: resolved
Type: task
Blocked by: none

## Problem

The generated `sc_justify` labels are lowercased (`hun_on_rom`), but the r56 catalog's
`sc_goal` labels mix case for the same pair:

- `common/scripted_effects/99_sandbox_scenarios.hsl` uses `ITA_on_rom`, `ITA_on_bul`,
  `ITA_on_tur`, `USA_on_can`, `USA_on_hun`, `ENG_on_sov`, `ENG_on_ger`, `GER_on_den`,
  `SOV_on_fin`, `JAP_on_sia`, `FRA_on_spr` and others, alongside lowercase `hun_on_cze`,
  `sov_on_pol`, `jap_on_chi`.
- Vanilla uses lowercase throughout (`ger_on_cze`, `sov_on_tur`, ...).

Because the generator emits plain lowercase, one arc pair can now read as `GER_on_eng` in
`sc_goal` and `ger_on_eng` in `sc_justify`. An earlier generator revision keyed the justify
labels off the catalog's `sc_goal` labels; that surfaced the inconsistency as 257 noisy diff
lines and was reverted (see issue 01, "Follow-up: label casing drift").

## Why it matters

The labels are the only key a session's telemetry lines carry for an aggressor/target pair, so
grepping one arc's story means matching both spellings. `docs/gdd/Scenarios.md` lists the
telemetry line names but not the label convention, so nothing pins the case today.

## Fix options

1. Normalize the r56 catalog `sc_goal` labels to lowercase (113 labels; matches vanilla and
   the generated `sc_justify` output). Larger diff, one convention afterwards.
2. Make the generator mirror the catalog's `sc_goal` label case. Keeps the catalog as-is but
   bakes an inconsistent convention into the tool.

Option 1 is preferred.

## Acceptance

- For every arc pair, `sc_goal` and `sc_justify` labels match exactly.
- Add the label convention to `docs/gdd/Scenarios.md` so the generator and the catalog cannot
  drift apart again.
- Regenerate both mods' `common/scripted_effects/99_sandbox_arc_hooks.hsl` and recompile.

## Fix

Option 1 (normalize the catalog), applied in `_sandbox-r56`:

- `.scratch/scripts/normalize_sc_goal_labels.py` rewrites every `sc_goal` label to lowercase
  and maps the non-existent tag `rou` to `rom`. 53 occurrences across 45 distinct labels
  changed; the other 68 labels were already lowercase and untouched.
- Two labels also carried the wrong tag: `hun_on_rou` / `rou_on_hun` used `ROU`, which is not a
  tag in this mod - `sandbox_set_targets` seeds arc 8 with `ROM`, so the generated `sc_justify`
  key is `hun_on_rom`. Lowercasing alone would have left that pair split, so the tag is
  corrected in the same pass.
- `docs/gdd/Scenarios.md` (both mods) gained a "Telemetry label convention" subsection pinning
  `<aggressor>_on_<target>` lowercase, noting that `sc_goal` also carries the reverse
  `<target>_on_<aggressor>` direction while `sc_justify` does not, and that a label tag must be
  a real seeded tag (`ROM`, never `ROU`).

The 22 case-variant duplicate pairs (`ENG_on_ger` beside `eng_on_ger` in the same file) collapse
to one spelling each as a side effect.

This is a per-mod catalog, so no core file changed (`core/` untouched, `sync_core.py --check`
still reports `drifted=0` for both mods).

## Verification: PASSED

`.scratch/scripts/check_sc_labels.py` (committed with this ticket) over both mods, reading the
catalogs and the generated arc hooks:

| Mod | goal labels | justify labels | non-lowercase | `ROU`-bearing | forward pairs missing |
| --- | --- | --- | --- | --- | --- |
| `_sandbox` | 23 | 23 | 0 | 0 | 0 / 0 |
| `_sandbox-r56` | 91 | 72 | 0 | 0 | 0 / 0 |

- Every forward (aggressor -> target) schema pair derived from `sandbox_set_targets` x
  `sandbox_seed_actors` appears in **both** streams: 23 pairs for vanilla, 72 for r56.
- The 19 r56 labels present only in `sc_goal` are all the reverse direction (target -> aggressor),
  which is by design: `sc_goal` logs wargoals from either side, `sc_justify` only the aggressor's
  justifications. The checker asserts that every `sc_goal`-only label is such a reverse pair.
- Both mods recompiled clean; `arc_hooks.hsl` was already lowercase (the generator was never the
  problem), so only the catalog changed.

## Comments
