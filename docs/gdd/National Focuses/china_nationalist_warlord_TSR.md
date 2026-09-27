# CHI_sea_military_affairs_commission

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CHI_sea_military_affairs_commission"))
    end
    subgraph tier_1["Tier 1"]
        n2["CHI_sea_army_reform"]
        n3["CHI_sea_bureau_of_investigation_and_statistics"]
        n4["CHI_sea_fortify_shanghai"]
    end
    subgraph tier_2["Tier 2"]
        n5["CHI_sea_60_divisions_plan"]
        n6["CHI_sea_the_chinese_hindenburg_line"]
        n7["CHI_sea_whampoa_military_academy"]
    end
    n2 --> n5
    n1 --> n2
    n1 --> n3
    n1 --> n4
    n4 --> n6
    n3 --> n7
```

# CHI_sea_unified_industrial_planning

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n8(("CHI_sea_unified_industrial_planning"))
    end
    subgraph tier_1["Tier 1"]
        n9["CHI_sea_expand_the_academica_sinica"]
        n10["CHI_sea_financial_policy"]
        n11["CHI_sea_rural_reconstruction_movement"]
    end
    subgraph tier_2["Tier 2"]
        n12["CHI_sea_chemical_research_institute"]
        n13["CHI_sea_mining_commission"]
        n14["CHI_sea_price_controls"]
    end
    subgraph tier_3["Tier 3"]
        n15["CHI_sea_develop_the_hanyan_arsenal"]
        n16["CHI_sea_grain_tax"]
        n17["CHI_sea_reform_the_national_bank"]
        n18["CHI_sea_taiyuan_arsenal"]
    end
    subgraph tier_4["Tier 4"]
        n19["CHI_sea_forced_loans"]
    end
    n9 --> n12
    n13 --> n15
    n8 --> n9
    n8 --> n10
    n17 --> n19
    n14 --> n16
    n11 --> n13
    n10 --> n14
    n14 --> n17
    n8 --> n11
    n13 --> n18
```

# CHI_tsr_form_a_preparatory_committee

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20(("CHI_tsr_form_a_preparatory_committee"))
        n21["CHI_tsr_repoen_the_natioal_assembly"]
    end
    subgraph tier_1["Tier 1"]
        n22["CHI_tsr_coronation_at_the_temple_of_heaven"]
        n23["CHI_tsr_legacy_of_the_hongxian_emperor"]
        n24["CHI_tsr_outlaw_the_kmt_and_cpc"]
    end
    subgraph tier_2["Tier 2"]
        n25["CHI_tsr_restoration_of_the_chinese_empire"]
    end
    subgraph tier_3["Tier 3"]
        n26["CHI_tsr_adopt_the_twelve_symbols"]
        n27["CHI_tsr_reestablish_xinhua_palace"]
        n28["CHI_tsr_reinstate_the_new_imperial_code"]
    end
    subgraph tier_4["Tier 4"]
        n29["CHI_tsr_reclaim_the_mandate_of_heaven"]
    end
    subgraph tier_5["Tier 5"]
        n30["CHI_tsr_five_races_under_one_union"]
        n31["CHI_tsr_never_another_national_protection_war"]
        n32["CHI_tsr_reestablish_the_beiyang_army"]
    end
    subgraph tier_6["Tier 6"]
        n33["CHI_tsr_reestablish_the_wuwei_corps"]
        n34["CHI_tsr_tianxia"]
        n35["CHI_tsr_zhonghua_minzu"]
    end
    n25 --> n26
    n20 --> n22
    n29 --> n30
    n20 --> n23
    n29 --> n31
    n20 --> n24
    n27 --> n29
    n28 --> n29
    n26 --> n29
    n29 --> n32
    n32 --> n33
    n25 --> n27
    n25 --> n28
    n24 --> n25
    n22 --> n25
    n23 --> n25
    n31 --> n34
    n30 --> n35
    n20 x--x n21
