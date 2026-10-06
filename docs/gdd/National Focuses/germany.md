# GER_develop_modern_maneuver_warfare

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"GER_develop_modern_maneuver_warfare"}
        n2["GER_dive_bombers"]
    end
    subgraph tier_1["Tier 1"]
        n3["GER_adopt_new_panzer_doctrine"]
        n4["GER_fortify_the_vaterland"]
        n5["GER_the_prussian_legacy"]
    end
    subgraph tier_2["Tier 2"]
        n6["GER_advanced_panzer_research"]
        n7["GER_all_terrain_military_motorcycle"]
        n8["GER_improve_motorized_troops"]
        n9["GER_instill_auftragstaktik"]
        n10["GER_lessons_of_the_great_war"]
        n11["GER_panzer_troops_school"]
        n12["GER_salvage_captured_equipment"]
    end
    subgraph tier_3["Tier 3"]
        n13["GER_artillery_bombardment"]
        n14["GER_combined_arms"]
        n15["GER_establish_the_afrikakorps"]
        n16["GER_establish_the_skijager"]
        n17["GER_expand_kummersdorfs_capacity"]
        n18{"GER_panzergrenadier"}
    end
    subgraph tier_4["Tier 4"]
        n19["GER_defend_the_vaterland"]
        n20["GER_improve_the_logistics_system"]
        n21["GER_kriegslokomotiven"]
        n22["GER_nationalize_ford_factories"]
        n23["GER_stormtroopers"]
    end
    subgraph tier_5["Tier 5"]
        n24["GER_uranverein"]
    end
    n1 --> n3
    n3 --> n6
    n5 --> n7
    n3 --> n7
    n10 --> n13
    n8 --> n13
    n6 --> n14
    n2 --> n14
    n18 --> n19
    n9 --> n15
    n9 --> n16
    n6 --> n17
    n11 --> n17
    n1 --> n4
    n5 --> n8
    n18 --> n20
    n5 --> n9
    n3 --> n9
    n18 --> n21
    n5 --> n10
    n18 --> n22
    n3 --> n11
    n9 --> n18
    n5 --> n12
    n3 --> n12
    n13 --> n23
    n1 --> n5
    n20 --> n24
    n19 --> n24
    n3 x--x n5
    n19 x--x n20
```

# GER_expanding_the_luftwaffe

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n6["GER_advanced_panzer_research"]
        n25["GER_construct_aircraft_carriers"]
        n26(("GER_expanding_the_luftwaffe"))
    end
    subgraph tier_1["Tier 1"]
        n27{"GER_aeronautical_research_institute"}
        n28["GER_fallschirmjager"]
        n29["GER_form_the_jagdwaffe"]
    end
    subgraph tier_2["Tier 2"]
        n30["GER_develop_the_knickebein"]
        n2["GER_dive_bombers"]
        n31["GER_experimental_rotorcrafts"]
        n32["GER_reorganize_the_luftwaffe"]
        n33["GER_tactical_bombers"]
        n34["GER_uralbomber_program"]
    end
    subgraph tier_3["Tier 3"]
        n14["GER_combined_arms"]
        n35["GER_defense_of_the_reich"]
        n36["GER_rocketry_innovations"]
        n37["GER_solve_the_logistical_bottlenecks"]
        n38["GER_torpedobomber"]
    end
    subgraph tier_4["Tier 4"]
        n39["GER_construct_the_kammhuber_line"]
        n40["GER_establish_carrier_groups"]
        n41["GER_establish_night_fighter_squadrons"]
    end
    subgraph tier_5["Tier 5"]
        n42["GER_aerodynamic_research_institute"]
    end
    subgraph tier_6["Tier 6"]
        n43["GER_amerikabomber"]
    end
    n37 --> n42
    n39 --> n42
    n41 --> n42
    n36 --> n42
    n26 --> n27
    n42 --> n43
    n6 --> n14
    n2 --> n14
    n35 --> n39
    n32 --> n35
    n30 --> n35
    n29 --> n30
    n27 --> n2
    n38 --> n40
    n25 --> n40
    n35 --> n41
    n29 --> n31
    n26 --> n28
    n26 --> n29
    n29 --> n32
    n2 --> n36
    n33 --> n36
    n34 --> n36
    n32 --> n37
    n27 --> n33
    n30 --> n38
    n27 --> n34
    n2 x--x n33
    n2 x--x n34
    n33 x--x n34
```

