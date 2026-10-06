# POL_assemble_the_regency_council

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("POL_assemble_the_regency_council"))
        n2["POL_complete_april_constitution"]
        n3{"POL_divide_lit"}
        n4["POL_nationalist_constitution"]
        n5["POL_organize_the_peasants_strike"]
        n6["POL_prepare_german_line"]
        n7{"POL_support_global_falangism"}
    end
    subgraph tier_1["Tier 1"]
        n8{"POL_fulfil_fifth_of_november"}
        n9["POL_seek_an_alliance_with_kaiser"]
    end
    subgraph tier_2["Tier 2"]
        n10["POL_claiming_lithuania"]
        n11["POL_cossack_king"]
        n12["POL_habsburg"]
        n13["POL_hohenzollern"]
        n14["POL_romanov"]
    end
    subgraph tier_3["Tier 3"]
        n15["POL_invite_exiled_nobility"]
        n16["POL_restoration_of_the_royal_sejm"]
        n17["POL_restore_bermontians"]
        n18["POL_restore_the_diet_of_galicia"]
        n19["POL_soldier_king"]
    end
    subgraph tier_4["Tier 4"]
        n20["POL_demand_LIT_pavel"]
        n21["POL_institute_royal_guards"]
        n22["POL_internal_romanian_support"]
        n23["POL_kings_guard"]
        n24["POL_pan_slavism"]
        n25["POL_royal_hussars"]
        n26["POL_support_monarchism_in_LIT"]
        n27["POL_support_monarchy_in_CZE"]
    end
    subgraph tier_5["Tier 5"]
        n28["POL_arm_monarchist_militants"]
        n29{"POL_demand_slovakia_pavel"}
        n30{"POL_demand_yugoslav_subjugation"}
        n31{"POL_governorate_livonia"}
        n32["POL_habsburg_monarchist_militants"]
        n33["POL_king_of_bohemia"]
        n34["POL_king_of_lithuania"]
        n35["POL_press_the_habsburg_claim"]
        n36{"POL_royal_officer_corps"}
    end
    subgraph tier_6["Tier 6"]
        n37["POL_LIT_union"]
        n38["POL_align_with_habsburgs"]
        n39["POL_assert_western_claims"]
        n40["POL_claim_russia"]
        n41["POL_king_michaels_coup"]
        n42{"POL_seek_german_alignment"}
        n43["POL_trust_in_the_west"]
        n44["POL_unite_west_slavia"]
    end
    subgraph tier_7["Tier 7"]
        n45["POL_assert_eastern_claims_pavel"]
        n46{"POL_claim_livonia"}
        n47["POL_demand_pomerania"]
        n48["POL_expand_lithuanian_shipyards"]
        n49{"POL_german_training"}
        n50["POL_join_CZE_industry"]
        n51["POL_join_CZE_rails"]
        n52{"POL_konfederacja_narodu"}
        n53["POL_lithuanian_rail"]
        n54{"POL_merge_internal_governments"}
        n55["POL_reclaim_west_slavia"]
    end
    subgraph tier_8["Tier 8"]
        n56["POL_claim_greater_lithuania"]
        n57["POL_claim_prussia"]
        n58["POL_complete_the_bermontian_mission"]
        n59{"POL_german_staff"}
        n60["POL_join_CZE_military"]
        n61["POL_merge_the_arms_industries"]
        n62{"POL_polish_shock_battallions"}
        n63["POL_pro_allied_government"]
        n64["POL_proclaim_slavic_unity"]
        n65["POL_push_for_ruthenia"]
        n66["POL_royal_dictatorship"]
    end
    subgraph tier_9["Tier 9"]
        n67["POL_ROM_join_allies"]
        n68["POL_demand_slovakia"]
        n69["POL_greater_commonwealth"]
        n70["POL_merge_civilian_industries"]
        n71{"POL_reach_out_to_underground_state"}
        n72{"POL_request_autonomous_status"}
        n73["POL_warsaw_to_crimea_railway"]
    end
    subgraph tier_10["Tier 10"]
        n74["POL_assurance_of_loyalty"]
        n75["POL_declare_independence"]
        n76["POL_restore_poland_hungary"]
    end
    subgraph tier_11["Tier 11"]
        n77["POL_anti_blitz_tactics"]
        n78["POL_radicalize_poles_in_germany"]
    end
    n34 --> n37
    n20 --> n37
    n63 --> n67
    n36 --> n38
    n6 --> n77
    n75 --> n77
    n26 --> n28
    n22 --> n28
    n42 --> n45
    n29 --> n39
    n31 --> n39
    n72 --> n74
    n46 --> n56
    n37 --> n46
    n34 --> n46
    n28 --> n46
    n46 --> n57
    n31 --> n40
    n29 --> n40
    n30 --> n40
    n8 --> n10
    n47 --> n58
    n45 --> n58
    n8 --> n11
    n72 --> n75
    n71 --> n75
    n17 --> n20
    n15 --> n20
    n39 --> n47
    n40 --> n47
    n66 --> n68
    n20 --> n29
    n24 --> n30
    n20 --> n30
    n37 --> n48
    n1 --> n8
    n49 --> n59
    n52 --> n59
    n3 --> n49
    n42 --> n49
    n20 --> n31
    n56 --> n69
    n57 --> n69
    n8 --> n12
    n27 --> n32
    n25 --> n32
    n8 --> n13
    n16 --> n21
    n13 --> n22
    n16 --> n22
    n14 --> n15
    n44 --> n50
    n50 --> n60
    n51 --> n60
    n44 --> n51
    n22 --> n41
    n28 --> n41
    n27 --> n33
    n25 --> n33
    n26 --> n34
    n21 --> n34
    n19 --> n23
    n3 --> n52
    n42 --> n52
    n7 --> n52
    n37 --> n53
    n61 --> n70
    n41 --> n54
    n53 --> n61
    n15 --> n24
    n49 --> n62
    n52 --> n62
    n23 --> n35
    n54 --> n63
    n46 --> n63
    n40 --> n64
    n47 --> n64
    n53 --> n65
    n6 --> n78
    n75 --> n78
    n59 --> n71
    n62 --> n71
    n38 --> n55
    n43 --> n55
    n44 --> n55
    n59 --> n72
    n62 --> n72
    n10 --> n16
    n13 --> n16
    n11 --> n17
    n68 --> n76
    n12 --> n18
    n8 --> n14
    n54 --> n66
    n18 --> n25
    n19 --> n25
    n23 --> n36
    n1 --> n9
    n29 --> n42
    n31 --> n42
    n12 --> n19
    n16 --> n26
    n10 --> n26
    n18 --> n27
    n36 --> n43
    n33 --> n44
    n32 --> n44
    n65 --> n73
    n38 x--x n43
    n1 x--x n2
    n1 x--x n4
    n1 x--x n5
    n39 x--x n40
    n39 x--x n42
    n74 x--x n75
    n40 x--x n42
    n10 x--x n11
    n10 x--x n12
    n10 x--x n13
    n10 x--x n14
    n11 x--x n12
    n11 x--x n13
    n11 x--x n14
    n59 x--x n62
    n49 x--x n52
    n12 x--x n13
    n12 x--x n14
    n13 x--x n14
    n63 x--x n66
    n71 x--x n72
