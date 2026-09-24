# 06 - Honor/Tyranny telemetry: `old` and `delta` fields are not real values

Status: needs-triage
Type: bug
Blocked by: none

## Problem

The `honor_*` / `tyranny_*` log lines carry three fields (`old -> new d=delta`), but in three
places `old` and `delta` are written with values that are not the previous value and not the
change. A reader of `sandbox_extract.txt` cannot use the delta column, and the numbers look like
corruption.

Session: `_sandbox`, 1936.1 - 1942.1 (72 months), 478 of the band lines carry a bogus `old`.

## Defect 1: the `999` sentinel leaks into `old` and `delta`

`prev_honor` / `prev_tyranny` use `999` as "no previous band" (`initialize_new_country_leader`,
`update_country_leader_traits`, `inherit_honor_on_ruling_party_change`,
`reset_honor_for_new_ruler`, `reset_tyranny_for_new_ruler`). The band logger then passes that
sentinel through as the old value:

`core/common/scripted_effects/99_sandbox_scripted_effects.hsl`:

```hsl
 290: sandbox_log_honor_band_if_changed():
 292:   if old_h == 999:
 293:     old_honor_band = -1
 ...
 316:     sandbox_log_old = old_h          # <- 999 on the first assign
 317:     sandbox_log_new = honor
 318:     sandbox_log_delta = honor - old_h # <- honor - 999
```

Session evidence (568 band lines total: 294 `honor_band_*` + 274 `tyranny_band_*`; 478 of them
carry `999.00`):

```
GER honor_band_righteous   999.00->79.00  d=-920.00 slot=-1 t=0 home=90.0
GER tyranny_band_despotic  999.00->85.00  d=-914.00 slot=-1 t=0 home=90.0
ENG honor_band_treacherous 999.00->-92.00 d=-1091.00 slot=-1 t=0 home=-90.0
```

The `new` value is correct; `old` and `d` are meaningless. 254 of the 478 fall in the
initialization month (`t=0`), but the rest are spread over 47 further months - every new ruler
(`reset_honor_for_new_ruler`, `inherit_honor_on_ruling_party_change`) and every civil-war rebel
tag re-emits the sentinel, so this is a steady leak, not a startup-only artifact.

## Defect 2: `honor_window_expire` writes the window age into `delta`

The expiry is a no-op for Honor (the pact/guarantee was already charged when it was dropped),
so `old == new`, but `delta` is set to the obligation's age in months:

`core/common/scripted_effects/99_sandbox_scripted_effects.hsl:419-424` and `441-446`:

```hsl
 419:       sandbox_log_other = v
 420:       sandbox_log_old = honor
 421:       sandbox_log_new = honor
 422:       sandbox_log_delta = age          # <- the 6-month age, not a change
```

Session evidence (30 lines, all `d=6.00`, all `old == new`):

```
TUR honor_window_expire -5.95->-5.95 d=6.00 other=IRQ slot=-1 t=20 home=25.0
IRQ honor_window_expire  6.30-> 6.30 d=6.00 other=TUR slot=-1 t=20 home=25.0
FRA honor_window_expire 90.20-> 90.20 d=6.00 other=BEL slot=-1 t=25 home=-90.0
```

The age is useful information, but it is not a delta and it collides with the field's meaning
in every other line.

## Defect 3: `tyranny_init` writes `tyranny_home` into `delta`

`initialize_new_country_leader` sets `old = 0`, `new = randi(min_tyranny, max_tyranny)` and then
`delta = tyranny_home` (the ideology midpoint), which is neither the delta nor the new value:

`core/common/scripted_effects/99_sandbox_scripted_effects.hsl:36-41`:

```hsl
  36:   sandbox_log_old = 0
  37:   sandbox_log_new = tyranny
  38:   sandbox_log_delta = tyranny_home
  40:   $sandbox_log_tyranny(tyranny_init)
```

Session evidence: 112 of 116 `tyranny_init` lines have `d != new`:

```
GER tyranny_init 0.00->85.00 d=90.00 other=HBC slot=-1 t=0 home=90.0
ENG tyranny_init 0.00->-81.00 d=-90.00 other=HBC slot=-1 t=0 home=-90.0
LUX tyranny_init 0.00->-67.00 d=-50.00 other=HBC slot=-1 t=0 home=-50.0
```

The `honor_init` line next to it is correct (`delta = honor - 0`), so the two initialization
lines disagree on what `d` means.

## Impact

`docs/gdd/Honor System.md` / `Tyranny System.md` acceptance reads the `old -> new d=` triple.
Any audit of "the +20 focus moved the value by exactly 20" is unreadable on the 478 band lines
and on every init/expiry line, and the fake `d=-1091.00` values invite false bug reports.

## Suggested fix (needs a decision)

- Defect 1: when `prev_* == 999`, log `old` as the sentinel-free value (e.g. emit the band
  transition as `new` only) or clamp `delta` to `new - 0`; keep the `999` sentinel internal.
- Defect 2: either drop `delta` from `honor_window_expire` (it is a no-op) and log `age` in its
  own field, or keep `d=0.00` and add `age=`.
- Defect 3: `sandbox_log_delta = tyranny` (or `tyranny - 0`) to match `honor_init`.

All three live in core files (`common/scripted_effects/99_sandbox_scripted_effects.hsl`), so the
fix goes to `sandbox-mod-core` and is synced outward per `.cursor/rules/sync-core-first.mdc`.

## Comments
