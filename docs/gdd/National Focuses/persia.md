# PER_establish_airforce

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("PER_establish_airforce"))
        n2["PER_import_rocketry"]
    end
    subgraph tier_1["Tier 1"]
        n3["PER_construct_air_bases"]
        n4{"PER_pilot_training"}
    end
    subgraph tier_2["Tier 2"]
        n5["PER_anti_air_research"]
        n6["PER_luftwaffe_planes"]
        n7["PER_raf_planes"]
    end
    subgraph tier_3["Tier 3"]
        n8{"PER_anti_air_development"}
        n9{"PER_establish_air_academy"}
        n10["PER_own_plane_designs"]
    end
    subgraph tier_4["Tier 4"]
        n11["PER_air_superiority"]
        n12["PER_battlefield_support"]
        n13["PER_legacy_of_gilani"]
        n14["PER_strategic_bombing"]
    end
    subgraph tier_5["Tier 5"]
        n15["PER_negotiate_with_america"]
        n16["PER_perfect_iranian_airforce"]
    end
    subgraph tier_6["Tier 6"]
        n17["PER_establish_nuclear_program"]
    end
    n9 --> n11
    n8 --> n11
    n5 --> n8
    n3 --> n5
    n9 --> n12
    n1 --> n3
    n6 --> n9
    n7 --> n9
    n15 --> n17
    n9 --> n13
    n4 --> n6
    n2 --> n15
    n14 --> n15
    n6 --> n10
    n7 --> n10
    n11 --> n16
    n14 --> n16
    n12 --> n16
    n1 --> n4
    n4 --> n7
    n9 --> n14
    n11 x--x n12
    n11 x--x n14
    n12 x--x n14
    n6 x--x n7
```

# PER_establish_the_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n18(("PER_establish_the_navy"))
    end
    subgraph tier_1["Tier 1"]
        n19{"PER_construct_naval_bases"}
        n20{"PER_officers_to_italy"}
    end
    subgraph tier_2["Tier 2"]
        n21["PER_bolster_the_caspian"]
        n22["PER_coastal_defense_initiative"]
        n23["PER_persian_gulf_fleet"]
    end
    subgraph tier_3["Tier 3"]
        n24["PER_purchase_foreign_ships"]
    end
    subgraph tier_4["Tier 4"]
        n25["PER_found_iranian_shipyards"]
    end
    subgraph tier_5["Tier 5"]
        n26{"PER_expand_dockyards"}
    end
    subgraph tier_6["Tier 6"]
        n27["PER_expert_raiders"]
        n28["PER_merchant_navy"]
    end
    n19 --> n21
    n20 --> n21
    n19 --> n22
    n18 --> n19
    n25 --> n26
    n26 --> n27
    n24 --> n25
    n26 --> n28
    n18 --> n20
    n20 --> n23
    n19 --> n23
    n21 --> n24
    n23 --> n24
    n21 x--x n23
    n27 x--x n28
```

# PER_fight_for_iran

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n29{"PER_fight_for_iran"}
    end
    subgraph tier_1["Tier 1"]
        n30{"PER_dig_and_defend"}
        n31{"PER_force_them_back"}
    end
    subgraph tier_2["Tier 2"]
        n32{"PER_capital_protect"}
        n33{"PER_push_to_deserts"}
        n34{"PER_push_to_mountains"}
        n35{"PER_secure_coastline"}
    end
    subgraph tier_3["Tier 3"]
        n36["PER_demand_war_reparations"]
        n37["PER_force_white_peace"]
        n38["PER_push_negotiations"]
        n39["PER_swear_fealty"]
    end
    subgraph tier_4["Tier 4"]
        n40{"PER_rebuilding_iran"}
    end
    subgraph tier_5["Tier 5"]
        n41["PER_azadi"]
        n42["PER_declare_loyalty_to_britain"]
    end
    subgraph tier_6["Tier 6"]
        n43["PER_invite_british_investors"]
        n44["PER_rally_bakhtiari_and_qashqai"]
        n45["PER_reinforce_iranian_identity"]
        n46["PER_reinstate_qajars"]
        n47["PER_request_british_equipment"]
    end
    subgraph tier_7["Tier 7"]
        n48["PER_iran_for_iranians"]
        n49["PER_our_place_in_empire"]
    end
    subgraph tier_8["Tier 8"]
        n50["PER_consolidate_british_territory"]
        n51["PER_retake_north_iran"]
    end
    n40 --> n41
    n30 --> n32
    n48 --> n50
    n40 --> n42
    n33 --> n36
    n34 --> n36
    n29 --> n30
    n29 --> n31
    n33 --> n37
    n34 --> n37
    n42 --> n43
    n44 --> n48
    n45 --> n48
    n47 --> n49
    n43 --> n49
    n32 --> n38
    n35 --> n38
    n31 --> n33
    n31 --> n34
    n41 --> n44
    n39 --> n40
    n41 --> n45
    n42 --> n46
    n42 --> n47
    n49 --> n51
    n48 --> n51
    n30 --> n35
    n32 --> n39
    n35 --> n39
    n41 x--x n42
    n32 x--x n35
    n36 x--x n37
    n30 x--x n31
    n38 x--x n39
    n33 x--x n34
