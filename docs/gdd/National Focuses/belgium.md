# BEL_belgian_air_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("BEL_belgian_air_force"))
        n2["CONGO_aviation_militaire_de_la_force_publique"]
    end
    subgraph tier_1["Tier 1"]
        n3["BEL_develop_belgian_air_industry"]
        n4["BEL_foreign_plane_purchases"]
    end
    subgraph tier_2["Tier 2"]
        n5["BEL_aviation_school"]
        n6["BEL_polish_licences"]
        n7["BEL_renard_constructions_aeronautiques"]
        n8["BEL_stampe_et_vertrongen"]
    end
    subgraph tier_3["Tier 3"]
        n9["BEL_air_doctrine"]
        n10["BEL_early_helicopters"]
        n11["BEL_legacy_of_the_belgian_airforce"]
        n12["BEL_pressurized_cabin_development"]
        n13["BEL_relocate_air_production"]
    end
    n5 --> n9
    n4 --> n5
    n3 --> n5
    n1 --> n3
    n5 --> n10
    n1 --> n4
    n5 --> n11
    n4 --> n6
    n7 --> n12
    n2 --> n12
    n7 --> n13
    n8 --> n13
    n3 --> n7
    n3 --> n8
```

# BEL_government_resigns

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n14["BEL_dyle_plan"]
        n15{"BEL_government_resigns"}
        n16["BEL_repudiate_treaty_with_france"]
    end
    subgraph tier_1["Tier 1"]
        n17["BEL_government_of_national_unity"]
        n18["BEL_investigate_bribery_charges"]
        n19["BEL_vandervelde_minority"]
    end
    subgraph tier_2["Tier 2"]
        n20["BEL_problem_of_language"]
        n21{"BEL_royal_intervention"}
    end
    subgraph tier_3["Tier 3"]
        n22["BEL_cooperative_cooperation"]
        n23{"BEL_degrelle"}
        n24["BEL_paul_emile_janson"]
        n25["BEL_trade_union_support"]
    end
    subgraph tier_4["Tier 4"]
        n26["BEL_aid_for_spain"]
        n27["BEL_constitutional_crisis"]
        n28["BEL_la_belgique_et_le_congo"]
        n29["BEL_plan_de_man"]
        n30["BEL_support_the_rexists"]
        n31["BEL_support_the_vnv"]
        n32["BEL_the_grand_place"]
    end
    subgraph tier_5["Tier 5"]
        n33["BEL_abandon_neutrality"]
        n34["BEL_contradictions_in_socialism"]
        n35["BEL_dissolve_political_parties"]
        n36["BEL_economic_recovery"]
        n37["BEL_growing_threat_of_fascism"]
        n38["BEL_kings_abdication"]
        n39["BEL_revitalize_nederlands"]
        n40["BEL_spanish_intervention"]
        n41["BEL_the_flemish_question"]
        n42["BEL_the_french_horse_and_the_red_rider"]
    end
    subgraph tier_6["Tier 6"]
        n43{"BEL_adriaan_martens_crisis"}
        n44["BEL_christian_corporatism"]
        n45["BEL_flanders_ascendant"]
        n46{"BEL_international_socialist_bureau"}
        n47["BEL_international_stipend"]
        n48["BEL_legacy_of_the_soldier_king"]
        n49["BEL_nationalize_the_banks"]
        n50["BEL_peacekeeping_missions"]
        n51["BEL_royal_commander_in_chief"]
        n52["BEL_snap_election"]
    end
    subgraph tier_7["Tier 7"]
        n53["BEL_benelux_union"]
        n54["BEL_civil_service_purge"]
        n55["BEL_dietsland"]
        n56["BEL_liberal_victory"]
        n57{"BEL_socialist_victory"}
        n58{"BEL_the_lost_tribe"}
        n59["BEL_traditional_family_values"]
        n60["BEL_tripartite_government"]
    end
    subgraph tier_8["Tier 8"]
        n61["BEL_anti_corruption_taskforce"]
        n62["BEL_belgian_east_indies"]
        n63["BEL_broken_neutrality"]
        n64["BEL_demand_calais"]
        n65["BEL_diplomatic_rapprochment"]
        n66["BEL_expression_of_belgian_unity"]
        n67["BEL_invite_german_tank_organization"]
        n68{"BEL_raise_the_red_flag"}
        n69["BEL_support_the_european_project"]
        n70["BEL_the_council_of_europe"]
        n71["BEL_the_european_crusade"]
        n72["BEL_the_walloon_legion"]
    end
    subgraph tier_9["Tier 9"]
        n73["BEL_belgian_maginot"]
        n74["BEL_belgian_renaissance"]
        n75{"BEL_burgundy_rising"}
        n76["BEL_european_community"]
        n77["BEL_join_allies"]
        n78["BEL_soviet_guarantee"]
        n79["BEL_the_new_ruhr"]
    end
    subgraph tier_10["Tier 10"]
        n80["BEL_demand_further_gallic_concessions"]
        n81["BEL_democratization_of_education"]
        n82["BEL_expedite_fort_construction"]
        n83["BEL_invite_soviet_tank_makers"]
        n84["BEL_join_axis"]
        n85["BEL_join_comintern"]
        n86["BEL_strength_and_brotherhood"]
    end
    subgraph tier_11["Tier 11"]
        n87["BEL_belgica"]
        n88["BEL_unity_makes_strength"]
    end
    subgraph tier_12["Tier 12"]
        n89["BEL_better_than_maginot"]
    end
    n30 --> n33
    n31 --> n33
    n36 --> n43
    n25 --> n26
    n56 --> n61
    n57 --> n61
    n55 --> n62
    n66 --> n73
    n61 --> n73
    n71 --> n74
    n80 --> n87
    n43 --> n53
    n88 --> n89
    n60 --> n63
    n64 --> n75
    n41 --> n44
    n49 --> n54
    n51 --> n54
    n47 --> n54
    n23 --> n27
    n28 --> n34
    n20 --> n22
    n21 --> n23
    n55 --> n64
    n75 --> n80
    n73 --> n81
    n45 --> n55
    n56 --> n65
    n30 --> n35
    n29 --> n36
    n14 --> n36
    n69 --> n76
    n73 --> n82
    n56 --> n66
    n57 --> n66
    n39 --> n45
    n15 --> n17
    n32 --> n37
    n37 --> n46
    n33 --> n47
    n42 --> n47
    n15 --> n18
    n58 --> n67
    n78 --> n83
    n65 --> n77
    n75 --> n84
    n58 --> n84
    n78 --> n85
    n27 --> n38
    n22 --> n28
    n41 --> n48
    n52 --> n56
    n33 --> n49
    n42 --> n49
    n21 --> n24
    n37 --> n50
    n26 --> n50
    n24 --> n29
    n19 --> n20
    n57 --> n68
    n46 --> n68
    n31 --> n39
    n33 --> n51
    n42 --> n51
    n18 --> n21
    n17 --> n21
    n16 --> n21
    n38 --> n52
    n52 --> n57
    n57 --> n78
    n68 --> n78
    n26 --> n40
    n75 --> n86
    n46 --> n69
    n57 --> n69
    n23 --> n30
    n23 --> n31
    n53 --> n70
    n54 --> n71
    n59 --> n71
    n30 --> n41
    n30 --> n42
    n31 --> n42
    n25 --> n32
    n22 --> n32
    n44 --> n58
    n48 --> n58
    n72 --> n79
    n58 --> n72
    n20 --> n25
    n49 --> n59
    n51 --> n59
    n47 --> n59
    n43 --> n60
    n82 --> n88
    n81 --> n88
    n15 --> n19
    n53 x--x n60
    n27 x--x n30
    n27 x--x n31
    n23 x--x n24
    n17 x--x n19
    n84 x--x n86
    n78 x--x n69
    n30 x--x n31
```

