# YUG_army_modernization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("YUG_army_modernization"))
    end
    subgraph tier_1["Tier 1"]
        n2{"YUG_army_maneuvers"}
        n3["YUG_motorize_the_cavalry"]
        n4["YUG_mountain_brigades"]
        n5["YUG_small_arms"]
    end
    subgraph tier_2["Tier 2"]
        n6{"YUG_armored_cavalry"}
        n7["YUG_domestic_artillery_production"]
        n8["YUG_independent_engineer_regiments"]
        n9["YUG_motorized_logistics"]
        n10["YUG_supremacy_of_defense"]
        n11["YUG_supremacy_of_offense"]
    end
    subgraph tier_3["Tier 3"]
        n12["YUG_anti_tank_defenses"]
        n13["YUG_artillery_regiments"]
        n14["YUG_modern_tanks"]
        n15["YUG_motorized_recon_companies"]
        n16["YUG_tank_conversions"]
    end
    subgraph tier_4["Tier 4"]
        n17["YUG_form_parachute_battalions"]
        n18["YUG_medal_for_extreme_bravery"]
        n19["YUG_tank_licenses"]
    end
    n7 --> n12
    n3 --> n6
    n1 --> n2
    n11 --> n13
    n10 --> n13
    n5 --> n7
    n15 --> n17
    n4 --> n8
    n13 --> n18
    n6 --> n14
    n1 --> n3
    n3 --> n9
    n8 --> n15
    n1 --> n4
    n1 --> n5
    n2 --> n10
    n2 --> n11
    n6 --> n16
    n14 --> n19
    n14 x--x n16
    n10 x--x n11
```

# YUG_expand_the_serbian_shipyards

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20["YUG_contest_the_adriatic"]
        n21(("YUG_expand_the_serbian_shipyards"))
        n22["YUG_expand_the_split_shipyards"]
    end
    subgraph tier_1["Tier 1"]
        n23["YUG_coastal_defense"]
    end
    subgraph tier_2["Tier 2"]
        n24["YUG_expand_the_submarine_fleet"]
        n25["YUG_naval_bombers"]
    end
    subgraph tier_3["Tier 3"]
        n26["YUG_modern_destroyers"]
    end
    n21 --> n23
    n23 --> n24
    n25 --> n26
    n20 --> n25
    n23 --> n25
    n21 x--x n22
```

# YUG_expand_the_split_shipyards

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n23["YUG_coastal_defense"]
        n21["YUG_expand_the_serbian_shipyards"]
        n22(("YUG_expand_the_split_shipyards"))
    end
    subgraph tier_1["Tier 1"]
        n20["YUG_contest_the_adriatic"]
    end
    subgraph tier_2["Tier 2"]
        n25["YUG_naval_bombers"]
        n27["YUG_replace_the_dalmacija"]
    end
    subgraph tier_3["Tier 3"]
        n28["YUG_heavy_cruiser_project"]
        n26["YUG_modern_destroyers"]
    end
    n22 --> n20
    n27 --> n28
    n25 --> n26
    n20 --> n25
    n23 --> n25
    n20 --> n27
    n21 x--x n22
```

# YUG_industrialization_program

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n29(("YUG_industrialization_program"))
    end
    subgraph tier_1["Tier 1"]
        n30{"YUG_expand_the_mining_industry"}
    end
    subgraph tier_2["Tier 2"]
        n31["YUG_develop_civilian_industry"]
        n32["YUG_develop_military_industry"]
        n33["YUG_rare_minerals_exploitation"]
    end
    subgraph tier_3["Tier 3"]
        n34{"YUG_expand_the_university_of_zagreb"}
        n35["YUG_exploit_the_pannonian_deposits"]
    end
    subgraph tier_4["Tier 4"]
        n36["YUG_improve_serbian_rail_network"]
        n37["YUG_integrated_rail_network"]
    end
    subgraph tier_5["Tier 5"]
        n38["YUG_develop_slovenian_industry"]
        n39["YUG_expand_the_university_of_belgrad"]
        n40["YUG_improve_light_industry"]
        n41["YUG_serbian_steel"]
    end
    subgraph tier_6["Tier 6"]
        n42["YUG_central_management"]
        n43["YUG_expand_the_university_of_ljubljana"]
        n44["YUG_local_self_management"]
    end
    subgraph tier_7["Tier 7"]
        n45["YUG_expand_the_sarajevo_arsenals"]
    end
    n39 --> n42
    n30 --> n31
    n30 --> n32
    n37 --> n38
    n29 --> n30
    n44 --> n45
    n42 --> n45
    n36 --> n39
    n38 --> n43
    n31 --> n34
    n32 --> n34
    n33 --> n35
    n37 --> n40
    n36 --> n40
    n34 --> n36
    n34 --> n37
    n38 --> n44
    n30 --> n33
    n36 --> n41
    n31 x--x n32
    n36 x--x n37
```

