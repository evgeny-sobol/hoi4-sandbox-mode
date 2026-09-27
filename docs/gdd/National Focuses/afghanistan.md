# AFG_adopt_nufus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("AFG_adopt_nufus"))
        n2["AFG_khyber_pass_riflining"]
        n3["AFG_maintain_quami"]
    end
    subgraph tier_1["Tier 1"]
        n4["AFG_establish_naval_bases"]
        n5["AFG_expand_border_guards"]
        n6["AFG_new_army"]
        n7["AFG_officialize_the_turkish_afghan_defense_treaty"]
        n8["AFG_utilize_cameleers"]
    end
    subgraph tier_2["Tier 2"]
        n9["AFG_approach_foreign_inteligence_services"]
        n10["AFG_establish_camelry_regiments"]
        n11["AFG_expand_academy"]
        n12{"AFG_naval_academy"}
        n13{"AFG_shipyards"}
    end
    subgraph tier_3["Tier 3"]
        n14["AFG_foreign_military_advisors"]
        n15["AFG_mountain_training"]
        n16["AFG_purchase_aircraft"]
        n17["AFG_purchase_destroyers"]
        n18["AFG_purchase_tanks"]
        n19["AFG_research_bonus_1"]
    end
    subgraph tier_4["Tier 4"]
        n20["AFG_expand_equipment_purchases"]
        n21["AFG_expand_standing_army"]
        n22["AFG_increase_air_purchases"]
        n23["AFG_mountain_training_2"]
        n24["AFG_purchase_capital_ships"]
        n25["AFG_research_bonus_2"]
    end
    subgraph tier_5["Tier 5"]
        n26["AFG_prussians_of_the_orient"]
    end
    n5 --> n9
    n8 --> n10
    n1 --> n4
    n6 --> n11
    n3 --> n5
    n1 --> n5
    n18 --> n20
    n14 --> n21
    n11 --> n14
    n16 --> n22
    n2 --> n15
    n11 --> n15
    n15 --> n23
    n4 --> n12
    n1 --> n6
    n1 --> n7
    n21 --> n26
    n22 --> n26
    n20 --> n26
    n11 --> n16
    n17 --> n24
    n13 --> n17
    n12 --> n17
    n11 --> n18
    n13 --> n19
    n12 --> n19
    n19 --> n25
    n4 --> n13
    n3 --> n8
    n1 --> n8
    n1 x--x n3
    n17 x--x n19
