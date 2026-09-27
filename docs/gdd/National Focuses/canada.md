# CAN_army_modernization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CAN_army_modernization"))
        n2{"CAN_long_branch_arsenal"}
        n3["CAN_send_in_the_zombies"]
        n4["CAN_the_plan"]
    end
    subgraph tier_1["Tier 1"]
        n5["CAN_canadian_infantry_corps"]
        n6["CAN_cmp_truck"]
    end
    subgraph tier_2["Tier 2"]
        n7["CAN_a_motorized_army"]
        n8["CAN_royal_regiment_of_canadian_artillery"]
        n9["CAN_the_walkie_talkie"]
    end
    subgraph tier_3["Tier 3"]
        n10["CAN_1st_canadian_parachute_battalion"]
        n11["CAN_red_deer_training_camp"]
    end
    subgraph tier_4["Tier 4"]
        n12{"CAN_independent_command"}
        n13["CAN_the_black_devils"]
        n14["CAN_the_rocky_mountain_rangers"]
        n15["CAN_the_valentine_tank"]
    end
    subgraph tier_5["Tier 5"]
        n16["CAN_compromise_with_quebec"]
        n17["CAN_forced_quebec_conscription"]
    end
    n4 --> n10
    n7 --> n10
    n6 --> n7
    n1 --> n5
    n1 --> n6
    n2 --> n16
    n12 --> n16
    n2 --> n17
    n12 --> n17
    n3 --> n12
    n11 --> n12
    n8 --> n11
    n7 --> n11
    n5 --> n8
    n11 --> n13
    n11 --> n14
    n11 --> n15
    n5 --> n9
    n6 --> n9
    n16 x--x n17
```

# CAN_crown_corporations

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18["CAN_canada_pacific_railway"]
        n19(("CAN_crown_corporations"))
        n20["CAN_defence_of_canada_regulations"]
        n21["CAN_national_resources_mobilization_act"]
        n22["CAN_national_steel_car"]
        n23["CAN_rowell_sirois_commission"]
        n24["CAN_war_bonds"]
    end
    subgraph tier_1["Tier 1"]
        n25["CAN_department_of_munitions_and_supply"]
        n26["CAN_national_housing_act"]
    end
    subgraph tier_2["Tier 2"]
        n27["CAN_bits_and_pieces_program"]
        n28["CAN_dollar_a_year_men"]
        n29["CAN_fund_the_national_research_council"]
        n30["CAN_victory_aircraft_limited"]
    end
    subgraph tier_3["Tier 3"]
        n31["CAN_john_inglis_and_company"]
        n32["CAN_polymer_corporation"]
        n33["CAN_retool_angus_shops"]
    end
    subgraph tier_4["Tier 4"]
        n34["CAN_if_day"]
        n35["CAN_imperial_oil"]
        n36["CAN_uranium_mining"]
    end
    subgraph tier_5["Tier 5"]
        n37["CAN_defense_research_grants"]
        n38["CAN_war_fueled_economy"]
    end
    n25 --> n27
    n34 --> n37
    n19 --> n25
    n20 --> n25
    n24 --> n25
    n26 --> n28
    n25 --> n29
    n21 --> n29
    n31 --> n34
    n30 --> n34
    n33 --> n35
    n27 --> n31
    n23 --> n26
    n19 --> n26
    n30 --> n32
    n29 --> n32
    n18 --> n33
    n27 --> n33
    n32 --> n36
    n22 --> n36
    n25 --> n30
    n22 --> n38
    n34 --> n38
```

# CAN_defence_of_canada_regulations

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18["CAN_canada_pacific_railway"]
        n19["CAN_crown_corporations"]
        n20(("CAN_defence_of_canada_regulations"))
        n11["CAN_red_deer_training_camp"]
        n24["CAN_war_bonds"]
    end
    subgraph tier_1["Tier 1"]
        n25["CAN_department_of_munitions_and_supply"]
        n21["CAN_national_resources_mobilization_act"]
        n39["CAN_wartime_prices_and_trade_board"]
    end
    subgraph tier_2["Tier 2"]
        n27["CAN_bits_and_pieces_program"]
        n40["CAN_canada_wheat_board"]
        n29["CAN_fund_the_national_research_council"]
        n41["CAN_mine_the_shield"]
        n30["CAN_victory_aircraft_limited"]
    end
    subgraph tier_3["Tier 3"]
        n42["CAN_alberta_coal_towns"]
        n43["CAN_commit_to_the_war"]
        n31["CAN_john_inglis_and_company"]
        n32["CAN_polymer_corporation"]
        n33["CAN_retool_angus_shops"]
    end
    subgraph tier_4["Tier 4"]
        n34["CAN_if_day"]
        n35["CAN_imperial_oil"]
        n22["CAN_national_steel_car"]
        n3["CAN_send_in_the_zombies"]
    end
    subgraph tier_5["Tier 5"]
        n37["CAN_defense_research_grants"]
        n12{"CAN_independent_command"}
        n2{"CAN_long_branch_arsenal"}
        n36["CAN_uranium_mining"]
        n38["CAN_war_fueled_economy"]
    end
    subgraph tier_6["Tier 6"]
        n16["CAN_compromise_with_quebec"]
        n17["CAN_forced_quebec_conscription"]
    end
    n41 --> n42
    n40 --> n42
    n25 --> n27
    n39 --> n40
    n40 --> n43
    n2 --> n16
    n12 --> n16
    n34 --> n37
    n19 --> n25
    n20 --> n25
    n24 --> n25
    n2 --> n17
    n12 --> n17
    n25 --> n29
    n21 --> n29
    n31 --> n34
    n30 --> n34
    n33 --> n35
    n3 --> n12
    n11 --> n12
    n27 --> n31
    n3 --> n2
    n21 --> n41
    n20 --> n21
    n42 --> n22
    n30 --> n32
    n29 --> n32
    n18 --> n33
    n27 --> n33
    n43 --> n3
    n32 --> n36
    n22 --> n36
    n25 --> n30
    n22 --> n38
    n34 --> n38
    n20 --> n39
    n16 x--x n17
