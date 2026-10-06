# POR_army_reorganization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("POR_army_reorganization"))
    end
    subgraph tier_1["Tier 1"]
        n2["POR_corpo_do_estado_maior"]
        n3["POR_metropolitan_army"]
    end
    subgraph tier_2["Tier 2"]
        n4["POR_staff_wargames"]
        n5{"POR_standardization"}
    end
    subgraph tier_3["Tier 3"]
        n6["POR_defend_the_borders"]
        n7["POR_field_maneuvers"]
        n8["POR_rebuild_the_lines_of_torres_vedras"]
    end
    subgraph tier_4["Tier 4"]
        n9["POR_tropas_paraquedistas"]
    end
    subgraph tier_5["Tier 5"]
        n10["POR_regimento_de_comandos"]
    end
    n1 --> n2
    n5 --> n6
    n4 --> n7
    n1 --> n3
    n5 --> n8
    n9 --> n10
    n2 --> n4
    n3 --> n5
    n6 --> n9
    n8 --> n9
    n6 x--x n8
```

# POR_colonial_assimilation_policy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n11{"POR_colonial_assimilation_policy"}
        n12["POR_roads_bridges_and_dams"]
    end
    subgraph tier_1["Tier 1"]
        n13{"POR_colonial_army"}
        n14["POR_haven_of_neutrality_macau"]
        n15["POR_infrastructure_in_angola"]
        n16["POR_luso_tropicalism"]
        n17{"POR_restart_investment_into_timor"}
    end
    subgraph tier_2["Tier 2"]
        n18["POR_develop_north_angola"]
        n19["POR_invest_in_sandalwood_and_coffee_production"]
        n20["POR_limited_self_rule"]
        n21["POR_revert_the_local_autonomy_policies"]
    end
    subgraph tier_3["Tier 3"]
        n22["POR_develop_south_angola"]
    end
    subgraph tier_4["Tier 4"]
        n23["POR_develop_mozambique"]
        n24["POR_portuguese_oil"]
    end
    n11 --> n13
    n22 --> n23
    n15 --> n18
    n12 --> n18
    n18 --> n22
    n11 --> n14
    n11 --> n15
    n17 --> n19
    n13 --> n20
    n11 --> n16
    n22 --> n24
    n11 --> n17
    n17 --> n21
    n19 x--x n21
    n20 x--x n16
```

# POR_continue_the_public_works

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n25{"POR_continue_the_public_works"}
        n15["POR_infrastructure_in_angola"]
        n26["POR_naval_research_institute"]
    end
    subgraph tier_1["Tier 1"]
        n27["POR_food_industries"]
        n28{"POR_instituto_superior_tecnico"}
    end
    subgraph tier_2["Tier 2"]
        n29["POR_industrial_modernization"]
        n30["POR_ogma"]
        n31["POR_ogme"]
        n12["POR_roads_bridges_and_dams"]
        n32["POR_textile_industry"]
    end
    subgraph tier_3["Tier 3"]
        n33["POR_a_new_industry"]
        n18["POR_develop_north_angola"]
        n34["POR_extraction_industries"]
        n35{"POR_light_aircraft_focus"}
        n36["POR_military_vehicles"]
        n37["POR_portuguese_artillery"]
    end
    subgraph tier_4["Tier 4"]
        n38["POR_advanced_light_aircraft"]
        n22["POR_develop_south_angola"]
        n39["POR_hydroelectricity"]
        n40{"POR_military_research_facilities"}
    end
    subgraph tier_5["Tier 5"]
        n41["POR_advanced_artillery"]
        n42["POR_air_naval_research"]
        n43["POR_armor_focus"]
        n23["POR_develop_mozambique"]
        n44["POR_jet_research"]
        n24["POR_portuguese_oil"]
    end
    subgraph tier_6["Tier 6"]
        n45["POR_mechanized_focus"]
    end
    n29 --> n33
    n37 --> n41
    n40 --> n41
    n35 --> n38
    n26 --> n42
    n38 --> n42
    n40 --> n43
    n22 --> n23
    n15 --> n18
    n12 --> n18
    n18 --> n22
    n12 --> n34
    n25 --> n27
    n34 --> n39
    n28 --> n29
    n25 --> n28
    n38 --> n44
    n30 --> n35
    n43 --> n45
    n36 --> n40
    n37 --> n40
    n35 --> n40
    n31 --> n36
    n28 --> n30
    n28 --> n31
    n31 --> n37
    n22 --> n24
    n28 --> n12
    n27 --> n32
    n38 x--x n43
    n27 x--x n29
