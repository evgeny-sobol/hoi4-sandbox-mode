# ENG_a_change_in_course

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"ENG_a_change_in_course"}
        n2["ENG_steady_as_she_goes"]
    end
    subgraph tier_1["Tier 1"]
        n3["ENG_concessions_to_the_trade_unions"]
        n4["ENG_organize_the_blackshirts"]
        n5["ENG_the_kings_party"]
    end
    subgraph tier_2["Tier 2"]
        n6["ENG_eliminate_the_upper_class"]
        n7["ENG_god_save_the_king"]
        n8["ENG_move_to_secure_the_dominions"]
        n9["ENG_reassess_continental_commitments"]
        n10["ENG_the_british_path_to_fascism"]
        n11["ENG_the_fate_of_the_royal_family"]
    end
    subgraph tier_3["Tier 3"]
        n12["ENG_appeal_to_imperial_loyalists"]
        n13["ENG_ceylon_forward_operating_base"]
        n14["ENG_consolidate_the_british_isles"]
        n15["ENG_enact_the_mosley_manifesto"]
        n16{"ENG_for_the_good_of_the_revolution"}
        n17{"ENG_isolate_the_mediterranean_threat"}
        n18{"ENG_secure_the_italian_alliance"}
    end
    subgraph tier_4["Tier 4"]
        n19["ENG_alliance_with_germany"]
        n20["ENG_bring_the_dominions_back_into_the_fold"]
        n21{"ENG_follow_moscow"}
        n22["ENG_gibraltar_for_spanish_support"]
        n23["ENG_imperial_conscription"]
        n24["ENG_noninterference_treaty_with_germany"]
        n25["ENG_pre_empt_spanish_alignment"]
        n26{"ENG_the_british_communist_alternative"}
    end
    subgraph tier_5["Tier 5"]
        n27{"ENG_enforce_decolonization"}
        n28["ENG_pre_empt_the_strategic_threat"]
        n29["ENG_prevent_a_continental_hegemony"]
        n30{"ENG_reach_out_across_the_channel"}
        n31["ENG_reclaim_burma"]
        n32["ENG_reclaim_the_jewel_in_the_crown"]
        n33["ENG_socialist_science_pool"]
        n34["ENG_tackle_capitalism"]
        n35["ENG_tackle_fascism"]
        n36["ENG_take_out_the_regia_marina"]
        n37["ENG_the_sun_never_sets"]
        n38["ENG_unite_the_anglosphere"]
    end
    subgraph tier_6["Tier 6"]
        n39["ENG_bermuda_invasion_launch_point"]
        n40["ENG_pre_empt_the_ideological_threat"]
        n41["ENG_preparing_the_second_front"]
        n42["ENG_soviet_cooperation"]
        n43["ENG_the_one_true_revolution"]
    end
    subgraph tier_7["Tier 7"]
        n44["ENG_crush_the_dream"]
        n45["ENG_expose_the_belly_of_the_bear"]
        n46["ENG_liberate_the_home_of_marx"]
    end
    subgraph tier_8["Tier 8"]
        n47["ENG_spirit_of_the_industrial_revolution"]
    end
    n17 --> n19
    n7 --> n12
    n34 --> n39
    n12 --> n20
    n7 --> n13
    n1 --> n3
    n7 --> n14
    n39 --> n44
    n3 --> n6
    n10 --> n15
    n26 --> n27
    n40 --> n45
    n16 --> n21
    n11 --> n16
    n6 --> n16
    n18 --> n22
    n5 --> n7
    n4 --> n7
    n13 --> n23
    n9 --> n17
    n43 --> n46
    n41 --> n46
    n4 --> n8
    n3 --> n8
    n17 --> n24
    n1 --> n4
    n18 --> n25
    n23 --> n40
    n36 --> n40
    n20 --> n28
    n35 --> n41
    n22 --> n29
    n25 --> n29
    n26 --> n30
    n5 --> n9
    n23 --> n31
    n23 --> n32
    n10 --> n18
    n21 --> n33
    n27 --> n42
    n30 --> n42
    n42 --> n47
    n46 --> n47
    n44 --> n47
    n21 --> n34
    n21 --> n35
    n24 --> n36
    n19 --> n36
    n16 --> n26
    n4 --> n10
    n3 --> n11
    n1 --> n5
    n27 --> n43
    n30 --> n43
    n20 --> n37
    n23 --> n38
    n20 --> n38
    n1 x--x n2
    n19 x--x n24
    n3 x--x n4
    n3 x--x n5
    n27 x--x n30
    n21 x--x n26
    n22 x--x n25
    n4 x--x n5
    n42 x--x n43
    n34 x--x n35
