# FIN_enhance_southern_infrastructure

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("FIN_enhance_southern_infrastructure"))
        n2["FIN_industrial_upgrade_in_harjavalta"]
        n3["FIN_outokumpu_for_defence_industry"]
    end
    subgraph tier_1["Tier 1"]
        n4["FIN_industrial_development"]
    end
    subgraph tier_2["Tier 2"]
        n5["FIN_bank_of_aland"]
        n6["FIN_janiskoski_power_plant"]
        n7["FIN_tire_factory_at_nokia"]
        n8["FIN_vaisala_radiosonde_tests"]
    end
    subgraph tier_3["Tier 3"]
        n9["FIN_contract_with_yhteissisu"]
        n10["FIN_expand_imatra_hydropower_plant"]
        n11["FIN_found_pohjolan_voima"]
        n12["FIN_suomen_akatemia"]
    end
    subgraph tier_4["Tier 4"]
        n13["FIN_expand_mining_prospection"]
        n14["FIN_makola_mine"]
        n15["FIN_power_from_the_dams"]
    end
    subgraph tier_5["Tier 5"]
        n16["FIN_elijarvi_mine"]
    end
    subgraph tier_6["Tier 6"]
        n17["FIN_tornio_steel_factory"]
    end
    n4 --> n5
    n7 --> n9
    n3 --> n9
    n13 --> n16
    n6 --> n10
    n10 --> n13
    n2 --> n13
    n6 --> n11
    n1 --> n4
    n4 --> n6
    n10 --> n14
    n10 --> n15
    n5 --> n12
    n4 --> n7
    n16 --> n17
    n4 --> n8
```

# FIN_finnish_neutrality

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18(("FIN_finnish_neutrality"))
        n19["FIN_keepers_of_the_north"]
        n20["FIN_right_wing_policies"]
        n21["FIN_seek_german_protection"]
        n22["FIN_social_democracy"]
        n23["FIN_suomalainen_sosialismi"]
    end
    subgraph tier_1["Tier 1"]
        n24{"FIN_national_unity"}
        n25["FIN_political_unity"]
        n26["FIN_reach_out_to_scandinavia"]
        n27["FIN_weapon_caches"]
    end
    subgraph tier_2["Tier 2"]
        n28["FIN_a_cry_for_help"]
        n29["FIN_align_the_agrarian_league"]
        n30["FIN_arm_the_lotta_svard"]
        n31["FIN_collaboration_with_the_left"]
        n32{"FIN_moderate_politics"}
        n33["FIN_railways_and_infrastructure"]
        n34["FIN_the_finnish_swedish_peoples_party"]
        n35["FIN_viron_kansa"]
    end
    subgraph tier_3["Tier 3"]
        n36["FIN_ambitions_in_the_south"]
        n37["FIN_join_the_allies"]
        n38["FIN_northern_defense_front"]
        n39["FIN_repurpose_small_industries"]
        n40["FIN_the_lone_wolf"]
        n41["FIN_union_of_finnish_brothers_in_arms"]
    end
    subgraph tier_4["Tier 4"]
        n42["FIN_cooperation_with_germany"]
        n43{"FIN_expand_state_military_factories"}
        n44["FIN_industrialize_the_region"]
        n45["FIN_militarized_society"]
        n46["FIN_military_aid"]
        n47["FIN_parmis_devils"]
    end
    subgraph tier_5["Tier 5"]
        n48["FIN_a_new_course_for_kokoomus"]
        n49["FIN_dreams_of_expansionism"]
        n50["FIN_german_military_advisors"]
        n51["FIN_increase_military_investment"]
        n52{"FIN_joint_scientific_program"}
        n53["FIN_mineral_wealth_development"]
        n54["FIN_strengthen_military_administration"]
        n55["FIN_wartsila_engine_production"]
    end
    subgraph tier_6["Tier 6"]
        n56["FIN_finnish_march_of_conquest"]
        n57["FIN_modernize_the_army"]
        n58["FIN_modernize_the_industry"]
        n59["FIN_the_finnish_throne"]
    end
    subgraph tier_7["Tier 7"]
        n60["FIN_greater_finland"]
    end
    n24 --> n28
    n43 --> n48
    n25 --> n29
    n22 --> n29
    n35 --> n36
    n24 --> n30
    n25 --> n31
    n40 --> n42
    n43 --> n49
    n39 --> n43
    n55 --> n56
    n50 --> n56
    n42 --> n50
    n56 --> n60
    n45 --> n60
    n19 --> n60
    n46 --> n51
    n44 --> n51
    n38 --> n44
    n32 --> n37
    n44 --> n52
    n42 --> n52
    n46 --> n52
    n41 --> n45
    n37 --> n46
    n46 --> n53
    n26 --> n32
    n52 --> n57
    n52 --> n58
    n18 --> n24
    n20 --> n24
    n32 --> n38
    n41 --> n47
    n18 --> n25
    n25 --> n33
    n18 --> n26
    n33 --> n39
    n43 --> n54
    n22 --> n34
    n25 --> n34
    n48 --> n59
    n32 --> n40
    n30 --> n41
    n24 --> n35
    n42 --> n55
    n18 --> n27
    n20 --> n27
    n28 x--x n21
    n48 x--x n49
    n48 x--x n54
    n49 x--x n54
    n18 x--x n20
    n18 x--x n23
    n37 x--x n38
    n37 x--x n40
    n57 x--x n58
    n38 x--x n40
```

