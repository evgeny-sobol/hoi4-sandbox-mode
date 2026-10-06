# FRA_air_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"FRA_air_focus"}
    end
    subgraph tier_1["Tier 1"]
        n2["FRA_bomber_focus"]
        n3["FRA_fighter_focus"]
    end
    subgraph tier_2["Tier 2"]
        n4["FRA_air_doctrine"]
        n5["FRA_heavy_bomber_focus"]
        n6["FRA_heavy_fighter_focus"]
        n7["FRA_naval_bomber_focus"]
    end
    n3 --> n4
    n2 --> n4
    n1 --> n2
    n1 --> n3
    n2 --> n5
    n3 --> n6
    n2 --> n7
    n2 x--x n3
```

# FRA_begin_rearmament

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n8{"FRA_begin_rearmament"}
    end
    subgraph tier_1["Tier 1"]
        n9{"FRA_aggressive_focus"}
        n10{"FRA_defensive_focus"}
    end
    subgraph tier_2["Tier 2"]
        n11["FRA_air_dominance"]
        n12["FRA_battle_of_maneuver"]
        n13["FRA_firepower_kills"]
        n14["FRA_infantry_tanks"]
        n15["FRA_methodical_battle"]
    end
    subgraph tier_3["Tier 3"]
        n16["FRA_cas_focus"]
        n17["FRA_fortification_focus"]
        n18["FRA_infantry_focus"]
        n19["FRA_motorized_focus"]
        n20["FRA_special_forces"]
    end
    subgraph tier_4["Tier 4"]
        n21["FRA_air_ground_cooperation"]
        n22["FRA_alpine_forts"]
        n23["FRA_artillery_focus"]
        n24["FRA_fusiliers_marine"]
        n25["FRA_mechanized_focus"]
    end
    subgraph tier_5["Tier 5"]
        n26["FRA_extend_the_maginot_line"]
        n27["FRA_flying_artillery"]
        n28["FRA_heavy_armor_focus"]
        n29["FRA_light_medium_armor"]
    end
    subgraph tier_6["Tier 6"]
        n30["FRA_army_reform"]
        n31["FRA_division_cuirassee"]
    end
    n8 --> n9
    n9 --> n11
    n16 --> n21
    n17 --> n22
    n29 --> n30
    n28 --> n30
    n26 --> n30
    n27 --> n30
    n18 --> n23
    n9 --> n12
    n11 --> n16
    n8 --> n10
    n28 --> n31
    n22 --> n26
    n10 --> n13
    n21 --> n27
    n15 --> n17
    n20 --> n24
    n23 --> n28
    n13 --> n18
    n10 --> n14
    n9 --> n14
    n25 --> n29
    n19 --> n25
    n10 --> n15
    n12 --> n19
    n14 --> n20
    n9 x--x n10
    n11 x--x n12
    n13 x--x n15
```

# FRA_devalue_the_franc

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n32(("FRA_devalue_the_franc"))
    end
    subgraph tier_1["Tier 1"]
        n33["FRA_autoroutes"]
        n34["FRA_invest_in_the_colonies"]
        n35["FRA_invest_in_the_metropole"]
    end
    subgraph tier_2["Tier 2"]
        n36["FRA_algerie_france"]
        n37["FRA_invest_in_indochina"]
        n38["FRA_invest_in_syria"]
        n39["FRA_invest_in_west_africa"]
        n40["FRA_metropolitan_france"]
    end
    subgraph tier_3["Tier 3"]
        n41["FRA_colonial_industry"]
        n42["FRA_industrial_expansion"]
    end
    subgraph tier_4["Tier 4"]
        n43["FRA_extra_research_slot"]
        n44["FRA_extra_research_slot_2"]
        n45["FRA_global_integration"]
        n46["FRA_military_factories"]
    end
    n35 --> n36
    n34 --> n36
    n32 --> n33
    n36 --> n41
    n39 --> n41
    n37 --> n41
    n38 --> n41
    n42 --> n43
    n41 --> n44
    n41 --> n45
    n40 --> n42
    n36 --> n42
    n34 --> n37
    n34 --> n38
    n32 --> n34
    n32 --> n35
    n34 --> n39
    n35 --> n40
    n42 --> n46
    n41 --> n46