```

# POR_estado_novo

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n46{"POR_estado_novo"}
        n47{"POR_popular_front"}
        n48["POR_support_the_spanish_republic"]
        n49["POR_the_popular_front_bloc"]
        n50["POR_they_need_our_help"]
    end
    subgraph tier_1["Tier 1"]
        n51["POR_a_royal_wedding"]
        n52["POR_strict_neutrality_in_the_spanish_civil_war"]
        n53["POR_support_the_spanish_nationalists"]
    end
    subgraph tier_2["Tier 2"]
        n54["POR_british_guns"]
        n55["POR_british_investment_in_mines"]
        n56{"POR_portuguese_legion"}
        n57["POR_the_return_of_duarte"]
    end
    subgraph tier_3["Tier 3"]
        n58["POR_british_industrial_investments"]
        n59["POR_monarchist_uprising_in_brazil"]
        n60["POR_national_syndicalism"]
        n61["POR_observation_mission"]
        n62["POR_promote_the_monarchist_cause_in_portugal"]
        n63["POR_strengthen_the_regime"]
        n64["POR_support_a_spanish_monarchy_in_the_war"]
    end
    subgraph tier_4["Tier 4"]
        n65{"POR_allow_free_elections"}
        n66["POR_appease_monarchists"]
        n67["POR_assist_the_requetes"]
        n68["POR_ditadura_militar"]
        n69["POR_refuse_the_naval_blockade"]
        n70{"POR_restoration_of_the_monarchy"}
        n71{"POR_send_assistance"}
        n72["POR_the_capital_of_espionage"]
        n73{"POR_the_empire_of_brazil"}
    end
    subgraph tier_5["Tier 5"]
        n74{"POR_camisas_azuis"}
        n75{"POR_concordat_with_the_holy_see"}
        n76["POR_iberian_summit"]
        n77["POR_intervention_in_spain"]
        n78["POR_join_the_allies"]
        n79{"POR_join_the_carlist_fight"}
        n80{"POR_mapa_cor_de_rosa"}
        n81{"POR_national_gold_reserves"}
        n82["POR_nationalist_intervention"]
        n83["POR_protect_chinese_civilians"]
        n84["POR_remember_olivenca"]
        n85["POR_securing_the_free_world"]
        n86["POR_the_kingdom_reunited"]
    end
    subgraph tier_6["Tier 6"]
        n87["POR_honor_anglo_portuguese_alliance"]
        n88["POR_join_the_axis"]
        n89["POR_proudly_alone"]
        n90["POR_recover_brazil"]
        n91["POR_recover_the_east_indies"]
        n92["POR_the_fifth_empire"]
        n93["POR_the_royal_iberian_alliance"]
    end
    subgraph tier_7["Tier 7"]
        n94["POR_deal_with_fascism"]
        n95["POR_deal_with_the_japanese_threat"]
        n96["POR_expand_the_chinese_territories"]
        n97["POR_latin_america"]
        n98["POR_oppose_germany"]
        n99["POR_research_agreements"]
        n100["POR_research_sharing"]
        n101["POR_the_eastern_menace"]
    end
    subgraph tier_8["Tier 8"]
        n102["POR_the_communist_threat"]
    end
    n46 --> n51
    n58 --> n65
    n63 --> n66
    n64 --> n67
    n52 --> n54
    n55 --> n58
    n54 --> n58
    n52 --> n55
    n68 --> n74
    n66 --> n75
    n84 --> n94
    n93 --> n94
    n92 --> n95
    n91 --> n95
    n60 --> n68
    n88 --> n96
    n92 --> n96
    n75 --> n87
    n65 --> n76
    n71 --> n76
    n50 --> n77
    n65 --> n77
    n65 --> n78
    n74 --> n88
    n67 --> n79
    n86 --> n97
    n90 --> n97
    n69 --> n80
    n57 --> n59
    n66 --> n81
    n56 --> n60
    n71 --> n82
    n56 --> n61
    n78 --> n98
    n87 --> n98
    n53 --> n56
    n57 --> n62
    n50 --> n83
    n65 --> n83
    n49 --> n83
    n81 --> n89
    n75 --> n89
    n80 --> n90
    n80 --> n91
    n60 --> n69
    n57 --> n69
    n70 --> n84
    n88 --> n99
    n78 --> n100
    n87 --> n100
    n62 --> n70
    n65 --> n85
    n61 --> n71
    n56 --> n63
    n47 --> n52
    n46 --> n52
    n57 --> n64
    n46 --> n53
    n63 --> n72
    n97 --> n102
    n89 --> n102
    n89 --> n101
    n59 --> n73
    n74 --> n92
    n70 --> n86
    n73 --> n86
    n51 --> n57
    n79 --> n93
    n51 x--x n52
    n51 x--x n53
    n51 x--x n48
    n46 x--x n47
    n87 x--x n89
    n76 x--x n82
    n88 x--x n92
    n60 x--x n63
    n90 x--x n86
    n84 x--x n93
    n52 x--x n53
    n52 x--x n48
    n53 x--x n48
```