# BEL_monetary_reconstruction

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n90(("BEL_monetary_reconstruction"))
        n91["CONGO_congo_free_state"]
        n92["CONGO_dominion_of_congo"]
        n93["CONGO_overseas_department_of_belgium"]
    end
    subgraph tier_1["Tier 1"]
        n94["BEL_gold_reserves"]
        n95["BEL_rebuild_wallonian_industry"]
    end
    subgraph tier_2["Tier 2"]
        n96["BEL_revive_coal_mining"]
        n97["BEL_social_partners"]
    end
    subgraph tier_3["Tier 3"]
        n98["BEL_40_hour_workweek"]
        n99["BEL_cockerill"]
        n100["BEL_railway_expansion"]
    end
    subgraph tier_4["Tier 4"]
        n101["BEL_corporate_social_responsibility"]
        n102["BEL_embrace_export_economy"]
        n103["BEL_engine_of_the_economy"]
    end
    subgraph tier_5["Tier 5"]
        n104["BEL_belgian_miracle"]
        n105["BEL_val_benoit_institutes"]
    end
    subgraph tier_6["Tier 6"]
        n106["BEL_stk"]
    end
    n97 --> n98
    n103 --> n104
    n91 --> n104
    n93 --> n104
    n92 --> n104
    n97 --> n99
    n96 --> n99
    n98 --> n101
    n100 --> n102
    n98 --> n103
    n99 --> n103
    n100 --> n103
    n90 --> n94
    n96 --> n100
    n90 --> n95
    n95 --> n96
    n95 --> n97
    n105 --> n106
    n103 --> n106
    n101 --> n105
