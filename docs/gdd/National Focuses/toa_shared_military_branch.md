# SMB_air_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("SMB_air_force"))
        n2["SMB_army"]
        n3["SMB_army_academy"]
        n4["SMB_blue_water_fleet"]
        n5["SMB_experimental_weapons_department"]
        n6["SMB_navy"]
    end
    subgraph tier_1["Tier 1"]
        n7{"SMB_air_academy"}
        n8["SMB_air_defense"]
        n9{"SMB_construct_air_bases"}
        n10["SMB_fortification_effort"]
    end
    subgraph tier_2["Tier 2"]
        n11["SMB_domestic_designs"]
        n12["SMB_joint_operative_command"]
        n13["SMB_license_designs"]
        n14["SMB_purchase_aircraft"]
    end
    subgraph tier_3["Tier 3"]
        n15{"SMB_establish_aircraft_industry"}
        n16["SMB_war_planning_office"]
        n17["SMB_women_in_aviation"]
    end
    subgraph tier_4["Tier 4"]
        n18{"SMB_flying_fortress"}
        n19{"SMB_nimble_air_force"}
        n20{"SMB_tactical_air_force"}
    end
    subgraph tier_5["Tier 5"]
        n21["SMB_army_support"]
        n22["SMB_naval_support"]
        n23["SMB_strategic_bombing"]
        n24["SMB_winning_the_air_war"]
    end
    subgraph tier_6["Tier 6"]
        n25["SMB_air_doctrine"]
        n26["SMB_air_modifier_boost_1"]
        n27["SMB_air_modifier_boost_2"]
        n28["SMB_aircraft_carriers"]
        n29["SMB_nuclear_program"]
    end
    n1 --> n7
    n2 --> n8
    n1 --> n8
    n24 --> n25
    n22 --> n25
    n23 --> n25
    n21 --> n25
    n23 --> n26
    n21 --> n26
    n24 --> n27
    n22 --> n27
    n22 --> n28
    n4 --> n28
    n18 --> n21
    n20 --> n21
    n1 --> n9
    n7 --> n11
    n9 --> n11
    n13 --> n15
    n11 --> n15
    n14 --> n15
    n15 --> n18
    n1 --> n10
    n6 --> n10
    n3 --> n12
    n7 --> n12
    n7 --> n13
    n9 --> n13
    n19 --> n22
    n15 --> n19
    n5 --> n29
    n23 --> n29
    n7 --> n14
    n9 --> n14
    n18 --> n23
    n15 --> n20
    n12 --> n16
    n20 --> n24
    n19 --> n24
    n12 --> n17
    n21 x--x n23
    n21 x--x n24
    n11 x--x n13
    n11 x--x n14
    n18 x--x n19
    n18 x--x n20
    n13 x--x n14
    n22 x--x n24
    n19 x--x n20
