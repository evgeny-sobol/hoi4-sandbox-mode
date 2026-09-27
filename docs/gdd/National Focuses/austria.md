# AUS_osterreichische_luftstreitkrafte

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["AUS_osterreichische_bundesheer"]
        n2(("AUS_osterreichische_luftstreitkrafte"))
    end
    subgraph tier_1["Tier 1"]
        n3{"AUS_preparing_the_industry"}
    end
    subgraph tier_2["Tier 2"]
        n4["AUS_focus_on_domestic_production"]
        n5["AUS_osterreichische_fallschirmsjager"]
        n6["AUS_purchase_foreign_designs"]
    end
    subgraph tier_3["Tier 3"]
        n7["AUS_flight_schools"]
        n8{"AUS_revitalize_austrian_air_industry"}
        n9["AUS_seek_international_partners"]
    end
    subgraph tier_4["Tier 4"]
        n10["AUS_air_research_boost"]
        n11["AUS_heavy_specialization"]
        n12["AUS_light_specialization"]
        n13["AUS_medium_specialization"]
    end
    subgraph tier_5["Tier 5"]
        n14["AUS_air_base_intiative"]
        n15["AUS_radar_effort"]
        n16["AUS_wien_anti_air_effort"]
    end
    subgraph tier_6["Tier 6"]
        n17["AUS_neustadter_flugzeugwerke"]
    end
    subgraph tier_7["Tier 7"]
        n18["AUS_aerial_strategies"]
    end
    n17 --> n18
    n12 --> n14
    n13 --> n14
    n11 --> n14
    n10 --> n14
    n9 --> n10
    n6 --> n7
    n4 --> n7
    n3 --> n4
    n8 --> n11
    n8 --> n12
    n8 --> n13
    n14 --> n17
    n16 --> n17
    n15 --> n17
    n1 --> n5
    n3 --> n5
    n2 --> n3
    n3 --> n6
    n12 --> n15
    n13 --> n15
    n11 --> n15
    n10 --> n15
    n4 --> n8
    n6 --> n9
    n12 --> n16
    n13 --> n16
    n11 --> n16
    n10 --> n16
    n4 x--x n6
    n11 x--x n12
    n11 x--x n13
    n12 x--x n13
```

# AUS_reestablish_austrian_navy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n19{"AUS_reestablish_austrian_navy"}
        n20["AUS_standardized_army_training"]
    end
    subgraph tier_1["Tier 1"]
        n21["AUS_defending_the_coast"]
        n22["AUS_rebuild_the_armada"]
    end
    subgraph tier_2["Tier 2"]
        n23["AUS_elin"]
        n24["AUS_light_ship_bonus"]
        n25["AUS_osterreichische_seebataillon"]
        n26["AUS_reclaim_dockyards"]
        n27["AUS_revive_stt"]
        n28["AUS_streamline_production"]
    end
    subgraph tier_3["Tier 3"]
        n29["AUS_coastal_defence_forts"]
        n30["AUS_continue_old_production"]
        n31["AUS_promote_admirals"]
    end
    subgraph tier_4["Tier 4"]
        n32["AUS_naval_efficiency"]
    end
    n24 --> n29
    n23 --> n29
    n28 --> n30
    n27 --> n30
    n19 --> n21
    n21 --> n23
    n21 --> n24
    n29 --> n32
    n30 --> n32
    n20 --> n25
    n22 --> n25
    n26 --> n31
    n19 --> n22
    n22 --> n26
    n21 --> n26
    n22 --> n27
    n22 --> n28
    n21 x--x n22
```