```

# POL_clamp_down_on_danzig

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n79["POL_attract_poles_to_gdynia"]
        n80(("POL_clamp_down_on_danzig"))
        n81["POL_develop_polish_ship_building"]
    end
    subgraph tier_1["Tier 1"]
        n82["POL_ban_the_nazi_party"]
        n83["POL_study_foreign_built_ships"]
    end
    subgraph tier_2["Tier 2"]
        n84["POL_develop_gdansk_ship_building"]
        n85["POL_expand_gdynia_seaport"]
        n86["POL_integrate_gdansk_industries"]
    end
    subgraph tier_3["Tier 3"]
        n87["POL_expand_northern_rail"]
        n88{"POL_import_submarine_technology"}
        n89{"POL_the_twin_threats"}
    end
    subgraph tier_4["Tier 4"]
        n90["POL_a_cruiser_navy"]
        n91["POL_coastal_defense"]
        n92["POL_commerce_attack"]
        n93["POL_strike_force"]
    end
    subgraph tier_5["Tier 5"]
        n94["POL_baltic_navy"]
    end
    n89 --> n90
    n93 --> n94
    n91 --> n94
    n80 --> n82
    n89 --> n91
    n88 --> n91
    n88 --> n92
    n82 --> n84
    n79 --> n85
    n83 --> n85
    n86 --> n87
    n85 --> n87
    n86 --> n88
    n85 --> n88
    n82 --> n86
    n89 --> n93
    n88 --> n93
    n81 --> n83
    n80 --> n83
    n86 --> n89
    n85 --> n89
    n80 x--x n81
    n91 x--x n93
```