```

# CAN_halifax_shipyards

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n44(("CAN_halifax_shipyards"))
    end
    subgraph tier_1["Tier 1"]
        n45{"CAN_destroyer_effort"}
    end
    subgraph tier_2["Tier 2"]
        n46{"CAN_heavy_cruiser_effort"}
        n47{"CAN_light_cruiser_effort"}
    end
    subgraph tier_3["Tier 3"]
        n48["CAN_escort_fleet"]
        n49["CAN_fleet_in_being"]
    end
    subgraph tier_4["Tier 4"]
        n50["CAN_degauss_ship_hulls"]
        n51["CAN_trade_fleet"]
    end
    subgraph tier_5["Tier 5"]
        n52["CAN_united_shipyards"]
    end
    n48 --> n50
    n49 --> n50
    n44 --> n45
    n47 --> n48
    n46 --> n48
    n47 --> n49
    n46 --> n49
    n45 --> n46
    n45 --> n47
    n48 --> n51
    n49 --> n51
    n51 --> n52
    n50 --> n52
    n48 x--x n49
    n46 x--x n47
```

# CAN_patriation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n53["CAN_montreal_laboratory_collaboration"]
        n54{"CAN_patriation"}
        n55["CAN_shadow_factories"]
        n56["CAN_strengthen_the_commonwealth_ties"]
        n4["CAN_the_plan"]
    end
    subgraph tier_1["Tier 1"]
        n57["CAN_burn_the_royal_portraits"]
        n58["CAN_permanent_joint_defense_board"]
        n59["CAN_swastika_clubs"]
    end
    subgraph tier_2["Tier 2"]
        n60["CAN_camp_x"]
        n61{"CAN_communist_labor_total_war_committee"}
        n62["CAN_dominion_rifle_association"]
        n63["CAN_north_american_alliance"]
        n64{"CAN_support_the_blue_shirts"}
    end
    subgraph tier_3["Tier 3"]
        n65["CAN_defence_scheme_no_2"]
        n66["CAN_habakkuk_carrier"]
        n67["CAN_join_germany"]
        n68["CAN_mend_relations_with_the_trotskyites"]
        n69["CAN_refuge_for_scientists"]
        n70["CAN_supply_the_empire"]
        n71["CAN_supply_the_red_army"]
        n72["CAN_support_a_synarchist_baja"]
    end
    subgraph tier_4["Tier 4"]
        n73["CAN_aluminium_company_of_canada"]
        n74["CAN_canada_united"]
        n75["CAN_canadian_citizenship_act"]
        n76["CAN_join_comintern"]
        n77{"CAN_pinion_the_eagle"}
        n78["CAN_reactivate_farmers_unity_league"]
        n79{"CAN_reject_authoritarianism"}
        n80{"CAN_skewer_the_eagle"}
        n81["CAN_turner_valley_oilfield"]
    end
    subgraph tier_5["Tier 5"]
        n82["CAN_defence_scheme_no_1"]
        n83["CAN_demand_labrador_and_newfoundland"]
        n84["CAN_liberate_the_workers_of_the_world"]
        n85["CAN_newfoundland_act"]
        n86["CAN_offer_concessions_for_labrador_and_newfoundland"]
        n87["CAN_support_the_world_revolution"]
    end
    n70 --> n73
    n54 --> n57
    n53 --> n60
    n58 --> n60
    n65 --> n74
    n63 --> n75
    n70 --> n75
    n57 --> n61
    n80 --> n82
    n77 --> n82
    n79 --> n82
    n61 --> n65
    n80 --> n83
    n77 --> n83
    n79 --> n83
    n58 --> n62
    n55 --> n62
    n59 --> n62
    n63 --> n66
    n71 --> n76
    n64 --> n67
    n79 --> n84
    n61 --> n68
    n75 --> n85
    n58 --> n63
    n80 --> n86
    n77 --> n86
    n79 --> n86
    n54 --> n58
    n67 --> n77
    n68 --> n78
    n63 --> n69
    n68 --> n79
    n72 --> n80
    n4 --> n70
    n60 --> n70
    n61 --> n71
    n64 --> n72
    n59 --> n64
    n74 --> n87
    n76 --> n87
    n54 --> n59
    n70 --> n81
    n57 x--x n58
    n57 x--x n59
    n65 x--x n68
    n65 x--x n71
    n83 x--x n86
    n67 x--x n72
    n68 x--x n71
    n54 x--x n56
    n58 x--x n59
