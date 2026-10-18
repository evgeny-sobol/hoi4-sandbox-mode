# 07 - Rt56 passthrough

Status: resolved
Type: task
Blocked by: 02, 03, 04, 05

## What to build

The same behaviour in the Rt56 adaptation, with the two per-mod facts that
differ.

- Opinion scale: Rt56 clamps opinion to [-200, 200]
  (`_sandbox-r56/common/_sandbox_scale.hml` returns 200). Every new threshold,
  veto and comparison goes through `$sandbox_opinion_scale()`; a literal 100
  would make "good" twice as strict in Rt56. Re-check the saturation the
  `opinion-scale` spec fixed: nothing new may clamp at half scale.
- DLC availability: Rt56 ships content with its own DLC assumptions. Write down
  which of By Blood Alone and Arms Against Tyranny the Rt56 build assumes, and
  align the guards with it. Where Rt56 already has its own trade or embargo
  content, the posture entries must not fight it: record the overlap in the GDD
  chapter instead of guessing.
- The generated ai_strategy output is per mod: regenerate from the same
  `sandbox-mod-core` macros, then run the checker (06) on the Rt56 output.
- Logging gate: add the commented `sandbox_log_economic` line to the Rt56
  on_actions file, beside the existing gates.

## Acceptance criteria

- [ ] Both mods compile; Rt56 `error.log` shows no posture lines and no
      invalid scope from the sweep.
- [ ] A Rt56 observer session produces the same acts as vanilla, with a partner
      at opinion 100 counting as "good" (not as half-way).
- [ ] The Rt56 DLC assumptions are written in the GDD chapter's DLC section.
- [ ] `check_economic_posture.py` passes on the Rt56 generated output.
- [ ] No literal opinion threshold survives in the Rt56 sources.

## Out of scope

- Rt56-specific content of its own (its focus trees, its own embargo focuses):
  the posture only reads the rivalry bands and opinion.

Implemented. Both mods compile (the fork against the Rt56 workshop root as its
`sandbox` root) and the synced core files reach both: the fork's generated plans
carry the same entries (825 plans, 275 tags) and `check_economic_posture.py`
passes on the fork's own file. The fork's two per-mod facts are answered in
`_sandbox-r56/docs/gdd/Economic Posture.md`, "Road to 56": the 200 scale (so
"good" is 100, never 50 - a literal would make the fork twice as strict), and the
DLC assumptions (the fork guards its own plans with 75 `has_dlc` checks, adds no
embargo content of its own, and writes its own `equipment_market_trade_desire` /
`diplo_action_desire` entries unguarded exactly as we do; the overlap is recorded,
not guessed). The commented `sandbox_log_economic` gate sits beside its siblings
in both mods' `on_actions`, and the fork's chapter and `Road to 56.md` both point
at the scale rule. The fork's observer session is issue 08's configuration 3.