# POL_complete_april_constitution

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["POL_assemble_the_regency_council"]
        n2(("POL_complete_april_constitution"))
        n95{"POL_draw_closer_to_britain"}
        n4["POL_nationalist_constitution"]
        n5["POL_organize_the_peasants_strike"]
        n96["POL_restore_the_sejm"]
    end
    subgraph tier_1["Tier 1"]
        n97["POL_polish_militarism"]
    end
    subgraph tier_2["Tier 2"]
        n98["POL_consolidate_sanation_government"]
    end
    subgraph tier_3["Tier 3"]
        n99{"POL_the_castle"}
        n100{"POL_the_sanation_left"}
        n101{"POL_the_sanation_right"}
    end
    subgraph tier_4["Tier 4"]
        n102["POL_codify_national_unity"]
        n103["POL_department_for_home_defence"]
        n104["POL_draft_a_new_constitution"]
        n105["POL_eliminate_socialist_parties"]
        n106["POL_legion_of_merit"]
        n107["POL_modus_vivendi"]
        n108["POL_promote_chemical_industry"]
        n109{"POL_second_man_of_the_state"}
        n110["POL_support_right_paramilitaries"]
        n111{"POL_the_left_chairman"}
    end
    subgraph tier_5["Tier 5"]
        n112{"POL_camp_of_national_unity"}
        n113{"POL_common_organization_of_society"}
        n114["POL_dissolve_the_sejm"]
        n115{"POL_ozon"}
    end
    subgraph tier_6["Tier 6"]
        n116{"POL_dissolve_the_bbwr"}
        n117{"POL_polish_revanchism"}
    end
    subgraph tier_7["Tier 7"]
        n118{"POL_align_with_the_west"}
        n119["POL_baltic_security"]
        n120["POL_pan_slavic_revanchism"]
    end
    subgraph tier_8["Tier 8"]
        n121["POL_annex_czech"]
        n122["POL_baltic_alliance_focus"]
        n123["POL_join_allies"]
        n124["POL_lithuanian_annexation"]
        n125["POL_lithuanian_ultimatum"]
        n126["POL_protect_czechozlovakia"]
        n127["POL_the_old_borders"]
    end
    subgraph tier_9["Tier 9"]
        n128["POL_baltic_ultimatums"]
        n129["POL_lithuanian_alliance"]
        n130["POL_romanian_alliance"]
        n131["POL_romanian_bridgehead_strategy"]
    end
    subgraph tier_10["Tier 10"]
        n132["POL_sea_to_sea"]
    end
    n112 --> n118
    n116 --> n118
    n115 --> n118
    n95 --> n118
    n120 --> n121
    n119 --> n122
    n116 --> n119
    n117 --> n128
    n124 --> n128
    n99 --> n112
    n111 --> n112
    n109 --> n112
    n101 --> n102
    n111 --> n113
    n97 --> n98
    n101 --> n103
    n113 --> n116
    n105 --> n114
    n100 --> n104
    n99 --> n105
    n118 --> n123
    n100 --> n106
    n125 --> n129
    n118 --> n124
    n117 --> n124
    n118 --> n125
    n100 --> n107
    n109 --> n115
    n117 --> n120
    n2 --> n97
    n115 --> n117
    n99 --> n108
    n119 --> n126
    n126 --> n130
    n122 --> n130
    n123 --> n131
    n128 --> n132
    n127 --> n132
    n101 --> n109
    n101 --> n110
    n98 --> n99
    n100 --> n111
    n120 --> n127
    n98 --> n100
    n98 --> n101
    n118 x--x n119
    n118 x--x n117
    n1 x--x n2
    n119 x--x n117
    n112 x--x n116
    n112 x--x n115
    n102 x--x n104
    n2 x--x n4
    n2 x--x n5
    n2 x--x n96
    n116 x--x n115
    n124 x--x n125
    n109 x--x n111