```

# PER_modernizing_iran

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n52(("PER_modernizing_iran"))
    end
    subgraph tier_1["Tier 1"]
        n53["PER_adult_literacy"]
        n54["PER_rapid_industrialization"]
        n55["PER_trans_iranian_railway"]
        n56["PER_white_revolution"]
    end
    subgraph tier_2["Tier 2"]
        n57["PER_develop_oil_fields"]
        n58{"PER_expand_tabriz_masshad"}
        n59{"PER_expand_tehran_abbas"}
        n60{"PER_expand_tehran_emam"}
        n61["PER_national_bank"]
        n62{"PER_national_museum"}
        n63["PER_tehran_power_plant"]
    end
    subgraph tier_3["Tier 3"]
        n64["PER_abolish_feudalism"]
        n65["PER_develop_cities"]
        n66{"PER_form_oil_company"}
        n67["PER_price_stabilization"]
        n68["PER_shiraz_university"]
        n69["PER_trains_from_britain"]
        n70["PER_trains_from_germany"]
        n71["PER_university_of_isfahan"]
    end
    subgraph tier_4["Tier 4"]
        n72["PER_educational_reforms"]
        n73["PER_feat_of_engineering"]
        n74["PER_food_for_all"]
        n75["PER_metropolitan_iran"]
        n76["PER_oil_baron"]
        n77["PER_profit_from_war"]
        n78["PER_women_vote"]
    end
    subgraph tier_5["Tier 5"]
        n79["PER_a_modern_iran"]
    end
    n77 --> n79
    n76 --> n79
    n75 --> n79
    n74 --> n79
    n78 --> n79
    n73 --> n79
    n72 --> n79
    n61 --> n64
    n52 --> n53
    n63 --> n65
    n54 --> n57
    n71 --> n72
    n68 --> n72
    n55 --> n58
    n55 --> n59
    n55 --> n60
    n69 --> n73
    n70 --> n73
    n67 --> n74
    n64 --> n74
    n57 --> n66
    n65 --> n75
    n56 --> n61
    n53 --> n62
    n66 --> n76
    n61 --> n67
    n66 --> n77
    n52 --> n54
    n62 --> n68
    n54 --> n63
    n58 --> n69
    n60 --> n69
    n59 --> n69
    n58 --> n70
    n60 --> n70
    n59 --> n70
    n52 --> n55
    n62 --> n71
    n52 --> n56
    n67 --> n78
    n64 --> n78
    n76 x--x n77
    n68 x--x n71
    n69 x--x n70
```