# GER_oppose_hitler

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n44(("GER_oppose_hitler"))
        n45["GER_oppose_hitler_ww"]
        n46["GER_remilitarize_the_rhineland"]
    end
    subgraph tier_1["Tier 1"]
        n47["GER_legion_condor"]
        n48{"GER_secure_the_new_state"}
    end
    subgraph tier_2["Tier 2"]
        n49["GER_reestablish_free_elections"]
        n50["GER_revive_the_kaiserreich"]
    end
    subgraph tier_3["Tier 3"]
        n51["GER_rebuild_the_nation"]
        n52{"GER_return_of_the_kaiser"}
        n53["GER_the_monarchy_compromise"]
    end
    subgraph tier_4["Tier 4"]
        n54["GER_a_new_and_better_germany"]
        n55{"GER_expatriate_the_communists"}
        n56["GER_fan_the_prussian_militarism"]
        n57{"GER_focus_on_the_true_enemy"}
        n58["GER_reverse_the_brain_drain"]
        n59["GER_see_to_the_eastern_front"]
        n60["GER_the_great_red_menace"]
    end
    subgraph tier_5["Tier 5"]
        n61["GER_accept_british_naval_dominance"]
        n62["GER_bulwark_against_bolshevism"]
        n63["GER_rebuild_the_high_seas_fleet"]
        n64["GER_safeguard_the_baltic"]
    end
    subgraph tier_6["Tier 6"]
        n65["GER_ally_the_shade"]
        n66["GER_central_european_alliance"]
        n67["GER_danzig_for_guarantees"]
        n68["GER_our_place_in_the_sun"]
        n69["GER_support_the_finns"]
    end
    subgraph tier_7["Tier 7"]
        n70["GER_anti_comintern_pact_unaligned"]
        n71["GER_carte_blanche_for_alsace_and_french_colonies"]
        n72["GER_danubian_membership"]
        n73["GER_low_countries_membership"]
        n74["GER_prepare_for_the_next_blockade"]
        n75["GER_pride_of_the_modern_germany"]
        n76["GER_scandinavian_membership"]
        n77["GER_shared_rd_programs"]
        n78["GER_the_central_powers"]
    end
    subgraph tier_8["Tier 8"]
        n79["GER_anti_soviet_pact_unaligned"]
        n80["GER_baltic_membership"]
        n81["GER_break_the_anglo_french_colonial_hegemony"]
        n82["GER_bypass_maginot_in_the_south"]
        n83["GER_danubian_expansion"]
        n84["GER_finnish_membership"]
        n85["GER_no_reds_in_western_europe"]
        n86["GER_polish_membership"]
        n87["GER_pool_technical_know_how"]
        n88["GER_prepare_italian_coup"]
        n89["GER_rekindle_imperial_sentiment"]
        n90["GER_the_mannheim_project"]
    end
    subgraph tier_9["Tier 9"]
        n91["GER_assassinate_mussolini"]
        n92["GER_no_balkan_communism"]
        n93["GER_schlieffen_once_more"]
        n94["GER_strike_at_the_source"]
        n95["GER_tackle_the_communist_threat"]
    end
    subgraph tier_10["Tier 10"]
        n96["GER_reinstate_imperial_possessions"]
        n97["GER_the_iberian_problem"]
    end
    n51 --> n54
    n55 --> n61
    n61 --> n65
    n69 --> n70
    n67 --> n70
    n70 --> n79
    n88 --> n91
    n76 --> n80
    n74 --> n81
    n56 --> n62
    n54 --> n62
    n71 --> n82
    n65 --> n71
    n60 --> n66
    n62 --> n66
    n72 --> n83
    n66 --> n72
    n59 --> n67
    n62 --> n67
    n52 --> n55
    n51 --> n56
    n76 --> n84
    n52 --> n57
    n46 --> n47
    n45 --> n47
    n44 --> n47
    n66 --> n73
    n83 --> n92
    n73 --> n85
    n63 --> n68
    n76 --> n86
    n77 --> n87
    n68 --> n74
    n78 --> n88
    n68 --> n75
    n57 --> n63
    n50 --> n51
    n49 --> n51
    n48 --> n49
    n93 --> n96
    n82 --> n96
    n78 --> n89
    n50 --> n52
    n53 --> n58
    n48 --> n50
    n59 --> n64
    n66 --> n76
    n81 --> n93
    n44 --> n48
    n52 --> n59
    n58 --> n77
    n66 --> n77
    n80 --> n94
    n86 --> n94
    n84 --> n94
    n64 --> n69
    n79 --> n95
    n71 --> n95
    n68 --> n78
    n53 --> n60
    n95 --> n97
    n77 --> n90
    n76 --> n90
    n49 --> n53
    n61 x--x n63
    n55 x--x n57
    n44 x--x n46
    n49 x--x n50
