# TUR_hava_okulu

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["TUR_construct_the_cakmak_line"]
        n2(("TUR_hava_okulu"))
        n3["TUR_modernising_the_army"]
    end
    subgraph tier_1["Tier 1"]
        n4["TUR_expand_the_air_bases"]
    end
    subgraph tier_2["Tier 2"]
        n5{"TUR_accelerate_native_fighter_designs"}
        n6["TUR_expand_the_golcuk_naval_base"]
    end
    subgraph tier_3["Tier 3"]
        n7["TUR_invoke_the_methods_of_mehmed_ii"]
        n8["TUR_patrol_the_seas"]
        n9{"TUR_relocate_from_yildiz_palace"}
    end
    subgraph tier_4["Tier 4"]
        n10["TUR_the_legacy_of_osmanli_donanmasi"]
        n11["TUR_the_path_of_the_wolf"]
        n12["TUR_turkish_air_defense_platforms"]
    end
    subgraph tier_5["Tier 5"]
        n13["TUR_fortified_defensive_bases"]
    end
    subgraph tier_6["Tier 6"]
        n14["TUR_turk_silahli_kuvvetleri"]
    end
    n4 --> n5
    n2 --> n4
    n3 --> n6
    n4 --> n6
    n1 --> n13
    n10 --> n13
    n11 --> n13
    n12 --> n13
    n5 --> n7
    n5 --> n8
    n6 --> n9
    n9 --> n10
    n9 --> n11
    n13 --> n14
    n8 --> n12
    n7 --> n12
    n7 x--x n8
    n10 x--x n11
```

# TUR_learning_from_the_great_war

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n4["TUR_expand_the_air_bases"]
        n15(("TUR_learning_from_the_great_war"))
        n12["TUR_turkish_air_defense_platforms"]
    end
    subgraph tier_1["Tier 1"]
        n3{"TUR_modernising_the_army"}
    end
    subgraph tier_2["Tier 2"]
        n16["TUR_embrace_military_tradition"]
        n6["TUR_expand_the_golcuk_naval_base"]
        n17["TUR_mechanising_our_army"]
    end
    subgraph tier_3["Tier 3"]
        n9{"TUR_relocate_from_yildiz_palace"}
        n18["TUR_superiority_of_arms"]
        n19["TUR_the_kirikkale_tank"]
        n20["TUR_utilising_our_terrain"]
    end
    subgraph tier_4["Tier 4"]
        n1["TUR_construct_the_cakmak_line"]
        n10["TUR_the_legacy_of_osmanli_donanmasi"]
        n11["TUR_the_path_of_the_wolf"]
    end
    subgraph tier_5["Tier 5"]
        n13["TUR_fortified_defensive_bases"]
    end
    subgraph tier_6["Tier 6"]
        n14["TUR_turk_silahli_kuvvetleri"]
    end
    n18 --> n1
    n3 --> n16
    n3 --> n6
    n4 --> n6
    n1 --> n13
    n10 --> n13
    n11 --> n13
    n12 --> n13
    n3 --> n17
    n15 --> n3
    n6 --> n9
    n16 --> n18
    n17 --> n18
    n17 --> n19
    n9 --> n10
    n9 --> n11
    n13 --> n14
    n16 --> n20
    n16 x--x n17
    n10 x--x n11
```

