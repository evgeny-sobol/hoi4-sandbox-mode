# NZL_army_reforms

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("NZL_army_reforms"))
        n2["NZL_department_of_scientific_and_industrial_research"]
        n3["NZL_full_employment"]
    end
    subgraph tier_1["Tier 1"]
        n4["NZL_bob_semple_tank"]
        n5["NZL_charlton_automatic_rifle"]
    end
    subgraph tier_2["Tier 2"]
        n6["NZL_domestic_arms_industry"]
        n7["NZL_schofield_tank"]
    end
    subgraph tier_3["Tier 3"]
        n8["NZL_artillery_focus"]
        n9["NZL_long_range_patrol"]
        n10["NZL_think_big"]
    end
    subgraph tier_4["Tier 4"]
        n11["NZL_big_bob_tank"]
        n12["NZL_expand_the_university_of_auckland"]
    end
    subgraph tier_5["Tier 5"]
        n13["NZL_research_collaboration"]
    end
    n7 --> n8
    n8 --> n11
    n1 --> n4
    n1 --> n5
    n5 --> n6
    n10 --> n12
    n2 --> n12
    n6 --> n9
    n11 --> n13
    n10 --> n13
    n4 --> n7
    n3 --> n10
    n6 --> n10
```

# NZL_bureau_of_industry

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n11["NZL_big_bob_tank"]
        n14(("NZL_bureau_of_industry"))
        n15["NZL_direct_the_coal_industry"]
        n6["NZL_domestic_arms_industry"]
        n16["NZL_heavy_bombers"]
        n17["NZL_ministry_of_public_works"]
        n18["NZL_modern_fighters"]
        n19["NZL_national_roads_board"]
        n20["NZL_rail_standardization"]
    end
    subgraph tier_1["Tier 1"]
        n21["NZL_restart_the_onekaka_ironworks"]
        n22["NZL_taranaki_oil"]
        n23["NZL_wairarapa_sheep_farms"]
        n24["NZL_women_in_the_workforce"]
    end
    subgraph tier_2["Tier 2"]
        n25["NZL_domestic_car_industry"]
        n26["NZL_new_zealand_steel"]
        n27["NZL_scrap_metal_recycling"]
        n28["NZL_support_allies_with_meat"]
    end
    subgraph tier_3["Tier 3"]
        n2["NZL_department_of_scientific_and_industrial_research"]
        n3["NZL_full_employment"]
    end
    subgraph tier_4["Tier 4"]
        n29["NZL_project_seal"]
        n10["NZL_think_big"]
    end
    subgraph tier_5["Tier 5"]
        n12["NZL_expand_the_university_of_auckland"]
        n30["NZL_national_defense_institute"]
        n13["NZL_research_collaboration"]
    end
    n26 --> n2
    n19 --> n25
    n21 --> n25
    n10 --> n12
    n2 --> n12
    n20 --> n3
    n15 --> n3
    n26 --> n3
    n25 --> n3
    n29 --> n30
    n21 --> n26
    n16 --> n29
    n18 --> n29
    n2 --> n29
    n11 --> n13
    n10 --> n13
    n14 --> n21
    n21 --> n27
    n23 --> n28
    n17 --> n22
    n14 --> n22
    n3 --> n10
    n6 --> n10
    n14 --> n23
    n17 --> n24
    n14 --> n24
```

# NZL_expand_the_nzpaf

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n31["NZL_coastal_defense"]
        n2["NZL_department_of_scientific_and_industrial_research"]
        n32(("NZL_expand_the_nzpaf"))
    end
    subgraph tier_1["Tier 1"]
        n33{"NZL_form_the_rnzaf"}
    end
    subgraph tier_2["Tier 2"]
        n34{"NZL_bomber_focus"}
        n35["NZL_defend_our_islands"]
        n36{"NZL_fighter_focus"}
    end
    subgraph tier_3["Tier 3"]
        n16["NZL_heavy_bombers"]
        n18["NZL_modern_fighters"]
    end
    subgraph tier_4["Tier 4"]
        n29["NZL_project_seal"]
        n37["NZL_the_plan"]
    end
    subgraph tier_5["Tier 5"]
        n30["NZL_national_defense_institute"]
    end
    n33 --> n34
    n33 --> n35
    n31 --> n35
    n33 --> n36
    n32 --> n33
    n36 --> n16
    n34 --> n16
    n36 --> n18
    n34 --> n18
    n29 --> n30
    n16 --> n29
    n18 --> n29
    n2 --> n29
    n16 --> n37
    n18 --> n37
    n34 x--x n36
    n16 x--x n18
