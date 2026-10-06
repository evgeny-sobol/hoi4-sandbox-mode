# RAJ_ammunition_factory_khadki

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("RAJ_ammunition_factory_khadki"))
        n2["RAJ_mechanization_of_the_cavalry"]
    end
    subgraph tier_1["Tier 1"]
        n3["RAJ_gun_and_shell_factory_cossipore"]
        n4["RAJ_rifle_factory_ishapore_west_bengal"]
    end
    subgraph tier_2["Tier 2"]
        n5["RAJ_cordite_factory_aruvankadu_tamil_nadu"]
        n6["RAJ_ordnance_factory_kanpur_uttar_pradesh"]
        n7["RAJ_ordnance_factory_khamaria_jabalpur"]
        n8["RAJ_ordnance_factory_medak"]
    end
    subgraph tier_3["Tier 3"]
        n9["RAJ_chariot_of_victory"]
        n10["RAJ_engineering_revolution"]
        n11["RAJ_the_ordnance_factories_board"]
    end
    n8 --> n9
    n6 --> n9
    n3 --> n5
    n2 --> n10
    n7 --> n10
    n1 --> n3
    n4 --> n6
    n3 --> n7
    n4 --> n8
    n1 --> n4
    n5 --> n11
    n6 --> n11
```

# RAJ_bombay_baroda_and_central_india_railway

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n12(("RAJ_bombay_baroda_and_central_india_railway"))
        n13["RAJ_east_india_railways_dlc"]
    end
    subgraph tier_1["Tier 1"]
        n14["RAJ_great_indian_peninsula_railway_dlc"]
        n15["RAJ_tata_steel_dlc"]
    end
    subgraph tier_2["Tier 2"]
        n16["RAJ_north_western_state_railway"]
        n17["RAJ_south_indian_railway_company"]
        n18{"RAJ_supply_center_fortifications"}
    end
    subgraph tier_3["Tier 3"]
        n19["RAJ_prioritize_army_cargo"]
        n20["RAJ_prioritize_civilian_cargo"]
    end
    n13 --> n14
    n12 --> n14
    n14 --> n16
    n18 --> n19
    n18 --> n20
    n14 --> n17
    n14 --> n18
    n12 --> n15
    n19 x--x n20
```

# RAJ_east_india_railways_dlc

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n12["RAJ_bombay_baroda_and_central_india_railway"]
        n13(("RAJ_east_india_railways_dlc"))
    end
    subgraph tier_1["Tier 1"]
        n21["RAJ_assam_oil_dlc"]
        n14["RAJ_great_indian_peninsula_railway_dlc"]
        n22["RAJ_the_burma_road"]
        n23["RAJ_the_calcutta_line"]
    end
    subgraph tier_2["Tier 2"]
        n16["RAJ_north_western_state_railway"]
        n17["RAJ_south_indian_railway_company"]
        n18{"RAJ_supply_center_fortifications"}
        n24["RAJ_the_ledo_road"]
    end
    subgraph tier_3["Tier 3"]
        n19["RAJ_prioritize_army_cargo"]
        n20["RAJ_prioritize_civilian_cargo"]
    end
    n13 --> n21
    n13 --> n14
    n12 --> n14
    n14 --> n16
    n18 --> n19
    n18 --> n20
    n14 --> n17
    n14 --> n18
    n13 --> n22
    n13 --> n23
    n22 --> n24
    n19 x--x n20