```

# AFG_against_kabul

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n27{"AFG_against_kabul"}
        n28["AFG_support_king_zahir"]
    end
    subgraph tier_1["Tier 1"]
        n29["AFG_contact_amanullah_loyalists"]
        n30["AFG_remember_the_khost_rebellion"]
    end
    subgraph tier_2["Tier 2"]
        n31["AFG_contact_rural_loyalists"]
        n32["AFG_invite_waziristan_rebels"]
        n33["AFG_request_german_support"]
        n34["AFG_request_japanese_support"]
        n35["AFG_secure_army_support"]
        n36["AFG_stir_unrest_in_the_east"]
    end
    subgraph tier_3["Tier 3"]
        n37["AFG_hold_a_loya_jirga"]
        n38["AFG_return_of_the_emir"]
        n39{"AFG_the_faqirs_revolt"}
    end
    subgraph tier_4["Tier 4"]
        n40["AFG_crown_the_bukharan_emir"]
        n41["AFG_crown_the_golden_emir"]
        n42["AFG_expand_the_madrasas"]
        n43["AFG_extend_a_hand_to_tokyo"]
        n44["AFG_invite_the_mughal_prince"]
        n45["AFG_revive_the_1923_constitution"]
        n46["AFG_unify_the_islamic_world"]
    end
    subgraph tier_5["Tier 5"]
        n47["AFG_education_for_women_and_girls"]
        n48["AFG_enforce_the_pashtunwali"]
        n49["AFG_enforce_western_attire"]
        n50["AFG_form_the_khuddamul_furqan"]
        n51["AFG_hone_the_shamshir"]
        n52["AFG_promote_muslim_work_ethic"]
        n53["AFG_raise_lashkar_regiments"]
        n54["AFG_reclaim_moghulistan"]
        n55["AFG_rehabilitate_the_saqqawists"]
        n56["AFG_reorganize_the_royal_guard"]
        n57["AFG_restore_herat"]
        n58["AFG_timurid_bureaucracy"]
    end
    subgraph tier_6["Tier 6"]
        n59["AFG_ally_the_sikhs"]
        n60["AFG_establish_darulaman"]
        n61["AFG_expand_state_run_factories"]
        n62["AFG_instate_a_compulsory_jizya"]
        n63["AFG_integrate_the_basmachi_movement"]
        n64["AFG_prepare_the_war_industries"]
        n65["AFG_proclaim_the_second_afghan_empire"]
        n66["AFG_reinforce_the_royal_guard"]
        n67["AFG_reintroduce_heavy_cavalry"]
        n68["AFG_reintroduce_war_elephants"]
        n69["AFG_return_to_delhi"]
        n70["AFG_support_nort_west_frontier_rebels"]
        n71["AFG_ulugh_beg_academy"]
    end
    subgraph tier_7["Tier 7"]
        n72["AFG_ally_the_brahui_khanate"]
        n73["AFG_appraoch_anti_communist_theologians"]
        n74["AFG_custail_pashtunwali_primacy"]
        n75["AFG_darulaman_university"]
        n76["AFG_increase_land_and_animal_taxes"]
        n77["AFG_rebuild_the_silk_road"]
        n78["AFG_reclaim_transoxiana"]
        n79["AFG_revive_the_workshop_of_the_world"]
        n80["AFG_the_conquerors_of_persia"]
        n81["AFG_the_echoes_of_panipat"]
    end
    subgraph tier_8["Tier 8"]
        n82["AFG_agreement_with_germany"]
        n83["AFG_ally_basmachi_remnants"]
        n84["AFG_eyes_on_the_north"]
        n85["AFG_form_the_turkestan_legion"]
        n86{"AFG_from_the_ashes"}
        n87["AFG_renounce_the_durand_line"]
        n88["AFG_restore_the_timurid_empire"]
        n89["AFG_the_amu_darya_plan"]
        n90["AFG_unite_pashtunistan"]
    end
    subgraph tier_9["Tier 9"]
        n91["AFG_alliance_with_turkik_peoples"]
        n92["AFG_exploit_turko_persian_heritage"]
        n93["AFG_fortify_pakistan"]
        n94["AFG_proclaim_a_new_caliphate"]
        n95["AFG_reclaim_the_emperors_lost_domain"]
        n96["AFG_the_crown_and_the_world"]
        n97["AFG_topple_iran"]
        n98["AFG_work_with_gestapo"]
    end
    subgraph tier_10["Tier 10"]
        n99["AFG_into_the_plains_of_india"]
        n100["AFG_red_threat"]
        n101["AFG_secure_baghdad"]
    end
    subgraph tier_11["Tier 11"]
        n102["AFG_pashtun_empire"]
        n103["AFG_savior_of_the_holy_lands"]
    end
    n74 --> n82
    n84 --> n91
    n74 --> n83
    n63 --> n72
    n58 --> n59
    n70 --> n73
    n27 --> n29
    n29 --> n31
    n30 --> n31
    n39 --> n40
    n39 --> n41
    n66 --> n74
    n60 --> n75
    n45 --> n47
    n41 --> n48
    n45 --> n49
    n47 --> n60
    n49 --> n61
    n39 --> n42
    n86 --> n92
    n39 --> n43
    n74 --> n84
    n41 --> n50
    n73 --> n85
    n87 --> n93
    n74 --> n86
    n31 --> n37
    n44 --> n51
    n40 --> n51
    n61 --> n76
    n50 --> n62
    n57 --> n63
    n93 --> n99
    n39 --> n44
    n30 --> n32
    n99 --> n102
    n100 --> n102
    n55 --> n64
    n52 --> n64
    n90 --> n94
    n57 --> n65
    n51 --> n65
    n42 --> n52
    n41 --> n53
    n69 --> n77
    n44 --> n54
    n89 --> n95
    n69 --> n78
    n91 --> n100
    n42 --> n55
    n47 --> n66
    n49 --> n66
    n56 --> n67
    n56 --> n68
    n27 --> n30
    n74 --> n87
    n42 --> n56
    n29 --> n33
    n30 --> n33
    n30 --> n34
    n40 --> n57
    n77 --> n88
    n35 --> n38
    n58 --> n69
    n51 --> n69
    n38 --> n45
    n64 --> n79
    n71 --> n79
    n101 --> n103
    n29 --> n35
    n92 --> n101
    n97 --> n101
    n30 --> n36
    n50 --> n70
    n48 --> n70
    n81 --> n89
    n65 --> n80
    n69 --> n80
    n88 --> n96
    n65 --> n81
    n63 --> n81
    n36 --> n39
    n32 --> n39
    n44 --> n58
    n86 --> n97
    n55 --> n71
    n52 --> n71
    n39 --> n46
    n73 --> n90
    n82 --> n98
    n27 x--x n28
    n29 x--x n30
    n40 x--x n41
    n40 x--x n44
    n41 x--x n44
    n92 x--x n97
    n43 x--x n46
```