```

# CHI_tsr_repoen_the_natioal_assembly

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n20["CHI_tsr_form_a_preparatory_committee"]
        n21(("CHI_tsr_repoen_the_natioal_assembly"))
    end
    subgraph tier_1["Tier 1"]
        n36["CHI_sea_three_principles_of_the_people"]
    end
    subgraph tier_2["Tier 2"]
        n37["CHI_sea_democracy"]
        n38["CHI_sea_nationalism"]
        n39["CHI_sea_welfare"]
    end
    subgraph tier_3["Tier 3"]
        n40["CHI_sea_constitutional_reform"]
        n41["CHI_sea_executive_yuan"]
        n42["CHI_sea_land_tax_reform"]
        n43["CHI_sea_prioritize_the_interior"]
        n44["CHI_sea_refugee_relief_agency"]
    end
    subgraph tier_4["Tier 4"]
        n45["CHI_sea_anti_communism"]
        n46["CHI_sea_inter_party_coordination_council"]
        n47["CHI_sea_new_life_movement"]
        n48["CHI_sea_republicanism"]
        n49["CHI_sea_subjugate_the_warlords"]
        n50["CHI_sea_unemployment_assistance"]
    end
    subgraph tier_5["Tier 5"]
        n51["CHI_sea_free_hospitals"]
        n52["CHI_sea_judicial_yuan"]
        n53["CHI_sea_legislative_yuan"]
        n54["CHI_sea_pick_a_fight_with_japan"]
    end
    subgraph tier_6["Tier 6"]
        n55["CHI_sea_control_yuan"]
        n56["CHI_sea_rural_schooling"]
        n57["CHI_sea_war_of_resistance"]
    end
    subgraph tier_7["Tier 7"]
        n58["CHI_sea_examination_yuan"]
        n59["CHI_sea_industrial_evacuations"]
        n60["CHI_sea_scorched_earth_tactics"]
        n61["CHI_sea_war_of_national_liberation"]
    end
    subgraph tier_8["Tier 8"]
        n62["CHI_sea_forced_conscription"]
        n63["CHI_sea_war_of_anti_imperialism"]
    end
    subgraph tier_9["Tier 9"]
        n64["CHI_sea_dare_to_die_corps"]
    end
    n43 --> n45
    n37 --> n40
    n52 --> n55
    n53 --> n55
    n62 --> n64
    n36 --> n37
    n55 --> n58
    n37 --> n41
    n60 --> n62
    n47 --> n51
    n50 --> n51
    n57 --> n59
    n40 --> n46
    n41 --> n46
    n48 --> n52
    n46 --> n52
    n39 --> n42
    n41 --> n53
    n46 --> n53
    n36 --> n38
    n44 --> n47
    n45 --> n54
    n38 --> n43
    n39 --> n44
    n40 --> n48
    n51 --> n56
    n57 --> n60
    n43 --> n49
    n21 --> n36
    n42 --> n50
    n61 --> n63
    n57 --> n61
    n54 --> n57
    n36 --> n39
    n20 x--x n21
```

# CHI_tsr_the_reorganied_government

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n65(("CHI_tsr_the_reorganied_government"))
    end
    subgraph tier_1["Tier 1"]
        n66["CHI_tsr_industrial_expansion_cooperation"]
        n67["CHI_tsr_military_industrial_collaboration"]
    end
    subgraph tier_2["Tier 2"]
        n68["CHI_tsr_expand_the_nanjing_army"]
    end
    subgraph tier_3["Tier 3"]
        n69["CHI_tsr_promote_tridemism"]
    end
    subgraph tier_4["Tier 4"]
        n70["CHI_tsr_anti_communism"]
        n71["CHI_tsr_national_construction"]
        n72["CHI_tsr_peace"]
    end
    subgraph tier_5["Tier 5"]
        n73["CHI_tsr_pan_asianism"]
    end
    subgraph tier_6["Tier 6"]
        n74{"CHI_tsr_establish_the_tewu"}
    end
    subgraph tier_7["Tier 7"]
        n75["CHI_tsr_a_new_chinese_identity"]
        n76["CHI_tsr_embrace_japanese_cultural_institutions"]
    end
    subgraph tier_8["Tier 8"]
        n77["CHI_tsr_deepen_our_collaboration"]
        n78["CHI_tsr_our_place_in_the_sphere"]
    end
    n74 --> n75
    n69 --> n70
    n76 --> n77
    n74 --> n76
    n73 --> n74
    n66 --> n68
    n67 --> n68
    n65 --> n66
    n65 --> n67
    n69 --> n71
    n75 --> n78
    n71 --> n73
    n70 --> n73
    n72 --> n73
    n69 --> n72
    n68 --> n69
    n75 x--x n76
```
