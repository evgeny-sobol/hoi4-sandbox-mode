# FRA_appeal_to_the_french_nation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("FRA_appeal_to_the_french_nation"))
        n2["FRA_cooperation_with_the_communists"]
        n3["FRA_the_civil_and_military_organization"]
    end
    subgraph tier_1["Tier 1"]
        n4["FRA_appeal_to_overseas_territories"]
        n5["FRA_continue_the_fight"]
    end
    subgraph tier_2["Tier 2"]
        n6["FRA_colonial_recruitment"]
        n7["FRA_intervention_in_central_africa"]
        n8["FRA_intervention_in_indochina"]
        n9["FRA_intervention_in_madagascar"]
        n10["FRA_intervention_in_north_africa"]
        n11["FRA_intervention_in_syria"]
        n12["FRA_intervention_in_west_africa"]
        n13["FRA_the_free_french_navy"]
        n14["FRA_the_regiment_normandie"]
    end
    subgraph tier_3["Tier 3"]
        n15["FRA_form_the_national_committee"]
    end
    subgraph tier_4["Tier 4"]
        n16["FRA_form_the_provisional_government_of_the_republic"]
        n17["FRA_national_council_of_the_resistance"]
    end
    subgraph tier_5["Tier 5"]
        n18["FRA_french_forces_of_the_interior"]
        n19["FRA_national_uprising"]
    end
    n1 --> n4
    n5 --> n6
    n1 --> n5
    n9 --> n15
    n11 --> n15
    n8 --> n15
    n10 --> n15
    n12 --> n15
    n7 --> n15
    n15 --> n16
    n17 --> n18
    n4 --> n7
    n4 --> n8
    n4 --> n9
    n4 --> n10
    n4 --> n11
    n4 --> n12
    n3 --> n17
    n2 --> n17
    n15 --> n17
    n17 --> n19
    n5 --> n13
    n5 --> n14
```

# FRA_refus_absurde

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n15["FRA_form_the_national_committee"]
        n20(("FRA_refus_absurde"))
    end
    subgraph tier_1["Tier 1"]
        n21["FRA_connections_to_industrialists"]
        n22["FRA_reach_out_to_trade_unions"]
        n23["FRA_the_maquis"]
    end
    subgraph tier_2["Tier 2"]
        n2["FRA_cooperation_with_the_communists"]
        n3["FRA_the_civil_and_military_organization"]
    end
    subgraph tier_3["Tier 3"]
        n17["FRA_national_council_of_the_resistance"]
    end
    subgraph tier_4["Tier 4"]
        n18["FRA_french_forces_of_the_interior"]
        n19["FRA_national_uprising"]
    end
    n20 --> n21
    n22 --> n2
    n17 --> n18
    n3 --> n17
    n2 --> n17
    n15 --> n17
    n17 --> n19
    n20 --> n22
    n21 --> n3
    n20 --> n23
```