# AFG_align_with_the_allies

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n104(("AFG_align_with_the_allies"))
        n105["AFG_pursue_our_own_agenda"]
    end
    subgraph tier_1["Tier 1"]
        n106["AFG_anti_soviet_cooperation"]
        n107["AFG_prepare_for_operation_countenance"]
    end
    subgraph tier_2["Tier 2"]
        n108["AFG_protector_of_the_tajiks"]
        n109["AFG_secure_iran"]
    end
    subgraph tier_3["Tier 3"]
        n110["AFG_future_of_balochistan"]
        n111["AFG_khorasan_buffer_state"]
        n112["AFG_repeal_the_durand_line"]
    end
    subgraph tier_4["Tier 4"]
        n113["AFG_linchpin_of_global_defense"]
    end
    n105 --> n106
    n104 --> n106
    n109 --> n110
    n109 --> n111
    n112 --> n113
    n110 --> n113
    n104 --> n107
    n106 --> n108
    n109 --> n112
    n107 --> n109
```

# AFG_alternative_partnerships

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n114(("AFG_alternative_partnerships"))
        n105["AFG_pursue_our_own_agenda"]
    end
    subgraph tier_1["Tier 1"]
        n115["AFG_graveyard_of_empires"]
        n116["AFG_officer_training"]
        n117["AFG_permit_axis_airbases"]
    end
    subgraph tier_2["Tier 2"]
        n118["AFG_axis_airforce"]
        n119["AFG_axis_equipment"]
        n120["AFG_join_axis"]
    end
    subgraph tier_3["Tier 3"]
        n121["AFG_kabul_conference"]
    end
    n117 --> n118
    n116 --> n119
    n105 --> n115
    n114 --> n115
    n117 --> n120
    n116 --> n120
    n120 --> n121
    n114 --> n116
    n114 --> n117
```

