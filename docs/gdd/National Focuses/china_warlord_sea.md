# CHI_sea_develop_capital

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CHI_sea_develop_capital"))
    end
    subgraph tier_1["Tier 1"]
        n2["CHI_sea_develop_capital_arsenal"]
        n3["CHI_sea_further_industrial_investment"]
    end
    subgraph tier_2["Tier 2"]
        n4["CHI_sea_expand_public_education"]
        n5["CHI_sea_long_term_economic_planning"]
        n6["CHI_sea_small_arms_production"]
    end
    subgraph tier_3["Tier 3"]
        n7{"CHI_sea_fund_research_projects"}
        n8["CHI_sea_heavy_weapons_development"]
        n9["CHI_sea_industrial_research_projects"]
    end
    subgraph tier_4["Tier 4"]
        n10["CHI_sea_modern_warfare"]
        n11["CHI_sea_rely_on_our_infantry"]
    end
    n1 --> n2
    n3 --> n4
    n2 --> n4
    n4 --> n7
    n1 --> n3
    n6 --> n8
    n5 --> n9
    n3 --> n5
    n7 --> n10
    n7 --> n11
    n2 --> n6
    n10 x--x n11
```

# CHI_sea_secure_internal_politics

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n12{"CHI_sea_secure_internal_politics"}
    end
    subgraph tier_1["Tier 1"]
        n13["CHI_sea_cooperation_with_the_communists"]
        n14["CHI_sea_cooperation_with_the_nationalists"]
        n15["CHI_sea_opposition"]
    end
    subgraph tier_2["Tier 2"]
        n16["CHI_sea_anti_opposition_campaigns"]
        n17["CHI_sea_institute_cross_border_raids"]
        n18["CHI_sea_land_redistribution"]
        n19{"CHI_sea_new_model_province"}
        n20["CHI_sea_public_works"]
        n21["CHI_sea_technological_cooperation"]
        n22["CHI_sea_war_taxes"]
    end
    subgraph tier_3["Tier 3"]
        n23["CHI_sea_cult_of_personality"]
        n24["CHI_sea_embrace_the_illicit_trade"]
        n25["CHI_sea_ideological_education"]
        n26["CHI_sea_labor_reform"]
        n27["CHI_sea_land_value_tax"]
        n28{"CHI_sea_personal_leadership"}
        n29["CHI_sea_root_out_corruption"]
        n30["CHI_sea_rural_militias"]
        n31["CHI_sea_seek_japanese_support"]
    end
    subgraph tier_4["Tier 4"]
        n32["CHI_sea_communist_administrators"]
        n33["CHI_sea_defensive_posture"]
        n34["CHI_sea_judiciary_reforms"]
        n35{"CHI_sea_land_reform"}
        n36["CHI_sea_provoke_border_clashes"]
        n37{"CHI_sea_reform_the_administration"}
    end
    subgraph tier_5["Tier 5"]
        n38["CHI_sea_battle_for_china"]
        n39["CHI_sea_join_the_chinese_soviet"]
        n40["CHI_sea_join_the_republican_government"]
        n41["CHI_sea_rapid_mobilization"]
    end
    subgraph tier_6["Tier 6"]
        n42["CHI_sea_a_new_expedition"]
        n43["CHI_sea_gain_warlord_support"]
        n44["CHI_sea_proclaim_rival_government"]
        n45["CHI_sea_propaganda_campaigns"]
        n46["CHI_sea_rally_the_warlords"]
        n47["CHI_sea_unified_army_structure"]
    end
    subgraph tier_7["Tier 7"]
        n48["CHI_sea_power_struggle"]
        n49["CHI_sea_the_yanan_incident"]
    end
    n38 --> n42
    n14 --> n16
    n13 --> n16
    n35 --> n38
    n37 --> n38
    n27 --> n32
    n12 --> n13
    n12 --> n14
    n22 --> n23
    n28 --> n33
    n19 --> n24
    n40 --> n43
    n18 --> n25
    n15 --> n17
    n34 --> n39
    n32 --> n39
    n35 --> n40
    n37 --> n40
    n25 --> n34
    n20 --> n26
    n13 --> n18
    n29 --> n35
    n18 --> n27
    n14 --> n19
    n12 --> n15
    n22 --> n28
    n43 --> n48
    n45 --> n48
    n42 --> n48
    n46 --> n48
    n30 --> n44
    n41 --> n44
    n40 --> n45
    n28 --> n36
    n13 --> n20
    n15 --> n20
    n38 --> n46
    n36 --> n41
    n33 --> n41
    n29 --> n37
    n24 --> n37
    n19 --> n29
    n20 --> n30
    n22 --> n31
    n14 --> n21
    n47 --> n49
    n39 --> n47
    n15 --> n22
    n38 x--x n40
    n13 x--x n14
    n13 x--x n15
    n14 x--x n15
    n33 x--x n36
    n24 x--x n29
```

