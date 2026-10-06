# SAF_abandon_westminster

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"SAF_abandon_westminster"}
        n2["SAF_expand_the_cape_corps"]
        n3["SAF_police_windhoek"]
        n4["SAF_support_the_policy_of_appeasement"]
    end
    subgraph tier_1["Tier 1"]
        n5["SAF_empower_the_workers"]
        n6["SAF_support_the_afrikaner_broederbond"]
    end
    subgraph tier_2["Tier 2"]
        n7{"SAF_celebrate_the_great_trek"}
        n8["SAF_native_laws_amendment_act"]
        n9["SAF_repeal_the_native_representation_act"]
        n10{"SAF_support_ossewabrandwag"}
        n11["SAF_support_spain"]
    end
    subgraph tier_3["Tier 3"]
        n12{"SAF_burn_the_kings_portraits"}
        n13["SAF_equal_opportunity_employment"]
        n14["SAF_south_africa_first"]
        n15["SAF_support_nazification_of_south_west_africa"]
        n16["SAF_voortrekker_monument"]
        n17{"SAF_work_for_all_poor"}
    end
    subgraph tier_4["Tier 4"]
        n18["SAF_anti_colonialist_crusade"]
        n19["SAF_commemorate_the_battle_of_blood_river"]
        n20["SAF_join_comintern"]
        n21["SAF_outlaw_strikes"]
        n22["SAF_reclaim_boer_colonies"]
        n23["SAF_support_the_german_coup"]
    end
    subgraph tier_5["Tier 5"]
        n24["SAF_Union_of_the_African_People"]
        n25["SAF_a_king_for_our_people"]
        n26["SAF_demand_madagascar"]
        n27["SAF_german_scientists"]
        n28["SAF_support_axis_interests"]
        n29["SAF_support_the_world_revolution"]
    end
    subgraph tier_6["Tier 6"]
        n30["SAF_invite_soviet_advisers"]
        n31["SAF_liberate_british"]
        n32["SAF_liberate_portugese"]
    end
    subgraph tier_7["Tier 7"]
        n33["SAF_liberate_belgian"]
        n34["SAF_south_african_soviet_research_treaty"]
    end
    n18 --> n24
    n23 --> n25
    n14 --> n25
    n12 --> n18
    n11 --> n12
    n9 --> n12
    n6 --> n7
    n15 --> n19
    n16 --> n19
    n18 --> n26
    n20 --> n26
    n1 --> n5
    n9 --> n13
    n23 --> n27
    n29 --> n30
    n12 --> n20
    n32 --> n33
    n24 --> n31
    n24 --> n32
    n3 --> n8
    n6 --> n8
    n17 --> n21
    n14 --> n22
    n5 --> n9
    n7 --> n14
    n30 --> n34
    n23 --> n28
    n10 --> n15
    n6 --> n10
    n5 --> n11
    n1 --> n6
    n15 --> n23
    n20 --> n29
    n8 --> n16
    n10 --> n16
    n8 --> n17
    n1 x--x n4
    n18 x--x n20
    n5 x--x n6
    n2 x--x n21
    n14 x--x n15
```

# SAF_commit_to_the_five_year_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n35{"SAF_commit_to_the_five_year_plan"}
    end
    subgraph tier_1["Tier 1"]
        n36["SAF_improve_the_hawker_hartbees"]
        n37["SAF_replace_the_blenheim"]
    end
    subgraph tier_2["Tier 2"]
        n38["SAF_perfect_the_cab_rank_technique"]
    end
    subgraph tier_3["Tier 3"]
        n39["SAF_desert_air_force"]
        n40["SAF_secure_the_cape_sea_route"]
    end
    subgraph tier_4["Tier 4"]
        n41["SAF_retain_experienced_pilots"]
    end
    n38 --> n39
    n35 --> n36
    n36 --> n38
    n37 --> n38
    n35 --> n37
    n39 --> n41
    n40 --> n41
    n38 --> n40
    n37 --> n40
    n36 x--x n37
```

# SAF_seaward_defence_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n42{"SAF_seaward_defence_force"}
    end
    subgraph tier_1["Tier 1"]
        n43["SAF_disrupt_the_trade"]
        n44["SAF_protect_the_trade"]
    end
    subgraph tier_2["Tier 2"]
        n45["SAF_expand_the_simons_town_base"]
    end
    subgraph tier_3["Tier 3"]
        n46{"SAF_anti_submarine_tactics"}
        n47{"SAF_submarine_warfare"}
    end
    subgraph tier_4["Tier 4"]
        n48["SAF_prepare_overseas_offensive"]
        n49["SAF_strengthen_the_cape_garrison_artillery"]
    end
    n45 --> n46
    n42 --> n43
    n44 --> n45
    n43 --> n45
    n46 --> n48
    n42 --> n44
    n47 --> n49
    n45 --> n47
    n43 x--x n44
    n48 x--x n49
