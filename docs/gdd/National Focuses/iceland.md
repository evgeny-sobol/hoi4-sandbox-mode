# ICE_expand_the_fishing_industry

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ICE_expand_the_fishing_industry"))
        n2["ICE_mineral_prospecting"]
    end
    subgraph tier_1["Tier 1"]
        n3["ICE_agricultural_expansion"]
        n4{"ICE_hydroelectric_power"}
    end
    subgraph tier_2["Tier 2"]
        n5["ICE_advanced_technology"]
        n6["ICE_develop_icelandic_shipping"]
        n7["ICE_heavy_industry"]
    end
    subgraph tier_3["Tier 3"]
        n8["ICE_expand_the_harbour"]
        n9["ICE_iceland_air"]
        n10["ICE_infrastructure_development"]
        n11["ICE_local_arms_industry"]
        n12["ICE_reykjavik_dockyards"]
    end
    subgraph tier_4["Tier 4"]
        n13["ICE_expand_the_civilian_fleet"]
        n14["ICE_hrafninn_flygur"]
        n15["ICE_industrial_research_school"]
    end
    n4 --> n5
    n1 --> n3
    n4 --> n6
    n12 --> n13
    n6 --> n8
    n7 --> n8
    n4 --> n7
    n9 --> n14
    n1 --> n4
    n2 --> n4
    n5 --> n9
    n11 --> n15
    n12 --> n15
    n9 --> n15
    n7 --> n10
    n5 --> n10
    n7 --> n11
    n6 --> n12
    n5 x--x n6
    n5 x--x n7
    n6 x--x n7
    n1 x--x n2
```

# ICE_international_trade

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n16(("ICE_international_trade"))
    end
    subgraph tier_1["Tier 1"]
        n17["ICE_banking_on_the_future"]
    end
    subgraph tier_2["Tier 2"]
        n18["ICE_infiltration"]
    end
    n16 --> n17
    n17 --> n18
```

# ICE_mineral_prospecting

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["ICE_expand_the_fishing_industry"]
        n2(("ICE_mineral_prospecting"))
    end
    subgraph tier_1["Tier 1"]
        n4{"ICE_hydroelectric_power"}
        n19["ICE_off_shore_oil_drilling"]
    end
    subgraph tier_2["Tier 2"]
        n5["ICE_advanced_technology"]
        n6["ICE_develop_icelandic_shipping"]
        n7["ICE_heavy_industry"]
    end
    subgraph tier_3["Tier 3"]
        n8["ICE_expand_the_harbour"]
        n9["ICE_iceland_air"]
        n10["ICE_infrastructure_development"]
        n11["ICE_local_arms_industry"]
        n12["ICE_reykjavik_dockyards"]
    end
    subgraph tier_4["Tier 4"]
        n13["ICE_expand_the_civilian_fleet"]
        n14["ICE_hrafninn_flygur"]
        n15["ICE_industrial_research_school"]
    end
    n4 --> n5
    n4 --> n6
    n12 --> n13
    n6 --> n8
    n7 --> n8
    n4 --> n7
    n9 --> n14
    n1 --> n4
    n2 --> n4
    n5 --> n9
    n11 --> n15
    n12 --> n15
    n9 --> n15
    n7 --> n10
    n5 --> n10
    n7 --> n11
    n2 --> n19
    n6 --> n12
    n5 x--x n6
    n5 x--x n7
    n6 x--x n7
    n1 x--x n2
```

# ICE_not_our_king

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20(("ICE_not_our_king"))
        n21["ICE_the_kingdom_of_iceland"]
    end
    subgraph tier_1["Tier 1"]
        n22["ICE_anti_capitalist_propaganda"]
        n23["ICE_expand_the_industrial_base"]
    end
    subgraph tier_2["Tier 2"]
        n24["ICE_international_relations"]
        n25["ICE_prepare_for_the_revolution"]
        n26["ICE_rally_the_workers_of_reykjavik"]
        n27["ICE_state_visits"]
    end
    subgraph tier_3["Tier 3"]
        n28["ICE_general_strike"]
        n29["ICE_organize_a_march"]
    end
    subgraph tier_4["Tier 4"]
        n30{"ICE_break_with_the_crown"}
    end
    subgraph tier_5["Tier 5"]
        n31["ICE_embrace_the_workers_revolution"]
        n32["ICE_state_corporatism"]
    end
    subgraph tier_6["Tier 6"]
        n33["ICE_international_brigades"]
        n34["ICE_organize_the_greyshirts"]
        n35["ICE_research_cooperation"]
        n36["ICE_state_owned_industry"]
    end
    subgraph tier_7["Tier 7"]
        n37["ICE_infiltrating_the_british_isles"]
        n38["ICE_the_viking_spirit"]
        n39["ICE_transformation_of_nature"]
    end
    subgraph tier_8["Tier 8"]
        n40["ICE_international_research_community"]
        n41["ICE_reclaiming_the_empire"]
        n42["ICE_recruiting_international_workers"]
        n43["ICE_securing_the_north_sea_passage"]
    end
    subgraph tier_9["Tier 9"]
        n44["ICE_vinland"]
    end
    n20 --> n22
    n28 --> n30
    n29 --> n30
    n30 --> n31
    n20 --> n23
    n26 --> n28
    n33 --> n37
    n31 --> n33
    n24 --> n33
    n23 --> n24
    n39 --> n40
    n25 --> n29
    n32 --> n34
    n22 --> n25
    n23 --> n26
    n38 --> n41
    n39 --> n42
    n37 --> n42
    n32 --> n35
    n27 --> n35
    n38 --> n43
    n30 --> n32
    n31 --> n36
    n22 --> n27
    n34 --> n38
    n36 --> n39
    n41 --> n44
    n43 --> n44
    n31 x--x n32
    n20 x--x n21
```