```

# SMB_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n7["SMB_air_academy"]
        n1["SMB_air_force"]
        n2(("SMB_army"))
        n23["SMB_strategic_bombing"]
    end
    subgraph tier_1["Tier 1"]
        n8["SMB_air_defense"]
        n3{"SMB_army_academy"}
        n30["SMB_department_of_propaganda"]
        n31["SMB_logistics_department"]
        n32{"SMB_military_facilities"}
    end
    subgraph tier_2["Tier 2"]
        n33["SMB_department_of_military_intelligence"]
        n12["SMB_joint_operative_command"]
        n34["SMB_motorized"]
        n35["SMB_regular_infantry"]
        n36["SMB_support_company"]
    end
    subgraph tier_3["Tier 3"]
        n37{"SMB_artillery"}
        n38["SMB_jungle_warfare_training"]
        n39{"SMB_tank_warfare"}
        n16["SMB_war_planning_office"]
        n17["SMB_women_in_aviation"]
    end
    subgraph tier_4["Tier 4"]
        n40["SMB_brown_water_navy"]
        n41{"SMB_domestic_production"}
        n42{"SMB_foreign_designs"}
        n43["SMB_jungle_pioneers"]
        n44["SMB_mechanized_troops"]
    end
    subgraph tier_5["Tier 5"]
        n45["SMB_atacama_training"]
        n46{"SMB_foreign_advisors"}
        n47["SMB_tierra_del_fuego_training"]
    end
    subgraph tier_6["Tier 6"]
        n48["SMB_a_land_of_mountains"]
        n49["SMB_army_professionalism"]
        n50["SMB_conscription"]
    end
    subgraph tier_7["Tier 7"]
        n5["SMB_experimental_weapons_department"]
        n51{"SMB_special_forces"}
    end
    subgraph tier_8["Tier 8"]
        n29["SMB_nuclear_program"]
        n52["SMB_special_forces_option_1"]
        n53["SMB_special_forces_option_2"]
        n54["SMB_special_forces_option_3"]
    end
    subgraph tier_9["Tier 9"]
        n55["SMB_mountain_guns"]
        n56["SMB_special_forces_option_1_continuation"]
        n57["SMB_special_forces_option_2_continuation"]
        n58["SMB_special_forces_option_3_continuation"]
    end
    n45 --> n48
    n47 --> n48
    n2 --> n8
    n1 --> n8
    n2 --> n3
    n46 --> n49
    n35 --> n37
    n34 --> n37
    n41 --> n45
    n42 --> n45
    n38 --> n40
    n46 --> n50
    n30 --> n33
    n2 --> n30
    n39 --> n41
    n49 --> n5
    n50 --> n5
    n41 --> n46
    n42 --> n46
    n39 --> n42
    n37 --> n42
    n3 --> n12
    n7 --> n12
    n38 --> n43
    n35 --> n38
    n2 --> n31
    n39 --> n44
    n34 --> n44
    n2 --> n32
    n32 --> n34
    n3 --> n34
    n52 --> n55
    n5 --> n29
    n23 --> n29
    n3 --> n35
    n32 --> n35
    n49 --> n51
    n50 --> n51
    n51 --> n52
    n52 --> n56
    n51 --> n53
    n53 --> n57
    n51 --> n54
    n54 --> n58
    n31 --> n36
    n34 --> n39
    n35 --> n39
    n41 --> n47
    n42 --> n47
    n12 --> n16
    n12 --> n17
    n49 x--x n50
    n45 x--x n47
    n41 x--x n42
    n34 x--x n35
    n52 x--x n53
    n52 x--x n54
    n53 x--x n54
```

# SMB_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["SMB_air_force"]
        n22["SMB_naval_support"]
        n6(("SMB_navy"))
    end
    subgraph tier_1["Tier 1"]
        n59["SMB_construct_naval_bases"]
        n10["SMB_fortification_effort"]
        n60["SMB_naval_academy"]
    end
    subgraph tier_2["Tier 2"]
        n61{"SMB_expand_repair_yards"}
        n62["SMB_naval_foreign_advisors"]
        n63["SMB_purchase_destroyers_and_subs"]
    end
    subgraph tier_3["Tier 3"]
        n64["SMB_carrier_conversion"]
        n65["SMB_merchant_marine"]
        n66{"SMB_reescalate_the_naval_arms_race"}
    end
    subgraph tier_4["Tier 4"]
        n4["SMB_blue_water_fleet"]
        n67["SMB_coastal_fleet"]
        n68["SMB_enlarge_naval_facilities"]
    end
    subgraph tier_5["Tier 5"]
        n28["SMB_aircraft_carriers"]
        n69["SMB_minelaying"]
        n70{"SMB_purchase_cruisers_and_dreadnoughts"}
    end
    subgraph tier_6["Tier 6"]
        n71["SMB_escort_fleet"]
        n72{"SMB_raiding_fleet"}
    end
    subgraph tier_7["Tier 7"]
        n73["SMB_cruiser_subs"]
        n74["SMB_degaussing"]
        n75["SMB_midget_subs"]
        n76["SMB_naval_invasion"]
    end
    n22 --> n28
    n4 --> n28
    n66 --> n4
    n61 --> n64
    n66 --> n67
    n6 --> n59
    n72 --> n73
    n71 --> n74
    n61 --> n68
    n66 --> n68
    n70 --> n71
    n59 --> n61
    n1 --> n10
    n6 --> n10
    n61 --> n65
    n72 --> n75
    n67 --> n69
    n6 --> n60
    n60 --> n62
    n59 --> n62
    n71 --> n76
    n4 --> n70
    n67 --> n70
    n59 --> n63
    n60 --> n63
    n70 --> n72
    n62 --> n66
    n63 --> n66
    n4 x--x n67
    n73 x--x n75
    n68 x--x n65
    n71 x--x n72
```