```

# SAF_south_african_railways

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n50(("SAF_south_african_railways"))
    end
    subgraph tier_1["Tier 1"]
        n51["SAF_expand_the_mining_industry"]
        n52["SAF_heavy_engineering"]
    end
    subgraph tier_2["Tier 2"]
        n53["SAF_infrastructure_effort"]
    end
    subgraph tier_3["Tier 3"]
        n54["SAF_armament_effort"]
        n55["SAF_south_african_steel"]
    end
    subgraph tier_4["Tier 4"]
        n56["SAF_expand_the_rand_mines"]
        n57["SAF_pretoria_arms"]
    end
    subgraph tier_5["Tier 5"]
        n58["SAF_fund_the_university_of_south_africa"]
    end
    subgraph tier_6["Tier 6"]
        n59["SAF_establish_the_atomics_energy_board"]
    end
    subgraph tier_7["Tier 7"]
        n60["SAF_defense_collaboration_initiative"]
        n61["SAF_the_cape_defense_institute"]
    end
    n53 --> n54
    n59 --> n60
    n58 --> n59
    n50 --> n51
    n55 --> n56
    n57 --> n58
    n56 --> n58
    n50 --> n52
    n52 --> n53
    n51 --> n53
    n54 --> n57
    n55 --> n57
    n53 --> n55
    n59 --> n61
```

# SAF_special_service_battalion

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n62(("SAF_special_service_battalion"))
    end
    subgraph tier_1["Tier 1"]
        n63["SAF_improve_the_three_oh_three"]
        n64["SAF_q_services_corps"]
    end
    subgraph tier_2["Tier 2"]
        n65["SAF__south_african_military_college"]
    end
    subgraph tier_3["Tier 3"]
        n66["SAF_expand_the_south_african_artillery"]
        n67["SAF_sa_engineer_corps"]
    end
    subgraph tier_4["Tier 4"]
        n68["SAF_equipment_effort"]
    end
    subgraph tier_5["Tier 5"]
        n69["SAF_mechanization_effort"]
        n70["SAF_south_african_special_forces"]
    end
    subgraph tier_6["Tier 6"]
        n71["SAF_armor_effort"]
    end
    n63 --> n65
    n64 --> n65
    n70 --> n71
    n69 --> n71
    n66 --> n68
    n67 --> n68
    n63 --> n66
    n65 --> n66
    n62 --> n63
    n68 --> n69
    n62 --> n64
    n64 --> n67
    n65 --> n67
    n68 --> n70
    n67 --> n70
```

# SAF_support_the_policy_of_appeasement

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["SAF_abandon_westminster"]
        n2["SAF_expand_the_cape_corps"]
        n15["SAF_support_nazification_of_south_west_africa"]
        n10["SAF_support_ossewabrandwag"]
        n6["SAF_support_the_afrikaner_broederbond"]
        n4(("SAF_support_the_policy_of_appeasement"))
        n72["SAF_war_measures_act"]
    end
    subgraph tier_1["Tier 1"]
        n73["SAF_csir"]
        n3["SAF_police_windhoek"]
    end
    subgraph tier_2["Tier 2"]
        n74["SAF_joint_air_training_scheme"]
        n8["SAF_native_laws_amendment_act"]
    end
    subgraph tier_3["Tier 3"]
        n75["SAF_desert_equipment"]
        n76["SAF_suppress_the_stormjaers"]
        n16["SAF_voortrekker_monument"]
        n17{"SAF_work_for_all_poor"}
    end
    subgraph tier_4["Tier 4"]
        n19["SAF_commemorate_the_battle_of_blood_river"]
        n21["SAF_outlaw_strikes"]
        n77["SAF_secure_interests_in_africa"]
    end
    n15 --> n19
    n16 --> n19
    n72 --> n73
    n4 --> n73
    n74 --> n75
    n73 --> n74
    n3 --> n8
    n6 --> n8
    n17 --> n21
    n4 --> n3
    n76 --> n77
    n75 --> n77
    n74 --> n76
    n3 --> n76
    n8 --> n16
    n10 --> n16
    n8 --> n17
    n1 x--x n4
    n2 x--x n21
```

# SAF_war_measures_act

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n21["SAF_outlaw_strikes"]
        n3["SAF_police_windhoek"]
        n4["SAF_support_the_policy_of_appeasement"]
        n72(("SAF_war_measures_act"))
    end
    subgraph tier_1["Tier 1"]
        n73["SAF_csir"]
        n78["SAF_emergency_workers"]
    end
    subgraph tier_2["Tier 2"]
        n79["SAF_cape_garrison_artillery"]
        n74["SAF_joint_air_training_scheme"]
    end
    subgraph tier_3["Tier 3"]
        n75["SAF_desert_equipment"]
        n80{"SAF_reconstitute_the_cape_corps"}
        n76["SAF_suppress_the_stormjaers"]
    end
    subgraph tier_4["Tier 4"]
        n2["SAF_expand_the_cape_corps"]
        n77["SAF_secure_interests_in_africa"]
    end
    n78 --> n79
    n72 --> n73
    n4 --> n73
    n74 --> n75
    n72 --> n78
    n80 --> n2
    n73 --> n74
    n79 --> n80
    n76 --> n77
    n75 --> n77
    n74 --> n76
    n3 --> n76
    n2 x--x n21
```
