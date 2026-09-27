# CHI_sea_invite_foreign_investors

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1{"CHI_sea_invite_foreign_investors"}
    end
    subgraph tier_1["Tier 1"]
        n2["CHI_sea_british_cooperation"]
        n3["CHI_sea_collaboration_with_the_japanese"]
        n4{"CHI_sea_mission_to_germany"}
        n5{"CHI_sea_mission_to_the_soviet_union"}
        n6["CHI_sea_mission_to_the_us"]
        n7["CHI_sea_reach_out_to_france"]
    end
    subgraph tier_2["Tier 2"]
        n8["CHI_sea_burma_road"]
        n9["CHI_sea_closer_ties_with_germany"]
        n10["CHI_sea_fighter_purchases"]
        n11["CHI_sea_give_falkenhausen_citizenship"]
        n12["CHI_sea_guarantee_the_hanoi_route"]
        n13["CHI_sea_hire_chennault"]
        n14["CHI_sea_investment_into_shipbuilding"]
        n15["CHI_sea_invite_soviet_advisers"]
        n16["CHI_sea_rapprochement_with_soviet_union"]
        n17["CHI_sea_small_arms_expertise"]
    end
    subgraph tier_3["Tier 3"]
        n18["CHI_sea_camco"]
        n19["CHI_sea_chinese_general_staff"]
        n20["CHI_sea_construction_battalions"]
        n21["CHI_sea_elite_mountaineers"]
        n22["CHI_sea_french_military_mission"]
        n23["CHI_sea_invite_the_flying_tigers"]
        n24["CHI_sea_order_destroyers"]
        n25["CHI_sea_purchase_tanks"]
        n26["CHI_sea_the_soviet_volunteer_group"]
    end
    subgraph tier_4["Tier 4"]
        n27["CHI_sea_chinese_panzers"]
        n28["CHI_sea_experimental_mechanised_unit"]
        n29["CHI_sea_heavy_weapons"]
        n30["CHI_sea_hire_soviet_designer"]
        n31["CHI_sea_light_cruiser_project"]
        n32["CHI_sea_local_fighter_production"]
        n33["CHI_sea_modern_submarines"]
        n34["CHI_sea_sino_american_cooperative_organization"]
        n35["CHI_sea_the_chu_x_po"]
        n36["CHI_sea_the_hump"]
        n37["CHI_sea_train_marines"]
        n38["CHI_sea_wargaming_division"]
    end
    subgraph tier_5["Tier 5"]
        n39["CHI_sea_chinese_expeditionary_force"]
        n40["CHI_sea_coastal_patrol_planes"]
        n41["CHI_sea_combined_arms_warfare"]
        n42["CHI_sea_french_drill"]
        n43["CHI_sea_heavy_cruiser_project"]
        n44["CHI_sea_joint_tank_development"]
        n45["CHI_sea_ledo_road"]
        n46["CHI_sea_local_bomber_production"]
        n47["CHI_sea_tank_plant"]
    end
    subgraph tier_6["Tier 6"]
        n48["CHI_sea_modern_logistics"]
        n49["CHI_sea_naval_aviation"]
    end
    subgraph tier_7["Tier 7"]
        n50["CHI_sea_carrier_air_wing"]
        n51{"CHI_sea_renegotiate_the_unequal_treaties"}
    end
    subgraph tier_8["Tier 8"]
        n52{"CHI_sea_anti_imperialism"}
        n53["CHI_sea_imperial_legacy"]
        n54{"CHI_sea_one_china_policy"}
    end
    subgraph tier_9["Tier 9"]
        n55["CHI_ncns_request_handover_of_coastal_cities"]
        n56{"CHI_sea_conquer_tibet"}
        n57["CHI_sea_dominate_japan"]
        n58["CHI_sea_guidance_and_support"]
        n59["CHI_sea_indian_cooperation"]
        n60{"CHI_sea_integrate_tibet"}
        n61["CHI_sea_overlordship_over_indochina"]
    end
    subgraph tier_10["Tier 10"]
        n62["CHI_sea_commit_to_korean_independence"]
        n63["CHI_sea_dominate_siam"]
        n64["CHI_sea_influence_mongolia"]
        n65["CHI_sea_renounce_the_mcmahon_line"]
        n66["CHI_sea_secure_the_peninsula"]
    end
    subgraph tier_11["Tier 11"]
        n67["CHI_sea_demand_mongolia"]
        n68["CHI_sea_push_into_manchuria"]
    end
    subgraph tier_12["Tier 12"]
        n69["CHI_sea_annex_tuva"]
    end
    n54 --> n55
    n67 --> n69
    n51 --> n52
    n1 --> n2
    n2 --> n8
    n10 --> n18
    n49 --> n50
    n36 --> n39
    n11 --> n19
    n9 --> n19
    n25 --> n27
    n9 --> n27
    n4 --> n9
    n33 --> n40
    n1 --> n3
    n28 --> n41
    n58 --> n62
    n54 --> n56
    n12 --> n20
    n8 --> n20
    n65 --> n67
    n53 --> n57
    n61 --> n63
    n15 --> n21
    n17 --> n21
    n25 --> n28
    n2 --> n10
    n6 --> n10
    n29 --> n42
    n22 --> n42
    n12 --> n22
    n4 --> n11
    n7 --> n12
    n52 --> n58
    n31 --> n43
    n21 --> n29
    n6 --> n13
    n25 --> n30
    n16 --> n30
    n51 --> n53
    n52 --> n59
    n59 --> n64
    n54 --> n60
    n6 --> n14
    n3 --> n14
    n5 --> n15
    n13 --> n23
    n30 --> n44
    n8 --> n45
    n36 --> n45
    n6 --> n31
    n24 --> n31
    n32 --> n46
    n8 --> n32
    n18 --> n32
    n1 --> n4
    n1 --> n5
    n1 --> n6
    n42 --> n48
    n45 --> n48
    n3 --> n33
    n24 --> n33
    n43 --> n49
    n40 --> n49
    n51 --> n54
    n14 --> n24
    n53 --> n61
    n9 --> n25
    n16 --> n25
    n66 --> n68
    n5 --> n16
    n1 --> n7
    n48 --> n51
    n41 --> n51
    n49 --> n51
    n60 --> n65
    n56 --> n65
    n61 --> n66
    n23 --> n34
    n7 --> n17
    n27 --> n47
    n18 --> n35
    n18 --> n36
    n13 --> n36
    n15 --> n26
    n24 --> n37
    n19 --> n38
    n52 x--x n53
    n2 x--x n7
    n9 x--x n16
    n3 x--x n6
    n56 x--x n60
    n59 x--x n65
```
