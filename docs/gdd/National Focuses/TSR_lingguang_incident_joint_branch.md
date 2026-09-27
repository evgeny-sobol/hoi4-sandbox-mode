# GXC_the_japanese_visit

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("GXC_the_japanese_visit"))
    end
    subgraph tier_1["Tier 1"]
        n2["GXC_question_chiangs_authority"]
        n3["GXC_rumors_of_deposition"]
    end
    subgraph tier_2["Tier 2"]
        n4["GXC_denounce_chiang"]
        n5["GXC_the_scorched_earth_speech"]
    end
    subgraph tier_3["Tier 3"]
        n6["GXC_formation_of_the_nraja"]
    end
    subgraph tier_4["Tier 4"]
        n7["GXC_declare_opposition"]
    end
    n6 --> n7
    n3 --> n4
    n4 --> n6
    n5 --> n6
    n1 --> n2
    n1 --> n3
    n2 --> n5
```
