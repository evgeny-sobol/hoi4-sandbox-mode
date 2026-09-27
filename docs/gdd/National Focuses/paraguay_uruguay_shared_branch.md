# GUAY_disperse_military_power

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["GUAY_cult_of_personality"]
        n2(("GUAY_disperse_military_power"))
        n3["GUAY_form_ties_with_the_military"]
    end
    subgraph tier_1["Tier 1"]
        n4["GUAY_military_licenses"]
        n5["GUAY_nationalize_foreign_owned_companies"]
    end
    subgraph tier_2["Tier 2"]
        n6["GUAY_abolish_low_level_income_tax"]
        n7["GUAY_cooperation_in_the_americas"]
        n8["GUAY_urbanization"]
    end
    subgraph tier_3["Tier 3"]
        n9["GUAY_defense_force"]
        n10["GUAY_free_seconday_schools"]
    end
    subgraph tier_4["Tier 4"]
        n11["GUAY_adopt_minority_languages"]
        n12["GUAY_mythologize_the_father_of_the_nation"]
        n13["GUAY_specialized_terrain_training"]
        n14["GUAY_volunteers"]
    end
    subgraph tier_5["Tier 5"]
        n15["GUAY_mass_drafts"]
    end
    n5 --> n6
    n1 --> n11
    n10 --> n11
    n5 --> n7
    n7 --> n9
    n8 --> n10
    n6 --> n10
    n13 --> n15
    n14 --> n15
    n3 --> n4
    n2 --> n4
    n1 --> n12
    n10 --> n12
    n2 --> n5
    n9 --> n13
    n5 --> n8
    n9 --> n14
    n2 x--x n3
```

# GUAY_form_ties_with_the_military

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n2["GUAY_disperse_military_power"]
        n3(("GUAY_form_ties_with_the_military"))
        n10["GUAY_free_seconday_schools"]
    end
    subgraph tier_1["Tier 1"]
        n16["GUAY_coup_detat"]
        n17["GUAY_enact_martial_law"]
        n4["GUAY_military_licenses"]
        n18["GUAY_place_opposition_leaders_in_house_arrest"]
    end
    subgraph tier_2["Tier 2"]
        n19["GUAY_a_domestic_arms_factory"]
        n20["GUAY_appease_the_generals"]
        n1["GUAY_cult_of_personality"]
        n21["GUAY_penal_battalions"]
    end
    subgraph tier_3["Tier 3"]
        n11["GUAY_adopt_minority_languages"]
        n22["GUAY_mobalize_the_economy"]
        n12["GUAY_mythologize_the_father_of_the_nation"]
        n23["GUAY_the_permanent_leader"]
    end
    n16 --> n19
    n1 --> n11
    n10 --> n11
    n16 --> n20
    n3 --> n16
    n16 --> n1
    n3 --> n17
    n3 --> n4
    n2 --> n4
    n19 --> n22
    n1 --> n12
    n10 --> n12
    n16 --> n21
    n3 --> n18
    n20 --> n23
    n1 --> n23
    n2 x--x n3
```

# GUAY_laissez_faire

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n24(("GUAY_laissez_faire"))
        n25["GUAY_workers_rights"]
    end
    subgraph tier_1["Tier 1"]
        n26["GUAY_empower_the_land_owners"]
    end
    subgraph tier_2["Tier 2"]
        n27["GUAY_agricultural_colonization"]
        n28["GUAY_river_trade"]
    end
    subgraph tier_3["Tier 3"]
        n29["GUAY_beef_and_hide_industry"]
        n30["GUAY_cash_crop_exports"]
        n31["GUAY_export_focus"]
        n32["GUAY_heavy_industry"]
    end
    subgraph tier_4["Tier 4"]
        n33["GUAY_wool_makers"]
    end
    n25 --> n27
    n26 --> n27
    n27 --> n29
    n28 --> n30
    n24 --> n26
    n28 --> n31
    n27 --> n32
    n26 --> n28
    n25 --> n28
    n29 --> n33
```

# GUAY_land_reforms

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n26["GUAY_empower_the_land_owners"]
        n34(("GUAY_land_reforms"))
    end
    subgraph tier_1["Tier 1"]
        n25["GUAY_workers_rights"]
    end
    subgraph tier_2["Tier 2"]
        n27["GUAY_agricultural_colonization"]
        n28["GUAY_river_trade"]
    end
    subgraph tier_3["Tier 3"]
        n29["GUAY_beef_and_hide_industry"]
        n30["GUAY_cash_crop_exports"]
        n31["GUAY_export_focus"]
        n32["GUAY_heavy_industry"]
    end
    subgraph tier_4["Tier 4"]
        n33["GUAY_wool_makers"]
    end
    n25 --> n27
    n26 --> n27
    n27 --> n29
    n28 --> n30
    n28 --> n31
    n27 --> n32
    n26 --> n28
    n25 --> n28
    n29 --> n33
    n34 --> n25
```

# GUAY_meet_with_the_old_powers

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n35(("GUAY_meet_with_the_old_powers"))
    end
    subgraph tier_1["Tier 1"]
        n36["GUAY_long_term_contracts"]
    end
    n35 --> n36
```

# GUAY_rekindle_old_gripes

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n37{"GUAY_rekindle_old_gripes"}
    end
    subgraph tier_1["Tier 1"]
        n38{"GUAY_clamp_down_on_new_territories"}
        n39{"GUAY_develop_new_territories"}
    end
    subgraph tier_2["Tier 2"]
        n40["GUAY_a_deal_with_devil"]
        n41["GUAY_no_second_american_colonization"]
    end
    subgraph tier_3["Tier 3"]
        n42["GUAY_demand_a_seat_at_the_high_table"]
        n43["GUAY_the_stuff_of_legends"]
    end
    n38 --> n40
    n39 --> n40
    n37 --> n38
    n40 --> n42
    n37 --> n39
    n39 --> n41
    n38 --> n41
    n41 --> n43
    n40 x--x n41
    n38 x--x n39
```

# GUAY_the_tag_economic_miracle

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n44(("GUAY_the_tag_economic_miracle"))
    end
    subgraph tier_1["Tier 1"]
        n45["GUAY_exploit_mineral_wealth"]
        n46["GUAY_protect_domestic_industries"]
    end
    subgraph tier_2["Tier 2"]
        n47["GUAY_national_academy_of_sciences"]
    end
    subgraph tier_3["Tier 3"]
        n48["GUAY_national_academy_of_sciences_2"]
    end
    subgraph tier_4["Tier 4"]
        n49["GUAY_national_academy_of_sciences_3"]
    end
    n44 --> n45
    n46 --> n47
    n45 --> n47
    n47 --> n48
    n48 --> n49
    n44 --> n46
```