```

# RAJ_great_depression_price_controls

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n25{"RAJ_great_depression_price_controls"}
        n26["RAJ_his_majestys_loyal_government"]
        n27["RAJ_provincial_autonomy"]
    end
    subgraph tier_1["Tier 1"]
        n28["RAJ_look_to_the_future"]
        n29["RAJ_look_to_the_past"]
        n30["RAJ_trade_port"]
    end
    subgraph tier_2["Tier 2"]
        n31["RAJ_fortify_aden"]
        n32["RAJ_lobby_parliment"]
        n33["RAJ_secure_weapons"]
        n34["RAJ_seek_intial_funding"]
        n35["RAJ_stir_unrest_in_the_north"]
    end
    subgraph tier_3["Tier 3"]
        n36["RAJ_incorporation_of_the_east_india_company"]
        n37["RAJ_the_mughal_uprising"]
    end
    subgraph tier_4["Tier 4"]
        n38["RAJ_appoint_a_c_suite"]
        n39["RAJ_forging_the_mughal_arsenal"]
        n40["RAJ_reform_the_agricultural_system"]
        n41["RAJ_the_legacy_of_babur"]
    end
    subgraph tier_5["Tier 5"]
        n42["RAJ_a_peacock_prince"]
        n43["RAJ_company_bonuses"]
        n44["RAJ_corporate_expansion"]
        n45["RAJ_form_a_police_force"]
        n46["RAJ_take_over_administrative_rights"]
    end
    subgraph tier_6["Tier 6"]
        n47["RAJ_halls_of_knowledge"]
        n48["RAJ_headhunt_army_personell"]
        n49["RAJ_land_grab"]
        n50["RAJ_legalize_the_opium_trade"]
        n51["RAJ_princely_autonomy"]
        n52["RAJ_privatized_healthcare"]
        n53["RAJ_privatized_tutelage"]
        n54["RAJ_reviving_the_workshop_of_the_world"]
        n55["RAJ_revolt_of_the_princes"]
        n56["RAJ_sharpen_the_tulwar"]
        n57["RAJ_timurid_bureaucracy"]
        n58["RAJ_union_busting"]
    end
    subgraph tier_7["Tier 7"]
        n59["RAJ_a_private_military"]
        n60["RAJ_arrest_congress_leaders"]
        n61["RAJ_conquer_afghanistan"]
        n62["RAJ_deforestation"]
        n63["RAJ_elephants_for_the_modern_age"]
        n64["RAJ_force_china_to_accept_opium_trade"]
        n65["RAJ_funnel_british_investments_into_princely_states"]
        n66["RAJ_halls_of_knowledge_2"]
        n67["RAJ_hostile_takeover"]
        n68["RAJ_rebuilding_the_empires_roads"]
        n69{"RAJ_unite_the_subcontinent"}
    end
    subgraph tier_8["Tier 8"]
        n70["RAJ_halls_of_knowledge_3"]
        n71["RAJ_legacy_of_timur"]
        n72["RAJ_lobby_for_increased_policing_responsibilities"]
        n73["RAJ_secular_rule"]
        n74["RAJ_theocratic_rule"]
        n75["RAJ_through_the_wakhan_corridor"]
        n76["RAJ_thunder_elephants"]
        n77["RAJ_vertical_integration"]
    end
    subgraph tier_9["Tier 9"]
        n78["RAJ_bombay_trade_port"]
        n79["RAJ_circuvment_demobilization_restrictions"]
        n80["RAJ_expand_tax_loopholes"]
        n81["RAJ_manipulate_army_statistics"]
        n82["RAJ_mughal_court"]
        n83["RAJ_new_economic_policy"]
        n84["RAJ_secret_weapons"]
        n85["RAJ_special_economic_zones"]
        n86["RAJ_the_silk_road"]
    end
    subgraph tier_10["Tier 10"]
        n87["RAJ_across_the_himalayas"]
        n88["RAJ_conquerors_of_persia"]
        n89["RAJ_creative_accounting"]
        n90["RAJ_open_up_new_markets"]
        n91["RAJ_peacock_throne_for_the_modern_age"]
        n92["RAJ_phantom_armies"]
        n93["RAJ_purchase_destroyers_and_subs"]
        n94["RAJ_restrictive_administration_budget"]
        n95["RAJ_shareholder_democracy"]
        n96["RAJ_take_in_british_naval_experts"]
        n97["RAJ_the_need_for_a_mercantile_navy"]
        n98["RAJ_the_true_mongols"]
    end
    subgraph tier_11["Tier 11"]
        n99{"RAJ_acquire_new_resources"}
        n100["RAJ_conquerors_of_iraq"]
        n101["RAJ_conquerors_of_turkey"]
        n102["RAJ_corporate_domination"]
        n103["RAJ_debt_manipulation"]
        n104["RAJ_institutional_money_laundering"]
        n105["RAJ_purchase_cruisers_and_dreadnoughts"]
        n106["RAJ_revisiting_inquities"]
        n107["RAJ_the_crown_and_the_world"]
        n108["RAJ_trade_protection"]
    end
    subgraph tier_12["Tier 12"]
        n109["RAJ_deathknell_to_the_raj"]
        n110["RAJ_mineral_exploitation_institute"]
        n111["RAJ_night_shifts"]
        n112["RAJ_procure_the_armor"]
        n113["RAJ_procure_the_guns"]
        n114["RAJ_procure_the_task_force"]
        n115["RAJ_productivity_mandate"]
        n116["RAJ_restore_the_timurid_empire"]
    end
    subgraph tier_13["Tier 13"]
        n117["RAJ_attract_scientists"]
        n118["RAJ_just_good_business"]
        n119["RAJ_mass_production"]
        n120["RAJ_the_varuna_class"]
    end
    subgraph tier_14["Tier 14"]
        n121["RAJ_crush_the_anathema"]
        n122["RAJ_nothing_personal"]
    end
    subgraph tier_15["Tier 15"]
        n123["RAJ_trade_federation_of_india"]
    end
    n41 --> n42
    n48 --> n59
    n90 --> n99
    n86 --> n87
    n36 --> n38
    n58 --> n60
    n110 --> n117
    n72 --> n78
    n72 --> n79
    n38 --> n43
    n57 --> n61
    n88 --> n100
    n86 --> n88
    n88 --> n101
    n92 --> n102
    n38 --> n44
    n80 --> n89
    n118 --> n121
    n104 --> n109
    n92 --> n103
    n49 --> n62
    n56 --> n63
    n77 --> n80
    n50 --> n64
    n37 --> n39
    n38 --> n45
    n30 --> n31
    n51 --> n65
    n42 --> n47
    n47 --> n66
    n66 --> n70
    n45 --> n48
    n53 --> n67
    n52 --> n67
    n32 --> n36
    n34 --> n36
    n94 --> n104
    n95 --> n104
    n109 --> n118
    n44 --> n49
    n61 --> n71
    n44 --> n50
    n59 --> n72
    n28 --> n32
    n25 --> n28
    n25 --> n29
    n72 --> n81
    n115 --> n119
    n111 --> n119
    n99 --> n110
    n73 --> n82
    n74 --> n82
    n77 --> n83
    n99 --> n111
    n118 --> n122
    n79 --> n90
    n81 --> n90
    n82 --> n91
    n80 --> n92
    n46 --> n51
    n46 --> n52
    n46 --> n53
    n108 --> n112
    n108 --> n113
    n108 --> n114
    n99 --> n115
    n93 --> n105
    n78 --> n93
    n54 --> n68
    n37 --> n40
    n101 --> n116
    n100 --> n116
    n85 --> n94
    n91 --> n106
    n42 --> n54
    n42 --> n55
    n70 --> n84
    n76 --> n84
    n69 --> n73
    n29 --> n33
    n28 --> n34
    n83 --> n95
    n42 --> n56
    n77 --> n85
    n29 --> n35
    n78 --> n96
    n38 --> n46
    n91 --> n107
    n37 --> n41
    n35 --> n37
    n33 --> n37
    n78 --> n97
    n75 --> n86
    n71 --> n86
    n86 --> n98
    n113 --> n120
    n114 --> n120
    n112 --> n120
    n69 --> n74
    n61 --> n75
    n63 --> n76
    n42 --> n57
    n121 --> n123
    n122 --> n123
    n25 --> n30
    n27 --> n30
    n97 --> n108
    n96 --> n108
    n45 --> n58
    n55 --> n69
    n67 --> n77
    n25 x--x n26
    n25 x--x n27
    n28 x--x n29
    n111 x--x n115
    n73 x--x n74
```

