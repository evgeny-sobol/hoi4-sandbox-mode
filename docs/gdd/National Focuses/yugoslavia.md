# YUG_army_modernization

```mermaid
flowchart TD
    n1["YUG_anti_tank_defenses"]
    n2{"YUG_armored_cavalry"}
    n3{"YUG_army_maneuvers"}
    n4(("YUG_army_modernization"))
    n5["YUG_artillery_regiments"]
    n6["YUG_domestic_artillery_production"]
    n7["YUG_form_parachute_battalions"]
    n8["YUG_independent_engineer_regiments"]
    n9["YUG_medal_for_extreme_bravery"]
    n10["YUG_modern_tanks"]
    n11["YUG_motorize_the_cavalry"]
    n12["YUG_motorized_logistics"]
    n13["YUG_motorized_recon_companies"]
    n14["YUG_mountain_brigades"]
    n15["YUG_small_arms"]
    n16["YUG_supremacy_of_defense"]
    n17["YUG_supremacy_of_offense"]
    n18["YUG_tank_conversions"]
    n19["YUG_tank_licenses"]
    n6 --> n1
    n11 --> n2
    n4 --> n3
    n17 --> n5
    n16 --> n5
    n15 --> n6
    n13 --> n7
    n14 --> n8
    n5 --> n9
    n2 --> n10
    n4 --> n11
    n11 --> n12
    n8 --> n13
    n4 --> n14
    n4 --> n15
    n3 --> n16
    n3 --> n17
    n2 --> n18
    n10 --> n19
    n10 x--x n18
    n16 x--x n17
```

# YUG_expand_the_serbian_shipyards

```mermaid
flowchart TD
    n20["YUG_coastal_defense"]
    n21["YUG_contest_the_adriatic"]
    n22(("YUG_expand_the_serbian_shipyards"))
    n23["YUG_expand_the_split_shipyards"]
    n24["YUG_expand_the_submarine_fleet"]
    n25["YUG_modern_destroyers"]
    n26["YUG_naval_bombers"]
    n22 --> n20
    n20 --> n24
    n26 --> n25
    n21 --> n26
    n20 --> n26
    n22 x--x n23
```

# YUG_expand_the_split_shipyards

```mermaid
flowchart TD
    n20["YUG_coastal_defense"]
    n21["YUG_contest_the_adriatic"]
    n22["YUG_expand_the_serbian_shipyards"]
    n23(("YUG_expand_the_split_shipyards"))
    n27["YUG_heavy_cruiser_project"]
    n25["YUG_modern_destroyers"]
    n26["YUG_naval_bombers"]
    n28["YUG_replace_the_dalmacija"]
    n23 --> n21
    n28 --> n27
    n26 --> n25
    n21 --> n26
    n20 --> n26
    n21 --> n28
    n22 x--x n23
```

# YUG_industrialization_program

```mermaid
flowchart TD
    n29["YUG_central_management"]
    n30["YUG_develop_civilian_industry"]
    n31["YUG_develop_military_industry"]
    n32["YUG_develop_slovenian_industry"]
    n33{"YUG_expand_the_mining_industry"}
    n34["YUG_expand_the_sarajevo_arsenals"]
    n35["YUG_expand_the_university_of_belgrad"]
    n36["YUG_expand_the_university_of_ljubljana"]
    n37{"YUG_expand_the_university_of_zagreb"}
    n38["YUG_exploit_the_pannonian_deposits"]
    n39["YUG_improve_light_industry"]
    n40["YUG_improve_serbian_rail_network"]
    n41(("YUG_industrialization_program"))
    n42["YUG_integrated_rail_network"]
    n43["YUG_local_self_management"]
    n44["YUG_rare_minerals_exploitation"]
    n45["YUG_serbian_steel"]
    n35 --> n29
    n33 --> n30
    n33 --> n31
    n42 --> n32
    n41 --> n33
    n43 --> n34
    n29 --> n34
    n40 --> n35
    n32 --> n36
    n30 --> n37
    n31 --> n37
    n44 --> n38
    n42 --> n39
    n40 --> n39
    n37 --> n40
    n37 --> n42
    n32 --> n43
    n33 --> n44
    n40 --> n45
    n30 x--x n31
    n40 x--x n42
```

# YUG_modernize_the_air_force

```mermaid
flowchart TD
    n46["YUG_bomber_license"]
    n47["YUG_bomber_project"]
    n48["YUG_fighter_license"]
    n49["YUG_heavy_fighter_project"]
    n50["YUG_ikarus"]
    n51{"YUG_license_production"}
    n52["YUG_local_developers"]
    n53{"YUG_modernize_the_air_force"}
    n54["YUG_purchase_foreign"]
    n55["YUG_rogozarski"]
    n56["YUG_the_ik_3"]
    n57["YUG_zmaj"]
    n51 --> n46
    n56 --> n47
    n51 --> n48
    n56 --> n49
    n52 --> n50
    n54 --> n51
    n53 --> n52
    n53 --> n54
    n52 --> n55
    n50 --> n56
    n55 --> n56
    n57 --> n56
    n52 --> n57
    n46 x--x n48
    n52 x--x n54
```

# YUG_recognize_the_soviet_union