# AFG_expand_telegraph_network

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n122(("AFG_expand_telegraph_network"))
        n123["AFG_parliamentary_democracy"]
        n124["AFG_promote_the_counter_elite"]
    end
    subgraph tier_1["Tier 1"]
        n125["AFG_clear_malarial_swamps"]
        n126{"AFG_fruit_packing"}
        n127["AFG_infrastructure_construction"]
        n128["AFG_ministry_of_supply"]
        n129["AFG_spinzar_cotton_factory"]
        n130{"AFG_sugar_processing"}
    end
    subgraph tier_2["Tier 2"]
        n131["AFG_connect_the_cities"]
        n132["AFG_electrification"]
        n133["AFG_expand_karakul_lambskin_industry"]
        n134["AFG_implement_currency_controls"]
        n135["AFG_look_to_other_partners"]
        n136["AFG_qargha_dam"]
        n137["AFG_renew_soviet_trade_agreement"]
    end
    subgraph tier_3["Tier 3"]
        n138["AFG_75_year_oil_concessions"]
        n139["AFG_establish_radio_networks"]
        n140["AFG_kajaki_dam"]
        n141["AFG_rail_construction"]
        n142["AFG_salang_pass"]
        n143["AFG_truck_factory"]
    end
    subgraph tier_4["Tier 4"]
        n144["AFG_chromite_mines"]
        n145["AFG_expand_kabul_university"]
        n146["AFG_iron_mines"]
        n147["AFG_socialist_coup"]
    end
    subgraph tier_5["Tier 5"]
        n148["AFG_international_brigades"]
        n149["AFG_modern_economy"]
        n150["AFG_request_soviet_support"]
        n151["AFG_soviet_research_cooperation"]
        n152["AFG_state_atheism"]
        n153["AFG_state_industries"]
    end
    subgraph tier_6["Tier 6"]
        n154["AFG_communist_industrialization"]
        n155["AFG_support_soviets_in_asia"]
    end
    subgraph tier_7["Tier 7"]
        n156["AFG_communist_propaganda"]
        n157["AFG_integrate_tajik_and_uzbek_republics"]
        n158["AFG_sov_iran_war"]
    end
    subgraph tier_8["Tier 8"]
        n159["AFG_development_in_taj"]
        n160["AFG_development_in_tms"]
        n161["AFG_development_in_uzb"]
    end
    subgraph tier_9["Tier 9"]
        n162["AFG_central_asian_unification"]
    end
    n135 --> n138
    n159 --> n162
    n161 --> n162
    n160 --> n162
    n140 --> n144
    n122 --> n125
    n152 --> n154
    n151 --> n154
    n154 --> n156
    n127 --> n131
    n157 --> n159
    n157 --> n160
    n157 --> n161
    n127 --> n132
    n132 --> n139
    n139 --> n145
    n141 --> n145
    n126 --> n133
    n130 --> n133
    n122 --> n126
    n128 --> n134
    n122 --> n127
    n154 --> n157
    n155 --> n157
    n147 --> n148
    n123 --> n148
    n140 --> n146
    n136 --> n140
    n126 --> n135
    n122 --> n128
    n146 --> n149
    n144 --> n149
    n125 --> n136
    n131 --> n141
    n130 --> n137
    n147 --> n150
    n137 --> n142
    n143 --> n147
    n142 --> n147
    n124 --> n147
    n155 --> n158
    n147 --> n151
    n122 --> n129
    n147 --> n152
    n145 --> n153
    n122 --> n130
    n152 --> n155
    n151 --> n155
    n137 --> n143
    n135 x--x n137
```

# AFG_maintain_quami

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["AFG_adopt_nufus"]
        n11["AFG_expand_academy"]
        n3(("AFG_maintain_quami"))
    end
    subgraph tier_1["Tier 1"]
        n163["AFG_asymmetric_warfare"]
        n5["AFG_expand_border_guards"]
        n8["AFG_utilize_cameleers"]
    end
    subgraph tier_2["Tier 2"]
        n9["AFG_approach_foreign_inteligence_services"]
        n10["AFG_establish_camelry_regiments"]
        n164["AFG_expand_quami_template"]
        n2["AFG_khyber_pass_riflining"]
    end
    subgraph tier_3["Tier 3"]
        n165["AFG_militia_cavalry"]
        n15["AFG_mountain_training"]
        n166["AFG_scavenging"]
    end
    subgraph tier_4["Tier 4"]
        n167["AFG_cross_border_ties"]
        n168["AFG_encourage_jezail_production"]
        n23["AFG_mountain_training_2"]
    end
    n5 --> n9
    n3 --> n163
    n165 --> n167
    n166 --> n168
    n8 --> n10
    n3 --> n5
    n1 --> n5
    n163 --> n164
    n163 --> n2
    n2 --> n165
    n2 --> n15
    n11 --> n15
    n15 --> n23
    n2 --> n166
    n3 --> n8
    n1 --> n8
    n1 x--x n3
```

# AFG_pursue_our_own_agenda

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n104["AFG_align_with_the_allies"]
        n114["AFG_alternative_partnerships"]
        n105{"AFG_pursue_our_own_agenda"}
    end
    subgraph tier_1["Tier 1"]
        n169["AFG_afghan_pakistan_cold_War"]
        n106["AFG_anti_soviet_cooperation"]
        n115["AFG_graveyard_of_empires"]
        n170["AFG_propose_confederation_with_pakistan"]
    end
    subgraph tier_2["Tier 2"]
        n171["AFG_accelerate_integration"]
        n172["AFG_hot_war_with_pakistan"]
        n108["AFG_protector_of_the_tajiks"]
    end
    n170 --> n171
    n105 --> n169
    n105 --> n106
    n104 --> n106
    n105 --> n115
    n114 --> n115
    n169 --> n172
    n105 --> n170
    n106 --> n108
    n169 x--x n170