# RAJ_his_majestys_loyal_government

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n25["RAJ_great_depression_price_controls"]
        n26{"RAJ_his_majestys_loyal_government"}
        n27["RAJ_provincial_autonomy"]
    end
    subgraph tier_1["Tier 1"]
        n124["RAJ_expand_the_zamindari_system"]
        n125{"RAJ_indian_gentleman_officers"}
        n126["RAJ_the_government_of_india_act"]
    end
    subgraph tier_2["Tier 2"]
        n127["RAJ_consult_with_congress_leaders"]
        n128["RAJ_crown_commodities"]
        n129["RAJ_linlithgows_declaration_of_war"]
        n130["RAJ_preemptive_invasion_of_iran"]
        n131["RAJ_the_aden_protectorate"]
        n132["RAJ_the_riches_of_the_raj"]
        n133{"RAJ_work_with_local_leaders"}
    end
    subgraph tier_3["Tier 3"]
        n134["RAJ_concessions_to_the_industrialists"]
        n135["RAJ_curtail_the_zamindars"]
        n136["RAJ_empower_provincial_authorities"]
        n137["RAJ_imperial_rail_renewal_act"]
        n138["RAJ_mobilization_of_the_indian_army"]
        n139["RAJ_strengthen_ties_with_british_investors_GOE"]
    end
    subgraph tier_4["Tier 4"]
        n140["RAJ_assume_eastern_naval_responsibilities"]
        n141{"RAJ_confer_with_the_congress"}
        n142["RAJ_exploit_the_frontier"]
        n143["RAJ_overlords_railway_investment"]
        n144["RAJ_raise_import_duties"]
        n145["RAJ_reform_the_agricultural_sector"]
        n146["RAJ_south_east_asia_command"]
        n147["RAJ_support_naval_invasions"]
        n148["RAJ_the_empires_workshop"]
    end
    subgraph tier_5["Tier 5"]
        n149{"RAJ_court_the_princes"}
        n150["RAJ_desert_training"]
        n151{"RAJ_favor_the_muslim_league"}
        n152["RAJ_hill_training"]
        n153["RAJ_imperial_industry_initiative"]
        n154["RAJ_jungle_training_GOE"]
        n155["RAJ_rural_development_plan"]
        n156["RAJ_rural_mechanization_program"]
        n157["RAJ_urban_training"]
    end
    subgraph tier_6["Tier 6"]
        n158["RAJ_defense_of_burma"]
        n159["RAJ_defense_of_malaya"]
        n160["RAJ_fortify_el_alamein"]
        n161["RAJ_free_abyssinia"]
        n162["RAJ_princely_state_donations_GOE"]
        n163["RAJ_territorial_development_scheme"]
        n164["RAJ_the_defense_of_hong_kong"]
        n165["RAJ_the_great_recovery"]
        n166["RAJ_the_indian_parliament"]
        n167["RAJ_the_integrity_of_india_act"]
    end
    subgraph tier_7["Tier 7"]
        n168["RAJ_holding_the_gates_of_india"]
        n169["RAJ_institute_of_fundamental_research_GOE"]
        n170["RAJ_the_jewel_becomes_the_crown"]
        n171["RAJ_the_punjab_accord"]
    end
    subgraph tier_8["Tier 8"]
        n172["RAJ_keep_calm_and_carry_on"]
        n173["RAJ_the_dominion_of_india"]
    end
    n138 --> n140
    n133 --> n134
    n134 --> n141
    n136 --> n141
    n125 --> n127
    n141 --> n149
    n124 --> n128
    n133 --> n135
    n154 --> n158
    n152 --> n158
    n154 --> n159
    n146 --> n150
    n133 --> n136
    n26 --> n124
    n137 --> n142
    n141 --> n151
    n150 --> n160
    n152 --> n161
    n146 --> n152
    n158 --> n168
    n144 --> n153
    n132 --> n137
    n26 --> n125
    n163 --> n169
    n148 --> n169
    n146 --> n154
    n169 --> n172
    n125 --> n129
    n129 --> n138
    n127 --> n138
    n137 --> n143
    n125 --> n130
    n149 --> n162
    n135 --> n144
    n135 --> n145
    n144 --> n155
    n145 --> n156
    n128 --> n156
    n138 --> n146
    n128 --> n139
    n132 --> n139
    n138 --> n147
    n155 --> n163
    n145 --> n163
    n125 --> n131
    n157 --> n164
    n171 --> n173
    n128 --> n148
    n139 --> n148
    n26 --> n126
    n153 --> n165
    n155 --> n165
    n151 --> n166
    n149 --> n166
    n149 --> n167
    n151 --> n167
    n166 --> n170
    n167 --> n170
    n166 --> n171
    n167 --> n171
    n124 --> n132
    n146 --> n157
    n126 --> n133
    n134 x--x n136
    n127 x--x n129
    n149 x--x n151
    n135 x--x n124
    n25 x--x n26
    n26 x--x n27
    n166 x--x n167