```

# POL_develop_polish_ship_building

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n80["POL_clamp_down_on_danzig"]
        n81(("POL_develop_polish_ship_building"))
        n86["POL_integrate_gdansk_industries"]
    end
    subgraph tier_1["Tier 1"]
        n79["POL_attract_poles_to_gdynia"]
        n83["POL_study_foreign_built_ships"]
    end
    subgraph tier_2["Tier 2"]
        n85["POL_expand_gdynia_seaport"]
    end
    subgraph tier_3["Tier 3"]
        n87["POL_expand_northern_rail"]
        n88{"POL_import_submarine_technology"}
        n89{"POL_the_twin_threats"}
    end
    subgraph tier_4["Tier 4"]
        n90["POL_a_cruiser_navy"]
        n91["POL_coastal_defense"]
        n92["POL_commerce_attack"]
        n93["POL_strike_force"]
    end
    subgraph tier_5["Tier 5"]
        n94["POL_baltic_navy"]
    end
    n89 --> n90
    n81 --> n79
    n93 --> n94
    n91 --> n94
    n89 --> n91
    n88 --> n91
    n88 --> n92
    n79 --> n85
    n83 --> n85
    n86 --> n87
    n85 --> n87
    n86 --> n88
    n85 --> n88
    n89 --> n93
    n88 --> n93
    n81 --> n83
    n80 --> n83
    n86 --> n89
    n85 --> n89
    n80 x--x n81
    n91 x--x n93
```

# POL_expand_polish_intelligence_no_mtg

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n133(("POL_expand_polish_intelligence_no_mtg"))
    end
    subgraph tier_1["Tier 1"]
        n134["POL_niech_zyje_opor_no_mtg"]
        n135["POL_the_bombe_no_mtg"]
        n136["POL_the_cyclometer_no_mtg"]
        n137["POL_the_long_push_home_no_mtg"]
    end
    n133 --> n134
    n133 --> n135
    n133 --> n136
    n133 --> n137
```

# POL_nationalist_constitution

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["POL_assemble_the_regency_council"]
        n2["POL_complete_april_constitution"]
        n4(("POL_nationalist_constitution"))
        n5["POL_organize_the_peasants_strike"]
        n42{"POL_seek_german_alignment"}
    end
    subgraph tier_1["Tier 1"]
        n138["POL_integrate_the_endecja"]
        n139["POL_integrate_the_falanga"]
    end
    subgraph tier_2["Tier 2"]
        n140{"POL_empower_falangist_militants"}
        n141{"POL_siodemki"}
    end
    subgraph tier_3["Tier 3"]
        n142{"POL_sideline_the_sanacja"}
    end
    subgraph tier_4["Tier 4"]
        n143{"POL_reopen_national_elections"}
        n144{"POL_riot_of_37"}
    end
    subgraph tier_5["Tier 5"]
        n145["POL_beck_ribbentrop"]
        n146["POL_reassert_silesian_claims"]
    end
    subgraph tier_6["Tier 6"]
        n147["POL_assert_eastern_claims"]
        n3{"POL_divide_lit"}
        n7{"POL_support_global_falangism"}
    end
    subgraph tier_7["Tier 7"]
        n148["POL_anti_germans_abroad"]
        n149["POL_demand_LIT"]
        n150["POL_falangist_international"]
        n151["POL_force_polish_upper_class"]
        n49{"POL_german_training"}
        n52{"POL_konfederacja_narodu"}
        n152["POL_state_catholicism"]
    end
    subgraph tier_8["Tier 8"]
        n59{"POL_german_staff"}
        n153["POL_integrate_greater_kashubia"]
        n154["POL_invite_the_baltics"]
        n155["POL_invite_the_lowlands"]
        n62{"POL_polish_shock_battallions"}
        n6["POL_prepare_german_line"]
        n156["POL_privatize_education"]
        n157["POL_support_falangists_in_the_americas"]
        n158["POL_the_national_commonwealth"]
    end
    subgraph tier_9["Tier 9"]
        n71{"POL_reach_out_to_underground_state"}
        n72{"POL_request_autonomous_status"}
    end
    subgraph tier_10["Tier 10"]
        n74["POL_assurance_of_loyalty"]
        n75["POL_declare_independence"]
    end
    subgraph tier_11["Tier 11"]
        n77["POL_anti_blitz_tactics"]
        n78["POL_radicalize_poles_in_germany"]
    end
    n6 --> n77
    n75 --> n77
    n7 --> n148
    n145 --> n147
    n146 --> n147
    n72 --> n74
    n144 --> n145
    n143 --> n145
    n72 --> n75
    n71 --> n75
    n7 --> n149
    n145 --> n3
    n139 --> n140
    n7 --> n150
    n3 --> n151
    n7 --> n151
    n49 --> n59
    n52 --> n59
    n3 --> n49
    n42 --> n49
    n149 --> n153
    n148 --> n153
    n4 --> n138
    n4 --> n139
    n150 --> n154
    n148 --> n154
    n150 --> n155
    n3 --> n52
    n42 --> n52
    n7 --> n52
    n49 --> n62
    n52 --> n62
    n149 --> n6
    n148 --> n6
    n151 --> n156
    n6 --> n78
    n75 --> n78
    n59 --> n71
    n62 --> n71
    n144 --> n146
    n143 --> n146
    n142 --> n143
    n141 --> n143
    n59 --> n72
    n62 --> n72
    n142 --> n144
    n140 --> n144
    n140 --> n142
    n141 --> n142
    n138 --> n141
    n7 --> n152
    n150 --> n157
    n146 --> n7
    n149 --> n158
    n148 x--x n149
    n1 x--x n4
    n74 x--x n75
    n145 x--x n146
    n2 x--x n4
    n59 x--x n62
    n49 x--x n52
    n4 x--x n5
    n71 x--x n72
    n143 x--x n144
```