# FIN_increase_military_budget

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n10["FIN_expand_imatra_hydropower_plant"]
        n61(("FIN_increase_military_budget"))
        n7["FIN_tire_factory_at_nokia"]
    end
    subgraph tier_1["Tier 1"]
        n62["FIN_suomen_ilmavoimat"]
        n63["FIN_suomen_maavoimat"]
        n64["FIN_suomen_merivoimat"]
    end
    subgraph tier_2["Tier 2"]
        n65["FIN_acquire_andros_dockyards"]
        n66{"FIN_coastal_defense"}
        n67["FIN_expand_air_bases"]
        n68["FIN_extra_refresher_exercises"]
        n69["FIN_mannerheim_line"]
        n70{"FIN_naval_airforce"}
        n71["FIN_operation_kilpapurjehdus"]
        n3["FIN_outokumpu_for_defence_industry"]
        n72["FIN_pilot_training"]
        n73["FIN_strengthen_the_naval_bases"]
        n74["FIN_the_merchant_fleet"]
        n75["FIN_underground_resistance_cells"]
    end
    subgraph tier_3["Tier 3"]
        n9["FIN_contract_with_yhteissisu"]
        n76["FIN_conversion_of_civilian_vessels"]
        n77["FIN_deep_sea_raiders"]
        n78["FIN_defense_in_depth"]
        n79["FIN_expand_air_force_academy"]
        n80["FIN_expand_ship_building_industry"]
        n81["FIN_foreign_aircraft"]
        n82["FIN_helsinki_air_defense"]
        n2["FIN_industrial_upgrade_in_harjavalta"]
        n83["FIN_integrate_oy_tikkakoski"]
        n84["FIN_jaeger_movement"]
        n85["FIN_marine_jaeger_divisions"]
        n86{"FIN_national_aircraft_production"}
        n87["FIN_oy_alkoholiliike"]
        n88["FIN_rapid_raiders"]
        n89{"FIN_salvaged_and_retooled"}
        n90["FIN_the_cold_front"]
    end
    subgraph tier_4["Tier 4"]
        n91{"FIN_dominate_the_skies"}
        n13["FIN_expand_mining_prospection"]
        n92["FIN_foreign_armor"]
        n93["FIN_motti_tactics"]
        n94["FIN_national_firepower"]
        n95["FIN_sea_mines_strategy"]
        n96{"FIN_support_for_ground_forces"}
        n97["FIN_winter_warfare"]
    end
    subgraph tier_5["Tier 5"]
        n16["FIN_elijarvi_mine"]
        n98["FIN_expand_production_lines"]
        n99["FIN_expansion_towards_the_atlantic"]
        n100{"FIN_finnish_radio_intelligence"}
        n101{"FIN_long_range_patrols"}
        n102["FIN_modernize_production_lines"]
        n103{"FIN_utilize_the_sami"}
    end
    subgraph tier_6["Tier 6"]
        n104["FIN_national_armor_focus"]
        n105["FIN_sissi"]
        n17["FIN_tornio_steel_factory"]
    end
    subgraph tier_7["Tier 7"]
        n106["FIN_innovative_designs"]
    end
    n64 --> n65
    n64 --> n66
    n7 --> n9
    n3 --> n9
    n74 --> n76
    n66 --> n76
    n66 --> n77
    n69 --> n78
    n86 --> n91
    n13 --> n16
    n62 --> n67
    n72 --> n79
    n10 --> n13
    n2 --> n13
    n96 --> n98
    n91 --> n98
    n73 --> n80
    n65 --> n80
    n95 --> n99
    n80 --> n99
    n63 --> n68
    n93 --> n100
    n67 --> n81
    n89 --> n92
    n69 --> n82
    n67 --> n82
    n3 --> n2
    n104 --> n106
    n3 --> n83
    n68 --> n84
    n97 --> n101
    n93 --> n101
    n63 --> n69
    n66 --> n85
    n91 --> n102
    n96 --> n102
    n70 --> n102
    n84 --> n93
    n89 --> n93
    n90 --> n93
    n67 --> n86
    n72 --> n86
    n89 --> n104
    n100 --> n104
    n83 --> n94
    n62 --> n70
    n64 --> n70
    n63 --> n71
    n63 --> n3
    n3 --> n87
    n62 --> n72
    n66 --> n88
    n68 --> n89
    n88 --> n95
    n77 --> n95
    n101 --> n105
    n100 --> n105
    n103 --> n105
    n64 --> n73
    n61 --> n62
    n61 --> n63
    n61 --> n64
    n86 --> n96
    n68 --> n90
    n64 --> n74
    n16 --> n17
    n63 --> n75
    n97 --> n103
    n90 --> n97
    n77 x--x n88
    n91 x--x n96
    n98 x--x n102
    n104 x--x n105