# AUS_regulate_austrian_finance_sector

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n33(("AUS_regulate_austrian_finance_sector"))
    end
    subgraph tier_1["Tier 1"]
        n34["AUS_architechtual_advancements"]
        n35["AUS_economic_resuscitation"]
        n36{"AUS_industrialization_effort"}
        n37["AUS_invest_in_erzberg_steel_mines"]
        n38["AUS_seek_papal_support"]
    end
    subgraph tier_2["Tier 2"]
        n39["AUS_autobahn_east"]
        n40["AUS_autobahn_south"]
        n41["AUS_autobahn_west"]
        n42["AUS_courting_the_princess_of_industry"]
        n43["AUS_devalue_the_schilling"]
        n44["AUS_invest_in_alpen_elektrowerke"]
        n45["AUS_invest_in_kapsch"]
    end
    subgraph tier_3["Tier 3"]
        n46["AUS_bbo_focus"]
        n47["AUS_bring_phonix_insurance_from_the_ashes"]
        n48["AUS_construction_guilds"]
        n49["AUS_expand_stpoltner_steelworks"]
        n50["AUS_great_austrian_economic_push"]
    end
    subgraph tier_4["Tier 4"]
        n51["AUS_apprentice_programmes"]
        n52["AUS_invest_in_semperit_synthetics"]
        n53["AUS_pulverfabrik_skodawerke"]
        n54["AUS_volkschule"]
    end
    subgraph tier_5["Tier 5"]
        n55["AUS_the_matzen_oil_fields"]
    end
    n48 --> n51
    n33 --> n34
    n34 --> n39
    n34 --> n40
    n34 --> n41
    n39 --> n46
    n41 --> n46
    n40 --> n46
    n43 --> n47
    n45 --> n48
    n44 --> n48
    n37 --> n42
    n35 --> n43
    n33 --> n35
    n42 --> n49
    n43 --> n50
    n33 --> n36
    n36 --> n44
    n33 --> n37
    n36 --> n45
    n49 --> n52
    n49 --> n53
    n33 --> n38
    n53 --> n55
    n52 --> n55
    n50 --> n54
    n47 --> n54
    n44 x--x n45