```

# BEL_perpetual_neutrality

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17["BEL_government_of_national_unity"]
        n46{"BEL_international_socialist_bureau"}
        n18["BEL_investigate_bribery_charges"]
        n107(("BEL_perpetual_neutrality"))
    end
    subgraph tier_1["Tier 1"]
        n108["BEL_independent_neutral_and_loyal"]
    end
    subgraph tier_2["Tier 2"]
        n109["BEL_defense_bill"]
        n110["BEL_defensive_neutrality"]
        n16["BEL_repudiate_treaty_with_france"]
    end
    subgraph tier_3["Tier 3"]
        n111["BEL_belgian_gates"]
        n14["BEL_dyle_plan"]
        n112["BEL_fn_herstal"]
        n113["BEL_increased_length_of_service"]
        n114["BEL_national_redoubt_at_antwerp"]
        n21{"BEL_royal_intervention"}
        n115["BEL_royal_military_academy"]
    end
    subgraph tier_4["Tier 4"]
        n23{"BEL_degrelle"}
        n116["BEL_department_of_ballistic_metrology"]
        n117["BEL_department_of_telecommunications"]
        n118["BEL_fortify_liege"]
        n119["BEL_iron_wall"]
        n120["BEL_junior_officer_training"]
        n121["BEL_minerva_imperia"]
        n122["BEL_multi_language_courses"]
        n24["BEL_paul_emile_janson"]
        n123["BEL_poudreries_reunies_de_belgique"]
    end
    subgraph tier_5["Tier 5"]
        n124["BEL_anti_tank_guns"]
        n125["BEL_center_for_advanced_military_studies"]
        n27["BEL_constitutional_crisis"]
        n126["BEL_eben_emael_fortress"]
        n127["BEL_fonderie_royale_de_canons_liege"]
        n128["BEL_legacy_of_the_great_war"]
        n129["BEL_our_southern_neighbour"]
        n29["BEL_plan_de_man"]
        n130["BEL_resist_and_bite"]
        n131["BEL_strategic_doctrine_development"]
        n30["BEL_support_the_rexists"]
        n31["BEL_support_the_vnv"]
    end
    subgraph tier_6["Tier 6"]
        n33["BEL_abandon_neutrality"]
        n132["BEL_belgian_special_forces"]
        n133["BEL_belgian_tank_development"]
        n134["BEL_center_of_nuclear_chemistry"]
        n35["BEL_dissolve_political_parties"]
        n135["BEL_doctrinal_innovations"]
        n36["BEL_economic_recovery"]
        n38["BEL_kings_abdication"]
        n136["BEL_koningshooikt_wavre_line"]
        n137["BEL_protect_against_france"]
        n39["BEL_revitalize_nederlands"]
        n138["BEL_senior_officer_training"]
        n41["BEL_the_flemish_question"]
        n42["BEL_the_french_horse_and_the_red_rider"]
    end
    subgraph tier_7["Tier 7"]
        n43{"BEL_adriaan_martens_crisis"}
        n44["BEL_christian_corporatism"]
        n45["BEL_flanders_ascendant"]
        n139["BEL_flooded_tank_barriers"]
        n47["BEL_international_stipend"]
        n140["BEL_interpreters"]
        n48["BEL_legacy_of_the_soldier_king"]
        n141["BEL_mobilize_the_nation"]
        n49["BEL_nationalize_the_banks"]
        n51["BEL_royal_commander_in_chief"]
        n52["BEL_snap_election"]
    end
    subgraph tier_8["Tier 8"]
        n53["BEL_benelux_union"]
        n54["BEL_civil_service_purge"]
        n142["BEL_dam_the_consequences"]
        n143["BEL_defensive_reorganization"]
        n55["BEL_dietsland"]
        n56["BEL_liberal_victory"]
        n57{"BEL_socialist_victory"}
        n58{"BEL_the_lost_tribe"}
        n59["BEL_traditional_family_values"]
        n60["BEL_tripartite_government"]
    end
    subgraph tier_9["Tier 9"]
        n61["BEL_anti_corruption_taskforce"]
        n62["BEL_belgian_east_indies"]
        n63["BEL_broken_neutrality"]
        n64["BEL_demand_calais"]
        n65["BEL_diplomatic_rapprochment"]
        n66["BEL_expression_of_belgian_unity"]
        n67["BEL_invite_german_tank_organization"]
        n144["BEL_modernized_army"]
        n68{"BEL_raise_the_red_flag"}
        n69["BEL_support_the_european_project"]
        n70["BEL_the_council_of_europe"]
        n71["BEL_the_european_crusade"]
        n72["BEL_the_walloon_legion"]
    end
    subgraph tier_10["Tier 10"]
        n73["BEL_belgian_maginot"]
        n74["BEL_belgian_renaissance"]
        n75{"BEL_burgundy_rising"}
        n76["BEL_european_community"]
        n77["BEL_join_allies"]
        n78["BEL_soviet_guarantee"]
        n79["BEL_the_new_ruhr"]
    end
    subgraph tier_11["Tier 11"]
        n80["BEL_demand_further_gallic_concessions"]
        n81["BEL_democratization_of_education"]
        n82["BEL_expedite_fort_construction"]
        n83["BEL_invite_soviet_tank_makers"]
        n84["BEL_join_axis"]
        n85["BEL_join_comintern"]
        n86["BEL_strength_and_brotherhood"]
    end
    subgraph tier_12["Tier 12"]
        n87["BEL_belgica"]
        n88["BEL_unity_makes_strength"]
    end
    subgraph tier_13["Tier 13"]
        n89["BEL_better_than_maginot"]
    end
    n30 --> n33
    n31 --> n33
    n36 --> n43
    n56 --> n61
    n57 --> n61
    n116 --> n124
    n55 --> n62
    n110 --> n111
    n66 --> n73
    n61 --> n73
    n71 --> n74
    n130 --> n132
    n131 --> n133
    n127 --> n133
    n80 --> n87
    n43 --> n53
    n88 --> n89
    n60 --> n63
    n64 --> n75
    n122 --> n125
    n117 --> n125
    n125 --> n134
    n41 --> n44
    n49 --> n54
    n51 --> n54
    n47 --> n54
    n23 --> n27
    n139 --> n142
    n108 --> n109
    n108 --> n110
    n141 --> n143
    n136 --> n143
    n21 --> n23
    n55 --> n64
    n75 --> n80
    n73 --> n81
    n115 --> n116
    n115 --> n117
    n45 --> n55
    n56 --> n65
    n30 --> n35
    n131 --> n135
    n16 --> n14
    n118 --> n126
    n29 --> n36
    n14 --> n36
    n69 --> n76
    n73 --> n82
    n56 --> n66
    n57 --> n66
    n39 --> n45
    n136 --> n139
    n109 --> n112
    n116 --> n127
    n114 --> n118
    n109 --> n113
    n107 --> n108
    n33 --> n47
    n42 --> n47
    n132 --> n140
    n58 --> n67
    n78 --> n83
    n111 --> n119
    n65 --> n77
    n75 --> n84
    n58 --> n84
    n78 --> n85
    n115 --> n120
    n27 --> n38
    n126 --> n136
    n119 --> n136
    n121 --> n128
    n41 --> n48
    n52 --> n56
    n112 --> n121
    n14 --> n121
    n129 --> n141
    n136 --> n141
    n143 --> n144
    n138 --> n144
    n135 --> n144
    n115 --> n122
    n110 --> n114
    n33 --> n49
    n42 --> n49
    n119 --> n129
    n21 --> n24
    n24 --> n29
    n112 --> n123
    n129 --> n137
    n57 --> n68
    n46 --> n68
    n108 --> n16
    n122 --> n130
    n31 --> n39
    n33 --> n51
    n42 --> n51
    n18 --> n21
    n17 --> n21
    n16 --> n21
    n109 --> n115
    n125 --> n138
    n38 --> n52
    n52 --> n57
    n57 --> n78
    n68 --> n78
    n120 --> n131
    n75 --> n86
    n46 --> n69
    n57 --> n69
    n23 --> n30
    n23 --> n31
    n53 --> n70
    n54 --> n71
    n59 --> n71
    n30 --> n41
    n30 --> n42
    n31 --> n42
    n44 --> n58
    n48 --> n58
    n72 --> n79
    n58 --> n72
    n49 --> n59
    n51 --> n59
    n47 --> n59
    n43 --> n60
    n82 --> n88
    n81 --> n88
    n53 x--x n60
    n27 x--x n30
    n27 x--x n31
    n23 x--x n24
    n84 x--x n86
    n78 x--x n69
    n30 x--x n31
```