```

# RAJ_indian_air_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n174["RAJ_abolish_agrarian_society_criteria"]
        n175(("RAJ_indian_air_force"))
    end
    subgraph tier_1["Tier 1"]
        n176["RAJ_trainer_planes"]
        n177["RAJ_womens_auxiliary_air_force"]
    end
    subgraph tier_2["Tier 2"]
        n178["RAJ_douglas_dakota"]
        n179["RAJ_ground_pounder"]
        n180["RAJ_long_range_escorts"]
        n181["RAJ_spitfire"]
    end
    subgraph tier_3["Tier 3"]
        n182["RAJ_british_air_experts"]
        n183["RAJ_vultee_vengeance"]
    end
    subgraph tier_4["Tier 4"]
        n184["RAJ_royal_indian_air_force_dlc"]
        n185["RAJ_smiling_buddah"]
        n186["RAJ_special_operations_executive"]
    end
    n181 --> n182
    n180 --> n182
    n176 --> n178
    n176 --> n179
    n176 --> n180
    n182 --> n184
    n182 --> n185
    n174 --> n185
    n182 --> n186
    n176 --> n181
    n175 --> n176
    n179 --> n183
    n175 --> n177
```

# RAJ_indianize_the_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n187(("RAJ_indianize_the_army"))
        n188["RAJ_keep_british_generals"]
    end
    subgraph tier_1["Tier 1"]
        n189["RAJ_defense_of_india_act"]
        n190{"RAJ_forming_an_indian_doctrine"}
    end
    subgraph tier_2["Tier 2"]
        n191{"RAJ_model_after_germany"}
        n192{"RAJ_model_after_soviet"}
        n193{"RAJ_model_after_usa"}
    end
    subgraph tier_3["Tier 3"]
        n194["RAJ_automating_the_army"]
        n195["RAJ_for_the_people_by_the_people"]
    end
    n193 --> n194
    n191 --> n194
    n187 --> n189
    n188 --> n189
    n193 --> n195
    n192 --> n195
    n187 --> n190
    n190 --> n191
    n190 --> n192
    n190 --> n193
    n194 x--x n195
    n187 x--x n188
    n191 x--x n192
    n191 x--x n193
    n192 x--x n193
```

# RAJ_keep_british_generals

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n187["RAJ_indianize_the_army"]
        n188(("RAJ_keep_british_generals"))
    end
    subgraph tier_1["Tier 1"]
        n189["RAJ_defense_of_india_act"]
        n196["RAJ_learn_from_the_crown"]
    end
    subgraph tier_2["Tier 2"]
        n197["RAJ_colonial_cadet_exchange"]
        n198["RAJ_join_the_shadow_scheme"]
    end
    subgraph tier_3["Tier 3"]
        n199["RAJ_learn_from_the_secret_intelligence_service"]
        n200["RAJ_purchase_british_supply_equipment"]
    end
    n196 --> n197
    n187 --> n189
    n188 --> n189
    n196 --> n198
    n188 --> n196
    n197 --> n199
    n197 --> n200
    n187 x--x n188
```

# RAJ_local_recruitment_offices

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n182["RAJ_british_air_experts"]
        n201(("RAJ_local_recruitment_offices"))
        n202["RAJ_military_pensions"]
    end
    subgraph tier_1["Tier 1"]
        n203["RAJ_legacy_of_military_service"]
    end
    subgraph tier_2["Tier 2"]
        n204["RAJ_indian_army_corps_of_engineers"]
        n205["RAJ_regimental_loyalty"]
        n206["RAJ_relax_agrarian_society_criteria"]
    end
    subgraph tier_3["Tier 3"]
        n174["RAJ_abolish_agrarian_society_criteria"]
        n207["RAJ_military_engineer_services"]
        n208["RAJ_siege_batteries"]
    end
    subgraph tier_4["Tier 4"]
        n209["RAJ_campaign_against_agrarian_societys"]
        n185["RAJ_smiling_buddah"]
    end
    n206 --> n174
    n205 --> n174
    n174 --> n209
    n203 --> n204
    n202 --> n204
    n201 --> n203
    n204 --> n207
    n203 --> n205
    n203 --> n206
    n204 --> n208
    n182 --> n185
    n174 --> n185