```

# AUS_repeal_the_may_constitution

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n56{"AUS_heimwehr_support"}
        n57["AUS_heritage_of_an_empire"]
        n58{"AUS_rapid_rearmament"}
        n59(("AUS_repeal_the_may_constitution"))
        n60["AUS_totalitarian_safety"]
    end
    subgraph tier_1["Tier 1"]
        n61{"AUS_austria_against_fascism"}
        n62{"AUS_release_imprisoned_leaders"}
    end
    subgraph tier_2["Tier 2"]
        n63["AUS_austromarxism_focus"]
        n64{"AUS_hold_elections"}
        n65{"AUS_reinstate_the_imperial_council"}
    end
    subgraph tier_3["Tier 3"]
        n66{"AUS_a_new_constitution"}
        n67["AUS_legacy_of_the_empire"]
        n68["AUS_rally_the_people"]
        n69{"AUS_rebuild_democratic_systems"}
        n70["AUS_the_danubian_federation"]
    end
    subgraph tier_4["Tier 4"]
        n71["AUS_ban_dnsap"]
        n72["AUS_bring_back_the_habsburg_rule"]
        n73["AUS_invite_danubian_countries"]
        n74["AUS_renounce_the_treaties"]
        n75["AUS_repeal_the_habsburgergesetz"]
        n76["AUS_schutzbund_support"]
        n77{"AUS_seek_support_from_guarantors"}
    end
    subgraph tier_5["Tier 5"]
        n78["AUS_danubian_unity"]
        n79["AUS_emergency_measaures"]
        n80["AUS_outlaw_the_radicals"]
        n81{"AUS_rebellious_rearmament"}
        n82["AUS_stabilize_the_political_climate"]
        n83{"AUS_the_right_to_rearm"}
    end
    subgraph tier_6["Tier 6"]
        n84["AUS_austrian_aggression"]
        n85{"AUS_bring_hungary_back_into_the_fold"}
        n86["AUS_defence_of_the_homeland"]
        n87{"AUS_demand_hungarian_submission"}
        n88{"AUS_intervention_in_spain"}
        n89["AUS_inviting_the_observers"]
        n90["AUS_legitimistische_studentenverbindung"]
        n91{"AUS_revolution"}
        n92["AUS_strengthen_legitimistische_corps"]
        n93{"AUS_strengthen_the_cabinet"}
        n94["AUS_unexpected_alliances"]
    end
    subgraph tier_7["Tier 7"]
        n95["AUS_a_royal_alliance"]
        n96["AUS_alpine_federation_focus"]
        n97["AUS_at_the_ready"]
        n98["AUS_celebrate_spanish_victory"]
        n99{"AUS_diplomatic_effort"}
        n100["AUS_invite_spanish_exiles"]
        n101["AUS_join_the_allies"]
        n102["AUS_join_the_axis"]
        n103["AUS_legitimistische_jugend"]
        n104["AUS_raid_military_storages"]
        n105["AUS_reclaiming_yugoslavian_territories"]
        n106["AUS_reforming_the_central_powers"]
        n107["AUS_repeal_the_adelsaufhebungsgesetz"]
        n108["AUS_seek_soviet_support"]
        n109["AUS_sturmscharen_support"]
        n110["AUS_subjugate_lands_of_old"]
        n111["AUS_the_czechoslovakian_lands"]
        n112["AUS_the_political_front"]
    end
    subgraph tier_8["Tier 8"]
        n113{"AUS_a_new_beginning"}
        n114{"AUS_demand_romanian_lands"}
        n115["AUS_eiserne_legion"]
        n116["AUS_form_evidenzburo"]
        n117["AUS_industrial_exchange"]
        n118["AUS_invite_the_entente"]
        n119["AUS_pardon_political_exiles"]
        n120["AUS_politicized_general_staff"]
        n121["AUS_promote_the_worthy"]
        n122["AUS_properly_trained_militias"]
        n123["AUS_protector_of_the_danube"]
        n124["AUS_take_albania"]
        n125{"AUS_take_back_galicia"}
        n126["AUS_the_evidenzburo"]
        n127["AUS_the_peoples_army"]
        n128["AUS_the_silesian_question"]
        n129{"AUS_tighten_control_of_subjects"}
        n130["AUS_via_danube_to_europe"]
    end
    subgraph tier_9["Tier 9"]
        n131{"AUS_a_safe_harbor_for_dissidents"}
        n132{"AUS_align_with_ussr"}
        n133["AUS_cut_ties_with_the_church"]
        n134["AUS_integrate_hungary"]
        n135["AUS_integrate_northwest"]
        n136["AUS_lawmaking_leniency"]
        n137["AUS_offensive_on_the_fascists"]
        n138["AUS_reclaim_habsburg"]
        n139["AUS_renew_claims_in_italy"]
        n140["AUS_strike_deal_with_italy"]
        n141["AUS_the_royals_of_liechtenstein"]
        n142["AUS_universitat_wien"]
        n143["AUS_war_against_guarantors"]
    end
    subgraph tier_10["Tier 10"]
        n144["AUS_centralize_the_industrial_sector"]
        n145["AUS_danubian_socialist_communes"]
        n146["AUS_empowering_the_chancellor"]
        n147["AUS_establish_rote_hilfe"]
        n148["AUS_extend_italian_claims"]
        n149["AUS_for_a_better_future"]
        n150["AUS_join_comintern"]
        n151["AUS_join_the_research_program"]
        n152["AUS_osterreichische_akademie"]
        n153["AUS_proclaim_austrian_empire"]
        n154["AUS_scientific_grants"]
        n155["AUS_womens_education_initiative"]
    end
    subgraph tier_11["Tier 11"]
        n156["AUS_beyond_our_old_lands"]
        n157["AUS_royal_scientific_grants"]
        n158["AUS_second_brothers_war"]
        n159{"AUS_spur_the_communist_resistance"}
        n160["AUS_the_right_to_self_determination"]
        n161["AUS_war_against_bolshevism"]
    end
    subgraph tier_12["Tier 12"]
        n162{"AUS_an_improved_german_state"}
        n163["AUS_crusade_on_communism"]
        n164["AUS_meticulous_preparations"]
        n165["AUS_our_brothers_in_the_east"]
        n166["AUS_rapid_revolutions"]
    end
    subgraph tier_13["Tier 13"]
        n167["AUS_demand_liberation_of_workers"]
        n168["AUS_restoring_our_rightful_flag"]
        n169["AUS_seek_to_purchase_alaska"]
    end
    subgraph tier_14["Tier 14"]
        n170{"AUS_union_of_danubian_socialist_republics"}
    end
    subgraph tier_15["Tier 15"]
        n171["AUS_deal_with_the_german_threat"]
        n172["AUS_seize_galicia"]
        n173["AUS_the_correct_communism"]
    end
    subgraph tier_16["Tier 16"]
        n174["AUS_end_european_fascism"]
    end
    n108 --> n113
    n104 --> n113
    n64 --> n66
    n87 --> n95
    n85 --> n95
    n122 --> n131
    n127 --> n131
    n121 --> n132
    n120 --> n132
    n93 --> n96
    n158 --> n162
    n84 --> n97
    n59 --> n61
    n83 --> n84
    n62 --> n63
    n61 --> n63
    n68 --> n71
    n153 --> n156
    n67 --> n72
    n81 --> n85
    n58 --> n85
    n56 --> n85
    n88 --> n98
    n113 --> n144
    n132 --> n144
    n161 --> n163
    n113 --> n133
    n113 --> n145
    n131 --> n145
    n73 --> n78
    n170 --> n171
    n160 --> n171
    n123 --> n171
    n130 --> n171
    n83 --> n86
    n81 --> n87
    n164 --> n167
    n166 --> n167
    n105 --> n114
    n111 --> n114
    n94 --> n99
    n89 --> n99
    n109 --> n115
    n71 --> n79
    n74 --> n79
    n136 --> n146
    n171 --> n174
    n131 --> n147
    n139 --> n148
    n140 --> n149
    n139 --> n149
    n134 --> n149
    n135 --> n149
    n97 --> n116
    n112 --> n116
    n62 --> n64
    n61 --> n64
    n101 --> n117
    n114 --> n134
    n125 --> n134
    n114 --> n135
    n125 --> n135
    n79 --> n88
    n77 --> n88
    n70 --> n73
    n88 --> n100
    n96 --> n118
    n78 --> n89
    n132 --> n150
    n113 --> n150
    n93 --> n101
    n87 --> n102
    n85 --> n102
    n136 --> n151
    n118 --> n136
    n117 --> n136
    n65 --> n67
    n90 --> n103
    n81 --> n90
    n159 --> n164
    n118 --> n137
    n141 --> n152
    n160 --> n165
    n77 --> n80
    n101 --> n119
    n96 --> n119
    n108 --> n120
    n134 --> n153
    n135 --> n153
    n139 --> n153
    n140 --> n153
    n108 --> n121
    n104 --> n122
    n99 --> n123
    n91 --> n104
    n63 --> n68
    n159 --> n166
    n75 --> n81
    n72 --> n81
    n64 --> n69
    n129 --> n138
    n125 --> n138
    n114 --> n138
    n85 --> n105
    n87 --> n106
    n85 --> n106
    n61 --> n65
    n59 --> n62
    n129 --> n139
    n68 --> n74
    n90 --> n107
    n92 --> n107
    n67 --> n75
    n162 --> n168
    n79 --> n91
    n152 --> n157
    n68 --> n76
    n69 --> n76
    n66 --> n76
    n142 --> n154
    n57 --> n158
    n149 --> n158
    n91 --> n108
    n66 --> n77
    n69 --> n77
    n162 --> n169
    n170 --> n172
    n133 --> n159
    n144 --> n159
    n77 --> n82
    n81 --> n92
    n80 --> n93
    n82 --> n93
    n129 --> n140
    n92 --> n109
    n87 --> n110
    n105 --> n124
    n105 --> n125
    n111 --> n125
    n170 --> n173
    n85 --> n111
    n64 --> n70
    n65 --> n70
    n107 --> n126
    n104 --> n127
    n86 --> n112
    n77 --> n83
    n70 --> n83
    n151 --> n160
    n146 --> n160
    n126 --> n141
    n103 --> n141
    n109 --> n141
    n110 --> n128
    n110 --> n129
    n78 --> n94
    n167 --> n170
    n113 --> n142
    n101 --> n142
    n96 --> n142
    n99 --> n130
    n141 --> n161
    n123 --> n161
    n149 --> n161
    n130 --> n161
    n129 --> n143
    n125 --> n143
    n114 --> n143
    n142 --> n155
    n95 x--x n102
    n95 x--x n106
    n96 x--x n101
    n84 x--x n86
    n63 x--x n64
    n63 x--x n65
    n85 x--x n87
    n98 x--x n100
    n145 x--x n150
    n64 x--x n65
    n134 x--x n135
    n102 x--x n106
    n67 x--x n77
    n67 x--x n70
    n90 x--x n92
    n164 x--x n166
    n80 x--x n82
    n123 x--x n130
    n104 x--x n108
    n139 x--x n140
    n59 x--x n60
    n168 x--x n169
    n77 x--x n70
    n172 x--x n173
```

