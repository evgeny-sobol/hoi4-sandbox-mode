# Scenarios Catalog

Generated from `docs/scenarios/*.toml` by `core/tools/build_scenario_catalog.py` -
do not edit by hand. The arc schema lives in `docs/gdd/Scenarios.md`.

## Reading a diagram

- `([id])` rounded - a branch entry / path root.
- `[[id]]` double-bordered - a key focus the director boosts and logs.
- `[id]` plain - an intermediate prerequisite, boosted as part of the path closure.
- `A --> B` - B requires A.
- `A x--x B` - mutually exclusive: taking one hides the other.

## Germany

| # | Aggressor | Arc | Variant A | Variant B | Key focuses | Status |
|---|---|---|---|---|---|---|
| 1 | GER | Axis expansion | CZE, POL | FRA, ENG | `remilitarize_the_rhineland`, `anschluss`, `demand_sudetenland`, `danzig_or_war`, `around_maginot`, `war_with_france` | ready |

### Arc 1: Axis expansion

The historical arc: Germany remilitarizes, absorbs Austria, pressures
Czechoslovakia and Poland through ultimatums, then turns on France. The
variant roll picks the eastern pair (CZE, POL) or the western pair
(FRA, ENG); the ladder releases claims and incidents at the crises rung
and ultimatums plus join offers at peak.

**Telemetry labels**: `sc_goal`: cze_on_ger, eng_on_ger, fra_on_ger, ger_on_cze, ger_on_eng, ger_on_fra, ger_on_pol, pol_on_ger; `sc_justify`: ger_on_cze, ger_on_eng, ger_on_fra, ger_on_pol.

```mermaid
flowchart TD
    subgraph arc1
        GER_anschluss[["GER_anschluss"]]
        GER_around_maginot[["GER_around_maginot"]]
        GER_danzig_or_war[["GER_danzig_or_war"]]
        GER_demand_sudetenland[["GER_demand_sudetenland"]]
        GER_fate_of_czechoslovakia["GER_fate_of_czechoslovakia"]
        GER_first_vienna_award["GER_first_vienna_award"]
        GER_heed_von_neuraths_concerns["GER_heed_von_neuraths_concerns"]
        GER_integrate_czechoslovakia(["GER_integrate_czechoslovakia"])
        GER_operation_weserubung["GER_operation_weserubung"]
        GER_reassert_eastern_claims["GER_reassert_eastern_claims"]
        GER_remilitarize_the_rhineland(["GER_remilitarize_the_rhineland"])
        GER_reorganize_the_wehrmacht["GER_reorganize_the_wehrmacht"]
        GER_war_preparations["GER_war_preparations"]
        GER_war_with_france[["GER_war_with_france"]]
        GER_anschluss --> GER_demand_sudetenland
        GER_anschluss --> GER_reassert_eastern_claims
        GER_around_maginot --> GER_war_with_france
        GER_danzig_or_war --> GER_around_maginot
        GER_danzig_or_war --> GER_operation_weserubung
        GER_demand_sudetenland --> GER_first_vienna_award
        GER_first_vienna_award --> GER_fate_of_czechoslovakia
        GER_heed_von_neuraths_concerns --> GER_anschluss
        GER_heed_von_neuraths_concerns --> GER_war_preparations
        GER_operation_weserubung --> GER_war_with_france
        GER_reassert_eastern_claims --> GER_danzig_or_war
        GER_remilitarize_the_rhineland --> GER_heed_von_neuraths_concerns
        GER_remilitarize_the_rhineland --> GER_reorganize_the_wehrmacht
        GER_reorganize_the_wehrmacht --> GER_anschluss
        GER_heed_von_neuraths_concerns x--x GER_reorganize_the_wehrmacht
    end
```