```

# RAJ_military_pensions

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n203["RAJ_legacy_of_military_service"]
        n202{"RAJ_military_pensions"}
        n210["RAJ_mountain_guns"]
        n211{"RAJ_royal_indian_artillery_dlc"}
    end
    subgraph tier_1["Tier 1"]
        n212["RAJ_frontier_corps"]
        n204["RAJ_indian_army_corps_of_engineers"]
        n213["RAJ_indian_states_force"]
        n214["RAJ_specialized_dietary_requirement"]
        n215["RAJ_standardized_rations"]
        n216["RAJ_womens_auxiliary_corps"]
    end
    subgraph tier_2["Tier 2"]
        n217["RAJ_indian_territorial_force"]
        n207["RAJ_military_engineer_services"]
        n218["RAJ_quinine"]
        n208["RAJ_siege_batteries"]
        n219["RAJ_the_burma_rifles"]
        n220["RAJ_viceroys_body_guard"]
    end
    subgraph tier_3["Tier 3"]
        n221["RAJ_gurkhas"]
        n222["RAJ_help_from_the_nagas"]
        n223["RAJ_re_establish_the_khyber_rifles"]
    end
    subgraph tier_4["Tier 4"]
        n224["RAJ_chindits_dlc"]
        n225["RAJ_lions_of_the_great_war_dlc"]
    end
    n223 --> n224
    n202 --> n212
    n219 --> n221
    n217 --> n222
    n203 --> n204
    n202 --> n204
    n202 --> n213
    n212 --> n217
    n221 --> n225
    n204 --> n207
    n214 --> n218
    n215 --> n218
    n217 --> n223
    n210 --> n223
    n204 --> n208
    n202 --> n214
    n211 --> n214
    n202 --> n215
    n211 --> n215
    n212 --> n219
    n213 --> n220
    n202 --> n216
    n214 x--x n215
```