# PER_rally_the_reformers

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n80(("PER_rally_the_reformers"))
        n81["PER_the_pahlavi_imperium"]
    end
    subgraph tier_1["Tier 1"]
        n82{"PER_propagate_political_literature"}
        n83{"PER_stage_mass_protests"}
    end
    subgraph tier_2["Tier 2"]
        n84["PER_iranian_culture"]
        n85{"PER_rally_behind_mosaddegh"}
        n86["PER_united_progressive_parties"]
    end
    subgraph tier_3["Tier 3"]
        n87["PER_constitutional_monarchy"]
        n88["PER_embrace_national_front"]
        n89["PER_form_sumka"]
        n90{"PER_reach_to_seperatists"}
    end
    subgraph tier_4["Tier 4"]
        n91["PER_ally_the_bazaari"]
        n92["PER_brown_shirts"]
        n93["PER_elevate_the_iran_party"]
        n94["PER_force_abdication"]
        n95{"PER_promise_clergy_power"}
        n96["PER_strengthen_iranian_parliament"]
        n97["PER_strengthen_the_tudeh"]
    end
    subgraph tier_5["Tier 5"]
        n98{"PER_free_elections"}
        n99["PER_iranian_revolutionary_vanguard"]
        n100["PER_iranian_socialist_revolution"]
        n101["PER_march_on_saadabad"]
    end
    subgraph tier_6["Tier 6"]
        n102["PER_appease_the_seperatists"]
        n103["PER_continue_westernization"]
        n104["PER_finding_a_shah"]
        n105["PER_iranian_socialism"]
        n106["PER_islamic_restoration"]
        n107["PER_one_for_all_all_for_one"]
        n108["PER_roll_back_reforms"]
        n109["PER_soviet_alignment"]
    end
    subgraph tier_7["Tier 7"]
        n110["PER_ally_bazaari"]
        n111["PER_communist_education_reform"]
        n112["PER_communist_industrialization"]
        n113["PER_communist_propaganda"]
        n114["PER_entice_foreign_investment"]
        n115{"PER_fascist_secularism"}
        n116{"PER_form_savama"}
        n117["PER_industrial_aid"]
        n118["PER_iranian_industrialization"]
        n119{"PER_pan_iranianism"}
        n120["PER_royal_college_funding"]
        n121["PER_secularize_the_state"]
    end
    subgraph tier_8["Tier 8"]
        n122{"PER_expand_oil_production"}
        n123["PER_fascist_reach_out_to_germany"]
        n124["PER_fascist_reach_out_to_japan"]
        n125["PER_increase_faculty_staffing_budget"]
        n126["PER_invest_in_univerity_facilities"]
        n127["PER_iran_first"]
        n128["PER_islamic_revolution"]
        n129["PER_land_reform"]
        n130["PER_reject_foreign_dominance"]
        n131["PER_soviet_iranian_oil_collaboration"]
        n132["PER_the_new_economy"]
    end
    subgraph tier_9["Tier 9"]
        n133["PER_comintern_research_collaboration"]
        n134["PER_fascist_attack_turkey"]
        n135["PER_increase_oil_sales"]
        n136["PER_intervene_in_central_asia"]
        n137["PER_intervention_in_iraq"]
        n138["PER_nationalize_oil_fields"]
        n139["PER_oil_and_rubber_industry"]
        n140["PER_workers_army"]
    end
    subgraph tier_10["Tier 10"]
        n141["PER_crush_saudi_arabia"]
        n142["PER_fascist_attack_afghanistan"]
        n143["PER_international_solidarity"]
        n144["PER_iranian_nuclear_program"]
        n145["PER_islamic_solidarity"]
        n146["PER_request_membership_allies"]
        n147["PER_the_peoples_airforce"]
        n148["PER_the_peoples_navy"]
    end
    subgraph tier_11["Tier 11"]
        n149["PER_communist_afghanistan_intervention"]
        n150["PER_communist_air_defense"]
        n151["PER_communist_basic_plane_design"]
        n152["PER_communist_destabilize_iraq"]
        n153["PER_communist_naval_designs"]
        n154["PER_communist_shore_defense"]
        n155["PER_proclaim_greater_iran"]
        n156["PER_secure_afghanistan"]
        n157["PER_secure_iraq"]
    end
    subgraph tier_12["Tier 12"]
        n158["PER_challenge_the_royal_navy"]
        n159["PER_communist_liberate_pashtuns"]
        n160["PER_communist_naval_bomber_design"]
        n161["PER_communist_submarine_design"]
        n162["PER_curtail_pan_arabism"]
        n163["PER_eastern_expansion"]
        n164["PER_post_war_spoils"]
        n165["PER_revolution_in_the_gulf"]
        n166["PER_there_can_be_only_one"]
    end
    subgraph tier_13["Tier 13"]
        n167["PER_hormuz_crisis"]
    end
    subgraph tier_14["Tier 14"]
        n168["PER_communist_gulf_hegemony"]
    end
    n106 --> n110
    n89 --> n91
    n100 --> n102
    n89 --> n92
    n151 --> n158
    n153 --> n158
    n131 --> n133
    n129 --> n133
    n143 --> n149
    n147 --> n150
    n147 --> n151
    n143 --> n152
    n105 --> n111
    n109 --> n111
    n167 --> n168
    n105 --> n112
    n109 --> n112
    n149 --> n159
    n151 --> n160
    n148 --> n153
    n105 --> n113
    n109 --> n113
    n148 --> n154
    n153 --> n161
    n85 --> n87
    n98 --> n103
    n134 --> n141
    n155 --> n162
    n155 --> n163
    n90 --> n93
    n85 --> n88
    n103 --> n114
    n110 --> n122
    n114 --> n122
    n137 --> n142
    n123 --> n134
    n124 --> n134
    n127 --> n134
    n116 --> n123
    n119 --> n123
    n115 --> n124
    n119 --> n124
    n108 --> n115
    n104 --> n115
    n101 --> n104
    n91 --> n104
    n88 --> n94
    n108 --> n116
    n104 --> n116
    n84 --> n89
    n94 --> n98
    n96 --> n98
    n165 --> n167
    n120 --> n125
    n114 --> n125
    n122 --> n135
    n109 --> n117
    n132 --> n143
    n138 --> n143
    n127 --> n136
    n124 --> n136
    n123 --> n136
    n123 --> n137
    n124 --> n137
    n127 --> n137
    n120 --> n126
    n114 --> n126
    n116 --> n127
    n119 --> n127
    n83 --> n84
    n82 --> n84
    n105 --> n118
    n133 --> n144
    n93 --> n99
    n100 --> n105
    n93 --> n105
    n97 --> n100
    n93 --> n100
    n98 --> n106
    n95 --> n106
    n110 --> n128
    n138 --> n145
    n117 --> n129
    n92 --> n101
    n91 --> n101
    n122 --> n138
    n132 --> n139
    n99 --> n107
    n108 --> n119
    n104 --> n119
    n157 --> n164
    n156 --> n164
    n136 --> n155
    n141 --> n155
    n142 --> n155
    n87 --> n95
    n80 --> n82
    n83 --> n85
    n82 --> n85
    n86 --> n90
    n112 --> n130
    n118 --> n130
    n135 --> n146
    n152 --> n165
    n149 --> n165
    n101 --> n108
    n106 --> n120
    n103 --> n120
    n103 --> n121
    n146 --> n156
    n146 --> n157
    n100 --> n109
    n97 --> n109
    n117 --> n131
    n80 --> n83
    n87 --> n96
    n90 --> n97
    n111 --> n132
    n113 --> n132
    n112 --> n132
    n140 --> n147
    n140 --> n148
    n155 --> n166
    n83 --> n86
    n82 --> n86
    n132 --> n140
    n87 x--x n88
    n103 x--x n106
    n93 x--x n97
    n123 x--x n124
    n123 x--x n127
    n124 x--x n127
    n135 x--x n138
    n84 x--x n85
    n84 x--x n86
    n85 x--x n86
    n80 x--x n81
