# 05 - Normalize r56 telemetry labels

Status: needs-triage
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

## Comments