# RAJ_provincial_autonomy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n25["RAJ_great_depression_price_controls"]
        n26["RAJ_his_majestys_loyal_government"]
        n27(("RAJ_provincial_autonomy"))
    end
    subgraph tier_1["Tier 1"]
        n226["RAJ_princely_states_policy"]
        n227{"RAJ_purna_swaraj"}
        n30["RAJ_trade_port"]
    end
    subgraph tier_2["Tier 2"]
        n31["RAJ_fortify_aden"]
        n228{"RAJ_league_against_gandhism"}
        n229["RAJ_mahatma"]
        n230["RAJ_swadeshi_movement"]
        n231["RAJ_uplifting_the_people_of_india"]
    end
    subgraph tier_3["Tier 3"]
        n232{"RAJ_a_congress_resurgent"}
        n233{"RAJ_all_india_kisan_sabha"}
        n234["RAJ_boycott_british_made_goods"]
        n235["RAJ_form_a_federal_court"]
        n236["RAJ_forward_bloc"]
        n237["RAJ_khadi_movement"]
        n238{"RAJ_rally_the_indian_left"}
        n239["RAJ_tenancy_reforms"]
    end
    subgraph tier_4["Tier 4"]
        n240["RAJ_agricultural_cooperatives"]
        n241["RAJ_cottage_industries"]
        n242["RAJ_debt_relief"]
        n243["RAJ_freedom_of_the_press"]
        n244["RAJ_india_united"]
        n245["RAJ_litteracy_effort"]
        n246["RAJ_national_planning_committee"]
        n247["RAJ_promote_violence_against_the_british"]
        n248["RAJ_protest_against_the_howell_monument"]
        n249["RAJ_red_in_the_shadows"]
        n250["RAJ_two_nation_theory_dlc"]
    end
    subgraph tier_5["Tier 5"]
        n251["RAJ_all_india_students_federation"]
        n252["RAJ_azad_hind_dlc"]
        n253{"RAJ_give_me_blood_and_i_will_grant_you_freedom"}
        n254["RAJ_go_into_hiding"]
        n255["RAJ_handloom_weaving"]
        n256["RAJ_indian_legion"]
        n257["RAJ_indo_centric_curriculum"]
        n258{"RAJ_local_resistance_to_land_taxes"}
        n259["RAJ_orchestrate_train_robberies"]
        n260["RAJ_power_sharing_agreement"]
        n261["RAJ_rani_of_jhansi_regiment"]
        n262["RAJ_royal_indian_navy_mutiny"]
        n263{"RAJ_tea_exports"}
        n264["RAJ_the_pakistan_movement"]
    end
    subgraph tier_6["Tier 6"]
        n265["RAJ_a_permanent_muslim_governmental_seat"]
        n266["RAJ_azad_hind_dlc_radio"]
        n267["RAJ_cabinet_mission_plan"]
        n268["RAJ_cripps_mission_dlc"]
        n269["RAJ_enrollment_of_dali_children"]
        n270["RAJ_founding_of_the_peoples_republic"]
        n271["RAJ_haripura_session_of_the_indian_national_congress"]
        n272["RAJ_hindutva"]
        n273["RAJ_infiltrate_aden"]
        n274{"RAJ_lahore_resolution"}
        n275{"RAJ_netaji"}
        n276["RAJ_seek_domestic_allies"]
        n277["RAJ_seek_japanese_support"]
        n278["RAJ_temple_entry_movements"]
        n279["RAJ_the_red_curtain_falls_over_asia"]
        n280["RAJ_war_taxes"]
    end
    subgraph tier_7["Tier 7"]
        n281["RAJ_akhand_bharat"]
        n282["RAJ_authoritarianship"]
        n283["RAJ_azad_hind_dlc_bank"]
        n284["RAJ_bhutanese_protectorate"]
        n285["RAJ_coal_fire_and_steel"]
        n286{"RAJ_constitution_for_the_masses"}
        n287["RAJ_cult_of_personality"]
        n288["RAJ_eastern_pakistan"]
        n289["RAJ_exile_princes"]
        n290["RAJ_expand_healthcare_facilities"]
        n291["RAJ_extend_indian_security_zone"]
        n292["RAJ_guided_democracy"]
        n293["RAJ_hindu_mahasabha"]
        n294["RAJ_inclusive_nationalism"]
        n295["RAJ_indian_independence_act"]
        n296["RAJ_jugantar"]
        n297{"RAJ_purge_the_reactionaries"}
        n298["RAJ_red_punjab_operation"]
        n299["RAJ_sanatani"]
        n300["RAJ_secure_rajahsthan"]
        n301["RAJ_sikh_religious_guarantees"]
        n302["RAJ_strike_eastern_pakistan"]
        n303["RAJ_the_enemy_of_my_enemy"]
        n304["RAJ_the_indian_national_army"]
        n305["RAJ_the_second_duar_war"]
        n306["RAJ_united_bengal"]
    end
    subgraph tier_8["Tier 8"]
        n307["RAJ_a_secular_state"]
        n308["RAJ_agrarian_socialism"]
        n309["RAJ_appoint_german_friendly_government"]
        n310["RAJ_deathblow_to_imperial_remnants"]
        n311["RAJ_demand_return_of_imperialist_colonies"]
        n312["RAJ_education_efforts_2"]
        n313["RAJ_heavy_industries"]
        n314["RAJ_hedgemony_of_the_subcontinent"]
        n315["RAJ_high_altitude_training"]
        n316["RAJ_hindi_as_a_national_language"]
        n317["RAJ_integrate_the_princes"]
        n318["RAJ_join_the_co_prospherity_sphere"]
        n319["RAJ_partition_preparation"]
        n320["RAJ_punjab_autonomy"]
        n321["RAJ_seek_financial_aid_from_the_ussr"]
        n322["RAJ_seven_shackles"]
        n323["RAJ_shaheed_and_swaraj"]
        n324["RAJ_strike_against_china"]
        n325["RAJ_the_second_gorkha_war"]
        n326["RAJ_the_sword_and_the_saffron"]
        n327["RAJ_urban_industrialism"]
    end
    subgraph tier_9["Tier 9"]
        n328["RAJ_appoint_soviet_friendly_government"]
        n329["RAJ_burn_down_the_cellular_jail"]
        n330["RAJ_central_comittee_authority"]
        n331["RAJ_comrades_of_the_city"]
        n332["RAJ_cultural_reawekening"]
        n333["RAJ_decentralize_the_party"]
        n334["RAJ_focus_on_the_countryside"]
        n335["RAJ_industrialize_the_ganges"]
        n336["RAJ_integrate_the_princes2"]
        n337["RAJ_land_of_the_tillers"]
        n338["RAJ_nationalize_british_owned_factories"]
        n339["RAJ_planned_economy"]
        n340["RAJ_rashtriya_swayamsevak_sangh"]
        n341["RAJ_stopping_the_japanese_threat_into_central_asia"]
        n342["RAJ_strike_burma"]
        n343{"RAJ_tryst_with_destiny"}
    end
    subgraph tier_10["Tier 10"]
        n344["RAJ_bhoodan_movement"]
        n345["RAJ_five_year_plan"]
        n346["RAJ_i_am_death"]
        n347["RAJ_pledge_for_the_allies"]
        n348["RAJ_sideline_the_conflict"]
        n349["RAJ_the_hindu_martial_tradition"]
        n350["RAJ_the_sun_sets"]
    end
    subgraph tier_11["Tier 11"]
        n351["RAJ_destroyer_of_worlds"]
        n352["RAJ_indian_socialism"]
        n353["RAJ_kingmaker"]
        n354["RAJ_preamble_to_the_constitution_of_india"]
        n355["RAJ_soviet_influence"]
    end
    subgraph tier_12["Tier 12"]
        n356["RAJ_arm_the_peasantry"]
        n357["RAJ_break_the_zamindars"]
        n358["RAJ_education_for_the_masses"]
        n359["RAJ_expand_industry_in_hyderabad"]
        n360["RAJ_india_indivisible"]
        n361["RAJ_indian_national_highways"]
        n362["RAJ_reorganize_the_five_year_plan_towards_heavy_industry"]
        n363["RAJ_rolling_nuke_barrages"]
        n364["RAJ_soviet_indian_industrial_cooperation"]
        n365["RAJ_the_peoples_liberation_army"]
        n366["RAJ_uranium_tipped_bullets"]
    end
    subgraph tier_13["Tier 13"]
        n367["RAJ_an_economy_unbound"]
        n368["RAJ_annex_goa"]
        n369["RAJ_contamination_cleanup_crew"]
        n370["RAJ_defend_burma"]
        n371["RAJ_every_man_a_gun"]
        n372["RAJ_focus_on_military_industry"]
        n373["RAJ_invite_soviet_industrial_experts"]
        n374["RAJ_jaguar"]
        n375["RAJ_nationalize_tata_group"]
        n376["RAJ_planned_but_decentralized"]
        n377["RAJ_suppress_paramilitary_organizations"]
        n378["RAJ_the_revolutionary_army_marches"]
    end
    subgraph tier_14["Tier 14"]
        n379["RAJ_a_tiger_unchained"]
        n380["RAJ_bathe_in_hellfire"]
        n381["RAJ_every_man_a_leader"]
        n382["RAJ_import_substitution_industrialisation"]
        n383["RAJ_nationalize_gun_carriage_agency"]
        n384["RAJ_planned_economy2"]
        n385["RAJ_quality_training"]
        n386["RAJ_socialist_self_reliance"]
    end
    subgraph tier_15["Tier 15"]
        n387["RAJ_continue_the_five_year_plan"]
        n388["RAJ_defenders_of_the_revolution"]
        n389["RAJ_fight_malnutrition"]
        n390["RAJ_iron_will_indoctrination"]
        n391["RAJ_land_reforms"]
        n392["RAJ_mixed_economy"]
    end
    subgraph tier_16["Tier 16"]
        n393["RAJ_education_efforts"]
    end
    subgraph tier_17["Tier 17"]
        n394["RAJ_to_shake_the_world"]
    end
    n229 --> n232
    n260 --> n265
    n294 --> n307
    n368 --> n379
    n297 --> n308
    n286 --> n308
    n239 --> n240
    n272 --> n281
    n228 --> n233
    n245 --> n251
    n360 --> n367
    n360 --> n368
    n287 --> n309
    n321 --> n328
    n352 --> n356
    n275 --> n282
    n248 --> n252
    n280 --> n283
    n252 --> n266
    n369 --> n380
    n374 --> n380
    n337 --> n344
    n275 --> n284
    n230 --> n234
    n352 --> n357
    n322 --> n329
    n260 --> n267
    n327 --> n330
    n275 --> n285
    n272 --> n285
    n327 --> n331
    n270 --> n286
    n366 --> n369
    n386 --> n387
    n383 --> n387
    n384 --> n387
    n239 --> n241
    n263 --> n268
    n275 --> n287
    n322 --> n332
    n316 --> n332
    n298 --> n310
    n300 --> n310
    n302 --> n310
    n239 --> n242
    n308 --> n333
    n360 --> n370
    n381 --> n388
    n282 --> n311
    n292 --> n311
    n346 --> n351
    n274 --> n288
    n389 --> n393
    n283 --> n312
    n352 --> n358
    n257 --> n269
    n356 --> n371
    n371 --> n381
    n279 --> n289
    n269 --> n290
    n352 --> n359
    n355 --> n359
    n275 --> n291
    n382 --> n389
    n333 --> n345
    n330 --> n345
    n362 --> n372
    n308 --> n334
    n231 --> n235
    n30 --> n31
    n228 --> n236
    n262 --> n270
    n235 --> n243
    n248 --> n253
    n247 --> n253
    n248 --> n254
    n275 --> n292
    n241 --> n255
    n240 --> n255
    n258 --> n271
    n285 --> n313
    n288 --> n314
    n306 --> n314
    n291 --> n315
    n299 --> n316
    n272 --> n293
    n275 --> n293
    n253 --> n272
    n343 --> n346
    n367 --> n382
    n267 --> n294
    n265 --> n294
    n354 --> n360
    n232 --> n244
    n271 --> n295
    n268 --> n295
    n248 --> n256
    n352 --> n361
    n355 --> n361
    n345 --> n352
    n333 --> n352
    n245 --> n257
    n327 --> n335
    n256 --> n273
    n254 --> n273
    n289 --> n317
    n315 --> n336
    n362 --> n373
    n385 --> n390
    n363 --> n374
    n303 --> n318
    n279 --> n296
    n230 --> n237
    n348 --> n353
    n264 --> n274
    n308 --> n337
    n382 --> n391
    n227 --> n228
    n235 --> n245
    n240 --> n258
    n234 --> n258
    n227 --> n229
    n382 --> n392
    n239 --> n246
    n310 --> n338
    n372 --> n383
    n361 --> n375
    n359 --> n375
    n253 --> n275
    n249 --> n259
    n306 --> n319
    n288 --> n319
    n358 --> n376
    n357 --> n376
    n321 --> n339
    n373 --> n384
    n343 --> n347
    n244 --> n260
    n348 --> n354
    n347 --> n354
    n346 --> n354
    n27 --> n226
    n236 --> n247
    n236 --> n248
    n301 --> n320
    n270 --> n297
    n27 --> n227
    n378 --> n385
    n228 --> n238
    n236 --> n261
    n249 --> n261
    n326 --> n340
    n233 --> n249
    n238 --> n249
    n279 --> n298
    n355 --> n362
    n351 --> n363
    n249 --> n262
    n272 --> n299
    n279 --> n300
    n254 --> n276
    n291 --> n321
    n252 --> n277
    n299 --> n322
    n303 --> n323
    n343 --> n348
    n278 --> n301
    n269 --> n301
    n257 --> n301
    n376 --> n386
    n355 --> n364
    n345 --> n355
    n330 --> n355
    n310 --> n341
    n291 --> n324
    n311 --> n342
    n279 --> n302
    n360 --> n377
    n227 --> n230
    n240 --> n263
    n257 --> n278
    n231 --> n239
    n277 --> n303
    n316 --> n349
    n340 --> n349
    n280 --> n304
    n250 --> n264
    n355 --> n365
    n262 --> n279
    n365 --> n378
    n275 --> n305
    n305 --> n325
    n284 --> n325
    n342 --> n350
    n299 --> n326
    n392 --> n394
    n391 --> n394
    n393 --> n394
    n25 --> n30
    n27 --> n30
    n306 --> n343
    n288 --> n343
    n307 --> n343
    n232 --> n250
    n274 --> n306
    n227 --> n231
    n351 --> n366
    n297 --> n327
    n286 --> n327
    n252 --> n280
    n308 x--x n327
    n282 x--x n292
    n284 x--x n305
    n268 x--x n271
    n288 x--x n306
    n236 x--x n249
    n25 x--x n27
    n272 x--x n275
    n26 x--x n27
    n346 x--x n347
    n346 x--x n348
    n244 x--x n250
    n228 x--x n229
    n347 x--x n348