```

# GER_oppose_hitler_ww

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n44["GER_oppose_hitler"]
        n45(("GER_oppose_hitler_ww"))
        n46["GER_remilitarize_the_rhineland"]
    end
    subgraph tier_1["Tier 1"]
        n47["GER_legion_condor"]
        n98["GER_rally_the_nation"]
        n99{"GER_tend_to_the_future_of_germany"}
    end
    subgraph tier_2["Tier 2"]
        n100["GER_denazification_campaigns"]
        n101{"GER_monarchist_sentiment"}
        n102["GER_rebuild_the_nation_ww"]
        n103["GER_start_the_proletarian_revolution"]
    end
    subgraph tier_3["Tier 3"]
        n104["GER_formalize_the_intelligence_wing"]
        n105["GER_ressurect_the_red_front_fighters_league"]
        n106["GER_revitalize_the_nation"]
        n107{"GER_revive_the_kaiserreich_ww"}
        n108["GER_the_monarchy_compromise_ww"]
        n109{"GER_the_peoples_victory"}
        n110{"GER_weltpolitik"}
    end
    subgraph tier_4["Tier 4"]
        n111["GER_accept_british_naval_dominance_ww"]
        n112["GER_effective_operations"]
        n113["GER_form_the_stasi"]
        n114["GER_legacy_of_the_spartacus_league"]
        n115["GER_military_dictatorship"]
        n116["GER_political_commissars"]
        n117["GER_proletarian_dictatorship"]
        n118["GER_re_establish_free_elections_ww"]
        n119{"GER_realpolitik"}
        n120["GER_reorganize_nationale_volksarmee"]
        n121["GER_return_of_the_kaiser_ww"]
        n122["GER_sign_the_second_treaty_of_berlin"]
        n123["GER_the_second_naval_race"]
    end
    subgraph tier_5["Tier 5"]
        n124["GER_assemble_red_orchestra"]
        n125["GER_assist_our_eastern_comrades"]
        n126{"GER_ban_political_uniforms"}
        n127["GER_carve_up_congo"]
        n128["GER_closer_sino_germanic_relations"]
        n129["GER_defense_treaty_with_the_soviet"]
        n130{"GER_demand_the_return_of_southern_jutland"}
        n131["GER_expatriate_the_communists_ww"]
        n132["GER_fan_prussian_militarism"]
        n133["GER_industrial_cooperation"]
        n134["GER_intervene_in_spain"]
        n135["GER_invite_scientists_back"]
        n136{"GER_mitteleuropa"}
        n137["GER_prepare_for_the_next_naval_blockade"]
        n138["GER_rapid_army_expansion"]
        n139["GER_re_ratify_the_locarno_treaty"]
        n140["GER_rebuild_the_high_seas_fleet_ww"]
        n141["GER_restore_the_brest_litovsk_borders"]
        n142["GER_reverse_the_brain_drain_ww"]
        n143{"GER_see_to_the_eastern_front_ww"}
        n144["GER_social_ownership"]
        n145["GER_state_controlled_economy"]
    end
    subgraph tier_6["Tier 6"]
        n146["GER_all_for_the_front"]
        n147{"GER_anglo_germanic_defense_pact"}
        n148{"GER_break_anglo_french_colonial_hegemony_ww"}
        n149{"GER_brothers_in_arms"}
        n150["GER_central_planning"]
        n151["GER_civil_liberties"]
        n152["GER_danzig_for_guarantees_ww"]
        n153["GER_embrace_democratic_institutions"]
        n154["GER_embrace_liberal_leanings"]
        n155["GER_franco_germanic_pact"]
        n156["GER_glorious_mechanical_machinations"]
        n157["GER_industrial_investments"]
        n158["GER_liberate_austria"]
        n159["GER_memel_ultimatum"]
        n160["GER_nationalize_industries"]
        n161["GER_offer_trade_proposal"]
        n162["GER_pool_technical_know_how_ww"]
        n163["GER_prussian_artillery"]
        n164["GER_re_establish_the_landwehr"]
        n165["GER_re_form_the_freikorps"]
        n166{"GER_reject_the_locarno_treaty"}
        n167["GER_resource_trade"]
        n168["GER_restore_eastern_imperial_possessions"]
        n169["GER_safeguard_poland"]
        n170["GER_safeguard_the_baltic_ww"]
        n171["GER_send_military_aid"]
        n172["GER_shared_rd_programs_ww"]
        n173["GER_spheres_of_influence"]
        n174["GER_strive_for_conservative_values"]
        n175["GER_tech_sharing"]
        n176{"GER_the_austrian_question"}
        n177["GER_tributes_for_guarantees"]
    end
    subgraph tier_7["Tier 7"]
        n178["GER_align_czechoslovakia"]
        n179["GER_anglo_germanic_cooperation_program"]
        n180["GER_asian_allies"]
        n181["GER_backdoor_negotiations"]
        n182["GER_build_the_eastern_bulwark"]
        n183{"GER_carte_blanche_for_alsace_and_french_colonies_ww"}
        n184["GER_carve_up_czechoslovakia"]
        n185["GER_czechoslovakia"]
        n186["GER_demand_further_polish_concessions"]
        n187["GER_demand_lithuanian_integration"]
        n188["GER_expand_african_reach"]
        n189["GER_factories_for_resources"]
        n190["GER_form_agricultural_cooperatives"]
        n191["GER_glory_to_the_imperial_army"]
        n192["GER_labor_rights_and_union_stuff"]
        n193["GER_launch_sino_germanic_joint_research_program"]
        n194["GER_liberate_italy"]
        n195["GER_liberate_oppressed_people"]
        n196["GER_offer_military_production_support"]
        n197["GER_our_place_in_the_sun_ww"]
        n198{"GER_petition_for_the_return_of_old_colonies"}
        n199["GER_poland"]
        n200["GER_rekindle_imperial_sentiment_ww"]
        n201["GER_request_the_return_of_french_held_colonies"]
        n202["GER_request_the_return_of_qingdao"]
        n203["GER_schlieffen_once_more_ww"]
        n204["GER_send_volunteers"]
        n205["GER_spark_the_flame_of_revolution"]
        n206["GER_strengthen_the_welfare_state"]
        n207["GER_support_the_finns_ww"]
        n208["GER_the_german_stakhanovite_movement"]
        n209["GER_the_mannheim_project_ww"]
    end
    subgraph tier_8["Tier 8"]
        n210["GER_african_allies"]
        n211["GER_ally_white_russian_forces"]
        n212["GER_bypass_maginot_in_the_south_ww"]
        n213["GER_democratic_shield"]
        n214["GER_effectivize_the_volkswerke"]
        n215["GER_establish_a_customs_union"]
        n216["GER_establish_eastern_grand_duchies"]
        n217["GER_expand_pacific_holdings"]
        n218["GER_expand_social_welfare"]
        n219["GER_hold_joint_military_drills"]
        n220["GER_hungary"]
        n221["GER_mitteleuropa_cooperation_sphere"]
        n222["GER_protect_the_revolution"]
        n223["GER_realize_mittelafrika"]
        n224["GER_support_the_proletarian_uprising"]
        n225["GER_sway_the_balkans"]
        n226["GER_the_end_to_fascist_europe"]
        n227["GER_the_first_berlin_award"]
        n228{"GER_the_sino_germanic_pact"}
        n229["GER_unify_west_africa"]
    end
    subgraph tier_9["Tier 9"]
        n230["GER_divide_and_conquer"]
        n231["GER_establish_volkskommissariats"]
        n232["GER_establish_western_grand_duchies"]
        n233["GER_extend_mitteleuropas_bounderies"]
        n234["GER_incorporate_the_polish_rump_state"]
        n235["GER_integrated_economies"]
        n236["GER_puppet_finland"]
        n237["GER_reinstate_imperial_possessions_ww"]
        n238["GER_strengthen_the_proletarian_international"]
        n239["GER_subduing_the_baltic_states"]
        n240["GER_the_northern_shield"]
        n241["GER_the_proletarian_legion"]
        n242{"GER_the_second_berlin_award"}
        n243{"GER_trade_agreements"}
        n244["GER_womens_rights_and_equality"]
    end
    subgraph tier_10["Tier 10"]
        n245{"GER_align_italy"}
        n246{"GER_conquer_italy"}
        n247{"GER_european_confederation"}
        n248["GER_industrialize_volkskommissariats"]
        n249["GER_instill_german_discipline"]
        n250["GER_integrate_western_german_speakers"]
        n251{"GER_prepare_italian_coup_ww"}
        n252["GER_reach_out_to_scandinavia"]
        n253["GER_red_europe"]
        n254["GER_strike_eastward"]
    end
    subgraph tier_11["Tier 11"]
        n255["GER_assassinate_mussolini_ww"]
        n256["GER_bring_turkey_into_the_fold"]
        n257["GER_end_european_communism"]
        n258["GER_german_hegemony_in_the_middle_east"]
        n259["GER_integrate_subjects_economies"]
        n260["GER_proletarian_solidarity"]
        n261["GER_restore_the_holy_roman_empire"]
        n262["GER_root_out_imperialism"]
    end
    subgraph tier_12["Tier 12"]
        n263["GER_align_south_america"]
        n264["GER_hegemony_over_europe"]
        n265["GER_instigate_middle_eastern_revolutions"]
        n266["GER_integrate_volkskommissariats"]
    end
    subgraph tier_13["Tier 13"]
        n267["GER_strike_at_the_rising_sun"]
        n268["GER_wage_war_on_capitalism"]
    end
    n110 --> n111
    n188 --> n210
    n176 --> n178
    n149 --> n178
    n243 --> n245
    n262 --> n263
    n137 --> n146
    n196 --> n211
    n195 --> n211
    n182 --> n211
    n147 --> n179
    n127 --> n147
    n148 --> n180
    n251 --> n255
    n113 --> n124
    n112 --> n124
    n114 --> n125
    n117 --> n125
    n166 --> n181
    n118 --> n126
    n140 --> n148
    n246 --> n256
    n247 --> n256
    n245 --> n256
    n251 --> n256
    n136 --> n149
    n170 --> n182
    n177 --> n182
    n152 --> n182
    n169 --> n182
    n166 --> n212
    n183 --> n212
    n147 --> n183
    n111 --> n127
    n176 --> n184
    n149 --> n184
    n145 --> n150
    n144 --> n151
    n111 --> n128
    n123 --> n128
    n242 --> n246
    n243 --> n246
    n173 --> n185
    n143 --> n152
    n122 --> n129
    n168 --> n186
    n159 --> n187
    n121 --> n130
    n115 --> n130
    n206 --> n213
    n98 --> n100
    n228 --> n230
    n104 --> n112
    n190 --> n214
    n192 --> n214
    n144 --> n153
    n126 --> n154
    n254 --> n257
    n178 --> n215
    n186 --> n216
    n187 --> n216
    n222 --> n231
    n181 --> n232
    n203 --> n232
    n212 --> n232
    n235 --> n247
    n148 --> n188
    n198 --> n217
    n190 --> n218
    n192 --> n218
    n121 --> n131
    n115 --> n131
    n215 --> n233
    n196 --> n233
    n195 --> n233
    n182 --> n233
    n175 --> n189
    n167 --> n189
    n121 --> n132
    n115 --> n132
    n160 --> n190
    n104 --> n113
    n103 --> n104
    n139 --> n155
    n246 --> n258
    n247 --> n258
    n245 --> n258
    n251 --> n258
    n135 --> n156
    n165 --> n191
    n164 --> n191
    n262 --> n264
    n196 --> n219
    n195 --> n219
    n182 --> n219
    n185 --> n220
    n199 --> n220
    n186 --> n234
    n216 --> n234
    n122 --> n133
    n128 --> n157
    n231 --> n248
    n262 --> n265
    n231 --> n249
    n248 --> n259
    n249 --> n259
    n259 --> n266
    n232 --> n250
    n237 --> n250
    n215 --> n235
    n221 --> n235
    n114 --> n134
    n117 --> n134
    n121 --> n135
    n160 --> n192
    n157 --> n193
    n109 --> n114
    n46 --> n47
    n45 --> n47
    n44 --> n47
    n144 --> n158
    n145 --> n158
    n158 --> n194
    n170 --> n195
    n177 --> n195
    n152 --> n195
    n169 --> n195
    n141 --> n159
    n107 --> n115
    n119 --> n136
    n184 --> n221
    n178 --> n221
    n99 --> n101
    n144 --> n160
    n145 --> n160
    n170 --> n196
    n177 --> n196
    n152 --> n196
    n169 --> n196
    n139 --> n161
    n148 --> n197
    n147 --> n198
    n173 --> n199
    n105 --> n116
    n142 --> n162
    n115 --> n137
    n242 --> n251
    n109 --> n117
    n253 --> n260
    n151 --> n222
    n153 --> n222
    n205 --> n222
    n135 --> n163
    n137 --> n163
    n207 --> n236
    n216 --> n236
    n45 --> n98
    n120 --> n138
    n116 --> n138
    n108 --> n118
    n132 --> n164
    n132 --> n165
    n118 --> n139
    n233 --> n252
    n188 --> n223
    n108 --> n119
    n107 --> n119
    n123 --> n140
    n98 --> n102
    n241 --> n253
    n238 --> n253
    n181 --> n237
    n203 --> n237
    n212 --> n237
    n119 --> n166
    n130 --> n166
    n149 --> n200
    n105 --> n120
    n155 --> n201
    n157 --> n202
    n171 --> n202
    n133 --> n167
    n103 --> n105
    n141 --> n168
    n119 --> n141
    n246 --> n261
    n251 --> n261
    n107 --> n121
    n118 --> n142
    n100 --> n106
    n102 --> n106
    n101 --> n107
    n226 --> n262
    n253 --> n262
    n143 --> n169
    n143 --> n170
    n166 --> n203
    n119 --> n143
    n128 --> n171
    n171 --> n204
    n142 --> n172
    n109 --> n122
    n114 --> n144
    n158 --> n205
    n145 --> n173
    n129 --> n173
    n99 --> n103
    n117 --> n145
    n224 --> n238
    n174 --> n206
    n154 --> n206
    n265 --> n267
    n239 --> n254
    n219 --> n254
    n126 --> n174
    n216 --> n239
    n170 --> n207
    n177 --> n207
    n159 --> n207
    n205 --> n224
    n178 --> n225
    n133 --> n175
    n45 --> n99
    n136 --> n176
    n194 --> n226
    n184 --> n227
    n150 --> n208
    n172 --> n209
    n162 --> n209
    n101 --> n108
    n220 --> n240
    n103 --> n109
    n224 --> n241
    n222 --> n241
    n227 --> n242
    n110 --> n123
    n202 --> n228
    n221 --> n243
    n143 --> n177
    n198 --> n229
    n263 --> n268
    n101 --> n110
    n218 --> n244
    n214 --> n244
    n111 x--x n123
    n178 x--x n184
    n245 x--x n246
    n245 x--x n251
    n181 x--x n212
    n181 x--x n203
    n256 x--x n258
    n149 x--x n176
    n212 x--x n203
    n183 x--x n166
    n246 x--x n251
    n152 x--x n169
    n230 x--x n217
    n230 x--x n197
    n154 x--x n174
    n217 x--x n197
    n114 x--x n117
    n115 x--x n121
    n101 x--x n103
    n45 x--x n46
    n141 x--x n143
    n107 x--x n108
    n170 x--x n177
```

