# IRQ_anglo_iraqi_oil_expansion

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("IRQ_anglo_iraqi_oil_expansion"))
        n2["IRQ_nationalize_the_anglo_iraqi_oil_company"]
    end
    subgraph tier_1["Tier 1"]
        n3["IRQ_demand_greater_stake_in_the_company"]
        n4["IRQ_expand_oil_production"]
    end
    subgraph tier_2["Tier 2"]
        n5["IRQ_export_infrastructure"]
    end
    n1 --> n3
    n1 --> n4
    n2 --> n4
    n4 --> n5
    n1 x--x n2
```

# IRQ_decouple_from_the_pound

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n6(("IRQ_decouple_from_the_pound"))
    end
    subgraph tier_1["Tier 1"]
        n7["IRQ_baghdad_colleges_of_engineering_and_education"]
        n8["IRQ_construct_the_kut_barrage"]
        n9["IRQ_found_the_iraqi_state_railways"]
        n10["IRQ_purchase_foreign_equipment"]
        n11["IRQ_strengthen_the_iraqi_dinar"]
    end
    subgraph tier_2["Tier 2"]
        n12["IRQ_expand_the_cotton_industries"]
        n13["IRQ_extensive_irrigation_projects"]
        n14["IRQ_finish_the_berlin_baghdad_railway"]
        n15["IRQ_found_company_for_cement"]
        n16["IRQ_found_southern_steel_plants"]
        n17{"IRQ_heavy_industry_investments"}
        n18["IRQ_rural_electrification"]
        n19["IRQ_strengthen_mesopotamian_farming"]
    end
    subgraph tier_3["Tier 3"]
        n20["IRQ_construct_the_dukan_dam"]
        n21["IRQ_found_the_state_company_for_iron_and_steel"]
        n22["IRQ_invite_foreign_arms_corporations"]
        n23["IRQ_local_arms_industry"]
    end
    subgraph tier_4["Tier 4"]
        n24["IRQ_forceful_industrialization"]
    end
    n6 --> n7
    n15 --> n20
    n7 --> n20
    n6 --> n8
    n11 --> n12
    n8 --> n13
    n9 --> n14
    n23 --> n24
    n22 --> n24
    n20 --> n24
    n11 --> n15
    n10 --> n16
    n6 --> n9
    n16 --> n21
    n11 --> n17
    n17 --> n22
    n17 --> n23
    n6 --> n10
    n8 --> n18
    n8 --> n19
    n6 --> n11
    n22 x--x n23
```

