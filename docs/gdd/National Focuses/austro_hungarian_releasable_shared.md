# ah_army_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ah_army_effort"))
        n2["ah_aviation_effort_2"]
    end
    subgraph tier_1["Tier 1"]
        n3["ah_doctrine_effort"]
        n4["ah_equipment_effort"]
        n5["ah_motorization_effort"]
    end
    subgraph tier_2["Tier 2"]
        n6["ah_CAS_effort"]
        n7["ah_doctrine_effort_2"]
        n8["ah_equipment_effort_2"]
        n9["ah_mechanization_effort"]
    end
    subgraph tier_3["Tier 3"]
        n10["ah_armor_effort"]
        n11["ah_equipment_effort_3"]
    end
    subgraph tier_4["Tier 4"]
        n12["ah_special_forces"]
    end
    n2 --> n6
    n5 --> n6
    n9 --> n10
    n1 --> n3
    n3 --> n7
    n1 --> n4
    n4 --> n8
    n8 --> n11
    n5 --> n9
    n1 --> n5
    n11 --> n12
    n7 --> n12
    n10 --> n12
```

# ah_aviation_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n13{"ah_aviation_effort"}
        n14["ah_flexible_navy"]
        n15["ah_infrastructure_effort"]
        n5["ah_motorization_effort"]
    end
    subgraph tier_1["Tier 1"]
        n16["ah_bomber_focus"]
        n17["ah_fighter_focus"]
    end
    subgraph tier_2["Tier 2"]
        n2["ah_aviation_effort_2"]
    end
    subgraph tier_3["Tier 3"]
        n6["ah_CAS_effort"]
        n18["ah_NAV_effort"]
        n19["ah_rocket_effort"]
    end
    n2 --> n6
    n5 --> n6
    n2 --> n18
    n14 --> n18
    n16 --> n2
    n17 --> n2
    n13 --> n16
    n13 --> n17
    n2 --> n19
    n15 --> n19
    n16 x--x n17
```

# ah_industrial_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n2["ah_aviation_effort_2"]
        n20(("ah_industrial_effort"))
    end
    subgraph tier_1["Tier 1"]
        n21["ah_construction_effort"]
        n22["ah_production_effort"]
    end
    subgraph tier_2["Tier 2"]
        n23["ah_construction_effort_2"]
        n24["ah_production_effort_2"]
    end
    subgraph tier_3["Tier 3"]
        n15["ah_infrastructure_effort"]
        n25["ah_production_effort_3"]
    end
    subgraph tier_4["Tier 4"]
        n26["ah_construction_effort_3"]
        n27["ah_infrastructure_effort_2"]
        n19["ah_rocket_effort"]
    end
    subgraph tier_5["Tier 5"]
        n28["ah_extra_tech_slot"]
        n29["ah_nuclear_effort"]
        n30["ah_secret_weapons"]
    end
    subgraph tier_6["Tier 6"]
        n31["ah_extra_tech_slot_2"]
    end
    n20 --> n21
    n21 --> n23
    n15 --> n26
    n27 --> n28
    n28 --> n31
    n23 --> n15
    n15 --> n27
    n27 --> n29
    n20 --> n22
    n22 --> n24
    n24 --> n25
    n2 --> n19
    n15 --> n19
    n27 --> n30
```

# ah_naval_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n2["ah_aviation_effort_2"]
        n32{"ah_naval_effort"}
    end
    subgraph tier_1["Tier 1"]
        n14["ah_flexible_navy"]
        n33["ah_large_navy"]
    end
    subgraph tier_2["Tier 2"]
        n18["ah_NAV_effort"]
        n34["ah_cruiser_effort"]
        n35["ah_submarine_effort"]
    end
    subgraph tier_3["Tier 3"]
        n36["ah_capital_ships_effort"]
        n37["ah_destroyer_effort"]
    end
    n2 --> n18
    n14 --> n18
    n34 --> n36
    n33 --> n34
    n14 --> n34
    n35 --> n37
    n32 --> n14
    n32 --> n33
    n14 --> n35
    n33 --> n35
    n14 x--x n33
```

# ah_political_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n38{"ah_political_effort"}
    end
    subgraph tier_1["Tier 1"]
        n39{"ah_collectivist_ethos"}
        n40{"ah_liberty_ethos"}
    end
    subgraph tier_2["Tier 2"]
        n41["ah_internationalism_focus"]
        n42["ah_interventionism_focus"]
        n43["ah_nationalism_focus"]
        n44["ah_neutrality_focus"]
    end
    subgraph tier_3["Tier 3"]
        n45["ah_deterrence"]
        n46["ah_militarism"]
        n47["ah_political_correctness"]
        n48["ah_volunteer_corps"]
    end
    subgraph tier_4["Tier 4"]
        n49["ah_foreign_expeditions"]
        n50["ah_indoctrination_focus"]
        n51["ah_military_youth"]
    end
    subgraph tier_5["Tier 5"]
        n52["ah_paramilitarism"]
        n53["ah_political_commissars"]
        n54["ah_why_we_fight"]
    end
    subgraph tier_6["Tier 6"]
        n55["ah_ideological_fanaticism"]
    end
    subgraph tier_7["Tier 7"]
        n56["ah_technology_sharing"]
    end
    n38 --> n39
    n44 --> n45
    n48 --> n49
    n52 --> n55
    n53 --> n55
    n47 --> n50
    n39 --> n41
    n40 --> n42
    n38 --> n40
    n43 --> n46
    n46 --> n51
    n39 --> n43
    n40 --> n44
    n51 --> n52
    n50 --> n53
    n41 --> n47
    n55 --> n56
    n54 --> n56
    n42 --> n48
    n49 --> n54
    n45 --> n54
    n39 x--x n40
    n41 x--x n43
    n42 x--x n44
```