```

# FRA_form_the_popular_front

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n47(("FRA_form_the_popular_front"))
        n48["FRA_protect_the_rights_of_man"]
        n49["FRA_revive_the_national_bloc"]
    end
    subgraph tier_1["Tier 1"]
        n50["FRA_ban_the_leagues"]
        n51["FRA_intervention_in_spain"]
        n52["FRA_invite_communist_ministers"]
        n53["FRA_leftist_rhetoric"]
        n54["FRA_reform_the_labour_laws"]
    end
    subgraph tier_2["Tier 2"]
        n55{"FRA_national_mobilization"}
        n56["FRA_nationalize_key_industry"]
        n57{"FRA_review_foreign_policy"}
        n58["FRA_strengthen_the_unions"]
        n59["FRA_the_blum_viollette_proposal"]
        n60["FRA_womens_suffrage"]
    end
    subgraph tier_3["Tier 3"]
        n61{"FRA_buy_time"}
        n62["FRA_celebrate_the_commune"]
        n63["FRA_confirm_eastern_commitments"]
        n64{"FRA_expand_the_citizenship"}
        n65["FRA_form_the_state_arsenals"]
        n66["FRA_humanite_unie"]
        n67["FRA_industrial_collectivization"]
        n68["FRA_join_comintern"]
        n69["FRA_legal_equality"]
        n70["FRA_reorganize_the_aviation_industry"]
        n71["FRA_support_the_finns"]
    end
    subgraph tier_4["Tier 4"]
        n72["FRA_agricultural_collectivization"]
        n73["FRA_encourage_immigration"]
        n74{"FRA_force_the_issue"}
        n75["FRA_france_leads"]
        n76["FRA_france_undividable"]
        n77["FRA_general_work_council"]
        n78["FRA_go_with_britain"]
        n79["FRA_revive_the_franco_polish_alliance"]
        n80["FRA_strengthen_the_little_entente"]
    end
    subgraph tier_5["Tier 5"]
        n81["FRA_arms_purchases_in_the_us"]
        n82["FRA_concessions_to_italy"]
        n83["FRA_dirigisme"]
        n84["FRA_foreign_guest_workers"]
        n85["FRA_franco_soviet_treaty"]
        n86["FRA_french_union"]
        n87["FRA_invite_yugoslavia"]
        n88["FRA_join_the_ententes"]
        n89["FRA_national_champions"]
        n90["FRA_reconciliation"]
        n91["FRA_revolution_to_the_utmost"]
        n92["FRA_strengthen_government_support"]
    end
    subgraph tier_6["Tier 6"]
        n93{"FRA_constitutional_convention"}
        n94["FRA_defensive_strategems"]
        n95{"FRA_destroy_the_counter_revolution"}
        n96["FRA_invite_romania"]
        n97["FRA_ratify_the_stresa_front"]
    end
    subgraph tier_7["Tier 7"]
        n98["FRA_anti_fascist_coalition"]
        n99["FRA_invest_in_our_weaker_allies"]
        n100["FRA_loyalty_to_moscow"]
        n101["FRA_loyalty_to_the_cause"]
        n102["FRA_revolutionary_zeal"]
    end
    subgraph tier_8["Tier 8"]
        n103["FRA_carry_the_revolution_north"]
        n104["FRA_coordinate_rearmament"]
        n105["FRA_invite_anti_fascist_emigrants"]
        n106["FRA_league_of_french_bolshevist_volunteers"]
    end
    subgraph tier_9["Tier 9"]
        n107["FRA_carry_the_revolution_east"]
        n108["FRA_carry_the_revolution_west"]
        n109["FRA_host_the_german_exiles"]
        n110["FRA_reconnect_to_the_balkans"]
    end
    subgraph tier_10["Tier 10"]
        n111["FRA_carry_the_revolution_south"]
        n112["FRA_pre_empt_the_fascist_attack"]
    end
    subgraph tier_11["Tier 11"]
        n113["FRA_egalite_liberte_solidarite"]
    end
    n67 --> n72
    n93 --> n98
    n78 --> n81
    n47 --> n50
    n57 --> n61
    n103 --> n107
    n101 --> n103
    n108 --> n111
    n107 --> n111
    n103 --> n108
    n58 --> n62
    n75 --> n82
    n57 --> n63
    n90 --> n93
    n99 --> n104
    n92 --> n94
    n91 --> n95
    n77 --> n83
    n111 --> n113
    n64 --> n73
    n59 --> n64
    n62 --> n74
    n69 --> n74
    n80 --> n84
    n56 --> n65
    n61 --> n75
    n64 --> n76
    n75 --> n85
    n76 --> n86
    n70 --> n77
    n65 --> n77
    n61 --> n78
    n106 --> n109
    n55 --> n66
    n60 --> n67
    n58 --> n67
    n47 --> n51
    n49 --> n51
    n96 --> n99
    n98 --> n105
    n47 --> n52
    n87 --> n96
    n80 --> n87
    n55 --> n68
    n80 --> n88
    n100 --> n106
    n47 --> n53
    n60 --> n69
    n93 --> n100
    n95 --> n100
    n95 --> n101
    n77 --> n89
    n53 --> n55
    n54 --> n56
    n110 --> n112
    n109 --> n112
    n82 --> n97
    n74 --> n90
    n105 --> n110
    n47 --> n54
    n56 --> n70
    n54 --> n57
    n48 --> n57
    n63 --> n79
    n74 --> n91
    n95 --> n102
    n80 --> n92
    n61 --> n92
    n63 --> n80
    n52 --> n58
    n57 --> n71
    n54 --> n59
    n48 --> n59
    n52 --> n60
    n98 x--x n100
    n98 x--x n101
    n61 x--x n63
    n73 x--x n76
    n47 x--x n49
    n75 x--x n78
    n66 x--x n68
    n100 x--x n101
    n90 x--x n91
```