# TUR_the_montreux_convention

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n21{"TUR_the_montreux_convention"}
    end
    subgraph tier_1["Tier 1"]
        n22{"TUR_continue_the_policy_of_etatism"}
        n23["TUR_fully_integrate_the_is_bank"]
    end
    subgraph tier_2["Tier 2"]
        n24["TUR_continue_the_sumerbank_industrialization_scheme"]
        n25["TUR_millet_mektebi_focus"]
        n26{"TUR_ratify_the_six_arrows"}
    end
    subgraph tier_3["Tier 3"]
        n27["TUR_assess_our_future"]
        n28["TUR_peace_at_home"]
        n29["TUR_privatize_the_anadolu_agency"]
        n30{"TUR_revive_turkish_revolutionism"}
        n31["TUR_the_sanayiciler"]
        n32["TUR_treaty_of_saadabad"]
    end
    subgraph tier_4["Tier 4"]
        n33["TUR_cooperate_with_the_debt_council"]
        n34["TUR_lift_the_ban_on_other_political_parties"]
        n35{"TUR_rehabilitate_the_kadro_movement"}
        n36["TUR_reinvigorate_turkish_nationalism"]
        n37["TUR_the_hatay_issue"]
        n38["TUR_turkish_state_railways"]
    end
    subgraph tier_5["Tier 5"]
        n39["TUR_holding_our_first_multi_party_election"]
        n40["TUR_kemalism_and_the_modern_movement"]
        n41["TUR_kemalist_socialist_theory"]
        n42["TUR_loosen_the_laws_on_secularism"]
        n43["TUR_peace_in_the_world"]
        n44["TUR_the_second_five_year_plan"]
        n45["TUR_utilize_foreign_capital"]
    end
    subgraph tier_6["Tier 6"]
        n46["TUR_democratic_transition_focus"]
        n47["TUR_integrate_the_fascist_council"]
        n48["TUR_intervene_in_the_spanish_civil_war"]
        n49["TUR_patriotism_over_internationalism"]
        n50["TUR_purify_the_diyanet"]
        n51["TUR_the_guardians_of_kemalism"]
        n52["TUR_the_sun_language_theory"]
    end
    subgraph tier_7["Tier 7"]
        n53["TUR_a_common_destiny_for_all_of_turkey"]
        n54["TUR_create_the_turkish_workers_militia"]
        n55["TUR_expanding_our_armaments"]
        n56["TUR_form_the_redshirts"]
        n57["TUR_permit_regional_elections"]
        n58["TUR_restack_the_officer_corps"]
        n59["TUR_variant_turkish_tax_focus"]
    end
    subgraph tier_8["Tier 8"]
        n60["TUR_fatherland_first"]
        n61["TUR_halk_ve_devlet"]
        n62["TUR_hunt_down_fifth_columnist_islamists"]
        n63["TUR_privatize_our_infrastructure"]
        n64["TUR_the_pontic_redoubt"]
        n65["TUR_turk_ulusu"]
    end
    subgraph tier_9["Tier 9"]
        n66{"TUR_abuse_the_office_of_soil_products"}
        n67["TUR_deal_for_the_oniki_islands"]
        n68{"TUR_democratic_capstone_focus"}
        n69["TUR_georgian_manganese_extraction"]
        n70["TUR_nationalise_all_private_industry"]
    end
    subgraph tier_10["Tier 10"]
        n71["TUR_pivot_to_the_past"]
        n72{"TUR_salt_the_scars_of_the_great_war"}
    end
    subgraph tier_11["Tier 11"]
        n73["TUR_continue_to_prioritise_balkan_integrity"]
        n74["TUR_purge_the_kemalists"]
        n75["TUR_reconfigure_our_foreign_policy"]
    end
    subgraph tier_12["Tier 12"]
        n76["TUR_reaffirm_the_balkan_pact"]
        n77["TUR_rebuilding_our_nation"]
        n78["TUR_renew_the_turkish_soviet_non_aggression_pact"]
        n79["TUR_restore_the_divan"]
        n80["TUR_the_anglo_turkish_agreement"]
        n81["TUR_the_german_turkish_friendship_treaty"]
    end
    subgraph tier_13["Tier 13"]
        n82["TUR_applying_british_oil_embargoes_on_iraq"]
        n83["TUR_balkan_defense_council"]
        n84["TUR_host_exiled_scientists"]
        n85["TUR_return_of_the_sultan"]
        n86["TUR_the_batumi_accord"]
        n87["TUR_the_clodius_agreement"]
        n88["TUR_three_year_industrial_plan"]
    end
    subgraph tier_14["Tier 14"]
        n89["TUR_approve_the_funkplan"]
        n90["TUR_create_the_balkan_central_bank"]
        n91["TUR_provide_refuge_to_the_victims_of_fascism"]
        n92["TUR_purchase_italian_light_tanks"]
        n93{"TUR_reclaim_macedonia"}
        n94["TUR_soviet_tank_factories"]
        n95["TUR_the_chester_concession"]
        n96["TUR_the_treaty_for_prosperity_and_trade"]
        n97["TUR_united_against_imperialism"]
    end
    subgraph tier_15["Tier 15"]
        n98{"TUR_adana_to_baku_highway"}
        n99{"TUR_american_motor_factories"}
        n100{"TUR_bomber_schematics"}
        n101["TUR_connecting_our_capitals"]
        n102{"TUR_dissolve_the_ODPA"}
        n103{"TUR_invite_german_officers_to_izmir"}
        n104["TUR_join_the_central_powers"]
        n105["TUR_joint_budgets_on_fortifications"]
        n106["TUR_press_the_austro_hungarian_claim"]
        n107{"TUR_the_italo_turkish_naval_academy"}
    end
    subgraph tier_16["Tier 16"]
        n108["TUR_aligning_bulgaria"]
        n109["TUR_anti_bolshevik_mediterranean_bloc"]
        n110["TUR_fortifying_contentious_areas"]
        n111["TUR_join_the_allies"]
        n112{"TUR_join_the_axis"}
        n113["TUR_readdress_the_montreux_convention"]
        n114["TUR_the_mediterranean_entente"]
    end
    subgraph tier_17["Tier 17"]
        n115["TUR_collaborative_civil_works_programme"]
        n116["TUR_controlling_the_skies_of_europe"]
        n117["TUR_expanding_our_navy"]
        n118["TUR_expanding_the_saadabad_pact"]
        n119{"TUR_increase_german_military_aid"}
        n120{"TUR_integrated_armed_forces"}
        n121{"TUR_invite_bulgaria"}
        n122["TUR_joint_caucasian_turkish_officer_school"]
        n123["TUR_reclaiming_our_lost_empire"]
        n124["TUR_the_balkan_academy_of_science"]
        n125["TUR_the_damascus_diktat"]
        n126["TUR_the_international_of_proletarian_freethinkers"]
        n127["TUR_the_petra_proposal"]
        n128{"TUR_the_tuz_golu_training_facility"}
    end
    subgraph tier_18["Tier 18"]
        n129["TUR_arctic_wolves_training_program"]
        n130["TUR_british_dockyards_in_turkey"]
        n131["TUR_carve_up_greece"]
        n132["TUR_cooperative_research_centers"]
        n133["TUR_entice_the_greeks"]
        n134["TUR_expanded_credit_on_our_debts"]
        n135["TUR_extend_an_olive_branch_to_bulgaria"]
        n136["TUR_fortifying_the_bosporus"]
        n137["TUR_guarding_our_western_frontiers"]
        n138["TUR_officers_of_the_revolution"]
        n139["TUR_pack_for_a_long_winter"]
        n140["TUR_preempt_bulgarian_alignment"]
        n141["TUR_refining_our_strategies"]
        n142["TUR_secure_the_iraqi_oil"]
        n143["TUR_seize_religious_property"]
        n144{"TUR_strengthening_our_navies"}
        n145["TUR_support_the_golden_square"]
        n146["TUR_supporting_the_east"]
        n147["TUR_the_pan_national_association_of_ulemas"]
    end
    subgraph tier_19["Tier 19"]
        n148["TUR_avenge_the_treaty_of_sevres"]
        n149["TUR_combined_operational_strategies"]
        n150["TUR_desert_camel_corps"]
        n151["TUR_edirne_research_exchange"]
        n152["TUR_imperial_factories"]
        n153["TUR_lift_the_turkiye_komunist_partisis_exile"]
        n154{"TUR_mediterranean_merchant_fleet"}
        n155["TUR_partnership_pact_with_bulgaria"]
        n156["TUR_peninsular_network_of_factories"]
        n157{"TUR_pressure_portugal_to_join"}
        n158["TUR_rebuke_the_treaty_of_lausanne"]
        n159["TUR_reinstate_the_darulfununu_sahane"]
        n160["TUR_scrapping_our_debts"]
        n161["TUR_strike_at_the_fascist_menace"]
        n162["TUR_the_turkish_tank_project"]
        n163["TUR_turkish_panzers"]
    end
    subgraph tier_20["Tier 20"]
        n164["TUR_brace_against_the_red_menace"]
        n165{"TUR_cleanse_iberia_of_bolshevism"}
        n166{"TUR_court_the_spanish"}
        n167["TUR_crush_the_warmongers_in_rome"]
        n168["TUR_establish_the_committee_of_pan_turkism"]
        n169["TUR_learning_from_the_tripolitanian_war"]
        n170["TUR_reconciling_kemalism_with_bolshevism"]
        n171["TUR_securing_iran"]
        n172["TUR_seizing_the_romanian_oil_fields"]
        n173["TUR_taking_responsibility_for_the_air_war"]
        n174["TUR_the_red_apples_of_sevres"]
    end
    subgraph tier_21["Tier 21"]
        n175["TUR_capitalise_on_rising_kurdish_nationalism"]
        n176["TUR_collectivising_our_agriculture"]
        n177["TUR_end_the_british_hegemony"]
        n178["TUR_integrate_german_officers_into_the_army"]
        n179["TUR_punish_french_weakness"]
        n180["TUR_realize_the_nightmare_of_meiji"]
        n181["TUR_stop_the_stalinist_charade"]
        n182["TUR_strike_the_british_imperialists"]
        n183["TUR_taking_over_defense_of_the_gulf"]
        n184["TUR_we_must_not_fall"]
    end
    subgraph tier_22["Tier 22"]
        n185["TUR_foreign_brigades_for_the_revolution"]
        n186["TUR_issue_an_ultimatium_to_the_bulgarians"]
        n187["TUR_restoring_our_nations_pride"]
        n188["TUR_victory_or_death_against_communism"]
    end
    subgraph tier_23["Tier 23"]
        n189["TUR_misak_i_milli"]
    end
    subgraph tier_24["Tier 24"]
        n190{"TUR_annul_the_ankara_anlasmasi"}
        n191{"TUR_rebuke_the_treaty_of_kars"}
        n192["TUR_recover_the_kardzhali_vilayet"]
    end
    subgraph tier_25["Tier 25"]
        n193["TUR_cypriot_and_oniki_ilhak"]
        n194["TUR_konfederasyon"]
        n195["TUR_liberate_the_kurdish_diaspora"]
        n196["TUR_reuniting_thrace_through_force"]
        n197["TUR_unite_the_azeri_diaspora"]
    end
    subgraph tier_26["Tier 26"]
        n198["TUR_turanist_ambition"]
    end
    subgraph tier_27["Tier 27"]
        n199["TUR_cin_turkleri"]
        n200["TUR_crowning_ourselves_with_the_fin_ugor"]
        n201["TUR_subdue_the_magyars"]
    end
    n48 --> n53
    n65 --> n66
    n60 --> n66
    n64 --> n66
    n91 --> n98
    n94 --> n98
    n104 --> n108
    n106 --> n108
    n95 --> n99
    n189 --> n190
    n102 --> n109
    n80 --> n82
    n87 --> n89
    n122 --> n129
    n26 --> n27
    n144 --> n148
    n76 --> n83
    n95 --> n100
    n156 --> n164
    n149 --> n164
    n151 --> n164
    n127 --> n130
    n162 --> n175
    n170 --> n175
    n121 --> n131
    n198 --> n199
    n157 --> n165
    n154 --> n165
    n114 --> n115
    n160 --> n176
    n170 --> n176
    n135 --> n149
    n140 --> n149
    n90 --> n101
    n96 --> n101
    n21 --> n22
    n22 --> n24
    n23 --> n24
    n68 --> n73
    n66 --> n73
    n72 --> n73
    n111 --> n116
    n31 --> n33
    n119 --> n132
    n115 --> n132
    n157 --> n166
    n154 --> n166
    n83 --> n90
    n88 --> n90
    n49 --> n54
    n198 --> n200
    n156 --> n167
    n149 --> n167
    n151 --> n167
    n192 --> n193
    n56 --> n67
    n60 --> n67
    n63 --> n68
    n43 --> n68
    n39 --> n46
    n45 --> n46
    n146 --> n150
    n91 --> n102
    n124 --> n151
    n135 --> n151
    n140 --> n151
    n166 --> n177
    n165 --> n177
    n121 --> n133
    n163 --> n168
    n116 --> n134
    n117 --> n134
    n46 --> n55
    n111 --> n117
    n108 --> n118
    n120 --> n135
    n47 --> n60
    n58 --> n60
    n181 --> n185
    n182 --> n185
    n47 --> n56
    n105 --> n110
    n101 --> n110
    n115 --> n136
    n21 --> n23
    n61 --> n69
    n126 --> n137
    n122 --> n137
    n54 --> n61
    n34 --> n39
    n80 --> n84
    n53 --> n62
    n147 --> n152
    n112 --> n119
    n158 --> n178
    n168 --> n178
    n40 --> n47
    n110 --> n120
    n40 --> n48
    n41 --> n48
    n114 --> n121
    n89 --> n103
    n175 --> n186
    n176 --> n186
    n99 --> n111
    n100 --> n111
    n103 --> n112
    n107 --> n112
    n93 --> n104
    n97 --> n105
    n90 --> n105
    n113 --> n122
    n35 --> n40
    n35 --> n41
    n191 --> n194
    n148 --> n169
    n161 --> n169
    n190 --> n195
    n29 --> n34
    n143 --> n153
    n137 --> n153
    n36 --> n42
    n136 --> n154
    n22 --> n25
    n23 --> n25
    n184 --> n189
    n188 --> n189
    n187 --> n189
    n185 --> n189
    n186 --> n189
    n61 --> n70
    n126 --> n138
    n119 --> n139
    n134 --> n155
    n41 --> n49
    n26 --> n28
    n37 --> n43
    n135 --> n156
    n140 --> n156
    n46 --> n57
    n68 --> n71
    n120 --> n140
    n93 --> n106
    n133 --> n157
    n131 --> n157
    n55 --> n63
    n57 --> n63
    n23 --> n29
    n26 --> n29
    n86 --> n91
    n166 --> n179
    n165 --> n179
    n87 --> n92
    n71 --> n74
    n42 --> n50
    n23 --> n26
    n22 --> n26
    n98 --> n113
    n73 --> n76
    n174 --> n180
    n74 --> n77
    n189 --> n191
    n145 --> n158
    n142 --> n158
    n85 --> n93
    n108 --> n123
    n153 --> n170
    n68 --> n75
    n66 --> n75
    n72 --> n75
    n189 --> n192
    n125 --> n141
    n30 --> n35
    n147 --> n159
    n123 --> n159
    n30 --> n36
    n75 --> n78
    n50 --> n58
    n47 --> n58
    n74 --> n79
    n177 --> n187
    n179 --> n187
    n178 --> n187
    n79 --> n85
    n77 --> n85
    n192 --> n196
    n26 --> n30
    n22 --> n30
    n67 --> n72
    n69 --> n72
    n62 --> n72
    n138 --> n160
    n128 --> n142
    n155 --> n171
    n126 --> n143
    n122 --> n143
    n155 --> n172
    n86 --> n94
    n169 --> n181
    n109 --> n144
    n126 --> n144
    n144 --> n161
    n169 --> n182
    n198 --> n201
    n128 --> n145
    n123 --> n146
    n130 --> n183
    n171 --> n183
    n156 --> n173
    n162 --> n173
    n75 --> n80
    n110 --> n124
    n78 --> n86
    n82 --> n95
    n84 --> n95
    n81 --> n87
    n108 --> n125
    n75 --> n81
    n38 --> n51
    n44 --> n51
    n27 --> n37
    n109 --> n126
    n113 --> n126
    n92 --> n107
    n107 --> n114
    n118 --> n147
    n123 --> n147
    n125 --> n147
    n111 --> n127
    n52 --> n64
    n59 --> n64
    n58 --> n64
    n150 --> n174
    n152 --> n174
    n159 --> n174
    n141 --> n174
    n26 --> n31
    n38 --> n44
    n36 --> n44
    n36 --> n52
    n44 --> n52
    n88 --> n96
    n129 --> n162
    n112 --> n128
    n76 --> n88
    n26 --> n32
    n193 --> n198
    n196 --> n198
    n194 --> n198
    n197 --> n198
    n195 --> n198
    n51 --> n65
    n59 --> n65
    n37 --> n65
    n139 --> n163
    n28 --> n38
    n191 --> n197
    n83 --> n97
    n33 --> n45
    n51 --> n59
    n52 --> n59
    n177 --> n188
    n179 --> n188
    n178 --> n188
    n183 --> n188
    n171 --> n184
    n109 x--x n111
    n109 x--x n112
    n109 x--x n113
    n109 x--x n114
    n148 x--x n161
    n131 x--x n133
    n165 x--x n166
    n22 x--x n23
    n73 x--x n71
    n73 x--x n75
    n177 x--x n179
    n135 x--x n140
    n111 x--x n112
    n111 x--x n113
    n111 x--x n114
    n112 x--x n113
    n112 x--x n114
    n104 x--x n106
    n40 x--x n41
    n194 x--x n197
    n195 x--x n197
    n139 x--x n128
    n28 x--x n30
    n71 x--x n75
    n113 x--x n114
    n35 x--x n36
    n142 x--x n145
```