```

# FIN_right_wing_policies

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n56["FIN_finnish_march_of_conquest"]
        n18["FIN_finnish_neutrality"]
        n20{"FIN_right_wing_policies"}
        n23["FIN_suomalainen_sosialismi"]
    end
    subgraph tier_1["Tier 1"]
        n107["FIN_discredit_the_democratic_system"]
        n24{"FIN_national_unity"}
        n108["FIN_prepare_a_military_coup"]
        n27["FIN_weapon_caches"]
    end
    subgraph tier_2["Tier 2"]
        n28["FIN_a_cry_for_help"]
        n109{"FIN_a_fascist_regime"}
        n30["FIN_arm_the_lotta_svard"]
        n35["FIN_viron_kansa"]
    end
    subgraph tier_3["Tier 3"]
        n110["FIN_academic_karelian_society"]
        n36["FIN_ambitions_in_the_south"]
        n111["FIN_finnish_supremacy_in_the_north"]
        n112["FIN_join_axis"]
        n113["FIN_patriotic_peoples_movement"]
        n21["FIN_seek_german_protection"]
        n41["FIN_union_of_finnish_brothers_in_arms"]
    end
    subgraph tier_4["Tier 4"]
        n114["FIN_finnish_legion_of_honor"]
        n115["FIN_industrial_cooperation"]
        n116["FIN_maan_turva"]
        n45["FIN_militarized_society"]
        n117["FIN_military_research"]
        n118["FIN_mustapaidat"]
        n47["FIN_parmis_devils"]
        n119["FIN_tactical_wargaming_department"]
        n120["FIN_take_over_the_suojeluskunta"]
    end
    subgraph tier_5["Tier 5"]
        n121["FIN_advanced_jaeger_training_program"]
        n122["FIN_bring_foreign_armor_experts"]
        n123["FIN_finnish_irredentism"]
        n124["FIN_indoctrinate_the_workers"]
        n125["FIN_military_promotions"]
        n126["FIN_sotilaalliset_kappalaiset"]
    end
    subgraph tier_6["Tier 6"]
        n127["FIN_intellectual_elite"]
        n19["FIN_keepers_of_the_north"]
        n128["FIN_national_fanatism"]
    end
    subgraph tier_7["Tier 7"]
        n60["FIN_greater_finland"]
    end
    n24 --> n28
    n107 --> n109
    n108 --> n109
    n109 --> n110
    n117 --> n121
    n114 --> n121
    n35 --> n36
    n24 --> n30
    n117 --> n122
    n115 --> n122
    n20 --> n107
    n114 --> n123
    n119 --> n123
    n111 --> n114
    n109 --> n111
    n56 --> n60
    n45 --> n60
    n19 --> n60
    n116 --> n124
    n112 --> n115
    n125 --> n127
    n124 --> n127
    n109 --> n112
    n123 --> n19
    n122 --> n19
    n110 --> n116
    n41 --> n45
    n120 --> n125
    n112 --> n117
    n113 --> n118
    n126 --> n128
    n18 --> n24
    n20 --> n24
    n41 --> n47
    n109 --> n113
    n20 --> n108
    n109 --> n21
    n118 --> n126
    n111 --> n119
    n113 --> n120
    n110 --> n120
    n30 --> n41
    n24 --> n35
    n18 --> n27
    n20 --> n27
    n28 x--x n21
    n107 x--x n108
    n18 x--x n20
    n111 x--x n112
    n20 x--x n23
```