# CHI_sea_strenghten_warlord_authority

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n50{"CHI_sea_strenghten_warlord_authority"}
        n51["SIK_a_new_xinjiang"]
        n52["SIK_military_cooperation"]
    end
    subgraph tier_1["Tier 1"]
        n53["CHI_sea_uplift_the_cavalry_regiments"]
        n54["CHI_sea_uplift_the_mountain_brigades"]
        n55["SIK_office_of_sinkiang_border_commissioner"]
    end
    subgraph tier_2["Tier 2"]
        n56["CHI_sea_consolidate_our_rule"]
        n57{"SIK_march_into_khotan"}
        n58["SIK_six_great_policies"]
    end
    subgraph tier_3["Tier 3"]
        n59["CHI_sea_brigade_specialization"]
        n60["CHI_sea_fortification_efforts"]
        n61["CHI_sea_infantry_efforts"]
        n62["SIK_a_united_sinkiang_clique"]
        n63["SIK_pursue_further_soviet_integration"]
        n64["SIK_soviet_intervention"]
    end
    subgraph tier_4["Tier 4"]
        n65["CHI_sea_the_army"]
        n66["SIK_a_new_nationality_policy"]
        n67["SIK_ensure_a_clean_government"]
        n68["SIK_protector_of_the_kyrgiz"]
        n69["SIK_settle_dzungarian_tribes"]
        n70["SIK_transformation_of_nature"]
    end
    subgraph tier_5["Tier 5"]
        n71["CHI_crackdown_on_looting"]
        n72{"SIK_king_of_sinkiang"}
    end
    subgraph tier_6["Tier 6"]
        n73["SIK_reaffirm_soviet_connections"]
        n74["SIK_reestablish_the_guominjun"]
        n75["SIK_rejoin_the_central_government"]
    end
    n65 --> n71
    n56 --> n59
    n54 --> n56
    n53 --> n56
    n56 --> n60
    n56 --> n61
    n59 --> n65
    n61 --> n65
    n50 --> n53
    n50 --> n54
    n62 --> n66
    n63 --> n66
    n57 --> n62
    n64 --> n67
    n63 --> n67
    n62 --> n72
    n66 --> n72
    n52 --> n57
    n55 --> n57
    n50 --> n55
    n64 --> n68
    n57 --> n63
    n72 --> n73
    n72 --> n74
    n72 --> n75
    n62 --> n69
    n55 --> n58
    n57 --> n64
    n64 --> n70
    n63 --> n70
    n51 --> n70
    n53 x--x n54
    n62 x--x n63
    n62 x--x n64
    n63 x--x n64
    n73 x--x n74
    n73 x--x n75
    n74 x--x n75
```

# KHM_call_for_aid

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n76(("KHM_call_for_aid"))
        n77["KHM_strike_the_governor"]
    end
    subgraph tier_1["Tier 1"]
        n78{"KHM_push_them_back"}
        n79{"KHM_utilize_family_contacts"}
    end
    subgraph tier_2["Tier 2"]
        n80["KHM_kumul_rebellion_avenged"]
        n81["KHM_our_position_remains"]
        n82["KHM_the_sinkiang_ma_clique"]
    end
    n78 --> n80
    n79 --> n80
    n78 --> n81
    n79 --> n81
    n76 --> n78
    n77 --> n78
    n78 --> n82
    n79 --> n82
    n76 --> n79
    n77 --> n79
    n76 x--x n77
    n80 x--x n81
    n80 x--x n82
    n81 x--x n82
```

# KHM_strike_the_governor

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n76["KHM_call_for_aid"]
        n77(("KHM_strike_the_governor"))
    end
    subgraph tier_1["Tier 1"]
        n78{"KHM_push_them_back"}
        n79{"KHM_utilize_family_contacts"}
    end
    subgraph tier_2["Tier 2"]
        n80["KHM_kumul_rebellion_avenged"]
        n81["KHM_our_position_remains"]
        n82["KHM_the_sinkiang_ma_clique"]
    end
    n78 --> n80
    n79 --> n80
    n78 --> n81
    n79 --> n81
    n76 --> n78
    n77 --> n78
    n78 --> n82
    n79 --> n82
    n76 --> n79
    n77 --> n79
    n76 x--x n77
    n80 x--x n81
    n80 x--x n82
    n81 x--x n82
