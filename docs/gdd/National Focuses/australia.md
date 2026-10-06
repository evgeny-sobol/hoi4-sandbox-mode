# AST_additional_militia_training

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("AST_additional_militia_training"))
        n2["AST_volunteer_air_observers_corps"]
    end
    subgraph tier_1["Tier 1"]
        n3["AST_promote_reservists"]
        n4["AST_royal_australian_artillery"]
    end
    subgraph tier_2["Tier 2"]
        n5["AST_daimler_dingo"]
        n6["AST_hmas_assault"]
        n7["AST_specialize_equipment"]
    end
    subgraph tier_3["Tier 3"]
        n8["AST_airborne_defence"]
        n9["AST_australian_army_catering_corps"]
        n10["AST_australian_womens_army_service"]
        n11["AST_fund_owen_gun_research"]
        n12["AST_sentinel_tank_project"]
    end
    subgraph tier_4["Tier 4"]
        n13["AST_introduce_unconventional_warfare"]
    end
    subgraph tier_5["Tier 5"]
        n14["AST_central_bureau"]
        n15["AST_m_special_unit"]
        n16["AST_z_special_unit"]
    end
    n7 --> n8
    n2 --> n8
    n6 --> n9
    n6 --> n10
    n13 --> n14
    n4 --> n5
    n6 --> n11
    n4 --> n6
    n3 --> n6
    n12 --> n13
    n8 --> n13
    n13 --> n15
    n1 --> n3
    n1 --> n4
    n5 --> n12
    n3 --> n7
    n13 --> n16
```

# AST_cockatoo_island_shipyards

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17{"AST_cockatoo_island_shipyards"}
        n18{"AST_kangaroo_point_shipyards"}
    end
    subgraph tier_1["Tier 1"]
        n19["AST_fly_the_jolly_roger"]
        n20["AST_protect_overseas_commerce"]
    end
    subgraph tier_2["Tier 2"]
        n21["AST_royal_australian_submarine_service"]
        n22["AST_scrap_iron_flotilla"]
    end
    subgraph tier_3["Tier 3"]
        n23["AST_naval_auxiliary_patrol"]
    end
    subgraph tier_4["Tier 4"]
        n24["AST_cruisers"]
        n25["AST_pacific_area_navy"]
    end
    n23 --> n24
    n17 --> n19
    n18 --> n19
    n21 --> n23
    n22 --> n23
    n23 --> n25
    n17 --> n20
    n18 --> n20
    n20 --> n21
    n19 --> n21
    n20 --> n22
    n19 --> n22
    n19 x--x n20
```

# AST_establish_advisory_war_council

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n26["AST_department_of_supply_and_development"]
        n27(("AST_establish_advisory_war_council"))
        n28["AST_expand_the_northern_railway"]
        n29["AST_strengthen_ties_with_uk"]
    end
    subgraph tier_1["Tier 1"]
        n30["AST_national_security_act"]
        n31["AST_volunteer_defence_corps"]
    end
    subgraph tier_2["Tier 2"]
        n32["AST_army_inventions_directorate"]
        n33["AST_citizen_military_forces"]
        n34["AST_civil_construction_corps"]
        n35["AST_invest_in_victory"]
        n36["AST_rats_of_tobruk"]
    end
    subgraph tier_3["Tier 3"]
        n37["AST_allied_works_council"]
        n38["AST_classify_aliens"]
        n39["AST_rationing_and_recycling"]
        n40["AST_squash_the_squanderbugs"]
    end
    subgraph tier_4["Tier 4"]
        n41["AST_australian_arms_production"]
        n42["AST_fight_work_or_perish"]
        n43["AST_fund_australian_defense_research"]
    end
    subgraph tier_5["Tier 5"]
        n44["AST_research_collaboration"]
        n45["AST_uranium_mining"]
    end
    n26 --> n37
    n34 --> n37
    n30 --> n32
    n37 --> n41
    n31 --> n33
    n30 --> n34
    n33 --> n38
    n34 --> n42
    n40 --> n42
    n39 --> n43
    n38 --> n43
    n30 --> n35
    n27 --> n30
    n35 --> n39
    n31 --> n36
    n29 --> n36
    n42 --> n44
    n41 --> n44
    n35 --> n40
    n28 --> n45
    n41 --> n45
    n27 --> n31