```

# ENG_revisit_colonial_policy

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n48(("ENG_revisit_colonial_policy"))
        n49["uk_empire_focus"]
    end
    subgraph tier_1["Tier 1"]
        n50["ENG_guide_the_colonies"]
    end
    subgraph tier_2["Tier 2"]
        n51["ENG_towards_dominion_independence"]
        n52["ENG_withdraw_from_contested_territories"]
    end
    subgraph tier_3["Tier 3"]
        n53["ENG_foundations_for_an_indian_state"]
        n54["ENG_self_government_for_the_mediterranean"]
        n55["ENG_self_government_for_the_middle_east"]
    end
    subgraph tier_4["Tier 4"]
        n56["ENG_self_government_for_africa"]
        n57["ENG_self_government_for_the_americas"]
        n58["ENG_the_three_nation_solution"]
        n59["ENG_towards_indian_independence"]
    end
    subgraph tier_5["Tier 5"]
        n60["ENG_self_government_for_asia"]
    end
    subgraph tier_6["Tier 6"]
        n61["ENG_decolonization"]
    end
    subgraph tier_7["Tier 7"]
        n62["ENG_the_winds_of_change"]
    end
    n56 --> n61
    n60 --> n61
    n59 --> n61
    n51 --> n53
    n48 --> n50
    n54 --> n56
    n57 --> n60
    n55 --> n57
    n52 --> n54
    n52 --> n55
    n53 --> n58
    n61 --> n62
    n50 --> n51
    n53 --> n59
    n50 --> n52
    n48 x--x n49
```

# ENG_steady_as_she_goes

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["ENG_a_change_in_course"]
        n2{"ENG_steady_as_she_goes"}
    end
    subgraph tier_1["Tier 1"]
        n63["ENG_global_defense"]
        n64["ENG_home_defence"]
    end
    subgraph tier_2["Tier 2"]
        n65["ENG_benelux_intervention"]
        n66["ENG_every_man_will_do_his_duty"]
        n67["ENG_issue_gasmasks"]
        n68["ENG_motion_of_no_confidence"]
        n69["ENG_prepare_for_the_inevitable"]
        n70["uk_iraq_focus"]
        n71["uk_scandinavian_focus"]
    end
    subgraph tier_3["Tier 3"]
        n72["ENG_belgium_security"]
        n73["ENG_danish_intervention"]
        n74["ENG_dutch_security"]
        n75["ENG_military_training_act"]
        n76{"ENG_no_further_appeasement"}
        n77["ENG_norwegian_intervention"]
        n78["ENG_swedish_intervention"]
        n79["uk_iran_focus"]
    end
    subgraph tier_4["Tier 4"]
        n80["ENG_embargo_germany"]
        n81["ENG_embargo_ussr"]
        n82["ENG_kickstart_the_war_industry"]
        n83["ENG_maintaining_imperial_integrity"]
        n84["ENG_maintaining_the_balance_of_power"]
    end
    subgraph tier_5["Tier 5"]
        n85["ENG_continental_intervention"]
        n86["ENG_enforce_the_naval_treaties"]
        n87["ENG_secure_the_oil_imports"]
        n88["ENG_war_with_germany"]
        n89["ENG_war_with_ussr"]
    end
    n65 --> n72
    n64 --> n65
    n84 --> n85
    n71 --> n73
    n65 --> n74
    n75 --> n80
    n79 --> n81
    n76 --> n81
    n83 --> n86
    n63 --> n66
    n2 --> n63
    n2 --> n64
    n64 --> n67
    n76 --> n82
    n76 --> n83
    n76 --> n84
    n67 --> n75
    n63 --> n68
    n66 --> n76
    n68 --> n76
    n71 --> n77
    n64 --> n69
    n82 --> n87
    n71 --> n78
    n80 --> n88
    n81 --> n89
    n70 --> n79
    n64 --> n70
    n64 --> n71
    n1 x--x n2
    n63 x--x n64
    n83 x--x n84