# FRA_naval_rearmament

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n114{"FRA_naval_rearmament"}
    end
    subgraph tier_1["Tier 1"]
        n115["FRA_colonial_naval_bases"]
        n116{"FRA_the_old_school"}
        n117["FRA_the_young_school"]
    end
    subgraph tier_2["Tier 2"]
        n118["FRA_capital_ship_focus"]
        n119["FRA_carrier_focus"]
        n120["FRA_develop_colonial_dockyards"]
        n121["FRA_surface_combat"]
        n122["FRA_undersea_combat"]
    end
    subgraph tier_3["Tier 3"]
        n123["FRA_carrier_planes"]
        n124["FRA_improved_screen_ships"]
        n125["FRA_prioritize_the_joffre"]
        n126["FRA_rush_the_richelieus"]
    end
    subgraph tier_4["Tier 4"]
        n127["FRA_naval_doctrine"]
    end
    n116 --> n118
    n116 --> n119
    n119 --> n123
    n114 --> n115
    n115 --> n120
    n121 --> n124
    n122 --> n124
    n125 --> n127
    n126 --> n127
    n124 --> n127
    n119 --> n125
    n118 --> n126
    n117 --> n121
    n114 --> n116
    n114 --> n117
    n117 --> n122
    n118 x--x n119
    n116 x--x n117