# BEL_re_establish_belgian_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n145(("BEL_re_establish_belgian_navy"))
    end
    subgraph tier_1["Tier 1"]
        n146["BEL_allied_donations"]
        n147["BEL_re_build_the_fleet"]
    end
    subgraph tier_2["Tier 2"]
        n148["BEL_corvette_fleet"]
        n149["BEL_port_of_antwerp"]
    end
    subgraph tier_3["Tier 3"]
        n150["BEL_antwerp_maritime_academy"]
        n151["BEL_boelwerf"]
        n152["BEL_cockerill_shipyards"]
        n153["BEL_convoy_protection_duties"]
    end
    subgraph tier_4["Tier 4"]
        n154["BEL_maritime_phoenix"]
        n155["BEL_naval_doctrine"]
    end
    n145 --> n146
    n149 --> n150
    n149 --> n151
    n149 --> n152
    n148 --> n153
    n147 --> n148
    n151 --> n154
    n152 --> n154
    n150 --> n155
    n147 --> n149
    n145 --> n147
```

# BEL_the_king_surrenders

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n156{"BEL_the_king_surrenders"}
    end
    subgraph tier_1["Tier 1"]
        n157["BEL_prisoner_king"]
        n158["BEL_unfit_to_reign"]
    end
    subgraph tier_2["Tier 2"]
        n159["BEL_government_in_exile"]
        n160["BEL_king_law_freedom"]
        n161["BEL_secretaries_general"]
    end
    subgraph tier_3["Tier 3"]
        n162["BEL_king_of_the_belgians"]
        n163["BEL_la_dame_blanche"]
        n164["BEL_moi_dabord"]
        n165["BEL_the_belgian_legion"]
        n166["BEL_the_secret_army"]
    end
    subgraph tier_4["Tier 4"]
        n167["BEL_develop_home_support"]
        n168["BEL_military_service_for_all_in_exile"]
        n169["BEL_rally_to_the_king"]
        n170{"BEL_v_for_victory"}
        n171["BEL_van_overstraeten_on_the_home_front"]
    end
    subgraph tier_5["Tier 5"]
        n172["BEL_charles_count_of_flanders"]
        n173["BEL_consolidate_resistance_groups"]
        n174["BEL_democratic_homecoming"]
        n175["BEL_expand_the_belgian_legion"]
        n176["BEL_leopolds_return"]
    end
    subgraph tier_6["Tier 6"]
        n177["BEL_free_belgian_forces"]
    end
    n170 --> n172
    n167 --> n173
    n170 --> n174
    n166 --> n167
    n165 --> n167
    n169 --> n175
    n168 --> n177
    n173 --> n177
    n175 --> n177
    n158 --> n159
    n157 --> n160
    n160 --> n162
    n159 --> n163
    n170 --> n176
    n166 --> n168
    n159 --> n164
    n156 --> n157
    n165 --> n169
    n162 --> n169
    n158 --> n161
    n157 --> n161
    n161 --> n165
    n161 --> n166
    n156 --> n158
    n164 --> n170
    n162 --> n171
    n172 x--x n174
    n172 x--x n176
    n174 x--x n176
    n157 x--x n158
```