```

# crypto_bomb_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n90(("crypto_bomb_focus"))
        n91["radar_focus"]
        n92["royal_ordinance_focus"]
    end
    subgraph tier_1["Tier 1"]
        n93["tizard_mission_focus"]
    end
    subgraph tier_2["Tier 2"]
        n94["maud_focus"]
    end
    subgraph tier_3["Tier 3"]
        n95["UK_secret_focus"]
    end
    n92 --> n95
    n94 --> n95
    n93 --> n94
    n90 --> n93
    n91 --> n93
```

# limited_rearmament_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n90["crypto_bomb_focus"]
        n96(("limited_rearmament_focus"))
        n97["uk_service_focus"]
    end
    subgraph tier_1["Tier 1"]
        n98["ENG_expand_the_secret_intelligence_service_focus"]
        n99["ENG_motorized_focus"]
        n100["air_defense_focus"]
        n101["general_rearmament_focus"]
        n102["shadow_scheme_focus"]
    end
    subgraph tier_2["Tier 2"]
        n103["ENG_special_air_service"]
        n104["ENG_tank_focus"]
        n105["air_rearmament_focus"]
        n106["naval_rearmament_focus"]
        n91["radar_focus"]
        n107["uk_industrial_focus"]
    end
    subgraph tier_3["Tier 3"]
        n108["ENG_anti_non_contact_committee"]
        n109["ENG_chiefs_of_staff_committee"]
        n110["ENG_parachute_regiments"]
        n111["ENG_secure_the_imperial_shipping_routes"]
        n112["ENG_vickers_experimental_facility_focus"]
        n113["bomber_command_focus"]
        n114["coastal_command_focus"]
        n115["fighter_command_focus"]
        n92["royal_ordinance_focus"]
        n93["tizard_mission_focus"]
        n116["uk_amphibious_focus"]
        n117["uk_destroyer_focus"]
        n118["uk_extra_tech_slot"]
        n119{"uk_waves_focus"}
    end
    subgraph tier_4["Tier 4"]
        n120["ENG_a_s_warfare"]
        n121["aircraft_production_focus"]
        n94["maud_focus"]
        n122["uk_battleship_focus"]
        n123["uk_carrier_focus"]
        n124["uk_convoy_focus"]
        n125["uk_small_arms_focus"]
    end
    subgraph tier_5["Tier 5"]
        n126["ENG_anti_submarine_training_school"]
        n127["ENG_expand_the_repair_yards"]
        n128["ENG_vanguard"]
        n95["UK_secret_focus"]
        n129["uk_jet_focus"]
    end
    n117 --> n120
    n106 --> n108
    n124 --> n126
    n105 --> n109
    n106 --> n109
    n122 --> n127
    n123 --> n127
    n96 --> n98
    n96 --> n99
    n103 --> n110
    n106 --> n111
    n97 --> n111
    n101 --> n103
    n99 --> n104
    n122 --> n128
    n107 --> n112
    n92 --> n95
    n94 --> n95
    n96 --> n100
    n101 --> n105
    n115 --> n121
    n113 --> n121
    n114 --> n121
    n105 --> n113
    n105 --> n114
    n105 --> n115
    n96 --> n101
    n93 --> n94
    n101 --> n106
    n100 --> n91
    n107 --> n92
    n96 --> n102
    n90 --> n93
    n91 --> n93
    n106 --> n116
    n119 --> n122
    n119 --> n123
    n117 --> n124
    n106 --> n117
    n107 --> n118
    n102 --> n107
    n121 --> n129
    n92 --> n125
    n106 --> n119
    n122 x--x n123
