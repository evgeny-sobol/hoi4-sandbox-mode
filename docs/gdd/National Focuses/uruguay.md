# URG_blanco_victory

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["URG_accion_revisionista_del_uruguay"]
        n2(("URG_blanco_victory"))
        n3["URG_break_diplomatic_relations_with_the_axis"]
        n4["URG_colorado_victory"]
    end
    subgraph tier_1["Tier 1"]
        n5["URG_herrerismo"]
        n6["URG_traditionalism"]
    end
    subgraph tier_2["Tier 2"]
        n7["URG_americanism"]
        n8["URG_ruralism"]
    end
    subgraph tier_3["Tier 3"]
        n9["URG_anti_imperialism"]
        n10["URG_anticentralism"]
    end
    subgraph tier_4["Tier 4"]
        n11["URG_join_the_allies"]
    end
    n6 --> n7
    n7 --> n9
    n8 --> n10
    n2 --> n5
    n3 --> n11
    n10 --> n11
    n5 --> n8
    n6 --> n8
    n2 --> n6
    n1 x--x n2
    n2 x--x n4
```

# URG_colorado_victory

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["URG_accion_revisionista_del_uruguay"]
        n10["URG_anticentralism"]
        n2["URG_blanco_victory"]
        n4(("URG_colorado_victory"))
    end
    subgraph tier_1["Tier 1"]
        n12["URG_a_new_constitution"]
        n13["URG_declare_neutrality"]
        n14["URG_legacy_of_batlle"]
        n15["URG_legalize_the_pool"]
    end
    subgraph tier_2["Tier 2"]
        n16["URG_investigate_german_and_italian_cultural_organization"]
        n17["URG_law_no_9914"]
        n18["URG_law_no_9943"]
        n19["URG_the_good_coup"]
    end
    subgraph tier_3["Tier 3"]
        n20["URG_american_air_bases"]
        n3["URG_break_diplomatic_relations_with_the_axis"]
    end
    subgraph tier_4["Tier 4"]
        n11["URG_join_the_allies"]
    end
    n4 --> n12
    n16 --> n20
    n18 --> n20
    n16 --> n3
    n18 --> n3
    n4 --> n13
    n13 --> n16
    n3 --> n11
    n10 --> n11
    n13 --> n17
    n13 --> n18
    n4 --> n14
    n4 --> n15
    n12 --> n19
    n1 x--x n4
    n2 x--x n4
```

# URG_terras_dictatorship

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n2["URG_blanco_victory"]
        n4["URG_colorado_victory"]
        n21(("URG_terras_dictatorship"))
    end
    subgraph tier_1["Tier 1"]
        n22["URG_prohibition_of_usury"]
        n23["URG_statism"]
        n24["URG_womens_vote"]
    end
    subgraph tier_2["Tier 2"]
        n25["URG_break_relations_with_the_ussr"]
        n26["URG_ministry_of_public_works"]
        n27["URG_revaluation_law"]
        n28["URG_right_to_food_housing_and_health"]
    end
    subgraph tier_3["Tier 3"]
        n29["URG_brou"]
        n30["URG_import_substitution"]
        n31["URG_rapid_industrialization"]
        n32["URG_recognize_francoist_spain"]
        n33["URG_rincon_del_bonete_hydroelectric_power_station"]
        n34["URG_tour_to_italy"]
    end
    subgraph tier_4["Tier 4"]
        n35{"URG_allow_nazi_movements_among_german_uruguayan"}
        n36["URG_conaprole"]
        n37["URG_la_teja_refinery"]
        n38["URG_mercado_modelo"]
        n39{"URG_merge_falangist_movements"}
        n40["URG_pay_of_all_external_debts"]
        n41["URG_pluna"]
    end
    subgraph tier_5["Tier 5"]
        n1["URG_accion_revisionista_del_uruguay"]
    end
    subgraph tier_6["Tier 6"]
        n42["URG_establish_the_german_uruguayan_cultural_center"]
        n43["URG_force_through_corporatism"]
    end
    subgraph tier_7["Tier 7"]
        n44["URG_the_fuhrmann_plan"]
    end
    subgraph tier_8["Tier 8"]
        n45["URG_food_for_the_warmachine"]
    end
    n35 --> n1
    n39 --> n1
    n33 --> n35
    n23 --> n25
    n27 --> n29
    n31 --> n36
    n1 --> n42
    n44 --> n45
    n1 --> n43
    n26 --> n30
    n31 --> n37
    n31 --> n38
    n32 --> n39
    n22 --> n26
    n29 --> n40
    n31 --> n41
    n21 --> n22
    n26 --> n31
    n25 --> n32
    n22 --> n27
    n23 --> n28
    n25 --> n33
    n21 --> n23
    n42 --> n44
    n25 --> n34
    n21 --> n24
    n1 x--x n2
    n1 x--x n4
```
