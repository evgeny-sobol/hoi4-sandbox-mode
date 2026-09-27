# CHI_industrial_investment

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CHI_industrial_investment"))
    end
    subgraph tier_1["Tier 1"]
        n2["CHI_local_arms_production"]
        n3["CHI_public_education_reform"]
    end
    subgraph tier_2["Tier 2"]
        n4["CHI_local_arms_development"]
        n5["CHI_long_term_economic_planning"]
    end
    subgraph tier_3["Tier 3"]
        n6["CHI_heavy_weapons_development"]
    end
    n4 --> n6
    n2 --> n4
    n1 --> n2
    n2 --> n5
    n1 --> n3
```

# CHI_secure_internal_politics

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n7{"CHI_secure_internal_politics"}
    end
    subgraph tier_1["Tier 1"]
        n8["CHI_cooperation_with_the_communists"]
        n9["CHI_cooperation_with_the_nationalists"]
        n10["CHI_opposition"]
    end
    subgraph tier_2["Tier 2"]
        n11["CHI_anti_opposition_campaigns"]
        n12["CHI_institute_cross_border_raids"]
        n13["CHI_land_redistribution"]
        n14{"CHI_new_model_province"}
        n15["CHI_public_works"]
        n16["CHI_technological_cooperation"]
        n17["CHI_war_taxes"]
    end
    subgraph tier_3["Tier 3"]
        n18["CHI_cult_of_personality"]
        n19["CHI_embrace_the_opium_trade"]
        n20["CHI_ideological_education"]
        n21["CHI_labor_reform"]
        n22["CHI_land_value_tax"]
        n23{"CHI_personal_leadership"}
        n24["CHI_root_out_corruption"]
        n25["CHI_rural_militias"]
        n26["CHI_seek_japanese_support"]
    end
    subgraph tier_4["Tier 4"]
        n27["CHI_communist_administrators"]
        n28["CHI_defensive_posture"]
        n29["CHI_judiciary_reforms"]
        n30["CHI_land_reform"]
        n31["CHI_provoke_border_clashes"]
        n32["CHI_reform_the_administration"]
    end
    subgraph tier_5["Tier 5"]
        n33["CHI_join_the_chinese_soviet"]
        n34["CHI_join_the_republican_government"]
        n35["CHI_rapid_mobilization"]
    end
    subgraph tier_6["Tier 6"]
        n36["CHI_power_struggle"]
        n37["CHI_proclaim_rival_government"]
        n38["CHI_the_yanan_incident"]
    end
    n9 --> n11
    n8 --> n11
    n22 --> n27
    n7 --> n8
    n7 --> n9
    n17 --> n18
    n23 --> n28
    n14 --> n19
    n13 --> n20
    n10 --> n12
    n29 --> n33
    n27 --> n33
    n30 --> n34
    n32 --> n34
    n20 --> n29
    n15 --> n21
    n8 --> n13
    n24 --> n30
    n13 --> n22
    n9 --> n14
    n7 --> n10
    n17 --> n23
    n34 --> n36
    n25 --> n37
    n35 --> n37
    n23 --> n31
    n8 --> n15
    n10 --> n15
    n31 --> n35
    n28 --> n35
    n24 --> n32
    n19 --> n32
    n14 --> n24
    n15 --> n25
    n17 --> n26
    n9 --> n16
    n33 --> n38
    n10 --> n17
    n8 x--x n9
    n8 x--x n10
    n9 x--x n10
    n28 x--x n31
    n19 x--x n24
```

# CHI_strenghten_warlord_authority

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n39{"CHI_strenghten_warlord_authority"}
    end
    subgraph tier_1["Tier 1"]
        n40["CHI_uplift_the_cavalry_regiments"]
        n41["CHI_uplift_the_mountain_brigades"]
    end
    n39 --> n40
    n39 --> n41
    n40 x--x n41
```
