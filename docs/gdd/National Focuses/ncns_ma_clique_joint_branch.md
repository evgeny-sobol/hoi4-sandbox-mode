# MA_develop_inter_province_ties

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("MA_develop_inter_province_ties"))
    end
    subgraph tier_1["Tier 1"]
        n2["MA_strenghten_regional_trade"]
        n3["MA_unified_training_program"]
    end
    subgraph tier_2["Tier 2"]
        n4["MA_promises_of_mutual_defense"]
    end
    subgraph tier_3["Tier 3"]
        n5["MA_formalize_the_ma_clique_collective"]
    end
    n4 --> n5
    n2 --> n4
    n3 --> n4
    n1 --> n2
    n1 --> n3
```
