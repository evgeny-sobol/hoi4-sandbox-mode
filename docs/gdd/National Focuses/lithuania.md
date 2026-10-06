# LIT_secure_a_loyal_cabinet

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["BALTIC_restore_workers_republic"]
        n2{"LIT_secure_a_loyal_cabinet"}
    end
    subgraph tier_1["Tier 1"]
        n3{"LIT_exile_voldemares"}
        n4["LIT_free_voldemares"]
        n5["LIT_integrate_the_opposition"]
        n6{"LIT_lithuanian_preservationism"}
        n7["LIT_rastikis_military_reforms"]
    end
    subgraph tier_2["Tier 2"]
        n8["LIT_a_king_for_our_people"]
        n9["LIT_a_martial_prime_minister"]
        n10["LIT_a_priestly_prime_minister"]
        n11["LIT_lithuanian_activist_front"]
        n12["LIT_organize_the_iron_wolf"]
        n13{"LIT_patriotic_education"}
        n14{"LIT_patriotic_socialism"}
        n15["LIT_purge_popular_resistance"]
        n16["LIT_root_out_the_iron_wolf"]
    end
    subgraph tier_3["Tier 3"]
        n17["LIT_a_new_noble_class"]
        n18["LIT_anti_communist_militia"]
        n19["LIT_arrest_nazis_in_memel"]
        n20["LIT_institute_royal_guards"]
        n21["LIT_lithuanian_youth"]
        n22["LIT_new_kind_of_iron_wolf"]
        n23["LIT_peace_with_poland"]
        n24["LIT_soviet_mutual_assistance"]
        n25["LIT_the_nation_and_its_power"]
        n26["LIT_the_nationalist_council"]
        n27{"LIT_unify_the_military"}
    end
    subgraph tier_4["Tier 4"]
        n28["LIT_abolish_the_presidency"]
        n29["LIT_fortify_memel"]
        n30{"LIT_peasants_reform"}
        n31["LIT_prepare_forest_brothers"]
        n32["LIT_presidential_reform"]
        n33["LIT_rapid_fortifications_in_the_east"]
        n34{"LIT_reminder_of_true_enemy"}
        n35["LIT_seek_ties_with_germany"]
        n36["LIT_state_media"]
        n37{"LIT_strength_in_unity"}
        n38{"LIT_victory_in_trust"}
    end
    subgraph tier_5["Tier 5"]
        n39["LIT_a_corporatist_economy"]
        n40["LIT_claim_lithuania_minor"]
        n41["LIT_claim_livonia"]
        n42["LIT_claim_livonia_monarchy"]
        n43["LIT_defence_from_above"]
        n44{"LIT_demand_vilnius"}
        n45{"LIT_expand_military_budget"}
        n46["LIT_exploit_the_international_bank"]
        n47{"LIT_indivisible_power_of_the_state"}
        n48["LIT_proclaim_greater_lithuania"]
        n49{"LIT_restore_public_elections"}
        n50["LIT_support_monarchism_in_POL"]
    end
    subgraph tier_6["Tier 6"]
        n51["LIT_appease_nazis"]
        n52["LIT_appease_soviets"]
        n53["LIT_arm_monarchist_militants"]
        n54["LIT_claim_greater_lithuania"]
        n55["LIT_claim_prussia"]
        n56["LIT_invade_poland"]
        n57["LIT_king_of_poland"]
        n58{"LIT_martial_law"}
        n59{"LIT_merge_the_military_and_civilian_governments"}
        n60["LIT_prepare_resistance"]
        n61["LIT_request_polish_occupation"]
        n62["LIT_support_polish_fascists"]
    end
    subgraph tier_7["Tier 7"]
        n63["LIT_POL_union"]
        n64["LIT_beyond_the_baltic"]
        n65["LIT_enforce_military_rule"]
        n66["LIT_formalize_baltic_entente"]
        n67["LIT_infiltrate_homeland"]
        n68["LIT_offer_military_basing"]
        n69["LIT_restore_order"]
        n70["LIT_underground_production_centers"]
    end
    subgraph tier_8["Tier 8"]
        n71["LIT_baltic_economic_union"]
        n72["LIT_expand_lithuanian_shipyards"]
        n73["LIT_greater_commonwealth"]
        n74["LIT_join_the_allies"]
        n75["LIT_lithuanian_rail"]
        n76["LIT_look_north"]
        n77["LIT_occupation"]
        n78["LIT_restore_greater_lithuania"]
    end
    subgraph tier_9["Tier 9"]
        n79["LIT_baltic_defence_army"]
        n80["LIT_merge_the_arms_industries"]
        n81["LIT_pan_baltic_bank"]
        n82["LIT_push_for_ruthenia"]
    end
    subgraph tier_10["Tier 10"]
        n83["LIT_merge_civilian_industries"]
        n84{"LIT_propose_baltic_union"}
        n85["LIT_warsaw_to_crimea_railway"]
    end
    subgraph tier_11["Tier 11"]
        n86["LIT_baltic_stronger_together"]
        n87["LIT_baltic_unification"]
    end
    n57 --> n63
    n32 --> n39
    n36 --> n39
    n3 --> n8
    n6 --> n8
    n6 --> n9
    n3 --> n9
    n8 --> n17
    n6 --> n10
    n3 --> n10
    n17 --> n28
    n20 --> n28
    n15 --> n18
    n47 --> n51
    n49 --> n51
    n47 --> n52
    n49 --> n52
    n50 --> n53
    n15 --> n19
    n71 --> n79
    n66 --> n71
    n49 --> n71
    n84 --> n86
    n84 --> n87
    n59 --> n64
    n49 --> n64
    n47 --> n64
    n42 --> n54
    n29 --> n40
    n29 --> n41
    n35 --> n41
    n28 --> n42
    n42 --> n55
    n33 --> n43
    n35 --> n44
    n29 --> n44
    n59 --> n65
    n58 --> n65
    n2 --> n3
    n63 --> n72
    n9 --> n45
    n26 --> n45
    n32 --> n45
    n36 --> n46
    n59 --> n66
    n49 --> n66
    n47 --> n66
    n27 --> n29
    n2 --> n4
    n54 --> n73
    n55 --> n73
    n63 --> n73
    n34 --> n47
    n38 --> n47
    n37 --> n47
    n60 --> n67
    n8 --> n20
    n2 --> n5
    n44 --> n56
    n64 --> n74
    n50 --> n57
    n4 --> n11
    n3 --> n11
    n2 --> n6
    n63 --> n75
    n12 --> n21
    n11 --> n21
    n66 --> n76
    n39 --> n58
    n45 --> n58
    n80 --> n83
    n75 --> n80
    n45 --> n59
    n11 --> n22
    n68 --> n77
    n52 --> n68
    n51 --> n68
    n4 --> n12
    n71 --> n81
    n7 --> n13
    n5 --> n14
    n14 --> n23
    n10 --> n30
    n26 --> n30
    n16 --> n31
    n21 --> n31
    n47 --> n60
    n49 --> n60
    n25 --> n32
    n35 --> n48
    n29 --> n48
    n81 --> n84
    n79 --> n84
    n7 --> n15
    n75 --> n82
    n21 --> n33
    n2 --> n7
    n18 --> n34
    n19 --> n34
    n44 --> n61
    n48 --> n78
    n69 --> n78
    n62 --> n69
    n56 --> n69
    n61 --> n69
    n34 --> n49
    n30 --> n49
    n37 --> n49
    n38 --> n49
    n3 --> n16
    n27 --> n35
    n13 --> n24
    n25 --> n36
    n23 --> n37
    n28 --> n50
    n44 --> n62
    n9 --> n25
    n10 --> n25
    n8 --> n25
    n9 --> n26
    n10 --> n26
    n60 --> n70
    n12 --> n27
    n24 --> n38
    n82 --> n85
    n1 x--x n2
    n8 x--x n9
    n8 x--x n10
    n9 x--x n10
    n51 x--x n52
    n51 x--x n60
    n52 x--x n60
    n86 x--x n87
    n64 x--x n65
    n64 x--x n66
    n65 x--x n66
    n3 x--x n4
    n29 x--x n35
    n47 x--x n59
    n47 x--x n49
    n56 x--x n61
    n56 x--x n62
    n59 x--x n49
    n23 x--x n24
    n61 x--x n62
```
