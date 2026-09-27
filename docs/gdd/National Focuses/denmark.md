# DEN_collaboration_government

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"DEN_collaboration_government"}
    end
    subgraph tier_1["Tier 1"]
        n2{"DEN_align_with_overlord"}
        n3{"DEN_seek_independence"}
    end
    subgraph tier_2["Tier 2"]
        n4["DEN_align_with_foreign_powers"]
        n5["DEN_contribute_to_the_war"]
        n6["DEN_create_danforce"]
        n7["DEN_sanction_sabotages"]
        n8{"DEN_seek_industrial_investments"}
    end
    subgraph tier_3["Tier 3"]
        n9["DEN_adjust_industrial_prioritize"]
        n10["DEN_ask_for_weapons"]
        n11["DEN_claim_sweden"]
        n12["DEN_establish_danske_flotille"]
        n13["DEN_form_the_danish_freedom_council"]
        n14["DEN_intel_sharing"]
        n15["DEN_pledge_allegiance"]
        n16["DEN_rigid_training"]
        n17["DEN_secure_the_norwegian_coast"]
        n18["DEN_seize_the_production"]
        n19["DEN_strengthen_the_danish_brigades"]
    end
    subgraph tier_4["Tier 4"]
        n20["DEN_acquire_military_equipment"]
        n21["DEN_arm_the_resistance"]
        n22["DEN_buy_allied_weapons"]
        n23["DEN_buy_foreign_aircraft"]
        n24["DEN_buy_foreign_ships"]
        n25["DEN_expand_the_brigades"]
        n26["DEN_increase_cooperation"]
        n27["DEN_reclaim_atlantic_islands"]
        n28["DEN_safeguard_the_eastern_front"]
        n29["DEN_seek_military_investments"]
        n30["DEN_support_battalions"]
    end
    subgraph tier_5["Tier 5"]
        n31["DEN_escalate_the_sabotages"]
        n32["DEN_expand_the_resistance"]
        n33["DEN_petition_for_independence"]
    end
    subgraph tier_6["Tier 6"]
        n34["DEN_declare_independence"]
    end
    subgraph tier_7["Tier 7"]
        n35["DEN_secure_danish_freedom"]
    end
    n9 --> n20
    n5 --> n20
    n8 --> n9
    n3 --> n4
    n1 --> n2
    n13 --> n21
    n4 --> n10
    n14 --> n22
    n10 --> n22
    n16 --> n23
    n12 --> n24
    n5 --> n11
    n2 --> n5
    n3 --> n6
    n31 --> n34
    n32 --> n34
    n21 --> n31
    n6 --> n12
    n19 --> n25
    n21 --> n32
    n7 --> n13
    n18 --> n26
    n9 --> n26
    n4 --> n14
    n29 --> n33
    n26 --> n33
    n8 --> n15
    n17 --> n27
    n6 --> n16
    n11 --> n28
    n3 --> n7
    n2 --> n7
    n34 --> n35
    n5 --> n17
    n1 --> n3
    n2 --> n8
    n15 --> n29
    n8 --> n18
    n6 --> n19
    n19 --> n30
    n2 x--x n3
    n15 x--x n7
