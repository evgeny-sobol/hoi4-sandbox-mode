# Economic posture is allowed to depend on DLC

Status: accepted

## Context

Two of the four requested mechanics sit behind paid content in vanilla. Every
vanilla use of `send_embargo` and `break_embargo` is wrapped in
`has_dlc = "By Blood Alone"` (`common/national_focus/argentina.txt`,
`belgium.txt`, `events/AAT_Sweden.txt`), and the equipment market plus market
access are Arms Against Tyranny (`EQUIPMENT_MARKET_*` defines; every vanilla
`has_dlc = "Arms Against Tyranny"` in `common/ai_strategy` sits next to
market-access entries). Licences are base-game, embargoes and the market are
not.

The repo already carries a term with the opposite instinct: `Content-portable
arc` in `CONTEXT.md` says an arc must exist "without a DLC gate". A reader who
knows that term would expect the same rule here, so the session of 2026-10-17
had to state the exception deliberately.

## Decision

Economic posture may depend on DLC, and DLC-gated mechanics get no DLC-free
fallback. Every branch that touches a paid mechanic is guarded with its
`has_dlc` check, so base-game owners see no behaviour change and no errors
rather than a degraded version.

## Considered Options

- **DLC-free fallbacks for every gated lever (rejected).** The only levers that
  exist without DLC are opinion and opinion-driven acceptance, which the engine
  already applies on its own. Code that re-applies them would change nothing
  observable and would exist only to satisfy a rule that is not about this
  feature.
- **Drop the DLC-gated mechanics entirely (rejected).** Two of the four
  requested mechanics are precisely the gated ones; dropping them leaves
  account-book bias with no teeth.
- **Emulate embargoes with defines or modifiers (rejected).** They are global:
  they would change how countries with no rivals treat the whole world.
- **Unguarded DLC calls (rejected).** `send_embargo` and the market entries are
  invalid without their DLC; unguarded script fills `error.log` and can leave
  scripted state pointing at actions the engine never ran.

## Consequences

- On the base game the feature is invisible: no embargoes, no market bias, no
  posture telemetry beyond the licence path. The GDD chapter states the DLC
  requirement instead of pretending parity.
- Every gated branch needs its guard checked in acceptance, including the case
  where the `allow_licensing` game rule blocks licensing outright.
- `Content-portable arc` keeps its meaning. This decision is scoped to
  economic posture and does not relax it for arcs or scenarios.
- If a DLC-free posture is ever wanted, it has to be argued as a new decision
  about useful levers, not as a restoration of symmetry.