```

# RAJ_royal_indian_artillery_dlc

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n217["RAJ_indian_territorial_force"]
        n202{"RAJ_military_pensions"}
        n7["RAJ_ordnance_factory_khamaria_jabalpur"]
        n211{"RAJ_royal_indian_artillery_dlc"}
    end
    subgraph tier_1["Tier 1"]
        n395["RAJ_armoured_corps_center_and_school"]
        n210["RAJ_mountain_guns"]
        n214["RAJ_specialized_dietary_requirement"]
        n215["RAJ_standardized_rations"]
    end
    subgraph tier_2["Tier 2"]
        n2["RAJ_mechanization_of_the_cavalry"]
        n218["RAJ_quinine"]
        n223["RAJ_re_establish_the_khyber_rifles"]
    end
    subgraph tier_3["Tier 3"]
        n224["RAJ_chindits_dlc"]
        n10["RAJ_engineering_revolution"]
        n396["RAJ_mountain_tanks"]
    end
    n211 --> n395
    n223 --> n224
    n2 --> n10
    n7 --> n10
    n395 --> n2
    n211 --> n210
    n2 --> n396
    n214 --> n218
    n215 --> n218
    n217 --> n223
    n210 --> n223
    n202 --> n214
    n211 --> n214
    n202 --> n215
    n211 --> n215
    n214 x--x n215
```