```

# NZL_ministry_of_public_works

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n11["NZL_big_bob_tank"]
        n14["NZL_bureau_of_industry"]
        n2["NZL_department_of_scientific_and_industrial_research"]
        n6["NZL_domestic_arms_industry"]
        n17(("NZL_ministry_of_public_works"))
        n26["NZL_new_zealand_steel"]
        n21["NZL_restart_the_onekaka_ironworks"]
    end
    subgraph tier_1["Tier 1"]
        n38["NZL_abolish_the_railways_board"]
        n15["NZL_direct_the_coal_industry"]
        n39["NZL_electrification"]
        n19["NZL_national_roads_board"]
        n22["NZL_taranaki_oil"]
        n24["NZL_women_in_the_workforce"]
    end
    subgraph tier_2["Tier 2"]
        n25["NZL_domestic_car_industry"]
        n40["NZL_establish_the_ncb"]
        n41["NZL_national_broadcasting_service"]
        n20["NZL_rail_standardization"]
    end
    subgraph tier_3["Tier 3"]
        n3["NZL_full_employment"]
    end
    subgraph tier_4["Tier 4"]
        n10["NZL_think_big"]
    end
    subgraph tier_5["Tier 5"]
        n12["NZL_expand_the_university_of_auckland"]
        n13["NZL_research_collaboration"]
    end
    n17 --> n38
    n17 --> n15
    n19 --> n25
    n21 --> n25
    n17 --> n39
    n15 --> n40
    n10 --> n12
    n2 --> n12
    n20 --> n3
    n15 --> n3
    n26 --> n3
    n25 --> n3
    n19 --> n41
    n17 --> n19
    n38 --> n20
    n11 --> n13
    n10 --> n13
    n17 --> n22
    n14 --> n22
    n3 --> n10
    n6 --> n10
    n17 --> n24
    n14 --> n24
```

# NZL_the_first_labor_government

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n42{"NZL_the_first_labor_government"}
    end
    subgraph tier_1["Tier 1"]
        n43["NZL_ratana_alliance"]
        n44{"NZL_statute_of_westminster"}
        n45["NZL_strengthen_the_commonwealth"]
    end
    subgraph tier_2["Tier 2"]
        n46["NZL_2nzef"]
        n47["NZL_constitution_amendment_act"]
        n48{"NZL_in_the_darkness"}
        n49["NZL_maori_affairs_act"]
        n50["NZL_social_security_act"]
        n51["NZL_the_lee_affair"]
    end
    subgraph tier_3["Tier 3"]
        n52["NZL_arrest_pacifist_leaders"]
        n53["NZL_befriend_japan"]
        n54["NZL_empower_the_working_class"]
        n55["NZL_independent_new_zealand"]
        n56["NZL_rule_them_all"]
        n57{"NZL_the_manpower_act"}
    end
    subgraph tier_4["Tier 4"]
        n58["NZL_amend_the_maori_affairs_act"]
        n59["NZL_join_comintern"]
        n60["NZL_technology_sharing_with_britain"]
        n61["NZL_technology_sharing_with_japan"]
        n62["NZL_waitangi_tribunal"]
    end
    subgraph tier_5["Tier 5"]
        n63["NZL_maori_conscription"]
        n64["NZL_maori_volunteers"]
        n65["NZL_technology_sharing_with_soviet_union"]
    end
    n45 --> n46
    n57 --> n58
    n46 --> n52
    n48 --> n53
    n44 --> n47
    n51 --> n54
    n44 --> n48
    n47 --> n55
    n54 --> n59
    n43 --> n49
    n58 --> n63
    n62 --> n64
    n42 --> n43
    n48 --> n56
    n43 --> n50
    n42 --> n44
    n42 --> n45
    n52 --> n60
    n53 --> n61
    n59 --> n65
    n44 --> n51
    n50 --> n57
    n49 --> n57
    n57 --> n62
    n58 x--x n62
    n53 x--x n56
    n47 x--x n48
    n47 x--x n51
    n48 x--x n51
    n44 x--x n45
```

# NZL_transfer_the_new_zealand_division

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n33["NZL_form_the_rnzaf"]
        n66(("NZL_transfer_the_new_zealand_division"))
    end
    subgraph tier_1["Tier 1"]
        n67["NZL_form_the_rnzn"]
    end
    subgraph tier_2["Tier 2"]
        n31["NZL_coastal_defense"]
        n68{"NZL_expand_devonport_naval_base"}
        n69["NZL_purchase_old_ships"]
    end
    subgraph tier_3["Tier 3"]
        n35["NZL_defend_our_islands"]
        n70["NZL_destroyer_effort"]
        n71["NZL_submarine_effort"]
    end
    subgraph tier_4["Tier 4"]
        n72["NZL_capital_ship_effort"]
        n73["NZL_light_cruiser_effort"]
    end
    n70 --> n72
    n71 --> n72
    n67 --> n31
    n33 --> n35
    n31 --> n35
    n68 --> n70
    n67 --> n68
    n66 --> n67
    n70 --> n73
    n71 --> n73
    n67 --> n69
    n68 --> n71
    n70 x--x n71
```