# POR_popular_front

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n51["POR_a_royal_wedding"]
        n46{"POR_estado_novo"}
        n87["POR_honor_anglo_portuguese_alliance"]
        n82["POR_nationalist_intervention"]
        n47{"POR_popular_front"}
        n71{"POR_send_assistance"}
        n53["POR_support_the_spanish_nationalists"]
    end
    subgraph tier_1["Tier 1"]
        n103["POR_nation_in_arms"]
        n52["POR_strict_neutrality_in_the_spanish_civil_war"]
        n48{"POR_support_the_spanish_republic"}
    end
    subgraph tier_2["Tier 2"]
        n54["POR_british_guns"]
        n55["POR_british_investment_in_mines"]
        n104["POR_nationalize_industry"]
        n105["POR_unify_leftist_youth_wings"]
        n106["POR_visit_the_front"]
        n107["POR_workers_of_iberia_unite"]
    end
    subgraph tier_3["Tier 3"]
        n58["POR_british_industrial_investments"]
        n108{"POR_reorganization_of_the_communist_party"}
        n109{"POR_the_iberian_socialist_union"}
        n50["POR_they_need_our_help"]
    end
    subgraph tier_4["Tier 4"]
        n65{"POR_allow_free_elections"}
        n110["POR_join_the_comintern"]
        n49["POR_the_popular_front_bloc"]
    end
    subgraph tier_5["Tier 5"]
        n111["POR_cooperate_with_french_militants"]
        n76["POR_iberian_summit"]
        n77["POR_intervention_in_spain"]
        n78["POR_join_the_allies"]
        n112["POR_latin_american_communism"]
        n83["POR_protect_chinese_civilians"]
        n113["POR_research_collaboration"]
        n85["POR_securing_the_free_world"]
    end
    subgraph tier_6["Tier 6"]
        n114["POR_anti_fascism"]
        n98["POR_oppose_germany"]
        n115["POR_our_comrades_overseas"]
        n100["POR_research_sharing"]
    end
    n58 --> n65
    n111 --> n114
    n52 --> n54
    n55 --> n58
    n54 --> n58
    n52 --> n55
    n110 --> n111
    n49 --> n111
    n65 --> n76
    n71 --> n76
    n50 --> n77
    n65 --> n77
    n65 --> n78
    n108 --> n110
    n49 --> n112
    n47 --> n103
    n103 --> n104
    n78 --> n98
    n87 --> n98
    n112 --> n115
    n50 --> n83
    n65 --> n83
    n49 --> n83
    n104 --> n108
    n105 --> n108
    n110 --> n113
    n78 --> n100
    n87 --> n100
    n65 --> n85
    n47 --> n52
    n46 --> n52
    n47 --> n48
    n107 --> n109
    n109 --> n49
    n106 --> n50
    n103 --> n105
    n48 --> n106
    n48 --> n107
    n51 x--x n52
    n51 x--x n48
    n46 x--x n47
    n76 x--x n82
    n110 x--x n49
    n52 x--x n53
    n52 x--x n48
    n53 x--x n48
    n106 x--x n107
```

# POR_second_navy_reequipment

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n38["POR_advanced_light_aircraft"]
        n116(("POR_second_navy_reequipment"))
    end
    subgraph tier_1["Tier 1"]
        n117["POR_a_powerful_merchant_marine"]
        n118["POR_arsenal_do_alfeite"]
        n119["POR_submarine_effort"]
    end
    subgraph tier_2["Tier 2"]
        n120["POR_merchant_marine_protection"]
        n121["POR_national_cruiser_production"]
    end
    subgraph tier_3["Tier 3"]
        n122["POR_atlantic_defense_strategy"]
        n123["POR_battleship_effort"]
        n124["POR_carrier_effort"]
        n125["POR_fuzileiros"]
    end
    subgraph tier_4["Tier 4"]
        n126["POR_endless_sea"]
        n26["POR_naval_research_institute"]
    end
    subgraph tier_5["Tier 5"]
        n42["POR_air_naval_research"]
    end
    n116 --> n117
    n26 --> n42
    n38 --> n42
    n116 --> n118
    n121 --> n122
    n121 --> n123
    n121 --> n124
    n122 --> n126
    n119 --> n125
    n120 --> n125
    n117 --> n120
    n118 --> n121
    n125 --> n26
    n116 --> n119
```
