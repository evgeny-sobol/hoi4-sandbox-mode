# 02 - Addressed market exclusion in the rival plans

Status: ready-for-agent
Type: task
Blocked by: 01

## What to build

Wave 1, declarative half: a country does not buy from its rivals.

- Extend the three band macros in `sandbox-mod-core/common/macros.hml` with
  entries addressed at the macro's `_country_`:
  - `rival_base` (any slot): `equipment_market_buy` with `seller = _country_`,
    value -200.
  - `rival_contain` (25 and above): `equipment_market_trade_desire` with
    `id = _country_`, value -50.
  - `rival_feud` (75 and above): `equipment_market_trade_desire` with
    `id = _country_`, value -200. Feud is the only tier whose plan is enabled
    at that intensity, so the -50 tier is not also active: do not stack.
- The generated `common/ai_strategy/99_sandbox_rivals_system.hsl` stays at
  three plans per tag (ADR-0007). Only macro bodies change, then regenerate.

## DLC guard and the decision rule

`ai_strategy` entries carry no conditions of their own: everything a plan can
be gated on lives in its `enable`, which also gates the military entries
(`antagonize`, `contain`, `conquer`, `prepare_for_war`). A per-entry
`has_dlc` check is therefore impossible without costing the military half.

- Primary path: write the market entries unguarded and verify on the base game
  (no Arms Against Tyranny) that `error.log` stays clean and no behaviour
  leaks. The tokens are engine-side, so the expectation is that they parse and
  do nothing when the market does not exist.
- Fallback, if that verification fails: three additional band plans per tag with
  `enable = { has_dlc = "Arms Against Tyranny" ... }`. That breaks ADR-0007's
  "three plans per tag", so the ADR has to be amended before it is written.

## Acceptance criteria

- [ ] At Rival and above, the generated `.txt` shows the negative entries
      against each rival tag of that country.
- [ ] Feud carries -200 for a tag, never both -50 and -200.
- [ ] Base game: no new `error.log` lines and no behaviour change.
- [ ] The generated file still holds three plans per tag.
- [ ] The starter values carry a comment saying they are calibrated from
      telemetry, not derived from balance.

## Out of scope

- The embargo sweep (03) and the wave 3 market-access denial (05).
- Buying bias of our own: the engine's opinion coefficients already do it, and a
  target-free bias cannot be attitude-scoped (spec, "Ladder").