# GER_prioritize_economic_growth

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n269["GER_autarky_efforts"]
        n270(("GER_prioritize_economic_growth"))
        n271["GER_the_four_year_plan"]
    end
    subgraph tier_1["Tier 1"]
        n272["GER_construct_the_reichsautobahn"]
        n273["GER_currency_reforms"]
    end
    subgraph tier_2["Tier 2"]
        n274["GER_build_the_rur_dam"]
        n275["GER_housing_developments"]
        n276["GER_kdf_wagen_factories"]
        n277["GER_lower_taxes"]
        n278["GER_trade_deal_with_sweden"]
    end
    subgraph tier_3["Tier 3"]
        n279["GER_abolish_price_controls"]
        n280["GER_develop_heraeus_facilities"]
        n281["GER_expand_the_reichsautobahn_east"]
        n282["GER_expand_the_reichsautobahn_south"]
        n283["GER_industrial_expansion"]
        n284["GER_workers_rights"]
    end
    subgraph tier_4["Tier 4"]
        n285["GER_agricultural_reforms"]
        n286["GER_increased_trade"]
        n287["GER_invest_in_vereinigte_stahlwerke"]
    end
    subgraph tier_5["Tier 5"]
        n288["GER_urbanization"]
        n289["GER_wirtschaftswunder"]
    end
    subgraph tier_6["Tier 6"]
        n290["GER_build_defense_industry"]
        n291["GER_mass_production"]
    end
    subgraph tier_7["Tier 7"]
        n292["GER_war_production"]
    end
    n277 --> n279
    n283 --> n285
    n284 --> n285
    n289 --> n290
    n272 --> n274
    n273 --> n274
    n270 --> n272
    n271 --> n272
    n270 --> n273
    n276 --> n280
    n276 --> n281
    n276 --> n282
    n273 --> n275
    n279 --> n286
    n275 --> n283
    n277 --> n283
    n283 --> n287
    n279 --> n287
    n272 --> n276
    n273 --> n277
    n289 --> n291
    n272 --> n278
    n269 --> n278
    n285 --> n288
    n291 --> n292
    n290 --> n292
    n287 --> n289
    n285 --> n289
    n275 --> n284
    n270 x--x n271