# AUS_secret_rearmament

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n3["AUS_preparing_the_industry"]
        n22["AUS_rebuild_the_armada"]
        n175(("AUS_secret_rearmament"))
    end
    subgraph tier_1["Tier 1"]
        n176["AUS_militarization_effort"]
    end
    subgraph tier_2["Tier 2"]
        n1{"AUS_osterreichische_bundesheer"}
        n20{"AUS_standardized_army_training"}
    end
    subgraph tier_3["Tier 3"]
        n177["AUS_establish_bohme_plan"]
        n178["AUS_follow_the_jansa_plan"]
        n179{"AUS_hirtenberger_artillery"}
        n5["AUS_osterreichische_fallschirmsjager"]
        n180["AUS_osterreichische_gebirgsjager"]
        n25["AUS_osterreichische_seebataillon"]
        n181["AUS_steyr_arms_investment"]
        n182["AUS_supporting_the_troops"]
    end
    subgraph tier_4["Tier 4"]
        n183["AUS_bring_generals_out_of_retirement"]
        n184["AUS_graf_und_stift_focus"]
        n185["AUS_improve_army_logistics"]
        n186["AUS_intensify_training_efforts"]
        n187["AUS_saurerwerke"]
        n188["AUS_the_homeland_front"]
    end
    subgraph tier_5["Tier 5"]
        n189["AUS_fortify_the_traun_line"]
        n190["AUS_heeding_the_call_of_duty"]
        n191["AUS_invite_foreign_tank_designers"]
        n192["AUS_reinforcing_the_supply_network"]
    end
    subgraph tier_6["Tier 6"]
        n193["AUS_basic_tanks"]
        n194["AUS_extend_the_traun_line"]
        n195["AUS_strengthen_the_arms_industry"]
    end
    subgraph tier_7["Tier 7"]
        n196["AUS_improved_warfare_strategies"]
    end
    n191 --> n193
    n178 --> n183
    n177 --> n183
    n1 --> n177
    n20 --> n177
    n189 --> n194
    n1 --> n178
    n20 --> n178
    n188 --> n189
    n179 --> n184
    n186 --> n190
    n20 --> n179
    n181 --> n185
    n182 --> n185
    n195 --> n196
    n177 --> n186
    n184 --> n191
    n187 --> n191
    n175 --> n176
    n176 --> n1
    n1 --> n5
    n3 --> n5
    n20 --> n180
    n1 --> n180
    n20 --> n25
    n22 --> n25
    n185 --> n192
    n179 --> n187
    n176 --> n20
    n1 --> n181
    n190 --> n195
    n188 --> n195
    n1 --> n182
    n178 --> n188
    n177 x--x n178
    n184 x--x n187