```

# PER_restructure_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n169(("PER_restructure_army"))
        n14["PER_strategic_bombing"]
    end
    subgraph tier_1["Tier 1"]
        n170["PER_expand_imperial_guard"]
        n171{"PER_expand_military_facilities"}
        n172{"PER_foreign_retraining"}
        n173["PER_special_units"]
    end
    subgraph tier_2["Tier 2"]
        n174["PER_bolster_infantry"]
        n175["PER_czech_tanks"]
        n176["PER_form_savak"]
        n177["PER_german_tanks"]
        n2["PER_import_rocketry"]
        n178["PER_special_forces_program"]
        n179["PER_swedish_artillery"]
    end
    subgraph tier_3["Tier 3"]
        n180["PER_cyrus_initiative"]
        n181["PER_develop_qorkhaneh"]
        n182["PER_establish_motor_arms"]
        n183["PER_expand_unique_unit"]
        n184["PER_fund_state_intelligence"]
        n185["PER_future_of_war"]
        n186["PER_increase_heavy_arms"]
        n15["PER_negotiate_with_america"]
        n187["PER_recruit_bakhtiari"]
        n188["PER_reverse_engineer_tanks"]
        n189["PER_transfer_officers_to_intelligence"]
    end
    subgraph tier_4["Tier 4"]
        n190{"PER_desert_training"}
        n17["PER_establish_nuclear_program"]
        n191["PER_establish_tehran_armor"]
        n192["PER_motorize_infantry"]
        n193["PER_our_own_artillery"]
        n194{"PER_train_tank_commanders"}
    end
    subgraph tier_5["Tier 5"]
        n195["PER_every_man_serves"]
        n196["PER_expand_tehran_armor"]
        n197["PER_military_excellency"]
    end
    n172 --> n174
    n2 --> n180
    n171 --> n175
    n181 --> n190
    n174 --> n181
    n179 --> n181
    n174 --> n182
    n15 --> n17
    n188 --> n191
    n190 --> n195
    n194 --> n195
    n169 --> n170
    n169 --> n171
    n191 --> n196
    n178 --> n183
    n169 --> n172
    n173 --> n176
    n176 --> n184
    n177 --> n185
    n175 --> n185
    n171 --> n177
    n173 --> n2
    n179 --> n186
    n190 --> n197
    n194 --> n197
    n182 --> n192
    n2 --> n15
    n14 --> n15
    n186 --> n193
    n178 --> n187
    n177 --> n188
    n175 --> n188
    n173 --> n178
    n169 --> n173
    n172 --> n179
    n185 --> n194
    n176 --> n189
    n174 x--x n179
    n175 x--x n177
    n195 x--x n197
```