# YUG_modernize_the_air_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n46{"YUG_modernize_the_air_force"}
    end
    subgraph tier_1["Tier 1"]
        n47["YUG_local_developers"]
        n48["YUG_purchase_foreign"]
    end
    subgraph tier_2["Tier 2"]
        n49["YUG_ikarus"]
        n50{"YUG_license_production"}
        n51["YUG_rogozarski"]
        n52["YUG_zmaj"]
    end
    subgraph tier_3["Tier 3"]
        n53["YUG_bomber_license"]
        n54["YUG_fighter_license"]
        n55["YUG_the_ik_3"]
    end
    subgraph tier_4["Tier 4"]
        n56["YUG_bomber_project"]
        n57["YUG_heavy_fighter_project"]
    end
    n50 --> n53
    n55 --> n56
    n50 --> n54
    n55 --> n57
    n47 --> n49
    n48 --> n50
    n46 --> n47
    n46 --> n48
    n47 --> n51
    n49 --> n55
    n51 --> n55
    n52 --> n55
    n47 --> n52
    n53 x--x n54
    n47 x--x n48
```

# YUG_recognize_the_soviet_union

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n58["YUG_friendship_treaty_with_italy"]
        n59(("YUG_recognize_the_soviet_union"))
        n60["YUG_reinforce_old_alliances"]
        n61["YUG_western_focus"]
    end
    subgraph tier_1["Tier 1"]
        n62["YUG_form_peasant_councils"]
        n63["YUG_mutual_economic_aid"]
    end
    subgraph tier_2["Tier 2"]
        n64{"YUG_abolish_the_monarchy"}
        n65["YUG_local_militias"]
    end
    subgraph tier_3["Tier 3"]
        n66["YUG_join_comintern"]
        n67["YUG_yugoslavian_path_to_communism"]
    end
    subgraph tier_4["Tier 4"]
        n68["YUG_form_the_federal_republic"]
        n69["YUG_pan_slavic_workers_congress"]
        n70["YUG_research_collaboration"]
    end
    subgraph tier_5["Tier 5"]
        n71["YUG_federal_defense_council"]
        n72["YUG_invite_albania"]
        n73["YUG_invite_bulgaria"]
    end
    subgraph tier_6["Tier 6"]
        n74["YUG_pan_balkan_workers_congress"]
    end
    subgraph tier_7["Tier 7"]
        n75["YUG_invite_greece"]
        n76["YUG_invite_hungary"]
        n77["YUG_invite_romania"]
    end
    subgraph tier_8["Tier 8"]
        n78["YUG_invite_turkey"]
    end
    n62 --> n64
    n63 --> n64
    n68 --> n71
    n59 --> n62
    n67 --> n68
    n66 --> n68
    n69 --> n72
    n69 --> n73
    n74 --> n75
    n74 --> n76
    n74 --> n77
    n75 --> n78
    n76 --> n78
    n77 --> n78
    n64 --> n66
    n60 --> n65
    n58 --> n65
    n62 --> n65
    n59 --> n63
    n73 --> n74
    n72 --> n74
    n71 --> n74
    n67 --> n69
    n66 --> n70
    n64 --> n67
    n66 x--x n67
    n59 x--x n61
```