```

# AST_expand_the_raaf

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n46(("AST_expand_the_raaf"))
        n12["AST_sentinel_tank_project"]
        n7["AST_specialize_equipment"]
    end
    subgraph tier_1["Tier 1"]
        n47["AST_cac_boomerang"]
        n48["AST_cac_woomera"]
        n49["AST_expand_northern_presence"]
    end
    subgraph tier_2["Tier 2"]
        n50["AST_naval_bombers"]
        n2["AST_volunteer_air_observers_corps"]
    end
    subgraph tier_3["Tier 3"]
        n8["AST_airborne_defence"]
        n51["AST_death_from_down_under"]
        n52["AST_womens_auxilliary_australian_air_force"]
    end
    subgraph tier_4["Tier 4"]
        n53["AST_dominate_the_skies"]
        n13["AST_introduce_unconventional_warfare"]
    end
    subgraph tier_5["Tier 5"]
        n14["AST_central_bureau"]
        n15["AST_m_special_unit"]
        n16["AST_z_special_unit"]
    end
    n7 --> n8
    n2 --> n8
    n46 --> n47
    n46 --> n48
    n13 --> n14
    n2 --> n51
    n52 --> n53
    n46 --> n49
    n12 --> n13
    n8 --> n13
    n13 --> n15
    n48 --> n50
    n47 --> n2
    n49 --> n2
    n2 --> n52
    n50 --> n52
    n13 --> n16
```

# AST_industries_assistance_corporation

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n34["AST_civil_construction_corps"]
        n42["AST_fight_work_or_perish"]
        n54(("AST_industries_assistance_corporation"))
        n55["AST_standard_gauge_railway"]
    end
    subgraph tier_1["Tier 1"]
        n56["AST_western_australian_government_railways"]
    end
    subgraph tier_2["Tier 2"]
        n26["AST_department_of_supply_and_development"]
        n57["AST_south_australian_housing_trust"]
    end
    subgraph tier_3["Tier 3"]
        n37["AST_allied_works_council"]
        n58["AST_expand_lithgow_small_arms_factory"]
    end
    subgraph tier_4["Tier 4"]
        n41["AST_australian_arms_production"]
        n28["AST_expand_the_northern_railway"]
    end
    subgraph tier_5["Tier 5"]
        n44["AST_research_collaboration"]
        n45["AST_uranium_mining"]
    end
    n26 --> n37
    n34 --> n37
    n37 --> n41
    n56 --> n26
    n57 --> n58
    n58 --> n28
    n42 --> n44
    n41 --> n44
    n56 --> n57
    n28 --> n45
    n41 --> n45
    n55 --> n56
    n54 --> n56
```

# AST_kangaroo_point_shipyards

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17{"AST_cockatoo_island_shipyards"}
        n18{"AST_kangaroo_point_shipyards"}
    end
    subgraph tier_1["Tier 1"]
        n19["AST_fly_the_jolly_roger"]
        n20["AST_protect_overseas_commerce"]
    end
    subgraph tier_2["Tier 2"]
        n21["AST_royal_australian_submarine_service"]
        n22["AST_scrap_iron_flotilla"]
    end
    subgraph tier_3["Tier 3"]
        n23["AST_naval_auxiliary_patrol"]
    end
    subgraph tier_4["Tier 4"]
        n24["AST_cruisers"]
        n25["AST_pacific_area_navy"]
    end
    n23 --> n24
    n17 --> n19
    n18 --> n19
    n21 --> n23
    n22 --> n23
    n23 --> n25
    n17 --> n20
    n18 --> n20
    n20 --> n21
    n19 --> n21
    n20 --> n22
    n19 --> n22
    n19 x--x n20
```