# RAJ_royal_indian_navy_dlc

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n397(("RAJ_royal_indian_navy_dlc"))
    end
    subgraph tier_1["Tier 1"]
        n398{"RAJ_black_swan_sloops"}
        n399{"RAJ_expand_mazagon_dock_dlc"}
        n400["RAJ_indian_marine_corps"]
    end
    subgraph tier_2["Tier 2"]
        n401["RAJ_found_scindia_shipyard_dlc"]
        n402["RAJ_madras_ship_repair_factories"]
        n403["RAJ_obtain_british_naval_contracts"]
    end
    subgraph tier_3["Tier 3"]
        n404["RAJ_dominate_the_bay_of_bengal"]
        n405["RAJ_indian_cruiser_development"]
        n406["RAJ_purchase_decomissioned_british_ships"]
        n407["RAJ_request_transfer_of_british_commanders"]
    end
    subgraph tier_4["Tier 4"]
        n408["RAJ_increase_funding_for_the_GRSE"]
        n409["RAJ_obtain_modern_ship_contracts"]
        n410["RAJ_womens_royal_indian_naval_service"]
    end
    subgraph tier_5["Tier 5"]
        n411["RAJ_eastern_shipyard_construction"]
        n412["RAJ_modernizing_navy_dlc"]
    end
    n397 --> n398
    n401 --> n404
    n408 --> n411
    n397 --> n399
    n398 --> n401
    n399 --> n401
    n404 --> n408
    n405 --> n408
    n401 --> n405
    n397 --> n400
    n400 --> n402
    n409 --> n412
    n408 --> n412
    n398 --> n403
    n399 --> n403
    n406 --> n409
    n403 --> n406
    n403 --> n407
    n405 --> n410
    n401 x--x n403
```
