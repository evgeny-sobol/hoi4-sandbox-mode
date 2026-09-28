# 06 - Generate and check telemetry labels against the HSL catalog

Status: ready-for-agent
Type: task
Blocked by: 03

## What to build

The expected telemetry labels are derived from the spec's aggressor and targets
instead of being hand-kept in two places. The generator emits the expected
label set into the catalog: `sc_goal` labels in both directions and `sc_justify`
labels from aggressor to target, always lowercase `aggressor_on_target`. The
check compares that set against the `.hsl` catalog, so a label that exists on
one side only, or differs in case, is a build error. This closes the class of
drift that produced the earlier label-case bug.

## Acceptance criteria

- [ ] The expected label set is derived from the spec (aggressor and targets).
- [ ] The catalog lists the expected `sc_goal` labels in both directions and the
      `sc_justify` labels aggressor-to-target, all lowercase.
- [ ] `--check` fails when a label in the set is missing from the `.hsl`
      catalog, or when a label differs in case.
- [ ] `axis_expansion` produces the expected `ger_on_cze`, `cze_on_ger` and
      `ger_on_cze` (justify) labels.

## Out of scope

- Changing what the `sc_goal` / `sc_justify` probes sample.
