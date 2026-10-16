# 05 - Trade agreement channel: deny rivals, try the positive seller

Status: ready-for-agent
Type: task
Blocked by: 01

## What to build

Wave 3, and the only part of the design that rests on an undocumented engine
behaviour.

- Denial half (safe): `diplo_action_desire` with `id = <rival tag>` and
  `target = market_access_rights`, value -200 at Feud, folded into
  `rival_feud` so the file stays at three plans per tag (ADR-0007). The DLC
  question is issue 02's: declarative entries cannot be guarded individually,
  so verify on the base game and only fall back to a DLC-gated tier if the log
  is dirty.
- Positive half (experimental): `equipment_market_buy` with
  `seller = <scoped variable>`. The vanilla documentation says the field "can
  be scoped variable" (`common/ai_strategy/_documentation.md`). Set the
  variable monthly to our best-opinion country that holds no rival slot, and
  add the entry with value +30 in a plan that is not per tag.
- If the engine refuses the variable form (an invalid-class log line, or the
  entry demonstrably does not change purchases in an observer run), delete the
  entry, log `ec_channel_unavailable` once per session, and keep the denial
  half. The rejected repair is 825 per-tag plans: the whole point of ADR-0007
  is that this cost is not paid.
- Whatever the outcome, the GDD chapter records which half shipped, and the
  spec's Risks section is updated with what was observed.

## Acceptance criteria

- [ ] Feud pairs show the negative `market_access_rights` desire in the
      generated file.
- [ ] Either the variable form changes purchase behaviour in an observer run,
      or the entry is gone and `ec_channel_unavailable` appears exactly once.
- [ ] The generated file still holds three plans per tag on both paths.
- [ ] Base game: `error.log` clean, sharing issue 02's answer.
- [ ] The spec's Risks section carries the observed result rather than the
      expectation.

## Out of scope

- New `scripted_diplomatic_actions` as a real trade agreement: vanilla ships the
  folder as a documentation stub with no definition anywhere, and Rt56 does not
  use it.
- Purchase contracts as such: the engine creates them; we only bias who is
  chosen, and the contract terms stay the engine's.