```

# KHM_undermine_kmt_rule

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n83(("KHM_undermine_kmt_rule"))
        n84["XSM_sideline_family_conflicts"]
    end
    subgraph tier_1["Tier 1"]
        n85["KHM_establish_the_kashgar_clique"]
        n86["KHM_expand_the_madrasas"]
        n87["KHM_indian_expeditionary_forces_plan"]
    end
    subgraph tier_2["Tier 2"]
        n88["KHM_promote_anti_communism"]
        n89["KHM_shizangs_coup"]
    end
    subgraph tier_3["Tier 3"]
        n90["KHM_promote_jadidism"]
        n91["KHM_raise_additional_dungan_regiments"]
        n92["KHM_rally_the_faithful"]
        n93["KHM_take_control_of_zakat_and_waqf"]
    end
    subgraph tier_4["Tier 4"]
        n94["KHM_implement_jizyah"]
        n95["KHM_revive_the_basmachi_movement"]
    end
    n83 --> n85
    n83 --> n86
    n84 --> n86
    n93 --> n94
    n83 --> n87
    n84 --> n87
    n86 --> n88
    n89 --> n90
    n88 --> n91
    n89 --> n92
    n90 --> n95
    n85 --> n89
    n89 --> n93
    n83 x--x n84
```

# KUM_victory_in_tihwa

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n96(("KUM_victory_in_tihwa"))
    end
    subgraph tier_1["Tier 1"]
        n97["KUM_restore_yettishar"]
    end
    n96 --> n97
```

# SIC_the_sichuan_clique

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n98(("SIC_the_sichuan_clique"))
    end
    subgraph tier_1["Tier 1"]
        n99["SIC_the_armies_of_yang_sen"]
        n100["SIC_the_domain_of_liu_wenhui"]
        n101["SIC_the_governor_of_sichuan"]
    end
    subgraph tier_2["Tier 2"]
        n102["SIC_anti_communism"]
        n103["SIC_develop_chongqing"]
        n104["SIC_develop_xikang"]
    end
    subgraph tier_3["Tier 3"]
        n105["SIC_armor_efforts"]
        n106["SIC_drive_out_the_japanese"]
        n107["SIC_push_back_the_tibetans"]
    end
    subgraph tier_4["Tier 4"]
        n108["SIC_sichuan_still_stands"]
    end
    n99 --> n102
    n103 --> n105
    n101 --> n103
    n100 --> n104
    n102 --> n106
    n104 --> n107
    n105 --> n108
    n98 --> n99
    n98 --> n100
    n98 --> n101
```

# SIK_cooperate_with_the_ussr

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n109(("SIK_cooperate_with_the_ussr"))
        n55["SIK_office_of_sinkiang_border_commissioner"]
    end
    subgraph tier_1["Tier 1"]
        n110["SIK_establish_the_xinjiangneft"]
        n52["SIK_military_cooperation"]
        n111["SIK_utilize_asperovs_contacts"]
    end
    subgraph tier_2["Tier 2"]
        n112["SIK_a_soviet_airforce"]
        n113["SIK_cooperate_with_the_nkvd"]
        n114["SIK_invest_in_the_dushanzi_oil_fields"]
        n57{"SIK_march_into_khotan"}
        n115["SIK_three_year_plan_for_reconstruction"]
    end
    subgraph tier_3["Tier 3"]
        n51["SIK_a_new_xinjiang"]
        n62["SIK_a_united_sinkiang_clique"]
        n63["SIK_pursue_further_soviet_integration"]
        n64["SIK_soviet_intervention"]
    end
    subgraph tier_4["Tier 4"]
        n66["SIK_a_new_nationality_policy"]
        n67["SIK_ensure_a_clean_government"]
        n68["SIK_protector_of_the_kyrgiz"]
        n69["SIK_settle_dzungarian_tribes"]
        n70["SIK_transformation_of_nature"]
    end
    subgraph tier_5["Tier 5"]
        n72{"SIK_king_of_sinkiang"}
    end
    subgraph tier_6["Tier 6"]
        n73["SIK_reaffirm_soviet_connections"]
        n74["SIK_reestablish_the_guominjun"]
        n75["SIK_rejoin_the_central_government"]
    end
    n62 --> n66
    n63 --> n66
    n115 --> n51
    n113 --> n51
    n52 --> n112
    n57 --> n62
    n111 --> n113
    n64 --> n67
    n63 --> n67
    n109 --> n110
    n110 --> n114
    n62 --> n72
    n66 --> n72
    n52 --> n57
    n55 --> n57
    n109 --> n52
    n64 --> n68
    n57 --> n63
    n72 --> n73
    n72 --> n74
    n72 --> n75
    n62 --> n69
    n57 --> n64
    n111 --> n115
    n64 --> n70
    n63 --> n70
    n51 --> n70
    n109 --> n111
    n62 x--x n63
    n62 x--x n64
    n63 x--x n64
    n73 x--x n74
    n73 x--x n75
    n74 x--x n75
