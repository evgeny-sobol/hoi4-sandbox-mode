# 06 - Generate and check telemetry labels against the HSL catalog

Status: resolved
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

## Verification: PASSED (tests + live build + compile)

- `expected_labels()` derives the set from spec aggressor/targets: `sc_goal`
  both directions, `sc_justify` aggressor-to-target, lowercase. The generated
  catalog carries a per-arc Telemetry labels section (axis: 8 goal + 4 justify).
- `check_labels()` compares against `99_sandbox_scenarios.hsl`: missing label,
  case drift (`GER_on_CZE` names the want), and unexpected label each fail
  distinctly. Labels of arcs without specs are skipped (migration state).
- The vanilla s7 had no reverse labels while the GDD documents both
  directions, so `.scratch/scripts/add_reverse_goal_lines.py` (spec-driven,
  idempotent) added the 4 axis reverse guards in target scope with the
  issue-16 justification alternative; actor always matches the label's first
  party. Compiled `.txt` confirms all four.
- 17/17 harness tests green, including the four new label tests; real
  `build` + `--check` green; full HSL recompile clean.