```

# DEN_declare_neutrality

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n36{"DEN_declare_neutrality"}
    end
    subgraph tier_1["Tier 1"]
        n37{"DEN_political_unity"}
        n38["DEN_unify_the_right"]
    end
    subgraph tier_2["Tier 2"]
        n39["DEN_conservatives_support"]
        n40["DEN_conspire_with_the_officer_corps"]
        n41["DEN_policy_of_disarmament"]
        n42["DEN_start_the_rearmament"]
    end
    subgraph tier_3["Tier 3"]
        n43["DEN_encourage_paramilitary"]
        n44["DEN_import_machinery_and_material"]
        n45["DEN_national_unity"]
        n46{"DEN_overthrow_the_government"}
        n47["DEN_social_stability"]
        n48["DEN_strengthen_the_officer_corp"]
    end
    subgraph tier_4["Tier 4"]
        n49{"DEN_build_motorveje"}
        n50["DEN_industrial_preparations"]
        n51{"DEN_king_assumes_power"}
        n52{"DEN_march_on_the_capital"}
        n53["DEN_modernize_agricultural_machinery"]
        n54["DEN_modernize_industrial_machinery"]
    end
    subgraph tier_5["Tier 5"]
        n55["DEN_agricultural_reinvestments"]
        n56["DEN_align_industries"]
        n57["DEN_ask_for_support"]
        n58{"DEN_civilian_preparations"}
        n59{"DEN_heavy_market_regulations"}
        n60["DEN_increase_industrial_production"]
        n61["DEN_industrial_reinvestments"]
        n62["DEN_konge_og_faedreland"]
        n63["DEN_limited_market_regulations"]
        n64{"DEN_military_preparations"}
        n65["DEN_no_market_regulations"]
        n66["DEN_research_and_development"]
        n67["DEN_scandinavian_security"]
        n68{"DEN_seek_protection"}
        n69["DEN_seize_power"]
    end
    subgraph tier_6["Tier 6"]
        n70["DEN_dano_german_military_cooperation"]
        n71["DEN_denmark_first"]
        n72["DEN_economic_mobilization_strategy"]
        n73["DEN_expand_kobenhavns_university"]
        n74["DEN_full_social_mobilization"]
        n75{"DEN_increase_maritime_trade"}
        n76{"DEN_increase_produce_production"}
        n77{"DEN_north_sea_oil_drilling"}
        n78["DEN_rally_the_nation"]
        n79["DEN_secure_swedish_steel"]
        n80["DEN_sign_non_aggression_deal"]
        n81["DEN_strength_in_numbers"]
        n82["DEN_the_royal_guard"]
        n83{"DEN_welcome_foreign_scientists"}
    end
    subgraph tier_7["Tier 7"]
        n84{"DEN_assault_troops"}
        n85{"DEN_experimental_technology"}
        n86["DEN_finish_off_finland"]
        n87["DEN_full_employment"]
        n88{"DEN_institute_corporatism"}
        n89["DEN_joint_military_drills"]
        n90["DEN_military_cooperation_program"]
        n91["DEN_reclaim_norway"]
        n92["DEN_reintegrate_iceland"]
        n93["DEN_science_pact"]
        n94{"DEN_side_with_industry"}
        n95{"DEN_side_with_unions"}
        n96["DEN_sign_a_trade_deal"]
        n97["DEN_sway_the_nordics"]
        n98{"DEN_swedish_steel_production"}
    end
    subgraph tier_8["Tier 8"]
        n99["DEN_develop_iceland"]
        n100["DEN_five_year_plan"]
        n101["DEN_limited_social_mobilization"]
        n102["DEN_nordic_security"]
        n103["DEN_offer_protection"]
        n104{"DEN_pan_scandinavianism"}
        n105["DEN_prioritize_army"]
        n106["DEN_prioritize_navy"]
        n107["DEN_territory_for_protection"]
        n108["DEN_train_mountain_infantry"]
    end
    subgraph tier_9["Tier 9"]
        n109["DEN_avenging_1864"]
        n110["DEN_dominium_maris_baltici"]
        n111{"DEN_military_might"}
        n112["DEN_total_war"]
    end
    subgraph tier_10["Tier 10"]
        n113["DEN_establish_the_danelaw"]
    end
    n53 --> n55
    n51 --> n56
    n52 --> n57
    n78 --> n84
    n104 --> n109
    n98 --> n109
    n47 --> n49
    n50 --> n58
    n38 --> n39
    n38 --> n40
    n57 --> n70
    n69 --> n71
    n92 --> n99
    n104 --> n110
    n62 --> n72
    n56 --> n72
    n39 --> n43
    n40 --> n43
    n104 --> n113
    n111 --> n113
    n56 --> n73
    n78 --> n85
    n79 --> n86
    n59 --> n100
    n95 --> n100
    n94 --> n100
    n76 --> n87
    n75 --> n87
    n77 --> n87
    n58 --> n74
    n64 --> n74
    n49 --> n59
    n41 --> n44
    n54 --> n60
    n60 --> n75
    n55 --> n76
    n45 --> n50
    n53 --> n61
    n78 --> n88
    n81 --> n89
    n46 --> n51
    n51 --> n62
    n49 --> n63
    n95 --> n101
    n94 --> n101
    n46 --> n52
    n81 --> n90
    n106 --> n111
    n105 --> n111
    n91 --> n111
    n50 --> n64
    n44 --> n53
    n44 --> n54
    n42 --> n45
    n49 --> n65
    n90 --> n102
    n89 --> n102
    n66 --> n77
    n61 --> n77
    n97 --> n103
    n39 --> n46
    n40 --> n46
    n79 --> n104
    n91 --> n104
    n37 --> n41
    n36 --> n37
    n88 --> n105
    n85 --> n105
    n84 --> n105
    n88 --> n106
    n85 --> n106
    n84 --> n106
    n69 --> n78
    n57 --> n78
    n67 --> n91
    n78 --> n91
    n67 --> n92
    n78 --> n92
    n54 --> n66
    n51 --> n67
    n80 --> n93
    n67 --> n79
    n45 --> n68
    n51 --> n68
    n52 --> n69
    n83 --> n94
    n83 --> n95
    n80 --> n96
    n68 --> n80
    n41 --> n47
    n42 --> n47
    n37 --> n42
    n68 --> n81
    n39 --> n48
    n40 --> n48
    n67 --> n97
    n78 --> n97
    n79 --> n98
    n96 --> n107
    n93 --> n107
    n62 --> n82
    n106 --> n112
    n105 --> n112
    n91 --> n108
    n36 --> n38
    n59 --> n83
    n63 --> n83
    n65 --> n83
    n57 x--x n69
    n109 x--x n110
    n110 x--x n113
    n100 x--x n87
    n100 x--x n74
    n100 x--x n101
    n87 x--x n74
    n87 x--x n101
    n74 x--x n101
    n59 x--x n63
    n59 x--x n65
    n51 x--x n52
    n63 x--x n65
    n41 x--x n42
    n37 x--x n38
    n105 x--x n106
    n67 x--x n81
    n94 x--x n95
```