# FIN_suomalainen_sosialismi

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18["FIN_finnish_neutrality"]
        n25["FIN_political_unity"]
        n20["FIN_right_wing_policies"]
        n23{"FIN_suomalainen_sosialismi"}
    end
    subgraph tier_1["Tier 1"]
        n22{"FIN_social_democracy"}
        n129{"FIN_towards_a_red_government"}
    end
    subgraph tier_2["Tier 2"]
        n29["FIN_align_the_agrarian_league"]
        n130["FIN_antagonize_the_soviets"]
        n131["FIN_approach_the_soviets"]
        n132["FIN_pragmatic_socialism"]
        n34["FIN_the_finnish_swedish_peoples_party"]
        n133{"FIN_the_second_finnish_civil_war"}
    end
    subgraph tier_3["Tier 3"]
        n134["FIN_cooperate_with_social_democrats"]
        n135{"FIN_defensive_preparations"}
        n136["FIN_finnish_federation_of_trade_unions"]
        n137["FIN_finnish_learned_societies"]
        n138{"FIN_finno_estonian_union"}
        n139{"FIN_finno_soviet_pact"}
        n140["FIN_mineral_wealth"]
        n141["FIN_social_democratic_womens_union"]
        n142{"FIN_sosialistinen_eduskuntaryhma"}
        n143["FIN_the_peoples_democratic_league"]
        n144["FIN_the_workers_state"]
    end
    subgraph tier_4["Tier 4"]
        n145["FIN_approach_major_democracies"]
        n146["FIN_funds_from_kalevala_koru_oy"]
        n147["FIN_join_the_comintern"]
        n148["FIN_subsidized_national_industrialization"]
        n149["FIN_the_red_watch"]
        n150["FIN_trade_agreements"]
        n151["FIN_united_under_the_north_star"]
    end
    subgraph tier_5["Tier 5"]
        n152["FIN_aid_for_entrepreneurs"]
        n153["FIN_confederated_finno_russian_republics"]
        n154["FIN_control_the_flux_of_iron_ore"]
        n155["FIN_finnish_autonomy"]
        n156["FIN_finnish_influence_in_the_baltic"]
        n157["FIN_integrate_kola_and_karelia"]
        n158["FIN_secure_the_baltic_sea"]
    end
    subgraph tier_6["Tier 6"]
        n159["FIN_british_threat"]
        n160["FIN_german_threat"]
        n161["FIN_keepers_of_the_baltic_countries"]
        n162["FIN_preserve_sapmi"]
        n163["FIN_proclaim_greater_finland"]
        n164["FIN_socialist_welfare"]
        n165["FIN_soviet_threat"]
    end
    subgraph tier_7["Tier 7"]
        n166["FIN_red_finland"]
    end
    n145 --> n152
    n151 --> n152
    n25 --> n29
    n22 --> n29
    n129 --> n130
    n22 --> n130
    n142 --> n145
    n135 --> n145
    n129 --> n131
    n22 --> n131
    n157 --> n159
    n151 --> n153
    n145 --> n154
    n133 --> n134
    n130 --> n135
    n147 --> n155
    n130 --> n136
    n131 --> n136
    n147 --> n156
    n151 --> n156
    n131 --> n137
    n130 --> n137
    n131 --> n138
    n130 --> n138
    n131 --> n139
    n141 --> n146
    n140 --> n146
    n156 --> n160
    n158 --> n160
    n147 --> n157
    n133 --> n147
    n139 --> n147
    n157 --> n161
    n156 --> n161
    n132 --> n140
    n22 --> n132
    n156 --> n162
    n154 --> n163
    n152 --> n163
    n161 --> n166
    n151 --> n158
    n145 --> n158
    n23 --> n22
    n132 --> n141
    n158 --> n164
    n132 --> n142
    n158 --> n165
    n152 --> n165
    n139 --> n148
    n22 --> n34
    n25 --> n34
    n133 --> n143
    n144 --> n149
    n129 --> n133
    n133 --> n144
    n23 --> n129
    n135 --> n150
    n138 --> n151
    n130 x--x n131
    n145 x--x n147
    n145 x--x n151
    n18 x--x n23
    n147 x--x n151
    n20 x--x n23
    n22 x--x n129
```