# POL_organize_the_peasants_strike

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["POL_assemble_the_regency_council"]
        n2["POL_complete_april_constitution"]
        n4["POL_nationalist_constitution"]
        n5(("POL_organize_the_peasants_strike"))
    end
    subgraph tier_1["Tier 1"]
        n159{"POL_woo_morges_staff"}
    end
    subgraph tier_2["Tier 2"]
        n160["POL_arm_peasant_militia"]
        n161["POL_ease_sanationist_tensions"]
        n162{"POL_raise_the_black_madonna"}
        n163{"POL_state_national_council"}
    end
    subgraph tier_3["Tier 3"]
        n164{"POL_KPP_focus"}
        n165["POL_a_leftist_sejm"]
        n166["POL_communal_governance"]
        n167["POL_elect_a_PSL_leader"]
        n168["POL_empower_the_morges"]
        n169["POL_reassemble_the_sejm"]
    end
    subgraph tier_4["Tier 4"]
        n170{"POL_invest_in_the_peasantry"}
        n171["POL_polish_path_to_socialism"]
        n172["POL_surrender_the_east"]
    end
    subgraph tier_5["Tier 5"]
        n173{"POL_anti_imperialism"}
        n174["POL_dabrowszczacy"]
        n175["POL_leftist_economics"]
        n176["POL_morges_pact"]
        n177["POL_polish_peoples_republic"]
    end
    subgraph tier_6["Tier 6"]
        n178["POL_anti_capitalist_revolution"]
        n179["POL_committee_of_national_liberation"]
        n180["POL_lower_class_education"]
        n181["POL_morges_economic_union"]
        n182["POL_non_discriminatory_recruitment"]
        n183{"POL_pressure_for_the_west"}
        n184{"POL_soviet_industry"}
        n185{"POL_soviet_military_staff"}
    end
    subgraph tier_7["Tier 7"]
        n186["POL_armia_ludowa"]
        n187["POL_baltic_socialism"]
        n188{"POL_com_independence"}
        n189["POL_greater_polish_SSR"]
        n190["POL_purchase_madagascar"]
    end
    subgraph tier_8["Tier 8"]
        n191["POL_dismantle_capitalist_empires"]
        n192["POL_preserve_bougoise_democracy"]
    end
    subgraph tier_9["Tier 9"]
        n193["POL_anti_fascist_military"]
        n194["POL_press_for_liberia"]
    end
    subgraph tier_10["Tier 10"]
        n195["POL_preserve_baltic_independence"]
        n196["POL_reopen_the_maritime_and_colonial_league"]
        n197["POL_support_colonial_workers_strikes"]
    end
    subgraph tier_11["Tier 11"]
        n198["POL_dismantle_fascist_empires"]
        n199["POL_invite_romania_to_morges"]
        n200["POL_social_commonwealth"]
    end
    subgraph tier_12["Tier 12"]
        n201["POL_dismantle_soviet_empire"]
    end
    n163 --> n164
    n163 --> n165
    n173 --> n178
    n192 --> n193
    n176 --> n193
    n171 --> n173
    n159 --> n160
    n179 --> n186
    n182 --> n186
    n178 --> n187
    n184 --> n188
    n183 --> n188
    n185 --> n188
    n175 --> n179
    n163 --> n166
    n171 --> n174
    n172 --> n174
    n170 --> n174
    n187 --> n191
    n191 --> n198
    n195 --> n198
    n198 --> n201
    n159 --> n161
    n162 --> n167
    n162 --> n168
    n184 --> n189
    n183 --> n189
    n185 --> n189
    n167 --> n170
    n181 --> n199
    n195 --> n199
    n171 --> n175
    n172 --> n175
    n170 --> n175
    n175 --> n180
    n176 --> n181
    n170 --> n176
    n175 --> n182
    n164 --> n171
    n172 --> n177
    n193 --> n195
    n173 --> n192
    n188 --> n192
    n170 --> n192
    n178 --> n194
    n192 --> n194
    n176 --> n194
    n177 --> n183
    n181 --> n190
    n159 --> n162
    n162 --> n169
    n194 --> n196
    n192 --> n196
    n195 --> n200
    n191 --> n200
    n177 --> n184
    n177 --> n185
    n159 --> n163
    n194 --> n197
    n178 --> n197
    n164 --> n172
    n5 --> n159
    n164 x--x n167
    n178 x--x n176
    n178 x--x n192
    n160 x--x n161
    n1 x--x n5
    n188 x--x n189
    n2 x--x n5
    n176 x--x n192
    n4 x--x n5
    n171 x--x n172