# DEN_fortify_our_borders

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n114(("DEN_fortify_our_borders"))
        n115["DEN_kanslergadeforliget"]
        n116["DEN_public_works"]
    end
    subgraph tier_1["Tier 1"]
        n117["DEN_build_a_modern_dannevirke"]
        n118["DEN_devalue_the_krone"]
        n119["DEN_refortify_tunestillingen"]
    end
    subgraph tier_2["Tier 2"]
        n120["DEN_fortify_the_islands"]
        n121["DEN_secure_our_supply_lines"]
        n122["DEN_trade_with_britain"]
        n123["DEN_trade_with_germany"]
    end
    subgraph tier_3["Tier 3"]
        n124["DEN_connect_the_islands"]
    end
    subgraph tier_4["Tier 4"]
        n125["DEN_develop_greenland"]
        n126["DEN_expand_institut_for_teoretisk_fysik"]
        n127["DEN_reorient_production_lines"]
    end
    subgraph tier_5["Tier 5"]
        n128["DEN_aalborg_portland_cement_plant"]
        n129["DEN_danske_stalvalsevaerket"]
        n130["DEN_expand_the_industries"]
        n131["DEN_expand_the_ivittuut_mine"]
        n132["DEN_prospecting_new_sites"]
        n133["DEN_strengthen_military_industries"]
    end
    subgraph tier_6["Tier 6"]
        n134["DEN_protect_bornholm"]
        n135["DEN_protect_greenland"]
        n136["DEN_protect_the_faroe_islands"]
        n137["DEN_support_bornholms_industries"]
        n138["DEN_support_the_faroes_industries"]
    end
    n126 --> n128
    n114 --> n117
    n116 --> n124
    n120 --> n124
    n127 --> n129
    n115 --> n118
    n114 --> n118
    n124 --> n125
    n124 --> n126
    n126 --> n130
    n125 --> n131
    n117 --> n120
    n119 --> n120
    n125 --> n132
    n129 --> n134
    n133 --> n134
    n132 --> n135
    n131 --> n135
    n129 --> n136
    n133 --> n136
    n114 --> n119
    n124 --> n127
    n119 --> n121
    n127 --> n133
    n130 --> n137
    n128 --> n137
    n130 --> n138
    n128 --> n138
    n118 --> n122
    n118 --> n123
    n114 x--x n115
```

# DEN_kanslergadeforliget

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n114["DEN_fortify_our_borders"]
        n120["DEN_fortify_the_islands"]
        n115(("DEN_kanslergadeforliget"))
    end
    subgraph tier_1["Tier 1"]
        n139["DEN_agricultural_subsidies"]
        n118["DEN_devalue_the_krone"]
        n140["DEN_industrial_investments"]
    end
    subgraph tier_2["Tier 2"]
        n116["DEN_public_works"]
        n141["DEN_support_schleswigian_farmers"]
        n122["DEN_trade_with_britain"]
        n123["DEN_trade_with_germany"]
    end
    subgraph tier_3["Tier 3"]
        n124["DEN_connect_the_islands"]
    end
    subgraph tier_4["Tier 4"]
        n125["DEN_develop_greenland"]
        n126["DEN_expand_institut_for_teoretisk_fysik"]
        n127["DEN_reorient_production_lines"]
    end
    subgraph tier_5["Tier 5"]
        n128["DEN_aalborg_portland_cement_plant"]
        n129["DEN_danske_stalvalsevaerket"]
        n130["DEN_expand_the_industries"]
        n131["DEN_expand_the_ivittuut_mine"]
        n132["DEN_prospecting_new_sites"]
        n133["DEN_strengthen_military_industries"]
    end
    subgraph tier_6["Tier 6"]
        n134["DEN_protect_bornholm"]
        n135["DEN_protect_greenland"]
        n136["DEN_protect_the_faroe_islands"]
        n137["DEN_support_bornholms_industries"]
        n138["DEN_support_the_faroes_industries"]
    end
    n126 --> n128
    n115 --> n139
    n116 --> n124
    n120 --> n124
    n127 --> n129
    n115 --> n118
    n114 --> n118
    n124 --> n125
    n124 --> n126
    n126 --> n130
    n125 --> n131
    n115 --> n140
    n125 --> n132
    n129 --> n134
    n133 --> n134
    n132 --> n135
    n131 --> n135
    n129 --> n136
    n133 --> n136
    n139 --> n116
    n140 --> n116
    n124 --> n127
    n127 --> n133
    n130 --> n137
    n128 --> n137
    n139 --> n141
    n130 --> n138
    n128 --> n138
    n118 --> n122
    n118 --> n123
    n114 x--x n115
```

