# PAR_fedrerista_land_reforms

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["PAR_emergency_powers"]
        n2(("PAR_fedrerista_land_reforms"))
        n3["PAR_reach_out_to_european_contacts"]
    end
    subgraph tier_1["Tier 1"]
        n4["PAR_allow_unions_to_strike"]
        n5["PAR_ban_vouchers"]
        n6["PAR_military_pensions"]
        n7["PAR_order_italian_planes"]
        n8["PAR_rebuild_humaita"]
        n9["PAR_urbanization"]
    end
    subgraph tier_2["Tier 2"]
        n10["PAR_allow_women_workers"]
        n11["PAR_central_bank_of_paraguay"]
        n12{"PAR_chaco_war_decoration"}
    end
    subgraph tier_3["Tier 3"]
        n13{"PAR_a_great_charter"}
        n14["PAR_revenge_for_the_chaco_war"]
    end
    subgraph tier_4["Tier 4"]
        n15["PAR_access_the_sea"]
        n16["PAR_get_rid_of_obsolete_guns"]
        n17["PAR_invite_japanese_settlers"]
        n18["PAR_neuter_the_guion_rojo"]
        n19["PAR_pull_back_troops_from_the_chaco"]
    end
    subgraph tier_5["Tier 5"]
        n20["PAR_discipline_hierarchy_and_order"]
        n21["PAR_liga_nacional_independiente"]
        n22["PAR_suspend_elections"]
        n23["PAR_the_permanent_leader"]
        n24["PAR_union_nacional_revolucionaria"]
    end
    subgraph tier_6["Tier 6"]
        n25["PAR_adopt_minority_languages"]
        n26["PAR_align_with_the_guion_rojo"]
        n27["PAR_ban_the_liberal_party"]
        n28["PAR_get_rid_of_colonel_peredes"]
        n29["PAR_nationalize_foreign_owned_companies"]
    end
    subgraph tier_7["Tier 7"]
        n30["PAR_cult_of_personality"]
        n31{"PAR_ensure_army_loyalty"}
        n32["PAR_free_seconday_schools"]
        n33["PAR_mass_drafts"]
        n34["PAR_mythologize_the_father_of_the_nation"]
    end
    subgraph tier_8["Tier 8"]
        n35{"PAR_accept_american_loans"}
        n36["PAR_join_the_axis"]
        n37["PAR_nazify_the_army"]
        n38["PAR_radicalize_the_police"]
    end
    subgraph tier_9["Tier 9"]
        n39["PAR_agricultural_technical_assistence"]
        n40["PAR_join_the_cominterm"]
    end
    subgraph tier_10["Tier 10"]
        n41{"PAR_brazilian_road_finance"}
    end
    subgraph tier_11["Tier 11"]
        n42["PAR_join_the_allies"]
    end
    n11 --> n13
    n10 --> n13
    n31 --> n35
    n21 --> n35
    n1 --> n35
    n14 --> n15
    n21 --> n25
    n1 --> n25
    n35 --> n39
    n22 --> n26
    n2 --> n4
    n4 --> n10
    n5 --> n10
    n22 --> n27
    n2 --> n5
    n39 --> n41
    n5 --> n11
    n6 --> n12
    n21 --> n30
    n24 --> n30
    n26 --> n30
    n19 --> n20
    n28 --> n31
    n27 --> n31
    n25 --> n32
    n22 --> n28
    n14 --> n16
    n13 --> n17
    n41 --> n42
    n31 --> n36
    n35 --> n40
    n18 --> n21
    n25 --> n33
    n2 --> n6
    n21 --> n34
    n26 --> n34
    n1 --> n29
    n24 --> n29
    n31 --> n37
    n14 --> n18
    n3 --> n7
    n2 --> n7
    n13 --> n19
    n31 --> n38
    n2 --> n8
    n3 --> n8
    n12 --> n14
    n19 --> n22
    n19 --> n23
    n14 --> n23
    n18 --> n24
    n3 --> n9
    n2 --> n9
    n2 x--x n3
    n42 x--x n36
    n42 x--x n40
    n36 x--x n40
    n19 x--x n14
```

# PAR_reach_out_to_european_contacts

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n31["PAR_ensure_army_loyalty"]
        n2["PAR_fedrerista_land_reforms"]
        n36["PAR_join_the_axis"]
        n21["PAR_liga_nacional_independiente"]
        n3(("PAR_reach_out_to_european_contacts"))
        n24["PAR_union_nacional_revolucionaria"]
    end
    subgraph tier_1["Tier 1"]
        n43["PAR_a_call_out_for_aid"]
        n7["PAR_order_italian_planes"]
        n8["PAR_rebuild_humaita"]
        n44["PAR_request_weapons"]
        n45["PAR_to_cross_a_river"]
        n9["PAR_urbanization"]
    end
    subgraph tier_2["Tier 2"]
        n46["PAR_ask_for_bankroll"]
        n47["PAR_specialized_terrain_training"]
    end
    subgraph tier_3["Tier 3"]
        n48{"PAR_by_all_means_which_to_win"}
        n1["PAR_emergency_powers"]
    end
    subgraph tier_4["Tier 4"]
        n35{"PAR_accept_american_loans"}
        n25["PAR_adopt_minority_languages"]
        n49["PAR_assasinate_rafael_franco"]
        n50["PAR_goad_bolivia"]
        n29["PAR_nationalize_foreign_owned_companies"]
    end
    subgraph tier_5["Tier 5"]
        n39["PAR_agricultural_technical_assistence"]
        n32["PAR_free_seconday_schools"]
        n40["PAR_join_the_cominterm"]
        n33["PAR_mass_drafts"]
        n51["PAR_put_estigarribia_on_a_pedestal"]
    end
    subgraph tier_6["Tier 6"]
        n41{"PAR_brazilian_road_finance"}
        n52["PAR_purge_the_military_of_dissent"]
    end
    subgraph tier_7["Tier 7"]
        n53["PAR_aftermath_of_the_coup"]
        n42["PAR_join_the_allies"]
        n54["PAR_soliders_for_prisoners"]
    end
    n3 --> n43
    n31 --> n35
    n21 --> n35
    n1 --> n35
    n21 --> n25
    n1 --> n25
    n52 --> n53
    n35 --> n39
    n43 --> n46
    n48 --> n49
    n39 --> n41
    n46 --> n48
    n46 --> n1
    n25 --> n32
    n48 --> n50
    n41 --> n42
    n35 --> n40
    n25 --> n33
    n1 --> n29
    n24 --> n29
    n3 --> n7
    n2 --> n7
    n51 --> n52
    n49 --> n51
    n50 --> n51
    n2 --> n8
    n3 --> n8
    n3 --> n44
    n52 --> n54
    n45 --> n47
    n3 --> n45
    n3 --> n9
    n2 --> n9
    n49 x--x n50
    n2 x--x n3
    n42 x--x n36
    n42 x--x n40
    n36 x--x n40
```