```

# FRA_revive_the_national_bloc

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n47["FRA_form_the_popular_front"]
        n54["FRA_reform_the_labour_laws"]
        n49{"FRA_revive_the_national_bloc"}
    end
    subgraph tier_1["Tier 1"]
        n128["FRA_agricultural_protectionism"]
        n129["FRA_ban_communism"]
        n51["FRA_intervention_in_spain"]
        n130["FRA_laissez_faire"]
        n131["FRA_right_wing_rhetoric"]
        n132{"FRA_utilize_the_leagues"}
    end
    subgraph tier_2["Tier 2"]
        n133{"FRA_army_of_aggression"}
        n134["FRA_economic_devolution"]
        n135["FRA_national_regeneration"]
        n48["FRA_protect_the_rights_of_man"]
        n136["FRA_the_council_of_rambouillet"]
    end
    subgraph tier_3["Tier 3"]
        n137["FRA_destroy_decadence"]
        n138{"FRA_diplomatic_freedom"}
        n139["FRA_france_first"]
        n140["FRA_freedom_front"]
        n141{"FRA_integralism"}
        n142["FRA_join_germany"]
        n143["FRA_political_unity"]
        n144["FRA_promote_entrepeneurship"]
        n57{"FRA_review_foreign_policy"}
        n145["FRA_revise_the_constitution"]
        n59["FRA_the_blum_viollette_proposal"]
        n146["FRA_woo_italy"]
    end
    subgraph tier_4["Tier 4"]
        n61{"FRA_buy_time"}
        n63["FRA_confirm_eastern_commitments"]
        n147["FRA_dismantle_the_democracies"]
        n64{"FRA_expand_the_citizenship"}
        n148["FRA_family"]
        n149["FRA_fatherland"]
        n150["FRA_latin_entente"]
        n151{"FRA_repeal_the_law_of_exile"}
        n152["FRA_stimulate_the_dynamic_market"]
        n71["FRA_support_the_finns"]
        n153["FRA_towards_a_new_europe"]
        n154["FRA_work"]
    end
    subgraph tier_5["Tier 5"]
        n155["FRA_compensate_italy"]
        n73["FRA_encourage_immigration"]
        n156{"FRA_establish_spheres_of_influence"}
        n75["FRA_france_leads"]
        n76["FRA_france_undividable"]
        n78["FRA_go_with_britain"]
        n157["FRA_orleanist_restoration"]
        n158["FRA_proclaim_the_third_empire"]
        n159["FRA_reach_out_to_spain"]
        n79["FRA_revive_the_franco_polish_alliance"]
        n80["FRA_strengthen_the_little_entente"]
        n160["FRA_the_legitimate_heir"]
    end
    subgraph tier_6["Tier 6"]
        n161["FRA_align_belgium"]
        n81["FRA_arms_purchases_in_the_us"]
        n162["FRA_avenge_waterloo"]
        n82["FRA_concessions_to_italy"]
        n84["FRA_foreign_guest_workers"]
        n85["FRA_franco_soviet_treaty"]
        n86["FRA_french_union"]
        n163["FRA_guarantee_the_constitution"]
        n164["FRA_intervention_in_greece"]
        n165["FRA_invite_portugal"]
        n87["FRA_invite_yugoslavia"]
        n88["FRA_join_the_ententes"]
        n166{"FRA_secure_the_crown_of_spain"}
        n167["FRA_split_belgium"]
        n92["FRA_strengthen_government_support"]
        n168["FRA_the_first_citizen_of_the_state"]
    end
    subgraph tier_7["Tier 7"]
        n169["FRA_counter_action"]
        n94["FRA_defensive_strategems"]
        n170["FRA_grow_the_empire"]
        n96["FRA_invite_romania"]
        n97["FRA_ratify_the_stresa_front"]
        n171["FRA_reorganize_the_dutch"]
        n172["FRA_retribution_for_sedan"]
        n173["FRA_the_congress_of_paris"]
        n174["FRA_two_countries_two_crowns"]
        n175["FRA_unite_the_crowns"]
    end
    subgraph tier_8["Tier 8"]
        n176["FRA_bring_home_quebec"]
        n177["FRA_disunite_germany"]
        n178["FRA_expand_to_the_suez"]
        n99["FRA_invest_in_our_weaker_allies"]
        n179["FRA_no_further_humiliations"]
        n180["FRA_return_to_borodino"]
        n181["FRA_slum_clearing"]
        n182["FRA_the_natural_borders_of_france"]
    end
    subgraph tier_9["Tier 9"]
        n104["FRA_coordinate_rearmament"]
        n183["FRA_dominate_the_middle_east"]
        n184["FRA_je_suis_la_deluge"]
        n185["FRA_public_welfare"]
    end
    n49 --> n128
    n156 --> n161
    n78 --> n81
    n131 --> n133
    n158 --> n162
    n49 --> n129
    n170 --> n176
    n57 --> n61
    n150 --> n155
    n75 --> n82
    n57 --> n63
    n99 --> n104
    n163 --> n169
    n168 --> n169
    n92 --> n94
    n135 --> n137
    n135 --> n138
    n146 --> n147
    n172 --> n177
    n178 --> n183
    n128 --> n134
    n130 --> n134
    n64 --> n73
    n153 --> n156
    n59 --> n64
    n164 --> n178
    n170 --> n178
    n141 --> n148
    n141 --> n149
    n80 --> n84
    n133 --> n139
    n61 --> n75
    n64 --> n76
    n75 --> n85
    n48 --> n140
    n76 --> n86
    n61 --> n78
    n167 --> n170
    n161 --> n170
    n157 --> n163
    n135 --> n141
    n155 --> n164
    n47 --> n51
    n49 --> n51
    n96 --> n99
    n159 --> n165
    n87 --> n96
    n80 --> n87
    n180 --> n184
    n133 --> n142
    n80 --> n88
    n49 --> n130
    n138 --> n150
    n132 --> n135
    n169 --> n179
    n151 --> n157
    n135 --> n143
    n151 --> n158
    n134 --> n144
    n130 --> n48
    n128 --> n48
    n181 --> n185
    n82 --> n97
    n150 --> n159
    n162 --> n171
    n145 --> n151
    n162 --> n172
    n172 --> n180
    n54 --> n57
    n48 --> n57
    n136 --> n145
    n63 --> n79
    n49 --> n131
    n160 --> n166
    n169 --> n181
    n156 --> n167
    n140 --> n152
    n144 --> n152
    n80 --> n92
    n61 --> n92
    n63 --> n80
    n57 --> n71
    n54 --> n59
    n48 --> n59
    n165 --> n173
    n164 --> n173
    n132 --> n136
    n157 --> n168
    n151 --> n160
    n173 --> n182
    n138 --> n153
    n166 --> n174
    n166 --> n175
    n49 --> n132
    n133 --> n146
    n141 --> n154
    n128 x--x n130
    n161 x--x n167
    n61 x--x n63
    n73 x--x n76
    n148 x--x n149
    n148 x--x n154
    n149 x--x n154
    n47 x--x n49
    n139 x--x n142
    n139 x--x n146
    n75 x--x n78
    n142 x--x n146
    n150 x--x n153
    n135 x--x n136
    n157 x--x n158
    n157 x--x n160
    n158 x--x n160
    n174 x--x n175
```