```mermaid
flowchart TD
    n58{"YUG_abolish_the_monarchy"}
    n59["YUG_federal_defense_council"]
    n60["YUG_form_peasant_councils"]
    n61["YUG_form_the_federal_republic"]
    n62["YUG_friendship_treaty_with_italy"]
    n63["YUG_invite_albania"]
    n64["YUG_invite_bulgaria"]
    n65["YUG_invite_greece"]
    n66["YUG_invite_hungary"]
    n67["YUG_invite_romania"]
    n68["YUG_invite_turkey"]
    n69["YUG_join_comintern"]
    n70["YUG_local_militias"]
    n71["YUG_mutual_economic_aid"]
    n72["YUG_pan_balkan_workers_congress"]
    n73["YUG_pan_slavic_workers_congress"]
    n74(("YUG_recognize_the_soviet_union"))
    n75["YUG_reinforce_old_alliances"]
    n76["YUG_research_collaboration"]
    n77["YUG_western_focus"]
    n78["YUG_yugoslavian_path_to_communism"]
    n60 --> n58
    n71 --> n58
    n61 --> n59
    n74 --> n60
    n78 --> n61
    n69 --> n61
    n73 --> n63
    n73 --> n64
    n72 --> n65
    n72 --> n66
    n72 --> n67
    n65 --> n68
    n66 --> n68
    n67 --> n68
    n58 --> n69
    n75 --> n70
    n62 --> n70
    n60 --> n70
    n74 --> n71
    n64 --> n72
    n63 --> n72
    n59 --> n72
    n78 --> n73
    n69 --> n76
    n58 --> n78
    n69 x--x n78
    n74 x--x n77
```

# YUG_western_focus

```mermaid
flowchart TD
    n79["YUG_all_yugoslavian_regiments"]
    n80["YUG_allied_air_combat_school"]
    n81{"YUG_attract_allied_capital"}
    n82{"YUG_attract_axis_capital"}
    n83{"YUG_autonomous_transylvania"}
    n84{"YUG_ban_slovene_nationalist_parties"}
    n85{"YUG_banat_for_support"}
    n86["YUG_brigadistas"]
    n87["YUG_claim_macedonia"]
    n88{"YUG_concessions_for_macedonians"}
    n89{"YUG_coronation"}
    n90{"YUG_crush_the_ustasa"}
    n91["YUG_defence_army_of_yugoslavia"]
    n92["YUG_defence_league"]
    n93{"YUG_devolved_croatia"}
    n94{"YUG_dissolve_serbia"}
    n95{"YUG_divide_bosnia"}
    n96["YUG_end_the_regency"]
    n97["YUG_enforced_neutrality"]
    n98{"YUG_establish_the_banovina_of_croatia"}
    n99{"YUG_evolution"}
    n60["YUG_form_peasant_councils"]
    n100{"YUG_fortify_banat"}
    n101["YUG_fortress_yugoslavia"]
    n62["YUG_friendship_treaty_with_italy"]
    n102["YUG_greater_yugoslavia"]
    n103["YUG_guarantee_religious_liberties"]
    n104["YUG_invite_german_military_mission"]
    n105["YUG_invite_italian_naval_experts"]
    n106["YUG_join_allies"]
    n107{"YUG_join_axis"}
    n108{"YUG_limited_self_government"}
    n70["YUG_local_militias"]
    n74["YUG_recognize_the_soviet_union"]
    n75["YUG_reinforce_old_alliances"]
    n109["YUG_reunite_the_kingdom"]
    n110{"YUG_royal_wedding"}
    n111{"YUG_safeguard_bosnia"}
    n112{"YUG_slovenia_for_support"}
    n113["YUG_surrender_italian_claims"]
    n114{"YUG_surrender_macedonia"}
    n115["YUG_towards_independence"]
    n116{"YUG_united_autonomous_croatia"}
    n117["YUG_united_kingdom"]
    n77{"YUG_western_focus"}
    n118["YUG_zara_for_axis"]
    n102 --> n79
    n106 --> n80
    n62 --> n81
    n75 --> n81
    n62 --> n82
    n75 --> n82
    n94 --> n83
    n111 --> n83
    n95 --> n83
    n90 --> n84
    n98 --> n84
    n94 --> n85
    n111 --> n85
    n95 --> n85
    n62 --> n86
    n75 --> n86
    n118 --> n87
    n113 --> n87
    n112 --> n88
    n84 --> n88
    n96 --> n89
    n107 --> n89
    n99 --> n90
    n115 --> n91
    n91 --> n92
    n108 --> n93
    n108 --> n94
    n116 --> n95
    n93 --> n95
    n88 --> n96
    n114 --> n96
    n85 --> n96
    n83 --> n96
    n100 --> n96
    n110 --> n97
    n89 --> n97
    n99 --> n98
    n81 --> n99
    n82 --> n99
    n94 --> n100
    n111 --> n100
    n95 --> n100
    n97 --> n101
    n77 --> n62
    n87 --> n102
    n117 --> n103
    n88 --> n104
    n114 --> n104
    n85 --> n104
    n83 --> n104
    n100 --> n104
    n118 --> n105
    n113 --> n105
    n110 --> n106
    n89 --> n106
    n88 --> n107
    n114 --> n107
    n85 --> n107
    n83 --> n107
    n100 --> n107
    n81 --> n108
    n82 --> n108
    n75 --> n70
    n62 --> n70
    n60 --> n70
    n77 --> n75
    n103 --> n109
    n96 --> n110
    n116 --> n111
    n93 --> n111
    n90 --> n112
    n98 --> n112
    n107 --> n113
    n112 --> n114
    n84 --> n114
    n85 --> n115
    n83 --> n115
    n100 --> n115
    n108 --> n116
    n85 --> n117
    n83 --> n117
    n100 --> n117
    n107 --> n118
    n83 x--x n85
    n83 x--x n100
    n84 x--x n112
    n85 x--x n100
    n88 x--x n114
    n90 x--x n98
    n93 x--x n116
    n95 x--x n111
    n96 x--x n107
    n97 x--x n106
    n99 x--x n108
    n62 x--x n75
    n74 x--x n77
    n113 x--x n118
    n115 x--x n117
```