```

# POL_prepare_for_the_inevitable

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n202(("POL_prepare_for_the_inevitable"))
    end
    subgraph tier_1["Tier 1"]
        n203["POL_expand_polish_intelligence"]
        n204["POL_foreign_air_support"]
        n205["POL_foreign_naval_support"]
        n206["POL_resistance_industries"]
    end
    subgraph tier_2["Tier 2"]
        n207["POL_aces_in_exile"]
        n208["POL_exile_industries"]
        n209["POL_foreign_army_support"]
        n210["POL_niech_zyje_opor"]
        n211["POL_the_bombe"]
        n212["POL_the_cyclometer"]
        n213["POL_the_long_push_home"]
    end
    n204 --> n207
    n206 --> n208
    n202 --> n203
    n202 --> n204
    n204 --> n209
    n202 --> n205
    n203 --> n210
    n202 --> n206
    n203 --> n211
    n203 --> n212
    n203 --> n213
```

# POL_prepare_for_the_next_war

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n214(("POL_prepare_for_the_next_war"))
    end
    subgraph tier_1["Tier 1"]
        n215["POL_new_military_academy"]
        n216["POL_plan_east"]
        n217["POL_plan_west"]
    end
    subgraph tier_2["Tier 2"]
        n218["POL_belorussian_army"]
        n219["POL_eastern_conscripts"]
        n220["POL_expand_poznan_forts"]
        n221["POL_fortification_of_belarus"]
        n222["POL_fortification_of_ukraine"]
        n223["POL_hel_fortified_area"]
        n224["POL_invest_anti_air"]
        n225["POL_local_eastern_plans"]
        n226["POL_local_western_plans"]
        n227["POL_ruthenian_army"]
        n228["POL_sabotage_polish_industry"]
        n229["POL_silesia_fortified_area"]
        n230["POL_standardisation_of_equipment"]
        n231["POL_sudeten_mountaineers"]
        n232["POL_supply_the_rail_nexus"]
        n233["POL_the_prusya_army"]
        n234["POL_the_prusya_line"]
    end
    subgraph tier_3["Tier 3"]
        n235["POL_air_base_expansion"]
        n236{"POL_army_modernisation"}
        n237["POL_complete_plan_east"]
        n238["POL_complete_plan_west"]
    end
    subgraph tier_4["Tier 4"]
        n239{"POL_air_innovations"}
        n240["POL_anti_tank_guns"]
        n241["POL_artillery_modernisation"]
        n242["POL_attract_foreign_motors"]
        n243{"POL_fighter_modernisation"}
        n244["POL_modernising_the_cavalry"]
    end
    subgraph tier_5["Tier 5"]
        n245["POL_adaptive_designs"]
        n246{"POL_heavy_fighter_concept"}
        n247["POL_naval_bomber_experiments"]
        n248["POL_study_foreign_tanks"]
    end
    subgraph tier_6["Tier 6"]
        n249["POL_anti_blitz_vehicles"]
        n250["POL_cruiser_tank_experiments"]
        n251["POL_light_bomber_focus"]
        n252["POL_medium_bomber_focus"]
    end
    subgraph tier_7["Tier 7"]
        n253["POL_air_modernisations_programme"]
    end
    subgraph tier_8["Tier 8"]
        n254["POL_rocket_development"]
    end
    n242 --> n245
    n240 --> n245
    n230 --> n235
    n235 --> n239
    n251 --> n253
    n252 --> n253
    n248 --> n249
    n240 --> n249
    n236 --> n240
    n230 --> n236
    n236 --> n241
    n236 --> n242
    n216 --> n218
    n221 --> n237
    n222 --> n237
    n232 --> n237
    n219 --> n237
    n218 --> n237
    n227 --> n237
    n225 --> n237
    n233 --> n238
    n229 --> n238
    n226 --> n238
    n231 --> n238
    n224 --> n238
    n234 --> n238
    n220 --> n238
    n223 --> n238
    n248 --> n250
    n216 --> n219
    n217 --> n220
    n235 --> n243
    n216 --> n221
    n216 --> n222
    n239 --> n246
    n243 --> n246
    n217 --> n223
    n217 --> n224
    n246 --> n251
    n243 --> n251
    n216 --> n225
    n217 --> n226
    n246 --> n252
    n239 --> n252
    n236 --> n244
    n239 --> n247
    n214 --> n215
    n214 --> n216
    n214 --> n217
    n253 --> n254
    n216 --> n227
    n216 --> n228
    n217 --> n228
    n217 --> n229
    n215 --> n230
    n244 --> n248
    n242 --> n248
    n217 --> n231
    n216 --> n232
    n217 --> n233
    n217 --> n234
    n242 x--x n244
    n251 x--x n252
