# PRC_sea_land_redistribution

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("PRC_sea_land_redistribution"))
    end
    subgraph tier_1["Tier 1"]
        n2{"PRC_sea_enforce_the_three_rules"}
        n3["PRC_sea_literacy_programs"]
        n4["PRC_sea_the_yanan_base_area"]
    end
    subgraph tier_2["Tier 2"]
        n5["PRC_sea_ban_the_opium_trade"]
        n6["PRC_sea_china_medical_university"]
        n7["PRC_sea_focus_on_china"]
        n8["PRC_sea_permit_opium_trade"]
        n9["PRC_sea_prepare_for_war_with_japan"]
    end
    subgraph tier_3["Tier 3"]
        n10["PRC_sea_abolish_the_land_rent"]
        n11["PRC_sea_anti_japanese_expedition"]
        n12["PRC_sea_exploit_the_weak_neighbours"]
        n13["PRC_sea_form_the_academy_of_sciences"]
        n14["PRC_sea_government_of_national_defense"]
        n15["PRC_sea_infiltration"]
    end
    subgraph tier_4["Tier 4"]
        n16["PRC_sea_confrontation_with_the_warlords"]
    end
    subgraph tier_5["Tier 5"]
        n17["PRC_sea_revolutionary_military_commission"]
    end
    subgraph tier_6["Tier 6"]
        n18["PRC_sea_central_military_commission"]
        n19["PRC_sea_military_intelligence_department"]
        n20{"PRC_sea_provoke_japan"}
    end
    subgraph tier_7["Tier 7"]
        n21["PRC_sea_central_security_bureau"]
        n22["PRC_sea_mobile_warfare"]
        n23["PRC_sea_peoples_liberation_army"]
        n24["PRC_sea_peoples_volunteer_army"]
        n25["PRC_sea_protracted_warfare"]
    end
    subgraph tier_8["Tier 8"]
        n26["PRC_sea_100_regiments_campaign"]
        n27["PRC_sea_peoples_war"]
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

# PRC_sea_strengthen_the_central_secretariat

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n28{"PRC_sea_strengthen_the_central_secretariat"}
    end
    subgraph tier_1["Tier 1"]
        n29["PRC_sea_inward_focus"]
        n30["PRC_sea_toe_the_soviet_line"]
    end
    subgraph tier_2["Tier 2"]
        n31["PRC_sea_aid_from_soviet_bolsheviks"]
        n32["PRC_sea_rally_the_industry"]
        n33["PRC_sea_reforming_our_ranks"]
        n34["PRC_sea_soviet_advisors"]
    end
    subgraph tier_3["Tier 3"]
        n35["PRC_sea_agrarian_socialism"]
        n36["PRC_sea_industrialisation_of_nature"]
    end
    subgraph tier_4["Tier 4"]
        n37["PRC_sea_comintern_integration"]
        n38["PRC_sea_forging_our_own_path"]
    end
    subgraph tier_5["Tier 5"]
        n39["PRC_sea_proclaim_the_peoples_republic"]
    end
    subgraph tier_6["Tier 6"]
        n40["PRC_sea_move_capital"]
        n41["PRC_sea_new_economic_direction"]
    end
    n33 --> n35
    n32 --> n35
    n30 --> n31
    n36 --> n37
    n35 --> n38
    n34 --> n36
    n31 --> n36
    n28 --> n29
    n39 --> n40
    n39 --> n41
    n37 --> n39
    n38 --> n39
    n29 --> n32
    n29 --> n33
    n30 --> n34
    n28 --> n30
    n29 x--x n30
```