```

# GER_remilitarize_the_rhineland

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n44["GER_oppose_hitler"]
        n45["GER_oppose_hitler_ww"]
        n46{"GER_remilitarize_the_rhineland"}
    end
    subgraph tier_1["Tier 1"]
        n293{"GER_anti_comintern_pact"}
        n294{"GER_bribe_senior_officers"}
        n295{"GER_fuhrerprinzip"}
        n296["GER_heed_von_neuraths_concerns"]
        n47["GER_legion_condor"]
        n297{"GER_reorganize_the_wehrmacht"}
    end
    subgraph tier_2["Tier 2"]
        n298{"GER_anschluss"}
        n299["GER_anti_soviet_pact"]
        n300["GER_army_indoctrination"]
        n301["GER_ascension_of_goebbels"]
        n302["GER_ascension_of_goring"]
        n303{"GER_ascension_of_himmler"}
        n304["GER_ascension_of_speer"]
        n305["GER_ascension_of_todt"]
        n306["GER_autonomy_in_the_kriegsschulen"]
        n307["GER_befriend_china"]
        n308["GER_befriend_japan"]
        n309["GER_molotov_ribbentrop_pact"]
        n310["GER_party_chancellor_bormann"]
        n311["GER_party_chancellor_hess"]
        n312["GER_uplift_the_rosenberg_office"]
        n313{"GER_war_preparations"}
        n314["GER_war_with_the_ussr"]
    end
    subgraph tier_3["Tier 3"]
        n315["GER_befriend_czechoslovakia"]
        n316["GER_befriend_turkey"]
        n317["GER_claim_old_colonies_in_the_east"]
        n318["GER_demand_slovenia"]
        n319["GER_demand_sudetenland"]
        n320["GER_demonstration_of_military_achievements"]
        n321{"GER_employ_philipp_holzmann"}
        n322["GER_expand_gestapo"]
        n323["GER_expand_ss_recruitment"]
        n324["GER_expand_ss_security_duties"]
        n325["GER_expand_the_truppenschulen"]
        n326{"GER_form_organization_todt"}
        n327["GER_innovative_warfare"]
        n328["GER_japanese_naval_cooperation"]
        n329["GER_ministry_of_public_enlightenment"]
        n330["GER_negotiate_old_colonies_in_the_east"]
        n331["GER_optimize_reich_labour_service"]
        n332["GER_prepare_for_the_next_blockade_ww"]
        n333{"GER_prioritize_the_four_year_plan"}
        n334["GER_re_establish_german_control_over_qingdao"]
        n335{"GER_reassert_eastern_claims"}
        n336["GER_reclaim_former_african_colonies"]
        n337["GER_reorganize_secret_services"]
        n338["GER_strafbataillon"]
        n339["GER_support_a_coup_in_liechtenstein"]
        n340["GER_support_finland"]
        n341["GER_the_final_blow_to_communism"]
        n342["GER_the_triumphant_will"]
        n343{"GER_treaty_with_the_ussr"}
    end
    subgraph tier_4["Tier 4"]
        n344["GER_absorb_the_abwehr"]
        n345["GER_alliance_with_the_ussr"]
        n346["GER_ally_chiang_kai_shek"]
        n347["GER_an_invincible_army"]
        n348["GER_autonomous_organization_todt"]
        n349{"GER_danzig_or_war"}
        n350["GER_expand_claims_in_baltic"]
        n351["GER_first_ljubljana_award"]
        n352["GER_first_vienna_award"]
        n353["GER_fund_the_film_department"]
        n354["GER_glorify_party_rallies"]
        n355{"GER_influence_the_baltics"}
        n356{"GER_integrate_czechoslovakia"}
        n357["GER_mittelafrika"]
        n358["GER_plenipotentiary_of_armaments"]
        n359["GER_plenipotentiary_of_the_four_year_plan"]
        n360["GER_rally_the_industrialists"]
        n361["GER_sentinels_of_the_pacific"]
        n362["GER_strengthen_the_waffen_ss"]
        n363["GER_subversive_infiltrators"]
    end
    subgraph tier_5["Tier 5"]
        n364["GER_create_asian_reichskommissariat"]
        n365{"GER_fate_of_czechoslovakia"}
        n366{"GER_fate_of_yugoslavia"}
        n367{"GER_hegemony_of_the_ss"}
        n368{"GER_integration_of_puppet_economies"}
        n369["GER_operation_weserubung"]
        n370{"GER_propaganda_master"}
        n371["GER_puppet_turkey"]
        n372["GER_south_east_asian_natural_wealth"]
        n373["GER_the_supreme_leader"]
        n374{"GER_total_control_over_domestic_affairs"}
        n375["GER_utilize_the_nordliche_gesellschaft"]
        n376{"GER_wunderwaffe"}
    end
    subgraph tier_6["Tier 6"]
        n377["GER_a_strong_successor"]
        n378["GER_blitzkrieg_across_the_pacific"]
        n379{"GER_danzig_for_slovakia"}
        n380["GER_demands_to_sweden"]
        n381{"GER_form_rome_berlin_axis"}
        n382["GER_influence_the_middle_east"]
        n383["GER_integrate_czech_manufacturers"]
        n384["GER_loyalty_to_the_fuhrer"]
        n385["GER_second_ljubljana_award"]
        n386["GER_secure_finland"]
        n387["GER_the_proud_eagle_and_the_resurgent_dragon"]
        n388["GER_war_with_greece"]
    end
    subgraph tier_7["Tier 7"]
        n389{"GER_around_maginot"}
        n390["GER_befriend_poland"]
        n391["GER_fate_of_greece"]
        n392{"GER_influence_the_benelux"}
        n393["GER_subjugate_romanian_economy"]
    end
    subgraph tier_8["Tier 8"]
        n394{"GER_invade_italy"}
        n395{"GER_war_with_france"}
    end
    subgraph tier_9["Tier 9"]
        n396{"GER_alliance_with_spain"}
        n397{"GER_operation_felix"}
        n398["GER_operation_sea_lion"]
        n399["GER_operation_tannenbaum"]
        n400["GER_reintegrate_luxemburg_and_alsace_lorraine"]
        n401["GER_the_swiss_gold"]
    end
    subgraph tier_10["Tier 10"]
        n402["GER_alliance_with_portugal"]
        n403["GER_crossing_the_atlantic"]
        n404["GER_operation_green"]
        n405["GER_operation_isabella"]
    end
    subgraph tier_11["Tier 11"]
        n406["GER_challenge_the_monroe_doctrine"]
        n407["GER_shatter_usas_hegemony"]
    end
    subgraph tier_12["Tier 12"]
        n408["GER_establish_protectorates_in_america"]
    end
    n367 --> n377
    n376 --> n377
    n368 --> n377
    n370 --> n377
    n374 --> n377
    n322 --> n344
    n396 --> n402
    n397 --> n402
    n381 --> n396
    n394 --> n396
    n343 --> n345
    n334 --> n346
    n317 --> n346
    n320 --> n347
    n297 --> n298
    n296 --> n298
    n46 --> n293
    n293 --> n299
    n294 --> n300
    n379 --> n389
    n349 --> n389
    n295 --> n301
    n295 --> n302
    n295 --> n303
    n295 --> n304
    n295 --> n305
    n326 --> n348
    n294 --> n306
    n293 --> n307
    n313 --> n315
    n293 --> n308
    n379 --> n390
    n314 --> n316
    n361 --> n378
    n372 --> n378
    n46 --> n294
    n403 --> n406
    n307 --> n317
    n346 --> n364
    n330 --> n364
    n398 --> n403
    n365 --> n379
    n356 --> n379
    n335 --> n349
    n298 --> n318
    n298 --> n319
    n369 --> n380
    n298 --> n320
    n304 --> n321
    n406 --> n408
    n407 --> n408
    n335 --> n350
    n303 --> n322
    n312 --> n323
    n303 --> n324
    n306 --> n325
    n352 --> n365
    n385 --> n391
    n351 --> n366
    n318 --> n351
    n319 --> n352
    n305 --> n326
    n365 --> n381
    n356 --> n381
    n46 --> n295
    n329 --> n353
    n331 --> n354
    n310 --> n354
    n46 --> n296
    n344 --> n367
    n362 --> n367
    n335 --> n355
    n379 --> n392
    n349 --> n392
    n371 --> n382
    n316 --> n382
    n300 --> n327
    n306 --> n327
    n356 --> n383
    n365 --> n383
    n315 --> n356
    n359 --> n368
    n389 --> n394
    n392 --> n394
    n308 --> n328
    n46 --> n47
    n45 --> n47
    n44 --> n47
    n367 --> n384
    n376 --> n384
    n368 --> n384
    n370 --> n384
    n374 --> n384
    n301 --> n329
    n336 --> n357
    n297 --> n309
    n308 --> n330
    n381 --> n397
    n394 --> n397
    n398 --> n404
    n397 --> n405
    n396 --> n405
    n395 --> n398
    n394 --> n398
    n395 --> n399
    n349 --> n369
    n311 --> n331
    n310 --> n331
    n295 --> n310
    n295 --> n311
    n321 --> n358
    n333 --> n359
    n313 --> n332
    n302 --> n333
    n353 --> n370
    n345 --> n371
    n331 --> n360
    n311 --> n360
    n307 --> n334
    n298 --> n335
    n307 --> n336
    n308 --> n336
    n395 --> n400
    n313 --> n337
    n46 --> n297
    n366 --> n385
    n369 --> n386
    n375 --> n386
    n328 --> n361
    n330 --> n361
    n403 --> n407
    n346 --> n372
    n330 --> n372
    n300 --> n338
    n324 --> n362
    n379 --> n393
    n349 --> n393
    n337 --> n363
    n298 --> n339
    n299 --> n340
    n314 --> n341
    n346 --> n387
    n364 --> n387
    n347 --> n373
    n395 --> n401
    n298 --> n342
    n354 --> n374
    n360 --> n374
    n309 --> n343
    n296 --> n312
    n297 --> n312
    n355 --> n375
    n296 --> n313
    n389 --> n395
    n369 --> n395
    n366 --> n388
    n293 --> n314
    n348 --> n376
    n358 --> n376
    n377 x--x n384
    n402 x--x n405
    n396 x--x n397
    n345 x--x n314
    n299 x--x n309
    n300 x--x n306
    n389 x--x n392
    n348 x--x n358
    n348 x--x n359
    n307 x--x n308
    n315 x--x n319
    n379 x--x n349
    n350 x--x n355
    n322 x--x n324
    n381 x--x n394
    n296 x--x n297
    n399 x--x n401
    n369 x--x n375
    n44 x--x n46
    n45 x--x n46
    n310 x--x n311
    n358 x--x n359
    n385 x--x n388
```

