# CHI_military_affairs_commission

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CHI_military_affairs_commission"))
    end
    subgraph tier_1["Tier 1"]
        n2["CHI_army_reform"]
        n3["CHI_bureau_of_investigation_and_statistics"]
        n4["CHI_fortify_shanghai"]
    end
    subgraph tier_2["Tier 2"]
        n5["CHI_60_divisions_plan"]
        n6["CHI_the_chinese_hindenburg_line"]
        n7["CHI_whampoa_military_academy"]
    end
    n2 --> n5
    n1 --> n2
    n1 --> n3
    n1 --> n4
    n4 --> n6
    n3 --> n7
```

# CHI_three_principles_of_the_people

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n8(("CHI_three_principles_of_the_people"))
    end
    subgraph tier_1["Tier 1"]
        n9["CHI_democracy"]
        n10{"CHI_nationalism"}
        n11["CHI_welfare"]
    end
    subgraph tier_2["Tier 2"]
        n12["CHI_constitutional_reform"]
        n13["CHI_executive_yuan"]
        n14["CHI_foreign_threats"]
        n15["CHI_land_tax_reform"]
        n16["CHI_prioritize_the_interior"]
        n17["CHI_refugee_relief_agency"]
    end
    subgraph tier_3["Tier 3"]
        n18["CHI_anti_communism"]
        n19["CHI_inter_party_coordination_council"]
        n20["CHI_new_life_movement"]
        n21["CHI_republicanism"]
        n22["CHI_subjugate_the_warlords"]
        n23["CHI_unemployment_assistance"]
        n24["CHI_united_front"]
    end
    subgraph tier_4["Tier 4"]
        n25["CHI_free_hospitals"]
        n26["CHI_judicial_yuan"]
        n27["CHI_legislative_yuan"]
        n28["CHI_pick_a_fight_with_japan"]
    end
    subgraph tier_5["Tier 5"]
        n29["CHI_control_yuan"]
        n30["CHI_rural_schooling"]
        n31["CHI_war_of_resistance"]
    end
    subgraph tier_6["Tier 6"]
        n32["CHI_examination_yuan"]
        n33["CHI_industrial_evacuations"]
        n34["CHI_scorched_earth_tactics"]
        n35["CHI_war_of_national_liberation"]
    end
    subgraph tier_7["Tier 7"]
        n36["CHI_forced_conscription"]
        n37["CHI_war_of_anti_imperialism"]
    end
    subgraph tier_8["Tier 8"]
        n38["CHI_dare_to_die_corps"]
    end
    n16 --> n18
    n9 --> n12
    n26 --> n29
    n27 --> n29
    n36 --> n38
    n8 --> n9
    n29 --> n32
    n9 --> n13
    n34 --> n36
    n10 --> n14
    n20 --> n25
    n23 --> n25
    n31 --> n33
    n12 --> n19
    n13 --> n19
    n21 --> n26
    n19 --> n26
    n11 --> n15
    n13 --> n27
    n19 --> n27
    n8 --> n10
    n17 --> n20
    n24 --> n28
    n18 --> n28
    n10 --> n16
    n11 --> n17
    n12 --> n21
    n25 --> n30
    n31 --> n34
    n16 --> n22
    n15 --> n23
    n14 --> n24
    n35 --> n37
    n31 --> n35
    n28 --> n31
    n8 --> n11
    n14 x--x n16
```

# CHI_unified_industrial_planning

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n39(("CHI_unified_industrial_planning"))
    end
    subgraph tier_1["Tier 1"]
        n40["CHI_expand_the_academica_sinica"]
        n41["CHI_financial_policy"]
        n42["CHI_rural_reconstruction_movement"]
    end
    subgraph tier_2["Tier 2"]
        n43["CHI_chemical_research_institute"]
        n44["CHI_mining_commission"]
        n45["CHI_price_controls"]
    end
    subgraph tier_3["Tier 3"]
        n46["CHI_develop_the_hanyan_arsenal"]
        n47["CHI_grain_tax"]
        n48["CHI_reform_the_national_bank"]
        n49["CHI_taiyuan_arsenal"]
    end
    subgraph tier_4["Tier 4"]
        n50["CHI_forced_loans"]
    end
    n40 --> n43
    n44 --> n46
    n39 --> n40
    n39 --> n41
    n48 --> n50
    n45 --> n47
    n42 --> n44
    n41 --> n45
    n45 --> n48
    n39 --> n42
    n44 --> n49
```