# PER_the_pahlavi_imperium

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n80["PER_rally_the_reformers"]
        n81{"PER_the_pahlavi_imperium"}
    end
    subgraph tier_1["Tier 1"]
        n198{"PER_legacy_of_greatness"}
        n199["PER_stand_with_giants"]
    end
    subgraph tier_2["Tier 2"]
        n200["PER_assassinate_reza_shah"]
        n201["PER_assessing_the_opposition"]
        n202["PER_forced_secularization"]
        n203["PER_imperial_funded_universities"]
        n204["PER_increase_education_funding"]
        n205["PER_increase_military_funding"]
        n206["PER_persian_german_trade"]
        n207["PER_root_out_conspiracies"]
        n208["PER_trial_fifty_three"]
    end
    subgraph tier_3["Tier 3"]
        n209["PER_absolute_monarchy"]
        n210["PER_his_fathers_footsteps"]
        n211["PER_imperial_expansionism"]
        n212["PER_military_high_schools"]
        n213["PER_open_abadan"]
        n214["PER_royal_visit_germany"]
        n215["PER_the_unification_initiative"]
    end
    subgraph tier_4["Tier 4"]
        n216{"PER_clamp_azerbaijani_dissidence"}
        n217{"PER_clamp_kurdish_dissidence"}
        n218["PER_establish_special_unit"]
        n219["PER_first_iranian_empire"]
        n220["PER_tehran_moscow_pact"]
        n221["PER_third_persian_empire"]
        n222{"PER_wether_the_storm"}
    end
    subgraph tier_5["Tier 5"]
        n223{"PER_choose_a_shahbanu"}
        n224["PER_demand_afghan_territory"]
        n225["PER_demand_iraqi_territory"]
        n226["PER_question_of_resources"]
        n227["PER_revive_old_ways"]
        n228["PER_shahanshah"]
        n229["PER_stand_our_ground"]
        n230["PER_state_atheism"]
        n231{"PER_take_regional_tour"}
        n232["PER_venerate_islam"]
    end
    subgraph tier_6["Tier 6"]
        n233["PER_bolster_civilian_industry"]
        n234["PER_embrace_industrial_powers"]
        n235["PER_embrace_opulence"]
        n236["PER_emperor_for_people"]
        n237["PER_limit_foreign_influence"]
        n238["PER_plant_resistance_cells"]
        n239["PER_prepare_for_worst"]
        n240["PER_rally_ancient_history"]
        n241["PER_upscale_military_production"]
        n242["PER_war_plan_cambyses"]
        n243["PER_war_plan_darius"]
        n244["PER_war_plan_xerxes"]
    end
    subgraph tier_7["Tier 7"]
        n245["PER_demand_west_asia"]
        n246["PER_foothold_in_indus"]
        n247["PER_fund_imperial_excellency"]
        n248["PER_modernize_iran_economy"]
        n249["PER_path_through_iraq"]
        n250["PER_preemptive_strike"]
        n251["PER_preparatory_mobilization"]
        n252["PER_rebuild_persepolis"]
        n253["PER_reclaim_turkish_peninsula"]
        n254["PER_stand_with_germany"]
        n255["PER_subserviant_to_noone"]
        n256["PER_uphold_civil_rights"]
        n257["PER_usurp_afghanistan"]
    end
    subgraph tier_8["Tier 8"]
        n258["PER_align_with_axis"]
        n259["PER_clash_of_titans"]
        n260["PER_establish_northern_buffer_states"]
        n261["PER_invasion_of_india"]
        n262["PER_last_thousand_years"]
        n263["PER_march_to_nile"]
        n264["PER_reintegrate_anatolia"]
        n265["PER_we_will_survive"]
    end
    subgraph tier_9["Tier 9"]
        n266["PER_absorb_byzantines"]
        n267["PER_donate_oil_fields"]
        n268["PER_glory_of_cyrus"]
        n269["PER_spoils_of_war"]
        n270["PER_the_memphis_initiative"]
        n271["PER_we_survived"]
    end
    subgraph tier_10["Tier 10"]
        n272["PER_middle_east_protectorate"]
    end
    n207 --> n209
    n259 --> n266
    n254 --> n258
    n198 --> n200
    n198 --> n201
    n229 --> n233
    n221 --> n223
    n215 --> n216
    n215 --> n217
    n253 --> n259
    n220 --> n224
    n220 --> n225
    n242 --> n245
    n258 --> n267
    n231 --> n234
    n223 --> n235
    n223 --> n236
    n250 --> n260
    n211 --> n218
    n209 --> n219
    n243 --> n246
    n199 --> n202
    n198 --> n202
    n235 --> n247
    n261 --> n268
    n264 --> n268
    n263 --> n268
    n200 --> n210
    n201 --> n211
    n198 --> n203
    n199 --> n204
    n199 --> n205
    n246 --> n261
    n257 --> n261
    n255 --> n262
    n247 --> n262
    n256 --> n262
    n248 --> n262
    n81 --> n198
    n231 --> n237
    n249 --> n263
    n269 --> n272
    n205 --> n212
    n234 --> n248
    n204 --> n213
    n242 --> n249
    n199 --> n206
    n226 --> n238
    n238 --> n250
    n239 --> n250
    n241 --> n251
    n233 --> n251
    n226 --> n239
    n222 --> n226
    n228 --> n240
    n240 --> n252
    n244 --> n253
    n253 --> n264
    n216 --> n227
    n217 --> n227
    n198 --> n207
    n206 --> n214
    n221 --> n228
    n219 --> n228
    n258 --> n269
    n222 --> n229
    n234 --> n254
    n81 --> n199
    n216 --> n230
    n217 --> n230
    n237 --> n255
    n219 --> n231
    n211 --> n220
    n263 --> n270
    n201 --> n215
    n210 --> n221
    n199 --> n208
    n236 --> n256
    n229 --> n241
    n243 --> n257
    n216 --> n232
    n217 --> n232
    n225 --> n242
    n224 --> n242
    n225 --> n243
    n224 --> n243
    n225 --> n244
    n224 --> n244
    n265 --> n271
    n260 --> n271
    n251 --> n265
    n214 --> n222
    n212 --> n222
    n200 x--x n207
    n234 x--x n237
    n235 x--x n236
    n198 x--x n199
    n226 x--x n229
    n80 x--x n81
    n227 x--x n230
    n227 x--x n232
    n230 x--x n232
```