# GER_strengthen_the_kriegsmarine

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n409(("GER_strengthen_the_kriegsmarine"))
        n38["GER_torpedobomber"]
    end
    subgraph tier_1["Tier 1"]
        n410["GER_plan_z"]
        n411["GER_re_establish_the_seekriegsleitung"]
        n412["GER_trade_interdiction"]
    end
    subgraph tier_2["Tier 2"]
        n413["GER_atlantic_naval_bases"]
        n414{"GER_cruiser_warfare"}
        n415["GER_expand_kriegsmarinewerft"]
        n416["GER_marinestosstrupp"]
        n417{"GER_wolfpack_tactics"}
    end
    subgraph tier_3["Tier 3"]
        n418["GER_atlantic_naval_dominance"]
        n25["GER_construct_aircraft_carriers"]
        n419["GER_grosskampfschiff_construction"]
        n420["GER_high_seas_fleet"]
        n421["GER_panzerschiff_raiders"]
        n422["GER_u_boat_efforts"]
    end
    subgraph tier_4["Tier 4"]
        n40["GER_establish_carrier_groups"]
        n423["GER_unrestricted_convoy_raiding"]
    end
    subgraph tier_5["Tier 5"]
        n424["GER_seeherrschaft"]
    end
    n411 --> n413
    n416 --> n418
    n413 --> n418
    n415 --> n25
    n412 --> n414
    n38 --> n40
    n25 --> n40
    n410 --> n415
    n415 --> n419
    n415 --> n420
    n411 --> n416
    n414 --> n421
    n409 --> n410
    n409 --> n411
    n420 --> n424
    n423 --> n424
    n409 --> n412
    n417 --> n422
    n421 --> n423
    n422 --> n423
    n412 --> n417
    n421 x--x n422