```

# POL_restore_the_sejm

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n119["POL_baltic_security"]
        n112{"POL_camp_of_national_unity"}
        n2["POL_complete_april_constitution"]
        n116{"POL_dissolve_the_bbwr"}
        n115{"POL_ozon"}
        n117{"POL_polish_revanchism"}
        n96(("POL_restore_the_sejm"))
        n127["POL_the_old_borders"]
    end
    subgraph tier_1["Tier 1"]
        n255{"POL_internationalism"}
    end
    subgraph tier_2["Tier 2"]
        n256{"POL_authoritarianism"}
        n257["POL_liberalism_focus"]
    end
    subgraph tier_3["Tier 3"]
        n95{"POL_draw_closer_to_britain"}
        n258["POL_go_left"]
        n259["POL_go_right"]
        n260["POL_intervention_focus"]
        n261["POL_paramilitarism"]
    end
    subgraph tier_4["Tier 4"]
        n118{"POL_align_with_the_west"}
        n262["POL_military_youth"]
        n263["POL_political_commissars"]
        n264["POL_seek_accommodation_with_USSR"]
        n265["POL_seek_accommodation_with_germany"]
        n266["POL_volunteer_corps"]
    end
    subgraph tier_5["Tier 5"]
        n123["POL_join_allies"]
        n124["POL_lithuanian_annexation"]
        n125["POL_lithuanian_ultimatum"]
    end
    subgraph tier_6["Tier 6"]
        n128["POL_baltic_ultimatums"]
        n129["POL_lithuanian_alliance"]
        n131["POL_romanian_bridgehead_strategy"]
    end
    subgraph tier_7["Tier 7"]
        n132["POL_sea_to_sea"]
    end
    n112 --> n118
    n116 --> n118
    n115 --> n118
    n95 --> n118
    n255 --> n256
    n117 --> n128
    n124 --> n128
    n257 --> n95
    n256 --> n258
    n256 --> n259
    n96 --> n255
    n257 --> n260
    n118 --> n123
    n255 --> n257
    n125 --> n129
    n118 --> n124
    n117 --> n124
    n118 --> n125
    n259 --> n262
    n256 --> n261
    n258 --> n263
    n123 --> n131
    n128 --> n132
    n127 --> n132
    n258 --> n264
    n259 --> n265
    n260 --> n266
    n118 x--x n119
    n118 x--x n117
    n256 x--x n257
    n2 x--x n96
    n258 x--x n259
    n124 x--x n125
```

