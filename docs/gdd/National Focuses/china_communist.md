# PRC_land_redistribution

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("PRC_land_redistribution"))
    end
    subgraph tier_1["Tier 1"]
        n2{"PRC_enforce_the_three_rules"}
        n3["PRC_literacy_programs"]
        n4["PRC_the_yanan_base_area"]
    end
    subgraph tier_2["Tier 2"]
        n5["PRC_ban_the_opium_trade"]
        n6["PRC_china_medical_university"]
        n7["PRC_focus_on_china"]
        n8["PRC_permit_opium_trade"]
        n9["PRC_prepare_for_war_with_japan"]
    end
    subgraph tier_3["Tier 3"]
        n10["PRC_abolish_the_land_rent"]
        n11["PRC_anti_japanese_expedition"]
        n12["PRC_exploit_the_weak_neighbours"]
        n13["PRC_form_the_academy_of_sciences"]
        n14["PRC_government_of_national_defense"]
        n15["PRC_infiltration"]
    end
    subgraph tier_4["Tier 4"]
        n16["PRC_confrontation_with_the_warlords"]
    end
    subgraph tier_5["Tier 5"]
        n17["PRC_revolutionary_military_commission"]
    end
    subgraph tier_6["Tier 6"]
        n18["PRC_central_military_commission"]
        n19["PRC_military_intelligence_department"]
        n20{"PRC_provoke_japan"}
    end
    subgraph tier_7["Tier 7"]
        n21["PRC_central_security_bureau"]
        n22["PRC_mobile_warfare"]
        n23["PRC_peoples_liberation_army"]
        n24["PRC_peoples_volunteer_army"]
        n25["PRC_protracted_warfare"]
    end
    subgraph tier_8["Tier 8"]
        n26["PRC_100_regiments_campaign"]
        n27["PRC_peoples_war"]
    end
    n22 --> n26
    n8 --> n10
    n5 --> n10
    n9 --> n11
    n2 --> n5
    n17 --> n18
    n19 --> n21
    n3 --> n6
    n14 --> n16
    n1 --> n2
    n7 --> n12
    n4 --> n7
    n6 --> n13
    n9 --> n14
    n7 --> n15
    n1 --> n3
    n17 --> n19
    n20 --> n22
    n18 --> n23
    n18 --> n24
    n25 --> n27
    n2 --> n8
    n4 --> n9
    n20 --> n25
    n17 --> n20
    n11 --> n20
    n16 --> n17
    n15 --> n17
    n1 --> n4
    n5 x--x n8
    n22 x--x n25
```

# PRC_strengthen_the_central_secretariat

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n28{"PRC_strengthen_the_central_secretariat"}
    end
    subgraph tier_1["Tier 1"]
        n29["PRC_agrarian_socialism"]
        n30["PRC_marxist_orthodoxy"]
        n31["PRC_social_democracy_focus"]
    end
    subgraph tier_2["Tier 2"]
        n32["PRC_coalition_government"]
        n33["PRC_rectification_campaign"]
        n34["PRC_soviet_leadership"]
    end
    subgraph tier_3["Tier 3"]
        n35["PRC_maoism"]
        n36["PRC_purge_the_radicals"]
        n37["PRC_soviet_economic_aid"]
        n38["PRC_strengthen_the_left_wing_of_the_kmt"]
    end
    subgraph tier_4["Tier 4"]
        n39["PRC_internationalism"]
        n40["PRC_remove_chiang_kai_shek"]
        n41["PRC_socialism_with_chinese_characteristics"]
    end
    subgraph tier_5["Tier 5"]
        n42["PRC_proclaim_the_peoples_republic"]
    end
    subgraph tier_6["Tier 6"]
        n43["PRC_socialist_market_economy"]
    end
    n28 --> n29
    n31 --> n32
    n37 --> n39
    n33 --> n35
    n28 --> n30
    n41 --> n42
    n39 --> n42
    n32 --> n36
    n29 --> n33
    n38 --> n40
    n36 --> n40
    n28 --> n31
    n35 --> n41
    n42 --> n43
    n40 --> n43
    n34 --> n37
    n30 --> n34
    n32 --> n38
    n29 x--x n30
    n29 x--x n31
    n30 x--x n31
```
