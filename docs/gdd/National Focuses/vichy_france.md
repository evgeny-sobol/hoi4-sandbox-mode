# VIC_emergency_powers_to_petain

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("VIC_emergency_powers_to_petain"))
    end
    subgraph tier_1["Tier 1"]
        n2["VIC_rebuild_the_military"]
        n3["VIC_the_legionary_service_order"]
        n4["VIC_the_national_bureau_of_statistics"]
        n5["VIC_the_national_revolution"]
    end
    subgraph tier_2["Tier 2"]
        n6["VIC_anti_bolshevist_volunteers"]
        n7["VIC_down_with_marianne"]
        n8["VIC_finish_the_naval_buildup"]
        n9["VIC_form_the_milice"]
        n10["VIC_hidden_materials"]
        n11["VIC_long_term_economic_planning"]
        n12["VIC_modernize_the_airforce"]
        n13["VIC_prosecute_the_losers"]
    end
    subgraph tier_3["Tier 3"]
        n14["VIC_aid_small_businesses"]
        n15["VIC_analyze_our_defeat"]
        n16["VIC_concessions_to_the_germans"]
        n17["VIC_learn_from_the_enemy"]
        n18["VIC_up_with_jean_darc"]
    end
    subgraph tier_4["Tier 4"]
        n19["VIC_buy_from_the_enemy"]
        n20["VIC_celebrate_motherhood"]
        n21["VIC_mandatory_work_service"]
        n22["VIC_venerate_the_craftsman"]
    end
    subgraph tier_5["Tier 5"]
        n23["VIC_a_nation_reborn"]
    end
    subgraph tier_6["Tier 6"]
        n24["VIC_end_the_occupation"]
    end
    n20 --> n23
    n22 --> n23
    n21 --> n23
    n11 --> n14
    n10 --> n15
    n3 --> n6
    n17 --> n19
    n18 --> n20
    n13 --> n16
    n5 --> n7
    n23 --> n24
    n2 --> n8
    n3 --> n9
    n2 --> n10
    n12 --> n17
    n5 --> n11
    n16 --> n21
    n2 --> n12
    n5 --> n13
    n1 --> n2
    n1 --> n3
    n1 --> n4
    n1 --> n5
    n7 --> n18
    n14 --> n22
```