```

# uk_empire_focus

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n48["ENG_revisit_colonial_policy"]
        n106["naval_rearmament_focus"]
        n49(("uk_empire_focus"))
    end
    subgraph tier_1["Tier 1"]
        n97["uk_service_focus"]
    end
    subgraph tier_2["Tier 2"]
        n111["ENG_secure_the_imperial_shipping_routes"]
        n130["uk_colonial_focus"]
        n131{"uk_mediterranean_focus"}
    end
    subgraph tier_3["Tier 3"]
        n132["uk_asia_focus"]
        n133["uk_commonwealth_focus"]
        n134["uk_malta_focus"]
        n135{"uk_protect_suez"}
        n136["uk_rock_focus"]
        n137["uk_spain_focus"]
    end
    subgraph tier_4["Tier 4"]
        n138["ENG_british_commonwealth_air_training_plan"]
        n139["hongkong_focus"]
        n140{"singapore_focus"}
        n141["uk_australia_focus"]
        n142["uk_balkan_strategy"]
        n143["uk_burma_focus"]
        n144["uk_canada_focus"]
        n145["uk_greece_focus"]
        n146{"uk_india_focus"}
        n147["uk_south_africa_focus"]
        n148["uk_turkey_focus"]
    end
    subgraph tier_5["Tier 5"]
        n149["ENG_indian_autonomy"]
        n150["ENG_royal_malay_regiment_focus"]
        n151["ENG_south_east_asia_air_command_focus"]
        n152["ENG_territorial_army_of_malaysia_focus"]
        n153["uk_free_india_focus"]
        n154["uk_new_zealand_focus"]
        n155["uk_sanction_italy_focus"]
        n156["uk_sanction_japan_focus"]
    end
    subgraph tier_6["Tier 6"]
        n157["ENG_imperial_conference"]
        n158["ENG_war_with_italy"]
        n159["peninsular_focus"]
        n160["uk_china_focus"]
    end
    subgraph tier_7["Tier 7"]
        n161["ENG_east_indies_fleet_focus"]
        n162["ENG_imperial_federation"]
        n163["ENG_sarawakrangers_focus"]
    end
    subgraph tier_8["Tier 8"]
        n164["ENG_war_with_japan"]
    end
    n133 --> n138
    n159 --> n161
    n151 --> n161
    n144 --> n157
    n154 --> n157
    n147 --> n157
    n157 --> n162
    n146 --> n149
    n140 --> n150
    n159 --> n163
    n106 --> n111
    n97 --> n111
    n139 --> n151
    n140 --> n152
    n155 --> n158
    n156 --> n164
    n163 --> n164
    n161 --> n164
    n132 --> n139
    n150 --> n159
    n152 --> n159
    n132 --> n140
    n130 --> n132
    n133 --> n141
    n135 --> n142
    n134 --> n142
    n132 --> n143
    n133 --> n144
    n151 --> n160
    n97 --> n130
    n130 --> n133
    n146 --> n153
    n135 --> n145
    n133 --> n146
    n131 --> n134
    n97 --> n131
    n141 --> n154
    n131 --> n135
    n131 --> n136
    n142 --> n155
    n143 --> n156
    n49 --> n97
    n133 --> n147
    n131 --> n137
    n135 --> n148
    n149 x--x n153
    n48 x--x n49
    n150 x--x n152
    n145 x--x n148
    n136 x--x n137
```
