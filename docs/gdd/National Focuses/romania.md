# ROM_army_maneuvers

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ROM_army_maneuvers"))
    end
    subgraph tier_1["Tier 1"]
        n2["ROM_army_war_college"]
        n3{"ROM_royal_guards_divisions"}
    end
    subgraph tier_2["Tier 2"]
        n4["ROM_reserve_divisions"]
        n5["ROM_the_armored_division"]
        n6["ROM_the_zb_53"]
    end
    subgraph tier_3["Tier 3"]
        n7{"ROM_acquire_modern_tanks"}
        n8{"ROM_artillery_modernization"}
        n9["ROM_vanatori_de_munte"]
    end
    subgraph tier_4["Tier 4"]
        n10["ROM_mobile_tank_destroyers"]
        n11["ROM_modern_at_guns"]
        n12["ROM_mountain_artillery"]
    end
    subgraph tier_5["Tier 5"]
        n13["ROM_the_maresal"]
    end
    n5 --> n7
    n4 --> n7
    n1 --> n2
    n6 --> n8
    n7 --> n10
    n8 --> n10
    n8 --> n11
    n8 --> n12
    n9 --> n12
    n3 --> n4
    n1 --> n3
    n3 --> n5
    n10 --> n13
    n2 --> n6
    n6 --> n9
    n10 x--x n11
    n4 x--x n5
```

# ROM_balkans_dominance

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n14(("ROM_balkans_dominance"))
        n15["ROM_civil_works"]
        n16["ROM_flexible_foreign_policy"]
        n17{"ROM_fortify_the_borders"}
        n18["ROM_preserve_greater_romania"]
        n19{"ROM_revise_the_constitution"}
    end
    subgraph tier_1["Tier 1"]
        n20{"ROM_align_hungary"}
        n21["ROM_national_defense_industry"]
        n22["ROM_puppet_bulgaria"]
    end
    subgraph tier_2["Tier 2"]
        n23["ROM_agrarian_reform"]
        n24["ROM_divide_yugoslavia"]
        n25["ROM_his_majestys_loyal_government"]
        n26["ROM_secure_greece"]
        n27["ROM_split_czechoslovakia"]
    end
    subgraph tier_3["Tier 3"]
        n28{"ROM_danubian_transport_network"}
        n29["ROM_militarize_the_sentinels"]
        n30["ROM_secure_the_bosporus"]
    end
    subgraph tier_4["Tier 4"]
        n31["ROM_all_parties_must_end"]
        n32["ROM_invite_foreign_motor_companies"]
        n33["ROM_malaxa"]
    end
    subgraph tier_5["Tier 5"]
        n34["ROM_hunedoara_steel_works"]
        n35["ROM_invest_in_the_iar"]
    end
    subgraph tier_6["Tier 6"]
        n36["ROM_expand_ploiesti_oil_production"]
    end
    subgraph tier_7["Tier 7"]
        n37["ROM_expand_the_university_of_bucharest"]
    end
    subgraph tier_8["Tier 8"]
        n38["ROM_exploit_the_baita_mines"]
    end
    n15 --> n23
    n21 --> n23
    n14 --> n20
    n29 --> n31
    n23 --> n28
    n22 --> n24
    n35 --> n36
    n34 --> n36
    n36 --> n37
    n37 --> n38
    n17 --> n25
    n20 --> n25
    n19 --> n25
    n32 --> n34
    n33 --> n34
    n32 --> n35
    n33 --> n35
    n28 --> n32
    n28 --> n33
    n25 --> n29
    n14 --> n21
    n14 --> n22
    n22 --> n26
    n26 --> n30
    n20 --> n27
    n14 x--x n18
    n16 x--x n25
    n32 x--x n33
```

# ROM_expand_the_air_force

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n39{"ROM_expand_the_air_force"}
    end
    subgraph tier_1["Tier 1"]
        n40{"ROM_acquire_licenses"}
        n41{"ROM_local_development"}
        n42["ROM_white_squadron_focus"]
    end
    subgraph tier_2["Tier 2"]
        n43["ROM_air_defense"]
        n44["ROM_air_superiority"]
        n45["ROM_ground_support"]
        n46["ROM_strategic_bomber_force"]
    end
    subgraph tier_3["Tier 3"]
        n47["ROM_acquire_fighters"]
        n48["ROM_cas"]
        n49["ROM_heavy_bombers"]
        n50["ROM_iar_80"]
        n51["ROM_medium_bombers"]
    end
    subgraph tier_4["Tier 4"]
        n52["ROM_nuclear_bomb_project"]
    end
    n43 --> n47
    n39 --> n40
    n40 --> n43
    n41 --> n44
    n44 --> n48
    n40 --> n45
    n46 --> n49
    n44 --> n50
    n39 --> n41
    n45 --> n51
    n49 --> n52
    n41 --> n46
    n39 --> n42
    n40 x--x n41
    n43 x--x n45
    n44 x--x n46