```

# GER_the_four_year_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n273["GER_currency_reforms"]
        n270["GER_prioritize_economic_growth"]
        n271(("GER_the_four_year_plan"))
    end
    subgraph tier_1["Tier 1"]
        n425["GER_accelerate_the_rearmament_program"]
        n269["GER_autarky_efforts"]
        n272["GER_construct_the_reichsautobahn"]
    end
    subgraph tier_2["Tier 2"]
        n274["GER_build_the_rur_dam"]
        n426["GER_coal_liquefaction"]
        n427["GER_concentrated_armament_program"]
        n428["GER_establish_production_targets"]
        n429["GER_establish_the_reichswerke"]
        n430["GER_institute_price_controls"]
        n276["GER_kdf_wagen_factories"]
        n278["GER_trade_deal_with_sweden"]
    end
    subgraph tier_3["Tier 3"]
        n280["GER_develop_heraeus_facilities"]
        n431["GER_establish_buna_werke"]
        n281["GER_expand_the_reichsautobahn_east"]
        n282["GER_expand_the_reichsautobahn_south"]
        n432["GER_seize_foreign_industries"]
        n433["GER_subsidize_hoesch_benzin"]
        n434["GER_zentrale_planung"]
    end
    subgraph tier_4["Tier 4"]
        n435["GER_armament_rationalization"]
        n436["GER_autarky_achieved"]
        n437["GER_create_rustungsstab"]
    end
    subgraph tier_5["Tier 5"]
        n438["GER_totaler_krieg"]
    end
    n271 --> n425
    n434 --> n435
    n432 --> n436
    n433 --> n436
    n431 --> n436
    n271 --> n269
    n272 --> n274
    n273 --> n274
    n269 --> n426
    n425 --> n427
    n270 --> n272
    n271 --> n272
    n434 --> n437
    n276 --> n280
    n426 --> n431
    n425 --> n428
    n269 --> n429
    n276 --> n281
    n276 --> n282
    n269 --> n430
    n272 --> n276
    n429 --> n432
    n426 --> n433
    n437 --> n438
    n435 --> n438
    n272 --> n278
    n269 --> n278
    n427 --> n434
    n428 --> n434
    n270 x--x n271
```