# IRQ_ensure_sunni_dominance

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n25{"IRQ_ensure_sunni_dominance"}
        n26["IRQ_promote_kurdish_culture"]
    end
    subgraph tier_1["Tier 1"]
        n27["IRQ_party_of_national_brotherhood"]
        n28["IRQ_rally_behind_the_hashemite_dynasty"]
    end
    subgraph tier_2["Tier 2"]
        n29["IRQ_bakr_sidqi_coup"]
        n30["IRQ_increase_anglo_iraqi_economic_ties"]
    end
    subgraph tier_3["Tier 3"]
        n31["IRQ_al_muthanna_club"]
        n32{"IRQ_increase_italian_business_relations"}
        n33["IRQ_kurdish_outreach"]
        n34{"IRQ_raf_levies_focus"}
        n35["IRQ_reach_out_to_jordan"]
        n36["IRQ_suppress_tribal_revolts"]
    end
    subgraph tier_4["Tier 4"]
        n37{"IRQ_assasination_of_sidqi"}
        n38{"IRQ_attempted_assasination_of_sidqi"}
        n39["IRQ_regional_economic_integration"]
        n40["IRQ_regional_military_integration"]
    end
    subgraph tier_5["Tier 5"]
        n41["IRQ_curtail_arabism"]
        n42["IRQ_demand_palestine"]
        n43["IRQ_eliminate_the_golden_square"]
        n44["IRQ_refuge_for_the_grand_mufti"]
        n45["IRQ_strengthen_the_golden_square"]
    end
    subgraph tier_6["Tier 6"]
        n46["IRQ_commander_of_the_faithful"]
        n47{"IRQ_demand_syria_hashemite"}
        n48{"IRQ_embargo_the_axis_powers"}
        n49["IRQ_encourage_federalism"]
        n50["IRQ_fligerfuhrer_irak"]
        n51["IRQ_increase_prime_ministers_powers"]
        n52["IRQ_iraqi_al_futuwwa"]
        n53["IRQ_rally_the_arab_world"]
        n54{"IRQ_restoration_of_hejaz"}
        n55{"IRQ_revoke_anglo_iraq_treaty"}
        n56["IRQ_strengthen_relations_with_iran"]
        n57["IRQ_strengthen_relations_with_turkey"]
    end
    subgraph tier_7["Tier 7"]
        n58["IRQ_a_new_caliph"]
        n59["IRQ_anti_western_alliance"]
        n60["IRQ_arab_free_legion"]
        n61["IRQ_arab_league"]
        n62["IRQ_hashemite_arab_federation"]
        n63["IRQ_iran_ultimatum"]
        n64["IRQ_join_axis"]
        n65["IRQ_reapproachment_with_the_tribes"]
        n66["IRQ_regime_change_in_arabia"]
        n67["IRQ_request_syria_from_vichy"]
        n68["IRQ_restore_regent"]
    end
    subgraph tier_8["Tier 8"]
        n69["IRQ_align_afghanistan_fasc"]
        n70["IRQ_arab_league_economic_cooperation"]
        n71["IRQ_carve_up_syria"]
        n72["IRQ_expand_membership"]
        n73["IRQ_liberate_levant"]
        n74["IRQ_liberate_north_africa"]
        n75["IRQ_proclaim_united_arab_republic"]
        n76["IRQ_seek_axis_investment"]
        n77["IRQ_support_the_allied_war_effort"]
        n78["IRQ_take_advantage_of_british_weakness"]
        n79["IRQ_unite_maghreb"]
        n80["IRQ_unite_mashriq"]
    end
    subgraph tier_9["Tier 9"]
        n81["IRQ_allied_training"]
        n82["IRQ_axis_training"]
        n83["IRQ_greater_iraq"]
        n84["IRQ_invite_oil_mission"]
        n85["IRQ_protector_of_the_gulf"]
        n86["IRQ_renegotiate_treaty"]
        n87["IRQ_restore_al_andalus"]
        n88["IRQ_status_of_lebanon"]
    end
    n54 --> n58
    n29 --> n31
    n59 --> n69
    n77 --> n81
    n56 --> n59
    n57 --> n59
    n53 --> n60
    n48 --> n61
    n55 --> n61
    n61 --> n70
    n34 --> n37
    n32 --> n37
    n32 --> n38
    n76 --> n82
    n27 --> n29
    n59 --> n71
    n42 --> n46
    n38 --> n41
    n40 --> n42
    n39 --> n42
    n42 --> n47
    n37 --> n43
    n38 --> n43
    n43 --> n48
    n41 --> n49
    n62 --> n72
    n45 --> n50
    n71 --> n83
    n78 --> n83
    n47 --> n62
    n28 --> n30
    n29 --> n32
    n42 --> n51
    n76 --> n84
    n53 --> n63
    n45 --> n52
    n41 --> n52
    n55 --> n64
    n30 --> n33
    n66 --> n73
    n66 --> n74
    n25 --> n27
    n66 --> n75
    n77 --> n85
    n30 --> n34
    n29 --> n34
    n25 --> n28
    n45 --> n53
    n30 --> n35
    n49 --> n65
    n38 --> n44
    n37 --> n44
    n53 --> n66
    n35 --> n39
    n35 --> n40
    n77 --> n86
    n58 --> n86
    n62 --> n86
    n50 --> n67
    n42 --> n54
    n79 --> n87
    n55 --> n68
    n45 --> n55
    n64 --> n76
    n71 --> n88
    n41 --> n56
    n41 --> n57
    n38 --> n45
    n37 --> n45
    n48 --> n77
    n68 --> n77
    n30 --> n36
    n29 --> n36
    n59 --> n78
    n58 --> n79
    n58 --> n80
    n58 x--x n62
    n61 x--x n64
    n61 x--x n68
    n37 x--x n38
    n41 x--x n45
    n25 x--x n26
    n64 x--x n68
    n27 x--x n28
```

# IRQ_nationalize_the_anglo_iraqi_oil_company

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["IRQ_anglo_iraqi_oil_expansion"]
        n2(("IRQ_nationalize_the_anglo_iraqi_oil_company"))
    end
    subgraph tier_1["Tier 1"]
        n4["IRQ_expand_oil_production"]
        n89["IRQ_form_opec"]
    end
    subgraph tier_2["Tier 2"]
        n5["IRQ_export_infrastructure"]
    end
    n1 --> n4
    n2 --> n4
    n4 --> n5
    n2 --> n89
    n1 x--x n2
```