# ICE_the_armed_forces_of_iceland

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n45{"ICE_the_armed_forces_of_iceland"}
    end
    subgraph tier_1["Tier 1"]
        n46["ICE_a_naval_hub_in_the_atlantic"]
        n47["ICE_an_airbase_in_the_sea"]
    end
    subgraph tier_2["Tier 2"]
        n48["ICE_flying_boats"]
        n49["ICE_mine_iceland"]
        n50["ICE_modernizing_the_coast_guard"]
    end
    subgraph tier_3["Tier 3"]
        n51["ICE_emergency_conversions"]
        n52["ICE_low_cost_aircrafts"]
        n53{"ICE_support_equipment"}
    end
    subgraph tier_4["Tier 4"]
        n54["ICE_a_profesional_army"]
        n55["ICE_enact_conscription"]
    end
    subgraph tier_5["Tier 5"]
        n56["ICE_civilian_war_duty"]
        n57["ICE_doctrinal_studies"]
        n58{"ICE_thungur_hnifur"}
    end
    subgraph tier_6["Tier 6"]
        n59["ICE_death_from_above"]
        n60["ICE_taking_the_fight_to_our_enemies"]
        n61["ICE_we_shall_defend_our_island"]
    end
    n45 --> n46
    n53 --> n54
    n45 --> n47
    n55 --> n56
    n58 --> n59
    n54 --> n57
    n49 --> n51
    n50 --> n51
    n53 --> n55
    n47 --> n48
    n48 --> n52
    n50 --> n52
    n46 --> n49
    n47 --> n50
    n46 --> n50
    n50 --> n53
    n58 --> n60
    n54 --> n58
    n55 --> n58
    n58 --> n61
    n46 x--x n47
    n54 x--x n55
    n59 x--x n60
    n59 x--x n61
    n60 x--x n61
```

# ICE_the_kingdom_of_iceland

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20["ICE_not_our_king"]
        n21{"ICE_the_kingdom_of_iceland"}
    end
    subgraph tier_1["Tier 1"]
        n62["ICE_declare_absolute_neutrality"]
        n63["ICE_united_we_stand"]
    end
    subgraph tier_2["Tier 2"]
        n64["ICE_engineering_projects"]
        n65["ICE_infrastructure_projects"]
        n66["ICE_joint_shipbuilding_programme"]
        n67["ICE_royal_marines"]
        n68["ICE_the_icelandic_police_force"]
    end
    subgraph tier_3["Tier 3"]
        n69["ICE_gardhur_airfield"]
        n70["ICE_joint_military_training"]
        n71["ICE_patrolling_the_atlantic"]
        n72["ICE_the_merchant_fleet"]
    end
    subgraph tier_4["Tier 4"]
        n73["ICE_anglo_icelandic_relations"]
        n74["ICE_expand_industrial_complexes"]
        n75["ICE_industrial_cooperation"]
        n76["ICE_not_standing_idly_by"]
        n77["ICE_political_unity"]
    end
    subgraph tier_5["Tier 5"]
        n78["ICE_american_protection"]
        n79["ICE_expanding_the_university_of_reykjavik"]
        n80["ICE_fighting_as_equals"]
        n81["ICE_trade_relations"]
    end
    subgraph tier_6["Tier 6"]
        n82["ICE_compensation"]
        n83["ICE_keflavik_airbase"]
        n84["ICE_modernizing_the_island"]
        n85["ICE_republicanism"]
    end
    subgraph tier_7["Tier 7"]
        n86["ICE_american_investments"]
        n87["ICE_state_owned_enterprises"]
    end
    subgraph tier_8["Tier 8"]
        n88["ICE_american_soldiers"]
    end
    subgraph tier_9["Tier 9"]
        n89["ICE_iceland_defense_force"]
    end
    n83 --> n86
    n77 --> n78
    n86 --> n88
    n72 --> n73
    n80 --> n82
    n21 --> n62
    n62 --> n64
    n69 --> n74
    n72 --> n74
    n70 --> n74
    n71 --> n74
    n76 --> n79
    n77 --> n79
    n76 --> n80
    n65 --> n69
    n88 --> n89
    n71 --> n75
    n62 --> n65
    n67 --> n70
    n63 --> n66
    n78 --> n83
    n79 --> n84
    n70 --> n76
    n71 --> n76
    n66 --> n71
    n69 --> n77
    n72 --> n77
    n81 --> n85
    n63 --> n67
    n84 --> n87
    n63 --> n68
    n62 --> n68
    n64 --> n72
    n77 --> n81
    n21 --> n63
    n62 x--x n63
    n20 x--x n21
```