# YUG_western_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n62["YUG_form_peasant_councils"]
        n59["YUG_recognize_the_soviet_union"]
        n61{"YUG_western_focus"}
    end
    subgraph tier_1["Tier 1"]
        n58["YUG_friendship_treaty_with_italy"]
        n60["YUG_reinforce_old_alliances"]
    end
    subgraph tier_2["Tier 2"]
        n79{"YUG_attract_allied_capital"}
        n80{"YUG_attract_axis_capital"}
        n81["YUG_brigadistas"]
        n65["YUG_local_militias"]
    end
    subgraph tier_3["Tier 3"]
        n82{"YUG_evolution"}
        n83{"YUG_limited_self_government"}
    end
    subgraph tier_4["Tier 4"]
        n84{"YUG_crush_the_ustasa"}
        n85{"YUG_devolved_croatia"}
        n86{"YUG_dissolve_serbia"}
        n87{"YUG_establish_the_banovina_of_croatia"}
        n88{"YUG_united_autonomous_croatia"}
    end
    subgraph tier_5["Tier 5"]
        n89{"YUG_ban_slovene_nationalist_parties"}
        n90{"YUG_divide_bosnia"}
        n91{"YUG_safeguard_bosnia"}
        n92{"YUG_slovenia_for_support"}
    end
    subgraph tier_6["Tier 6"]
        n93{"YUG_autonomous_transylvania"}
        n94{"YUG_banat_for_support"}
        n95{"YUG_concessions_for_macedonians"}
        n96{"YUG_fortify_banat"}
        n97{"YUG_surrender_macedonia"}
    end
    subgraph tier_7["Tier 7"]
        n98["YUG_end_the_regency"]
        n99["YUG_invite_german_military_mission"]
        n100{"YUG_join_axis"}
        n101["YUG_towards_independence"]
        n102["YUG_united_kingdom"]
    end
    subgraph tier_8["Tier 8"]
        n103{"YUG_coronation"}
        n104["YUG_defence_army_of_yugoslavia"]
        n105["YUG_guarantee_religious_liberties"]
        n106{"YUG_royal_wedding"}
        n107["YUG_surrender_italian_claims"]
        n108["YUG_zara_for_axis"]
    end
    subgraph tier_9["Tier 9"]
        n109["YUG_claim_macedonia"]
        n110["YUG_defence_league"]
        n111["YUG_enforced_neutrality"]
        n112["YUG_invite_italian_naval_experts"]
        n113["YUG_join_allies"]
        n114["YUG_reunite_the_kingdom"]
    end
    subgraph tier_10["Tier 10"]
        n115["YUG_allied_air_combat_school"]
        n116["YUG_fortress_yugoslavia"]
        n117["YUG_greater_yugoslavia"]
    end
    subgraph tier_11["Tier 11"]
        n118["YUG_all_yugoslavian_regiments"]
    end
    n117 --> n118
    n113 --> n115
    n58 --> n79
    n60 --> n79
    n58 --> n80
    n60 --> n80
    n86 --> n93
    n91 --> n93
    n90 --> n93
    n84 --> n89
    n87 --> n89
    n86 --> n94
    n91 --> n94
    n90 --> n94
    n58 --> n81
    n60 --> n81
    n108 --> n109
    n107 --> n109
    n92 --> n95
    n89 --> n95
    n98 --> n103
    n100 --> n103
    n82 --> n84
    n101 --> n104
    n104 --> n110
    n83 --> n85
    n83 --> n86
    n88 --> n90
    n85 --> n90
    n95 --> n98
    n97 --> n98
    n94 --> n98
    n93 --> n98
    n96 --> n98
    n106 --> n111
    n103 --> n111
    n82 --> n87
    n79 --> n82
    n80 --> n82
    n86 --> n96
    n91 --> n96
    n90 --> n96
    n111 --> n116
    n61 --> n58
    n109 --> n117
    n102 --> n105
    n95 --> n99
    n97 --> n99
    n94 --> n99
    n93 --> n99
    n96 --> n99
    n108 --> n112
    n107 --> n112
    n106 --> n113
    n103 --> n113
    n95 --> n100
    n97 --> n100
    n94 --> n100
    n93 --> n100
    n96 --> n100
    n79 --> n83
    n80 --> n83
    n60 --> n65
    n58 --> n65
    n62 --> n65
    n61 --> n60
    n105 --> n114
    n98 --> n106
    n88 --> n91
    n85 --> n91
    n84 --> n92
    n87 --> n92
    n100 --> n107
    n92 --> n97
    n89 --> n97
    n94 --> n101
    n93 --> n101
    n96 --> n101
    n83 --> n88
    n94 --> n102
    n93 --> n102
    n96 --> n102
    n100 --> n108
    n93 x--x n94
    n93 x--x n96
    n89 x--x n92
    n94 x--x n96
    n95 x--x n97
    n84 x--x n87
    n85 x--x n88
    n90 x--x n91
    n98 x--x n100
    n111 x--x n113
    n82 x--x n83
    n58 x--x n60
    n59 x--x n61
    n107 x--x n108
    n101 x--x n102
```