# DEN_sign_forsvarsforliget

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n142(("DEN_sign_forsvarsforliget"))
    end
    subgraph tier_1["Tier 1"]
        n143{"DEN_expand_vaernepligten"}
        n144["DEN_sikkerhedspolitiet"]
        n145["DEN_stockpile_oil"]
    end
    subgraph tier_2["Tier 2"]
        n146["DEN_domestic_designs"]
        n147{"DEN_expand_ubadsvabnet"}
        n148["DEN_foreign_designs"]
        n149["DEN_haeren_reorganization"]
    end
    subgraph tier_3["Tier 3"]
        n150["DEN_expand_dansk_industri_syndikat"]
        n151["DEN_expand_haerens_tekniske_korps"]
        n152["DEN_hjemmevaernet"]
        n153["DEN_modernize_the_navy"]
        n154["DEN_refit_civilian_ships"]
        n155["DEN_unify_flyvevabnet"]
    end
    subgraph tier_4["Tier 4"]
        n156{"DEN_appropriate_odense_staalskibsvaerft"}
        n157["DEN_convert_automobile_production"]
        n158["DEN_flyveskolen"]
        n159["DEN_new_artillery_tactics"]
        n160{"DEN_restructuring_sovaernet"}
        n161{"DEN_sovaernets_operative_kommando"}
    end
    subgraph tier_5["Tier 5"]
        n162{"DEN_air_force_power_projection"}
        n163["DEN_baltic_sea_domination"]
        n164["DEN_establish_domestic_tank_manufacturing"]
        n165{"DEN_flyvertaktisk_kommando"}
        n166["DEN_generalkommandoen"]
        n167["DEN_north_sea_ambitions"]
        n168["DEN_slaedepatruljen_sirius"]
    end
    subgraph tier_6["Tier 6"]
        n169["DEN_bombefly"]
        n170["DEN_fromandskorpset"]
        n171["DEN_jagerfly"]
        n172["DEN_luftstotte"]
        n173["DEN_naval_power_projection"]
        n174["DEN_torpedofly"]
    end
    subgraph tier_7["Tier 7"]
        n175["DEN_advanced_flight"]
    end
    n171 --> n175
    n172 --> n175
    n169 --> n175
    n158 --> n162
    n154 --> n156
    n153 --> n156
    n161 --> n163
    n160 --> n163
    n156 --> n163
    n165 --> n169
    n162 --> n169
    n150 --> n157
    n151 --> n157
    n143 --> n146
    n157 --> n164
    n149 --> n150
    n149 --> n151
    n143 --> n147
    n142 --> n143
    n158 --> n165
    n155 --> n158
    n143 --> n148
    n163 --> n170
    n166 --> n170
    n159 --> n166
    n157 --> n166
    n143 --> n149
    n149 --> n152
    n165 --> n171
    n162 --> n171
    n165 --> n172
    n162 --> n172
    n147 --> n153
    n163 --> n173
    n167 --> n173
    n151 --> n159
    n161 --> n167
    n160 --> n167
    n156 --> n167
    n147 --> n154
    n154 --> n160
    n153 --> n160
    n142 --> n144
    n159 --> n168
    n157 --> n168
    n154 --> n161
    n153 --> n161
    n142 --> n145
    n165 --> n174
    n162 --> n174
    n167 --> n174
    n146 --> n155
    n148 --> n155
    n163 x--x n167
    n169 x--x n171
    n169 x--x n172
    n146 x--x n148
    n171 x--x n172
    n153 x--x n154
```