```

# AUS_totalitarian_safety

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n87{"AUS_demand_hungarian_submission"}
        n123["AUS_protector_of_the_danube"]
        n81{"AUS_rebellious_rearmament"}
        n139["AUS_renew_claims_in_italy"]
        n59["AUS_repeal_the_may_constitution"]
        n140["AUS_strike_deal_with_italy"]
        n141["AUS_the_royals_of_liechtenstein"]
        n129["AUS_tighten_control_of_subjects"]
        n60(("AUS_totalitarian_safety"))
        n130["AUS_via_danube_to_europe"]
    end
    subgraph tier_1["Tier 1"]
        n197["AUS_clamp_down_on_dnsap"]
    end
    subgraph tier_2["Tier 2"]
        n198["AUS_approach_democratic_guarantors"]
        n199["AUS_reach_out_to_italy"]
        n200["AUS_supporting_italy_in_ethiopia_focus"]
    end
    subgraph tier_3["Tier 3"]
        n201{"AUS_refine_vaterlandische_front"}
    end
    subgraph tier_4["Tier 4"]
        n202["AUS_disregard_the_treaties"]
        n203["AUS_integrate_dnsap_remnants"]
        n204["AUS_seek_agreement_for_rearmament"]
    end
    subgraph tier_5["Tier 5"]
        n56{"AUS_heimwehr_support"}
        n58{"AUS_rapid_rearmament"}
    end
    subgraph tier_6["Tier 6"]
        n85{"AUS_bring_hungary_back_into_the_fold"}
        n205["AUS_frontmiliz_focus"]
        n206{"AUS_spanish_intervention"}
    end
    subgraph tier_7["Tier 7"]
        n95["AUS_a_royal_alliance"]
        n207["AUS_demand_part_of_spanish_winnings"]
        n208["AUS_fit_for_fight"]
        n209["AUS_invite_spanish_refugees"]
        n102["AUS_join_the_axis"]
        n105["AUS_reclaiming_yugoslavian_territories"]
        n106["AUS_reforming_the_central_powers"]
        n111["AUS_the_czechoslovakian_lands"]
    end
    subgraph tier_8["Tier 8"]
        n210["AUS_consolidate_industries"]
        n114{"AUS_demand_romanian_lands"}
        n211["AUS_form_nachrichtenabteilun"]
        n124["AUS_take_albania"]
        n125{"AUS_take_back_galicia"}
        n212["AUS_wienfilm_propaganda_effort"]
    end
    subgraph tier_9["Tier 9"]
        n57["AUS_heritage_of_an_empire"]
        n134["AUS_integrate_hungary"]
        n135["AUS_integrate_northwest"]
        n138["AUS_reclaim_habsburg"]
        n213["AUS_universitat_graz"]
        n143["AUS_war_against_guarantors"]
    end
    subgraph tier_10["Tier 10"]
        n149["AUS_for_a_better_future"]
        n153["AUS_proclaim_austrian_empire"]
        n214["AUS_recruiting_the_graduates"]
    end
    subgraph tier_11["Tier 11"]
        n156["AUS_beyond_our_old_lands"]
        n158["AUS_second_brothers_war"]
        n161["AUS_war_against_bolshevism"]
    end
    subgraph tier_12["Tier 12"]
        n162{"AUS_an_improved_german_state"}
        n163["AUS_crusade_on_communism"]
    end
    subgraph tier_13["Tier 13"]
        n168["AUS_restoring_our_rightful_flag"]
        n169["AUS_seek_to_purchase_alaska"]
    end
    n87 --> n95
    n85 --> n95
    n158 --> n162
    n197 --> n198
    n153 --> n156
    n81 --> n85
    n58 --> n85
    n56 --> n85
    n60 --> n197
    n208 --> n210
    n161 --> n163
    n206 --> n207
    n105 --> n114
    n111 --> n114
    n201 --> n202
    n205 --> n208
    n140 --> n149
    n139 --> n149
    n134 --> n149
    n135 --> n149
    n208 --> n211
    n56 --> n205
    n58 --> n205
    n203 --> n56
    n211 --> n57
    n212 --> n57
    n210 --> n57
    n201 --> n203
    n114 --> n134
    n125 --> n134
    n114 --> n135
    n125 --> n135
    n206 --> n209
    n87 --> n102
    n85 --> n102
    n134 --> n153
    n135 --> n153
    n139 --> n153
    n140 --> n153
    n202 --> n58
    n204 --> n58
    n197 --> n199
    n129 --> n138
    n125 --> n138
    n114 --> n138
    n85 --> n105
    n213 --> n214
    n199 --> n201
    n198 --> n201
    n87 --> n106
    n85 --> n106
    n162 --> n168
    n57 --> n158
    n149 --> n158
    n201 --> n204
    n162 --> n169
    n58 --> n206
    n56 --> n206
    n197 --> n200
    n105 --> n124
    n105 --> n125
    n111 --> n125
    n85 --> n111
    n210 --> n213
    n212 --> n213
    n141 --> n161
    n123 --> n161
    n149 --> n161
    n130 --> n161
    n129 --> n143
    n125 --> n143
    n114 --> n143
    n208 --> n212
    n95 x--x n102
    n95 x--x n106
    n85 x--x n87
    n207 x--x n209
    n202 x--x n204
    n134 x--x n135
    n102 x--x n106
    n59 x--x n60
    n168 x--x n169
```