```

# ROM_expand_the_galati_shipyards

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n53{"ROM_expand_the_galati_shipyards"}
    end
    subgraph tier_1["Tier 1"]
        n54["ROM_black_sea_dominance"]
        n55["ROM_coastal_defense_navy"]
    end
    subgraph tier_2["Tier 2"]
        n56["ROM_capital_ships"]
        n57["ROM_coastal_defense_ships"]
        n58["ROM_modern_destroyers"]
    end
    subgraph tier_3["Tier 3"]
        n59["ROM_expand_the_marine_regiment"]
        n60["ROM_modern_submarines"]
        n61["ROM_torpedo_boats"]
        n62["ROM_torpedo_bombers"]
    end
    n53 --> n54
    n54 --> n56
    n53 --> n55
    n55 --> n57
    n56 --> n59
    n55 --> n58
    n54 --> n58
    n58 --> n60
    n57 --> n61
    n58 --> n62
    n54 x--x n55
```

# ROM_institute_royal_dictatorship

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20{"ROM_align_hungary"}
        n63(("ROM_institute_royal_dictatorship"))
    end
    subgraph tier_1["Tier 1"]
        n64["ROM_crack_down_on_extremism"]
        n17{"ROM_fortify_the_borders"}
        n19{"ROM_revise_the_constitution"}
    end
    subgraph tier_2["Tier 2"]
        n16["ROM_flexible_foreign_policy"]
        n25["ROM_his_majestys_loyal_government"]
        n65["ROM_the_royal_foundation"]
    end
    subgraph tier_3["Tier 3"]
        n66["ROM_appoint_allied_friendly_government"]
        n67{"ROM_appoint_german_friendly_government"}
        n68["ROM_appoint_soviet_friendly_government"]
        n29["ROM_militarize_the_sentinels"]
    end
    subgraph tier_4["Tier 4"]
        n31["ROM_all_parties_must_end"]
        n69{"ROM_constitutional_guarantees"}
        n70{"ROM_iron_guard"}
        n71{"ROM_national_christian_party"}
        n72{"ROM_securitate"}
    end
    subgraph tier_5["Tier 5"]
        n73["ROM_force_abdication"]
        n74["ROM_handle_the_king"]
    end
    subgraph tier_6["Tier 6"]
        n75["ROM_king_michaels_coup"]
    end
    n29 --> n31
    n16 --> n66
    n16 --> n67
    n16 --> n68
    n66 --> n69
    n63 --> n64
    n19 --> n16
    n70 --> n73
    n72 --> n73
    n71 --> n73
    n63 --> n17
    n69 --> n74
    n17 --> n25
    n20 --> n25
    n19 --> n25
    n67 --> n70
    n73 --> n75
    n25 --> n29
    n67 --> n71
    n63 --> n19
    n68 --> n72
    n19 --> n65
    n16 x--x n25
    n73 x--x n74
    n70 x--x n71
```

# ROM_preserve_greater_romania

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n14["ROM_balkans_dominance"]
        n21["ROM_national_defense_industry"]
        n18(("ROM_preserve_greater_romania"))
    end
    subgraph tier_1["Tier 1"]
        n76["ROM_a_deal_with_the_devil"]
        n15["ROM_civil_works"]
        n77["ROM_renew_the_romanian_polish_alliance"]
        n78["ROM_trade_treaty_with_germany"]
    end
    subgraph tier_2["Tier 2"]
        n23["ROM_agrarian_reform"]
        n79["ROM_basing_rights_for_soviet_union"]
        n80["ROM_demand_a_western_guarantee"]
        n81["ROM_form_peasant_militias"]
        n82["ROM_invite_german_advisors"]
        n83["ROM_the_cordon_sanitaire"]
    end
    subgraph tier_3["Tier 3"]
        n28{"ROM_danubian_transport_network"}
        n84["ROM_join_allies"]
        n85["ROM_join_axis"]
        n86["ROM_join_comintern"]
        n87["ROM_license_german_equipment"]
        n88["ROM_military_modernization"]
        n89["ROM_romanian_volunteer_brigades"]
    end
    subgraph tier_4["Tier 4"]
        n90["ROM_demand_transnistria"]
        n91["ROM_german_romanian_oil_exploitation_company"]
        n32["ROM_invite_foreign_motor_companies"]
        n92["ROM_joint_allied_staff_college"]
        n33["ROM_malaxa"]
    end
    subgraph tier_5["Tier 5"]
        n34["ROM_hunedoara_steel_works"]
        n35["ROM_invest_in_the_iar"]
    end
    subgraph tier_6["Tier 6"]
        n36["ROM_expand_ploiesti_oil_production"]
    end
    subgraph tier_7["Tier 7"]
        n37["ROM_expand_the_university_of_bucharest"]
    end
    subgraph tier_8["Tier 8"]
        n38["ROM_exploit_the_baita_mines"]
    end
    n18 --> n76
    n15 --> n23
    n21 --> n23
    n76 --> n79
    n18 --> n15
    n23 --> n28
    n77 --> n80
    n85 --> n90
    n35 --> n36
    n34 --> n36
    n36 --> n37
    n37 --> n38
    n76 --> n81
    n85 --> n91
    n32 --> n34
    n33 --> n34
    n32 --> n35
    n33 --> n35
    n28 --> n32
    n78 --> n82
    n80 --> n84
    n82 --> n85
    n79 --> n86
    n84 --> n92
    n88 --> n92
    n82 --> n87
    n28 --> n33
    n80 --> n88
    n18 --> n77
    n79 --> n89
    n77 --> n83
    n18 --> n78
    n14 x--x n18
    n32 x--x n33
```
