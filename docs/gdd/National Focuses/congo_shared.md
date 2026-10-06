# CONGO_belgian_congo

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("CONGO_belgian_congo"))
        n2["CONGO_congo_investments"]
        n3["CONGO_societe_generale_de_belgique"]
    end
    subgraph tier_1["Tier 1"]
        n4["CONGO_establish_university_of_louvain"]
        n5["CONGO_expand_villages"]
        n6["CONGO_free_enterprise_fund"]
        n7["CONGO_rawji_group"]
        n8["CONGO_secure_international_funding"]
        n9["CONGO_the_heart_of_africa"]
        n10["CONGO_weapon_repair_workshops"]
    end
    subgraph tier_2["Tier 2"]
        n11["CONGO_belgian_devaluation"]
        n12["CONGO_ccci"]
        n13["CONGO_force_publique"]
        n14["CONGO_forminiere"]
        n15["CONGO_french_congo"]
        n16["CONGO_jungle_industry"]
        n17["CONGO_regional_specialization"]
        n18["CONGO_ruanda_urundi"]
    end
    subgraph tier_3["Tier 3"]
        n19["CONGO_aviation_militaire_de_la_force_publique"]
        n20["CONGO_bakwanga_mine"]
        n21["CONGO_chefs_coutumiers"]
        n22["CONGO_colonial_ambitions"]
        n23["CONGO_congo_army"]
        n24{"CONGO_congos_place_in_the_world"}
        n25["CONGO_expand_tungsten_mines"]
        n26["CONGO_humanitarian_aid"]
        n27["CONGO_interfaith_school_subsidies"]
        n28["CONGO_modernize_force_publique"]
        n29["CONGO_prince_leopold_mine"]
        n30["CONGO_purchasing_commission"]
        n31["CONGO_rubber_plantations"]
        n32["CONGO_shinkolobwe_mine"]
    end
    subgraph tier_4["Tier 4"]
        n33["CONGO_appoint_van_overstraeten"]
        n34["CONGO_belgian_officer_corps"]
        n35["CONGO_congo_free_state"]
        n36["CONGO_develop_infrastructure"]
        n37["CONGO_dominion_of_congo"]
        n38["CONGO_establish_cometro"]
        n39["CONGO_expand_force_publique_recruitment"]
        n40["CONGO_expand_metallurgical_industry"]
        n41["CONGO_expand_ndolo_and_elisabethville_airports"]
        n42["CONGO_expanded_rubber_plantations"]
        n43["CONGO_jungle_fighting"]
        n44["CONGO_kasai_secessionist_state"]
        n45["CONGO_new_vegetable_produce_markets"]
        n46["CONGO_overseas_department_of_belgium"]
        n47["CONGO_separate_corporations_from_politics"]
        n48["CONGO_smuggle_diamonds"]
        n49["CONGO_smuggle_uranium"]
        n50["CONGO_societe_miniere_de_bakwanga"]
        n51["CONGO_soviet_interest"]
        n52["CONGO_uranium_development_trust"]
        n53{"CONGO_whispers_of_independence"}
    end
    subgraph tier_5["Tier 5"]
        n54["CONGO_antwerp_diamond_district"]
        n55["CONGO_compagnie_belge_maritime_du_congo"]
        n56["CONGO_congolese_generals"]
        n57["CONGO_copper_cartridges"]
        n58["CONGO_even_a_hospital_can_do_better"]
        n59["CONGO_heat_resistant_cobalt"]
        n60["CONGO_improved_employment_contracts"]
        n61["CONGO_office_des_transports_coloniaux"]
        n62["CONGO_republic_of_congo"]
        n63["CONGO_research_grants"]
    end
    subgraph tier_6["Tier 6"]
        n64["CONGO_african_union"]
        n65["CONGO_expand_matadi_seaport"]
        n66["CONGO_gold_and_diamonds"]
        n67["CONGO_great_war_of_africa"]
        n68["CONGO_legacy_of_lake_tanganyika"]
    end
    n62 --> n64
    n50 --> n54
    n23 --> n33
    n13 --> n19
    n14 --> n20
    n9 --> n11
    n23 --> n34
    n3 --> n12
    n9 --> n12
    n17 --> n21
    n15 --> n22
    n36 --> n55
    n45 --> n55
    n13 --> n23
    n24 --> n35
    n34 --> n56
    n17 --> n24
    n40 --> n57
    n21 --> n36
    n24 --> n37
    n24 --> n38
    n1 --> n4
    n39 --> n58
    n23 --> n39
    n55 --> n65
    n29 --> n40
    n19 --> n41
    n18 --> n25
    n1 --> n5
    n31 --> n42
    n9 --> n13
    n3 --> n14
    n9 --> n14
    n1 --> n6
    n9 --> n15
    n54 --> n66
    n62 --> n67
    n40 --> n59
    n17 --> n26
    n36 --> n60
    n11 --> n27
    n28 --> n43
    n9 --> n16
    n20 --> n44
    n55 --> n68
    n13 --> n28
    n21 --> n45
    n36 --> n61
    n24 --> n46
    n12 --> n29
    n17 --> n30
    n1 --> n7
    n9 --> n17
    n53 --> n62
    n40 --> n63
    n48 --> n63
    n9 --> n18
    n16 --> n31
    n1 --> n8
    n27 --> n47
    n17 --> n32
    n20 --> n48
    n32 --> n49
    n29 --> n50
    n20 --> n50
    n24 --> n51
    n2 --> n9
    n1 --> n9
    n32 --> n52
    n1 --> n10
    n24 --> n53
    n35 x--x n37
    n35 x--x n46
    n35 x--x n62
    n37 x--x n46
    n37 x--x n62
    n46 x--x n62
```

# orphans

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n69["BEL_monetary_reconstruction"]
        n70["BEL_railway_expansion"]
    end
    subgraph tier_1["Tier 1"]
        n2["CONGO_congo_investments"]
    end
    subgraph tier_2["Tier 2"]
        n3["CONGO_societe_generale_de_belgique"]
    end
    subgraph tier_3["Tier 3"]
        n71["CONGO_cheap_labor"]
        n72["CONGO_symbiotic_industrialization"]
    end
    subgraph tier_4["Tier 4"]
        n73["CONGO_fuel_for_belgium"]
        n74["CONGO_requisition_funds"]
    end
    n3 --> n71
    n69 --> n2
    n71 --> n73
    n71 --> n74
    n2 --> n3
    n3 --> n72
    n70 --> n72
```