```

# AFG_support_king_zahir

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n27["AFG_against_kabul"]
        n142["AFG_salang_pass"]
        n28{"AFG_support_king_zahir"}
        n143["AFG_truck_factory"]
    end
    subgraph tier_1["Tier 1"]
        n173["AFG_biding_our_time"]
        n174["AFG_expand_the_kings_powerbase"]
    end
    subgraph tier_2["Tier 2"]
        n175["AFG_forge_a_national_identity"]
        n176["AFG_placeholder_1"]
        n177["AFG_retire_the_uncles"]
        n178["AFG_seek_british_investment"]
        n179["AFG_visit_foreign_capitals"]
    end
    subgraph tier_3["Tier 3"]
        n180["AFG_expand_royal_guard"]
        n181["AFG_introduce_national_service"]
        n124["AFG_promote_the_counter_elite"]
        n182["AFG_reform_2"]
    end
    subgraph tier_4["Tier 4"]
        n183["AFG_ally_the_young_afghans"]
        n184["AFG_gain_religious_support_for_reforms"]
        n185["AFG_gant_refuge_to_jadidists"]
        n123["AFG_parliamentary_democracy"]
        n186["AFG_secure_dynasty"]
        n147["AFG_socialist_coup"]
    end
    subgraph tier_5["Tier 5"]
        n187["AFG_hold_elections"]
        n148["AFG_international_brigades"]
        n188["AFG_maintain_neutrality"]
        n189["AFG_reform_1"]
        n150["AFG_request_soviet_support"]
        n151["AFG_soviet_research_cooperation"]
        n152["AFG_state_atheism"]
    end
    subgraph tier_6["Tier 6"]
        n154["AFG_communist_industrialization"]
        n190["AFG_expel_allied_nationals"]
        n191["AFG_expel_axis_nationals"]
        n192["AFG_recruit_foreign_experts"]
        n193["AFG_reform_3"]
        n194["AFG_reform_4"]
        n155["AFG_support_soviets_in_asia"]
    end
    subgraph tier_7["Tier 7"]
        n156["AFG_communist_propaganda"]
        n195["AFG_concessions_to_pashtuns"]
        n157["AFG_integrate_tajik_and_uzbek_republics"]
        n196["AFG_rapprochement_with_non_pashtuns"]
        n197["AFG_seek_american_aid"]
        n158["AFG_sov_iran_war"]
    end
    subgraph tier_8["Tier 8"]
        n198["AFG_defending_democracy"]
        n159["AFG_development_in_taj"]
        n160["AFG_development_in_tms"]
        n161["AFG_development_in_uzb"]
    end
    subgraph tier_9["Tier 9"]
        n162["AFG_central_asian_unification"]
        n199["AFG_follower_of_islam"]
        n200["AFG_republic_of_afghanistan"]
        n201["AFG_sinkiang_intervention"]
    end
    n124 --> n183
    n28 --> n173
    n159 --> n162
    n161 --> n162
    n160 --> n162
    n152 --> n154
    n151 --> n154
    n154 --> n156
    n193 --> n195
    n196 --> n198
    n157 --> n159
    n157 --> n160
    n157 --> n161
    n179 --> n180
    n28 --> n174
    n188 --> n190
    n188 --> n191
    n198 --> n199
    n197 --> n199
    n174 --> n175
    n173 --> n175
    n124 --> n184
    n124 --> n185
    n123 --> n187
    n154 --> n157
    n155 --> n157
    n147 --> n148
    n123 --> n148
    n179 --> n181
    n186 --> n188
    n124 --> n123
    n173 --> n176
    n177 --> n124
    n194 --> n196
    n189 --> n192
    n184 --> n192
    n123 --> n189
    n184 --> n189
    n176 --> n182
    n178 --> n182
    n189 --> n193
    n187 --> n193
    n189 --> n194
    n198 --> n200
    n195 --> n200
    n147 --> n150
    n174 --> n177
    n182 --> n186
    n192 --> n197
    n173 --> n178
    n198 --> n201
    n143 --> n147
    n142 --> n147
    n124 --> n147
    n155 --> n158
    n147 --> n151
    n147 --> n152
    n152 --> n155
    n151 --> n155
    n174 --> n179
    n173 --> n179
    n27 x--x n28
    n173 x--x n174
```