```

# CAN_rcaf_station_borden

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n88(("CAN_rcaf_station_borden"))
    end
    subgraph tier_1["Tier 1"]
        n89["CAN_the_pacific_coast_air_defence_radar_system"]
        n90["CAN_we_have_the_hurricane"]
    end
    subgraph tier_2["Tier 2"]
        n91["CAN_commonwealth_air_training_plan"]
    end
    subgraph tier_3["Tier 3"]
        n92["CAN_cookie_carriers"]
        n93["CAN_fund_fairchilds_development"]
    end
    subgraph tier_4["Tier 4"]
        n94["CAN_the_sabre_project"]
    end
    n89 --> n91
    n90 --> n91
    n91 --> n92
    n91 --> n93
    n88 --> n89
    n92 --> n94
    n93 --> n94
    n88 --> n90
```

# CAN_rowell_sirois_commission

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n27["CAN_bits_and_pieces_program"]
        n19["CAN_crown_corporations"]
        n23(("CAN_rowell_sirois_commission"))
    end
    subgraph tier_1["Tier 1"]
        n18["CAN_canada_pacific_railway"]
        n26["CAN_national_housing_act"]
    end
    subgraph tier_2["Tier 2"]
        n28["CAN_dollar_a_year_men"]
        n95["CAN_maritime_colonial_railway"]
        n33["CAN_retool_angus_shops"]
    end
    subgraph tier_3["Tier 3"]
        n35["CAN_imperial_oil"]
    end
    n23 --> n18
    n26 --> n28
    n33 --> n35
    n18 --> n95
    n23 --> n26
    n19 --> n26
    n18 --> n33
    n27 --> n33
```

# CAN_strengthen_the_commonwealth_ties

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n7["CAN_a_motorized_army"]
        n63["CAN_north_american_alliance"]
        n54["CAN_patriation"]
        n58["CAN_permanent_joint_defense_board"]
        n56(("CAN_strengthen_the_commonwealth_ties"))
        n59["CAN_swastika_clubs"]
    end
    subgraph tier_1["Tier 1"]
        n53["CAN_montreal_laboratory_collaboration"]
        n55["CAN_shadow_factories"]
    end
    subgraph tier_2["Tier 2"]
        n60["CAN_camp_x"]
        n62["CAN_dominion_rifle_association"]
        n4["CAN_the_plan"]
    end
    subgraph tier_3["Tier 3"]
        n10["CAN_1st_canadian_parachute_battalion"]
        n70["CAN_supply_the_empire"]
    end
    subgraph tier_4["Tier 4"]
        n73["CAN_aluminium_company_of_canada"]
        n75["CAN_canadian_citizenship_act"]
        n81["CAN_turner_valley_oilfield"]
    end
    subgraph tier_5["Tier 5"]
        n85["CAN_newfoundland_act"]
    end
    n4 --> n10
    n7 --> n10
    n70 --> n73
    n53 --> n60
    n58 --> n60
    n63 --> n75
    n70 --> n75
    n58 --> n62
    n55 --> n62
    n59 --> n62
    n56 --> n53
    n75 --> n85
    n56 --> n55
    n4 --> n70
    n60 --> n70
    n55 --> n4
    n70 --> n81
    n54 x--x n56
```

# CAN_war_bonds

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18["CAN_canada_pacific_railway"]
        n19["CAN_crown_corporations"]
        n20["CAN_defence_of_canada_regulations"]
        n21["CAN_national_resources_mobilization_act"]
        n22["CAN_national_steel_car"]
        n24(("CAN_war_bonds"))
    end
    subgraph tier_1["Tier 1"]
        n25["CAN_department_of_munitions_and_supply"]
    end
    subgraph tier_2["Tier 2"]
        n27["CAN_bits_and_pieces_program"]
        n29["CAN_fund_the_national_research_council"]
        n30["CAN_victory_aircraft_limited"]
    end
    subgraph tier_3["Tier 3"]
        n31["CAN_john_inglis_and_company"]
        n32["CAN_polymer_corporation"]
        n33["CAN_retool_angus_shops"]
    end
    subgraph tier_4["Tier 4"]
        n34["CAN_if_day"]
        n35["CAN_imperial_oil"]
        n36["CAN_uranium_mining"]
    end
    subgraph tier_5["Tier 5"]
        n37["CAN_defense_research_grants"]
        n38["CAN_war_fueled_economy"]
    end
    n25 --> n27
    n34 --> n37
    n19 --> n25
    n20 --> n25
    n24 --> n25
    n25 --> n29
    n21 --> n29
    n31 --> n34
    n30 --> n34
    n33 --> n35
    n27 --> n31
    n30 --> n32
    n29 --> n32
    n18 --> n33
    n27 --> n33
    n32 --> n36
    n22 --> n36
    n25 --> n30
    n22 --> n38
    n34 --> n38
```