```

# XIC_northwest_bandit_suppression_headquarters

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n116{"XIC_northwest_bandit_suppression_headquarters"}
    end
    subgraph tier_1["Tier 1"]
        n117["XIC_discussions_in_luochuan"]
        n118["XIC_sixth_encirclement_campaign"]
    end
    subgraph tier_2["Tier 2"]
        n119["XIC_non_agression_pact_with_the_cpc"]
        n120["XIC_request_relocation_to_northeastern_command"]
        n121["XIC_send_a_representative_to_sheng_shicai"]
    end
    subgraph tier_3["Tier 3"]
        n122["XIC_invite_zuolin_loyalsits"]
        n123["XIC_reestablish_the_zhili_army"]
        n124["XIC_the_fushi_conference"]
    end
    subgraph tier_4["Tier 4"]
        n125["XIC_anti_japanese_national_salvation_agreement"]
        n126["XIC_recruit_mancurian_bandits"]
        n127["XIC_restore_the_glory_of_the_fengtian_army"]
    end
    subgraph tier_5["Tier 5"]
        n128["XIC_form_the_anti_japanese_comrades_association"]
        n129["XIC_reclaim_the_lost_birthright"]
        n130["XIC_withdraw_forces_from_yanan"]
    end
    subgraph tier_6["Tier 6"]
        n131["XIC_invite_chiang_for_troop_inspections"]
        n132["XIC_restore_the_homeland"]
    end
    subgraph tier_7["Tier 7"]
        n133["XIC_revive_the_beiyang_government"]
    end
    n124 --> n125
    n116 --> n117
    n125 --> n128
    n128 --> n131
    n130 --> n131
    n120 --> n122
    n117 --> n119
    n127 --> n129
    n123 --> n126
    n120 --> n123
    n118 --> n120
    n123 --> n127
    n122 --> n127
    n129 --> n132
    n132 --> n133
    n117 --> n121
    n116 --> n118
    n119 --> n124
    n121 --> n124
    n125 --> n130
    n117 x--x n118
```

# XSM_sideline_family_conflicts

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n83["KHM_undermine_kmt_rule"]
        n84(("XSM_sideline_family_conflicts"))
    end
    subgraph tier_1["Tier 1"]
        n86["KHM_expand_the_madrasas"]
        n87["KHM_indian_expeditionary_forces_plan"]
        n134{"XSM_strengthening_our_position"}
    end
    subgraph tier_2["Tier 2"]
        n88["KHM_promote_anti_communism"]
        n135["XSM_demand_submission"]
        n136["XSM_strike_at_the_detractors"]
    end
    subgraph tier_3["Tier 3"]
        n91["KHM_raise_additional_dungan_regiments"]
        n137["XSM_a_united_ma_state"]
    end
    n83 --> n86
    n84 --> n86
    n83 --> n87
    n84 --> n87
    n86 --> n88
    n88 --> n91
    n135 --> n137
    n136 --> n137
    n134 --> n135
    n84 --> n134
    n134 --> n136
    n83 x--x n84
    n135 x--x n136
```

# XSM_the_military_governor

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n138(("XSM_the_military_governor"))
    end
    subgraph tier_1["Tier 1"]
        n139["XSM_a_hui_army"]
        n140["XSM_sway_the_people"]
    end
    subgraph tier_2["Tier 2"]
        n141{"XSM_sweep_out_communists"}
    end
    subgraph tier_3["Tier 3"]
        n142["XSM_send_ma_lin_on_hajj"]
        n143["XSM_the_civilian_governor_remains"]
    end
    subgraph tier_4["Tier 4"]
        n144["XSM_ma_qis_natural_successor"]
        n145["XSM_recruit_salar_officers"]
        n146["XSM_solidifying_control"]
    end
    subgraph tier_5["Tier 5"]
        n147["XSM_rebuild_the_ninghai_army"]
    end
    n138 --> n139
    n143 --> n144
    n146 --> n147
    n142 --> n145
    n141 --> n142
    n143 --> n146
    n142 --> n146
    n138 --> n140
    n140 --> n141
    n139 --> n141
    n141 --> n143
    n142 x--x n143
```

# YUN_rally_around_long_yun

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n148(("YUN_rally_around_long_yun"))
    end
    subgraph tier_1["Tier 1"]
        n149["YUN_a_land_of_mountains"]
        n150["YUN_expand_local_infrastructure"]
    end
    subgraph tier_2["Tier 2"]
        n151["YUN_political_reforms"]
        n152["YUN_strive_for_self_sufficiency"]
    end
    subgraph tier_3["Tier 3"]
        n153["YUN_eduational_reforms"]
    end
    subgraph tier_4["Tier 4"]
        n154["YUN_the_democratic_fortress"]
    end
    subgraph tier_5["Tier 5"]
        n155["YUN_strengthen_burmic_ties"]
    end
    n148 --> n149
    n151 --> n153
    n152 --> n153
    n148 --> n150
    n149 --> n151
    n154 --> n155
    n150 --> n152
    n153 --> n154
```
