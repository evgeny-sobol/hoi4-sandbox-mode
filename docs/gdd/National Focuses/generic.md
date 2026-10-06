# army_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("army_effort"))
        n2["aviation_effort_2"]
    end
    subgraph tier_1["Tier 1"]
        n3["doctrine_effort"]
        n4["equipment_effort"]
        n5["motorization_effort"]
    end
    subgraph tier_2["Tier 2"]
        n6["CAS_effort"]
        n7["doctrine_effort_2"]
        n8["equipment_effort_2"]
        n9["mechanization_effort"]
    end
    subgraph tier_3["Tier 3"]
        n10["armor_effort"]
        n11["equipment_effort_3"]
    end
    subgraph tier_4["Tier 4"]
        n12["special_forces"]
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

# aviation_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n13{"aviation_effort"}
        n14["flexible_navy"]
        n15["infrastructure_effort"]
        n5["motorization_effort"]
    end
    subgraph tier_1["Tier 1"]
        n16["bomber_focus"]
        n17["fighter_focus"]
    end
    subgraph tier_2["Tier 2"]
        n2["aviation_effort_2"]
    end
    subgraph tier_3["Tier 3"]
        n6["CAS_effort"]
        n18["NAV_effort"]
        n19["rocket_effort"]
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

# industrial_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n2["aviation_effort_2"]
        n20(("industrial_effort"))
    end
    subgraph tier_1["Tier 1"]
        n21["construction_effort"]
        n22["production_effort"]
    end
    subgraph tier_2["Tier 2"]
        n23["construction_effort_2"]
        n24["production_effort_2"]
    end
    subgraph tier_3["Tier 3"]
        n15["infrastructure_effort"]
        n25["production_effort_3"]
    end
    subgraph tier_4["Tier 4"]
        n26["construction_effort_3"]
        n27["infrastructure_effort_2"]
        n19["rocket_effort"]
    end
    subgraph tier_5["Tier 5"]
        n28["extra_tech_slot"]
        n29["nuclear_effort"]
        n30["secret_weapons"]
    end
    subgraph tier_6["Tier 6"]
        n31["extra_tech_slot_2"]
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

# naval_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n2["aviation_effort_2"]
        n32{"naval_effort"}
    end
    subgraph tier_1["Tier 1"]
        n14["flexible_navy"]
        n33["large_navy"]
    end
    subgraph tier_2["Tier 2"]
        n18["NAV_effort"]
        n34["cruiser_effort"]
        n35["submarine_effort"]
    end
    subgraph tier_3["Tier 3"]
        n36["capital_ships_effort"]
        n37["destroyer_effort"]
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

# political_effort

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n38{"political_effort"}
    end
    subgraph tier_1["Tier 1"]
        n39{"collectivist_ethos"}
        n40{"liberty_ethos"}
    end
    subgraph tier_2["Tier 2"]
        n41["internationalism_focus"]
        n42["interventionism_focus"]
        n43["nationalism_focus"]
        n44["neutrality_focus"]
    end
    subgraph tier_3["Tier 3"]
        n45["deterrence"]
        n46["militarism"]
        n47["political_correctness"]
        n48["volunteer_corps"]
    end
    subgraph tier_4["Tier 4"]
        n49["foreign_expeditions"]
        n50["indoctrination_focus"]
        n51["military_youth"]
    end
    subgraph tier_5["Tier 5"]
        n52["paramilitarism"]
        n53["political_commissars"]
        n54["why_we_fight"]
    end
    subgraph tier_6["Tier 6"]
        n55["ideological_fanaticism"]
    end
    subgraph tier_7["Tier 7"]
        n56["technology_sharing"]
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