# AST_never_another_gallipoli

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n59{"AST_never_another_gallipoli"}
        n60["AST_support_the_policy_of_appeasement"]
    end
    subgraph tier_1["Tier 1"]
        n61{"AST_abandon_the_westminster_system"}
        n62["AST_protect_the_homeland"]
    end
    subgraph tier_2["Tier 2"]
        n63["AST_empower_the_workers"]
        n64["AST_sever_ties_with_uk"]
        n65["AST_support_the_centre_party"]
        n66["AST_the_swpa_menace"]
    end
    subgraph tier_3["Tier 3"]
        n67["AST_delegation_to_china"]
        n68{"AST_demand_new_zealand"}
        n69["AST_protect_the_dutch_colonies"]
        n70["AST_supply_indonesian_nationalists"]
        n71["AST_woo_usa"]
    end
    subgraph tier_4["Tier 4"]
        n72{"AST_commitment_to_the_cause"}
        n73["AST_support_indonesian_uprising"]
        n74["AST_the_south_west_pacific_initiative"]
    end
    subgraph tier_5["Tier 5"]
        n75{"AST_direct_support"}
        n76{"AST_indirect_support"}
        n77{"AST_protect_the_south_west_pacific"}
        n78["AST_research_cooperation"]
    end
    subgraph tier_6["Tier 6"]
        n79["AST_a_deal_with_japan"]
        n80["AST_join_comintern"]
        n81["AST_our_own_empire"]
        n82["AST_preemptive_intervention"]
        n83["AST_workers_paradise"]
    end
    subgraph tier_7["Tier 7"]
        n84["AST_japan_tech_sharing"]
        n85["AST_nz_puppet"]
        n86["AST_research_city_excursions"]
        n87["AST_the_threat_against_the_people"]
        n88["AST_war_on_japan"]
    end
    n77 --> n79
    n59 --> n61
    n67 --> n72
    n63 --> n67
    n65 --> n68
    n63 --> n68
    n72 --> n75
    n61 --> n63
    n72 --> n76
    n79 --> n84
    n76 --> n80
    n75 --> n80
    n83 --> n85
    n80 --> n85
    n77 --> n81
    n68 --> n81
    n78 --> n82
    n64 --> n69
    n59 --> n62
    n73 --> n77
    n80 --> n86
    n74 --> n78
    n62 --> n64
    n65 --> n70
    n70 --> n73
    n61 --> n65
    n71 --> n74
    n69 --> n74
    n62 --> n66
    n83 --> n87
    n81 --> n88
    n66 --> n71
    n64 --> n71
    n75 --> n83
    n79 x--x n81
    n61 x--x n62
    n75 x--x n76
    n63 x--x n65
    n80 x--x n83
    n59 x--x n60
```

# AST_standard_gauge_railway

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n34["AST_civil_construction_corps"]
        n42["AST_fight_work_or_perish"]
        n54["AST_industries_assistance_corporation"]
        n55(("AST_standard_gauge_railway"))
    end
    subgraph tier_1["Tier 1"]
        n56["AST_western_australian_government_railways"]
    end
    subgraph tier_2["Tier 2"]
        n26["AST_department_of_supply_and_development"]
        n57["AST_south_australian_housing_trust"]
    end
    subgraph tier_3["Tier 3"]
        n37["AST_allied_works_council"]
        n58["AST_expand_lithgow_small_arms_factory"]
    end
    subgraph tier_4["Tier 4"]
        n41["AST_australian_arms_production"]
        n28["AST_expand_the_northern_railway"]
    end
    subgraph tier_5["Tier 5"]
        n44["AST_research_collaboration"]
        n45["AST_uranium_mining"]
    end
    n26 --> n37
    n34 --> n37
    n37 --> n41
    n56 --> n26
    n57 --> n58
    n58 --> n28
    n42 --> n44
    n41 --> n44
    n56 --> n57
    n28 --> n45
    n41 --> n45
    n55 --> n56
    n54 --> n56
```

# AST_support_the_policy_of_appeasement

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n59["AST_never_another_gallipoli"]
        n60(("AST_support_the_policy_of_appeasement"))
        n31["AST_volunteer_defence_corps"]
    end
    subgraph tier_1["Tier 1"]
        n29["AST_strengthen_ties_with_uk"]
        n89["AST_the_singapore_strategy"]
    end
    subgraph tier_2["Tier 2"]
        n90["AST_adopt_westminster"]
        n36["AST_rats_of_tobruk"]
    end
    subgraph tier_3["Tier 3"]
        n91["AST_CSIR"]
        n92["AST_swpa_protector"]
    end
    subgraph tier_4["Tier 4"]
        n93["AST_commonwealth_aircraft_corporation"]
        n94["AST_empire_air_training_scheme"]
    end
    n90 --> n91
    n29 --> n90
    n89 --> n90
    n91 --> n93
    n92 --> n93
    n91 --> n94
    n92 --> n94
    n31 --> n36
    n29 --> n36
    n60 --> n29
    n90 --> n92
    n60 --> n89
    n59 x--x n60
```
