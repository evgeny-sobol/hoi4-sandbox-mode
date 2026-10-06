# 31 - Focus telemetry is not owned by the builder

Status: resolved
Type: bug
Blocked by: none

## What to build

`build_scenario_catalog.py` must own the per-focus `sc_focus` telemetry splice
the same way it owns the boost splice: emit a `+completion_reward:` block with
`$sandbox_log_sc_focus(<id>)` for every focus in an arc's boost plan, remove it
when the focus leaves the plan, and fail `--check` when it drifts.

## Problem

The builder owns the boost splices, but the focus-completion telemetry lives in
a one-off `.scratch` script (`add_sc_focus_to_boosted.py`) that is not part of
the generator. When `5d194b4` rewired slot 4 to `soviet_west`, it added the
boost splices but no `sc_focus` lines, so the new path shipped blind: the
2026-10-04 session logged 4 `sc_focus` lines, none on the path foci the arc
needs to walk (`SOV_baltic_security`, `SOV_claims_in_baltic`,
`SOV_secure_leningrad`, `SOV_control_scandinavia`,
`SOV_respect_baltic_self_determination`, `SOV_claims_on_poland`,
`SOV_demand_eastern_poland`), and there was no telemetry to tell that the AI
had taken the wrong fork.

The drift is wider than the SOV path: `italy.include` has 38 boosted foci with
no log, `japan.include` 16, `soviet.include` 7. `germany`/`uk`/`usa` are 1:1.

Evidence that the log belongs to exactly the boost set: every existing
`+completion_reward:` block in the six `.include` files holds only the
`sc_focus` macro (germany 16/16, uk 9/9, usa 6/6, italy 18/18, japan 9/9,
soviet 5/5), and `germany`/`uk`/`usa` carry one per boosted focus.

## Acceptance

- [x] Canonical splice shape is `    +completion_reward:` with
      `      $sandbox_log_sc_focus(<id>)`, appended at the end of the focus
      body; the builder adds, removes and idempotently keeps it.
- [x] The `sc_focus` set equals the boost plan of every spec; `--check` exits 1
      on a boosted focus without the log and on a log without the boost.
- [x] After a build, the seven `soviet_west` path foci carry `sc_focus`; the
      `italy`/`japan`/`soviet` drift is converged.
- [x] `test_build_scenario_catalog.py` covers add / remove / idempotency and
      the two `--check` failures.
- [ ] A `soviet_west` run logs `sc_focus` on the path (needs a game run).

## Verification: PASSED (source + compiled + guard)

- Core `41514c8`: `log_insert()` / `FOCUS_LOG_RE` / `FOCUS_LOG_MARKER`; the
  builder appends one block per plan focus and strips it when the focus leaves
  the plan. `--check` fails on missing/unexpected/non-canonical for both owned
  shapes.
- Apply gave every plan focus the log: the compiled `soviet.txt` shows the
  expanded `sc_focus SOV_*` on 9 foci (7 path + 2 shared), and the
  `italy`/`japan` drift converged. 32/32 tests pass (new:
  `test_focus_log_added_on_apply`, `test_missing_focus_log_detected`,
  `test_focus_log_idempotent`); `check_focus_splices.py` rule 3 reports 0.
- `_sandbox` and `_sandbox-r56` recompile clean. The observer box is the
  pinned `soviet_west` run in `verification-run.md`.

## Out of scope

- The monthly `sc_goal`/`sc_justify` sampling, already builder-owned.
- Changing which foci are boosted (issue 30 owns the set).