# IRQ_promote_kurdish_culture

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n25["IRQ_ensure_sunni_dominance"]
        n26(("IRQ_promote_kurdish_culture"))
    end
    subgraph tier_1["Tier 1"]
        n90["IRQ_kurdish_democratic"]
        n91["IRQ_kurdish_socialist"]
    end
    subgraph tier_2["Tier 2"]
        n92["IRQ_kurdish_revolt"]
    end
    subgraph tier_3["Tier 3"]
        n93["IRQ_kurdish_form_the_peshmerga"]
        n94["IRQ_kurdish_language"]
    end
    subgraph tier_4["Tier 4"]
        n95["IRQ_effectivize_the_production_line"]
        n96["IRQ_kurdish_industry"]
        n97["IRQ_kurdish_women_in_military"]
    end
    subgraph tier_5["Tier 5"]
        n98["IRQ_kurdish_oil"]
        n99["IRQ_kurdish_reject_ankara_treaty"]
    end
    subgraph tier_6["Tier 6"]
        n100["IRQ_further_ussr_support"]
        n101["IRQ_support_from_skies_above"]
        n102["IRQ_support_from_the_mountains"]
    end
    subgraph tier_7["Tier 7"]
        n103["IRQ_kurdish_attack_iran"]
        n104["IRQ_kurdish_attack_turkey"]
    end
    subgraph tier_8["Tier 8"]
        n105["IRQ_kurdish_united"]
    end
    n93 --> n95
    n99 --> n100
    n101 --> n103
    n102 --> n103
    n101 --> n104
    n102 --> n104
    n26 --> n90
    n92 --> n93
    n94 --> n96
    n92 --> n94
    n96 --> n98
    n96 --> n99
    n97 --> n99
    n91 --> n92
    n90 --> n92
    n26 --> n91
    n103 --> n105
    n104 --> n105
    n93 --> n97
    n99 --> n101
    n99 --> n102
    n25 x--x n26
```

# IRQ_royal_iraqi_army

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n106(("IRQ_royal_iraqi_army"))
    end
    subgraph tier_1["Tier 1"]
        n107["IRQ_approach_tribes_for_support"]
        n108["IRQ_establish_iraqi_coastal_defense_force"]
        n109["IRQ_expand_habbaniya_airbase"]
        n110["IRQ_infantry_focus"]
        n111["IRQ_invest_in_ordnance_mountain_howitzers"]
        n112["IRQ_modernization"]
    end
    subgraph tier_2["Tier 2"]
        n113["IRQ_cavalry_integration"]
        n114["IRQ_create_repair_yards"]
        n115{"IRQ_independent_flight_schools"}
        n116["IRQ_invite_foreign_advisors"]
        n117["IRQ_purchase_armored_equipment"]
        n118["IRQ_purchase_mechanized_equipment"]
        n119["IRQ_scavenging"]
    end
    subgraph tier_3["Tier 3"]
        n120["IRQ_basra_military_port_focus"]
        n121["IRQ_expand_camel_corps"]
        n122["IRQ_form_the_independent_mechanized_brigade"]
        n123["IRQ_purchase_alternative_aricraft"]
        n124["IRQ_purchase_british_aircraft"]
        n125["IRQ_purchase_small_ships"]
        n126["IRQ_training"]
    end
    subgraph tier_4["Tier 4"]
        n127["IRQ_army_research_bonus"]
        n128["IRQ_bomber_training"]
        n129["IRQ_develop_the_kuwaiti_port"]
        n130["IRQ_fighter_training"]
        n131["IRQ_naval_air_support"]
        n132["IRQ_navy_research_bonus"]
    end
    subgraph tier_5["Tier 5"]
        n133["IRQ_air_research_bonus"]
        n134["IRQ_project_babylon_focus"]
        n135["IRQ_special_forces"]
    end
    subgraph tier_6["Tier 6"]
        n136["IRQ_special_projects"]
    end
    n130 --> n133
    n131 --> n133
    n128 --> n133
    n106 --> n107
    n126 --> n127
    n114 --> n120
    n123 --> n128
    n124 --> n128
    n110 --> n113
    n108 --> n114
    n120 --> n129
    n106 --> n108
    n113 --> n121
    n106 --> n109
    n123 --> n130
    n124 --> n130
    n118 --> n122
    n117 --> n122
    n109 --> n115
    n106 --> n110
    n106 --> n111
    n108 --> n116
    n106 --> n112
    n123 --> n131
    n124 --> n131
    n125 --> n132
    n127 --> n134
    n115 --> n123
    n112 --> n117
    n115 --> n124
    n112 --> n118
    n116 --> n125
    n110 --> n119
    n127 --> n135
    n133 --> n136
    n127 --> n136
    n113 --> n126
    n118 --> n126
    n117 --> n126
    n123 x--x n124
```