# POL_the_between_the_seas_concept

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n267(("POL_the_between_the_seas_concept"))
    end
    subgraph tier_1["Tier 1"]
        n268["POL_the_baltic_alliance"]
        n269["POL_the_mediterranean"]
        n270["POL_the_north_sea"]
    end
    subgraph tier_2["Tier 2"]
        n271["POL_coerce_czechoslovakia"]
        n272["POL_finno_polish_pact"]
        n273{"POL_protect_yugoslavia"}
        n274["POL_treaty_with_lithuania"]
    end
    subgraph tier_3["Tier 3"]
        n275["POL_austro_hungarian_alliance"]
        n276["POL_control_the_bosporus"]
        n277["POL_invite_denmark"]
        n278["POL_invite_greece"]
        n279["POL_invite_norway"]
        n280["POL_invite_sweden"]
    end
    subgraph tier_4["Tier 4"]
        n281["POL_italian_alliance"]
    end
    n271 --> n275
    n269 --> n271
    n273 --> n276
    n270 --> n272
    n272 --> n277
    n273 --> n278
    n272 --> n279
    n272 --> n280
    n276 --> n281
    n278 --> n281
    n275 --> n281
    n269 --> n273
    n267 --> n268
    n267 --> n269
    n267 --> n270
    n268 --> n274
    n276 x--x n278
```

# POL_the_four_year_plan

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n282(("POL_the_four_year_plan"))
    end
    subgraph tier_1["Tier 1"]
        n283["POL_additional_research_slot1"]
        n284["POL_central_region_strategy"]
        n285["POL_fill_the_railways_gaps"]
    end
    subgraph tier_2["Tier 2"]
        n286["POL_agrarian_reform"]
        n287["POL_central_defence_of_poland"]
        n288["POL_expansion_of_new_towns"]
        n289["POL_invest_in_the_old_polish_region"]
        n290["POL_national_defence_fund"]
    end
    subgraph tier_3["Tier 3"]
        n291{"POL_additional_research_slot2"}
        n292["POL_develop_upper_silesia"]
        n293["POL_expand_katowice_mines"]
        n294["POL_modernize_congressional_factories"]
        n295["POL_start_central_industrial_region"]
    end
    subgraph tier_4["Tier 4"]
        n296["POL_abolish_segregated_seating"]
        n297["POL_expand_central_industrial_region"]
        n298["POL_ideological_fanaticism"]
        n299["POL_invest_in_eastern_poland"]
        n300["POL_warsaw_main_railway_station"]
    end
    subgraph tier_5["Tier 5"]
        n301["POL_atomic_physics_institute"]
    end
    n291 --> n296
    n282 --> n283
    n288 --> n291
    n285 --> n286
    n298 --> n301
    n296 --> n301
    n285 --> n287
    n284 --> n287
    n282 --> n284
    n287 --> n292
    n295 --> n297
    n288 --> n293
    n284 --> n288
    n282 --> n285
    n291 --> n298
    n286 --> n299
    n292 --> n299
    n284 --> n289
    n289 --> n294
    n285 --> n290
    n288 --> n295
    n294 --> n300
    n296 x--x n298
```
