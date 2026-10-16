# 06 - Static checker for the generated posture output

Status: ready-for-agent
Type: task
Blocked by: 02, 03

## What to build

`.scratch/scripts/check_economic_posture.py`, in the style of the existing
`check_cw_fuses.py` and `check_peak_coverage.py`: it reads the generated
`common/ai_strategy/99_sandbox_rivals_system.txt` of both mods and asserts the
invariants the design promises, so a generator regression is visible without
launching the game. No game install, standard library only, exit non-zero with
file and line on failure.

Invariants:

- Three plans per tag, no more: `*_is_rival`, `*_is_rival_contain` and
  `*_is_rival_feud` in equal numbers, and the total matches the counts recorded
  in the baseline copy.
- A `*_is_rival_feud` plan that carries `equipment_market_trade_desire` carries
  -200 for its own tag, and no tag ends up with both -50 and -200.
- No `equipment_market_buy` entry without a `seller` or an `equipment_type`.
- Every market entry sits inside a plan whose `enable` holds the band check it
  belongs to, so no entry leaks to a country that does not hold that rival.
- No `send_embargo`, `break_embargo` or `create_production_license` inside the
  generated ai_strategy files: those are script-side acts.
- No literal opinion threshold in the sources: where `has_opinion` appears in
  the `.hml` and `.hsl`, the value must come from the scale macro.

## Acceptance criteria

- [ ] Passes on the current generated output of both mods.
- [ ] Fails with a file and line when a value is deliberately edited in a copy
      (for example a dropped -200 or a fourth plan for one tag).
- [ ] Usage line at the top, matching the existing checkers.
- [ ] Runs in the same way as the other checkers (documented command), and its
      output is quoted in issue 08.

## Out of scope

- Runtime behaviour: this checks the generated text, not the game. The observer
  run is issue 08.
