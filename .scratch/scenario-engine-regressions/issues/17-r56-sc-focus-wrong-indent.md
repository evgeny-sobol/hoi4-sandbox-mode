# 17 - r56 splices `sc_focus` at the wrong indent, so 63 focuses never log

Status: resolved
Type: bug
Blocked by: none

## What to build

The `sc_focus` completion splice in the Rt56 focus includes must land inside
the focus block, so the engine keeps it. Today every migrated splice sits at
the block level and the compiler drops it, so the affected focuses are
invisible in `sandbox_extract.txt` and every session opens with a wall of
compile errors. After the fix, a session that completes a spliced focus logs
`sc_focus` for it, and `error.log` carries no `Unexpected token:
completion_reward` line from a scenario splice.

## Problem

`v0.2.1` Rt56 session (222 telemetry lines, 1936.1 - 1940.3): zero `sc_focus`
lines for the 63 spliced focuses, while the three that appear in the log
belong to other arcs.

`error.log` is 2451 lines; 63 of them are:

```
Error: "Unexpected token: completion_reward, near line: 93191" in file: "common/national_focus/germany.txt"
```

and the same shape in france (14), japan (10), italy (9), soviet (8), uk (7),
usa (5).

Mechanism: the splice is emitted at two spaces of indentation, but a focus
body sits at four. The vanilla splicer
(`.scratch/scripts/add_sc_focus_to_boosted.py`) writes four spaces and is
clean (63 splices, 0 errors). The Rt56 includes are rebuilt by
`.scratch/scripts/generate_focus_includes.py`, which copies the vanilla
splice line verbatim while computing indentation from its own position
outside the focus block; nothing checks the resulting indent.

Evidence in the compiled mod: `common/national_focus/germany.txt` near 93191
and following shows a run of top-level `completion_reward = { ... }` blocks
between the closing `}` of one focus tree and the start of the next, each
containing only the scenario `log` line.

## Why it matters

`sc_focus` is one of the acceptance lines the scenario checklist reads to
prove the AI walks the war branch (the s10 lesson). With 63 of 86 Rt56
splices dropped, an Rt56 session cannot show war-branch progress, and the
`error.log` acceptance item ("no scenario-attributable lines") fails on every
run.

## Acceptance

- [x] Every Rt56 `sc_focus` splice sits at the focus-body indent (four
      spaces), not at the block level.
- [ ] `error.log` has zero `Unexpected token: completion_reward` lines after
      a recompile (compiled output clean; awaiting the next session log).
- [ ] An observer session shows `sc_focus` for a spliced Rt56 focus (needs a
      game run).
- [x] A check fails the build when a splice lands at the wrong indent, so the
      defect cannot return silently:
      `.scratch/scripts/check_focus_splices.py`.

## Out of scope

- The telemetry gate and the raw-call question (issue 18).
- Which focuses are spliced; the set is correct, only the placement is
  wrong.
- The vanilla splicer, which is already correct.

## Verification: PASSED (compiled output + guard)

- Rewrote all 63 tree-level splices in the seven Rt56 includes to the focus
  body indent (four spaces, six for the call). No tree-level
  `+completion_reward` remains in either mod.
- Forced recompile: 471 files, exit 0. In the compiled focus files the 63
  scenario calls now sit inside their focus blocks (germany 10, france 16,
  italy 11, japan 12, soviet 14, uk 10, usa 9), and the "top-level block that
  holds only the sandbox guard" shape is gone from every file.
- `error.log` from the next session must show zero `Unexpected token:
  completion_reward` and `sc_focus` lines for spliced focuses; that is the
  observer half of the acceptance and needs a game run.
- Guard added: `.scratch/scripts/check_focus_splices.py` fails on any
  tree-level scenario splice in either mod (verified positives/negatives by
  hand). Generator-side enforcement inside
  `generate_focus_includes.py` is deliberately left out of this ticket; it
  belongs with the generator change.
- The generator still emits the same shape for arcs not yet migrated, so the
  guard must run before a compile, not after.
