# ABDA_abdacom

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ABDA_abdacom"))
    end
    subgraph tier_1["Tier 1"]
        n2["ABDA_corps_expeditionnaire"]
        n3["ABDA_fortress_singapore"]
        n4["ABDA_maintain_strategic_flexibility"]
    end
    subgraph tier_2["Tier 2"]
        n5["ABDA_develop_naval_infrastructure"]
        n6["ABDA_the_malay_barrier"]
    end
    subgraph tier_3["Tier 3"]
        n7["ABDA_unified_naval_command"]
    end
    subgraph tier_4["Tier 4"]
        n8["ABDA_keep_trade_open"]
        n9["ABDA_naval_procurement"]
        n10["ABDA_ship_a_day_sinking_quotas"]
    end
    subgraph tier_5["Tier 5"]
        n11["ABDA_expand_the_command"]
    end
    n1 --> n2
    n2 --> n5
    n4 --> n5
    n9 --> n11
    n8 --> n11
    n10 --> n11
    n1 --> n3
    n7 --> n8
    n1 --> n4
    n7 --> n9
    n7 --> n10
    n3 --> n6
    n2 --> n6
    n6 --> n7
    n5 --> n7
```
