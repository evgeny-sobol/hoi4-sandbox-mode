# HUN_balanced_budget

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("HUN_balanced_budget"))
        n2["HUN_economic_intervention"]
        n3["HUN_renew_the_rome_protocols"]
        n4["HUN_strengthen_fascists"]
    end
    subgraph tier_1["Tier 1"]
        n5["HUN_strengthen_the_monarchists"]
    end
    subgraph tier_2["Tier 2"]
        n6{"HUN_elect_a_king"}
    end
    subgraph tier_3["Tier 3"]
        n7["HUN_elect_a_democratic_king"]
        n8["HUN_elect_a_fascist_king"]
        n9{"HUN_invite_the_habsburg_prince"}
    end
    subgraph tier_4["Tier 4"]
        n10["HUN_demand_a_referendum"]
        n11{"HUN_renounce_the_treaty_of_trianon"}
        n12["HUN_responsible_government"]
        n13["HUN_take_austria_by_force"]
    end
    subgraph tier_5["Tier 5"]
        n14["HUN_proclaim_the_restoration_of_austria_hungary"]
        n15{"HUN_rapproachement_with_little_entente"}
        n16["HUN_reaffirm_territorial_claims"]
        n17["HUN_trade_deal_with_germany"]
    end
    subgraph tier_6["Tier 6"]
        n18["HUN_demand_southern_slovakia"]
        n19["HUN_demand_transylvania"]
        n20["HUN_join_allies"]
        n21["HUN_joint_aluminum_mining_company"]
        n22["HUN_protect_czechoslovakia"]
        n23["HUN_the_balkan_pact"]
    end
    subgraph tier_7["Tier 7"]
        n24["HUN_an_unlikely_alliance"]
        n25["HUN_claim_galicia"]
        n26["HUN_claim_overlordship_over_slovakia"]
        n27["HUN_claim_transylvania"]
        n28["HUN_demand_the_vojvodina"]
        n29["HUN_join_axis"]
        n30["HUN_joint_oil_exploitation_company"]
    end
    subgraph tier_8["Tier 8"]
        n31["HUN_claim_the_bucovina"]
        n32["HUN_march_to_the_shore"]
        n33["HUN_proclaim_greater_hungary"]
    end
    subgraph tier_9["Tier 9"]
        n34["HUN_reclaim_venetia"]
    end
    subgraph tier_10["Tier 10"]
        n35["HUN_reclaim_the_empire"]
    end
    n23 --> n24
    n22 --> n25
    n18 --> n26
    n25 --> n31
    n22 --> n27
    n9 --> n10
    n16 --> n18
    n19 --> n28
    n18 --> n28
    n16 --> n19
    n6 --> n7
    n6 --> n8
    n5 --> n6
    n6 --> n9
    n15 --> n20
    n21 --> n29
    n17 --> n21
    n20 --> n30
    n27 --> n32
    n28 --> n33
    n10 --> n14
    n13 --> n14
    n14 --> n22
    n12 --> n15
    n11 --> n16
    n34 --> n35
    n31 --> n35
    n32 --> n34
    n4 --> n11
    n8 --> n11
    n7 --> n12
    n1 --> n5
    n9 --> n13
    n15 --> n23
    n11 --> n17
    n1 x--x n2
    n10 x--x n13
    n7 x--x n8
    n7 x--x n9
    n8 x--x n9
    n20 x--x n23
    n3 x--x n17
```

# HUN_economic_intervention

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1["HUN_balanced_budget"]
        n2{"HUN_economic_intervention"}
        n8["HUN_elect_a_fascist_king"]
    end
    subgraph tier_1["Tier 1"]
        n36["HUN_council_of_peoples_commissars"]
        n4{"HUN_strengthen_fascists"}
    end
    subgraph tier_2["Tier 2"]
        n37{"HUN_assassinate_horthy"}
        n3["HUN_renew_the_rome_protocols"]
        n11{"HUN_renounce_the_treaty_of_trianon"}
    end
    subgraph tier_3["Tier 3"]
        n38["HUN_join_comintern"]
        n39["HUN_protect_austria"]
        n16["HUN_reaffirm_territorial_claims"]
        n40["HUN_the_hungarian_red_army"]
        n41["HUN_the_revolutionary_council"]
        n17["HUN_trade_deal_with_germany"]
    end
    subgraph tier_4["Tier 4"]
        n42["HUN_alliance_with_italy"]
        n18["HUN_demand_southern_slovakia"]
        n19["HUN_demand_transylvania"]
        n43["HUN_intervene_in_czechoslovakia"]
        n21["HUN_joint_aluminum_mining_company"]
        n44["HUN_pressure_romania"]
        n45["HUN_soviet_hungarian_military_academy"]
    end
    subgraph tier_5["Tier 5"]
        n26["HUN_claim_overlordship_over_slovakia"]
        n28["HUN_demand_the_vojvodina"]
        n29["HUN_join_axis"]
    end
    subgraph tier_6["Tier 6"]
        n33["HUN_proclaim_greater_hungary"]
    end
    n39 --> n42
    n36 --> n37
    n18 --> n26
    n2 --> n36
    n16 --> n18
    n19 --> n28
    n18 --> n28
    n16 --> n19
    n38 --> n43
    n21 --> n29
    n37 --> n38
    n17 --> n21
    n38 --> n44
    n28 --> n33
    n3 --> n39
    n11 --> n16
    n4 --> n3
    n4 --> n11
    n8 --> n11
    n40 --> n45
    n2 --> n4
    n37 --> n40
    n37 --> n41
    n11 --> n17
    n1 x--x n2
    n36 x--x n4
    n38 x--x n41
    n3 x--x n17
```

# HUN_industrial_revitalization

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n46{"HUN_establish_the_air_force"}
        n47(("HUN_industrial_revitalization"))
        n48["HUN_joint_air_development"]
        n49["HUN_license_foreign_designs"]
    end
    subgraph tier_1["Tier 1"]
        n50["HUN_reintegrate_the_railroads"]
    end
    subgraph tier_2["Tier 2"]
        n51["HUN_support_domestic_industry"]
        n52["HUN_support_urbanization"]
    end
    subgraph tier_3["Tier 3"]
        n53["HUN_institute_for_industrial_techniques"]
    end
    subgraph tier_4["Tier 4"]
        n54{"HUN_announce_the_gyor_program"}
    end
    subgraph tier_5["Tier 5"]
        n55["HUN_civilian_industry"]
        n56["HUN_domestic_arms_industry"]
    end
    subgraph tier_6["Tier 6"]
        n57["HUN_aeronautic_technology_institute"]
        n58["HUN_autarky"]
        n59["HUN_invite_foreign_investors"]
    end
    subgraph tier_7["Tier 7"]
        n60{"HUN_boost_hungarian_aviation_industry"}
        n61["HUN_expand_the_aluminum_industry"]
        n62["HUN_expand_the_manfred_weiss_steel_works"]
        n63["HUN_synthetic_industry"]
    end
    subgraph tier_8["Tier 8"]
        n64["HUN_expand_the_technical_university_of_budapest"]
        n65{"HUN_indigenous_designs"}
    end
    subgraph tier_9["Tier 9"]
        n66["HUN_cas_focus"]
        n67["HUN_heavy_fighter_effort"]
        n68["HUN_light_fighter_effort"]
        n69["HUN_tac_focus"]
    end
    n56 --> n57
    n53 --> n54
    n55 --> n58
    n56 --> n58
    n57 --> n60
    n65 --> n66
    n54 --> n55
    n54 --> n56
    n59 --> n61
    n59 --> n62
    n62 --> n64
    n61 --> n64
    n65 --> n67
    n46 --> n65
    n60 --> n65
    n52 --> n53
    n51 --> n53
    n55 --> n59
    n65 --> n68
    n47 --> n50
    n50 --> n51
    n50 --> n52
    n58 --> n63
    n65 --> n69
    n66 x--x n69
    n55 x--x n56
    n67 x--x n68
    n65 x--x n48
    n65 x--x n49
```

# HUN_secret_rearmament

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n60{"HUN_boost_hungarian_aviation_industry"}
        n70(("HUN_secret_rearmament"))
    end
    subgraph tier_1["Tier 1"]
        n71{"HUN_naval_warfare"}
        n72["HUN_theoretical_air_efforts"]
        n73["HUN_war_games"]
    end
    subgraph tier_2["Tier 2"]
        n74["HUN_bled_agreement"]
        n75["HUN_dockyards"]
        n76["HUN_reform"]
        n77["HUN_restauration"]
    end
    subgraph tier_3["Tier 3"]
        n78{"HUN_army_maneuvers"}
        n79["HUN_capital_ships"]
        n80["HUN_destroyer"]
        n46{"HUN_establish_the_air_force"}
        n81["HUN_submarines"]
    end
    subgraph tier_4["Tier 4"]
        n82["HUN_a_new_flagship"]
        n83["HUN_carriers"]
        n84["HUN_cruisers"]
        n85{"HUN_home_defense"}
        n65{"HUN_indigenous_designs"}
        n48["HUN_joint_air_development"]
        n49["HUN_license_foreign_designs"]
        n86{"HUN_mobile_focus"}
    end
    subgraph tier_5["Tier 5"]
        n87["HUN_assault_gun_focus"]
        n88["HUN_bomber_competition"]
        n66["HUN_cas_focus"]
        n89["HUN_danuvia_submachine_guns"]
        n90["HUN_develop_tanks"]
        n91["HUN_fighter_competition"]
        n67["HUN_heavy_fighter_effort"]
        n68["HUN_light_fighter_effort"]
        n69["HUN_tac_focus"]
        n92["HUN_the_botond"]
    end
    subgraph tier_6["Tier 6"]
        n93["HUN_armored_warfare"]
        n94["HUN_artillery_effort"]
        n95["HUN_joint_tank_procurement"]
        n96["HUN_light_infantry_divisions_doctrine"]
        n97["HUN_motorized_logistics"]
    end
    subgraph tier_7["Tier 7"]
        n98["HUN_form_parachute_battalions"]
        n99["HUN_mobile_corps_doctrine"]
    end
    n79 --> n82
    n92 --> n93
    n74 --> n78
    n89 --> n94
    n86 --> n87
    n85 --> n87
    n73 --> n74
    n72 --> n74
    n49 --> n88
    n77 --> n79
    n81 --> n83
    n65 --> n66
    n80 --> n84
    n85 --> n89
    n77 --> n80
    n76 --> n80
    n86 --> n90
    n71 --> n75
    n74 --> n46
    n49 --> n91
    n96 --> n98
    n65 --> n67
    n78 --> n85
    n46 --> n65
    n60 --> n65
    n46 --> n48
    n90 --> n95
    n87 --> n95
    n46 --> n49
    n65 --> n68
    n89 --> n96
    n93 --> n99
    n78 --> n86
    n92 --> n97
    n70 --> n71
    n71 --> n76
    n71 --> n77
    n76 --> n81
    n65 --> n69
    n86 --> n92
    n70 --> n72
    n70 --> n73
    n87 x--x n90
    n66 x--x n69
    n67 x--x n68
    n85 x--x n86
    n65 x--x n48
    n65 x--x n49
    n48 x--x n49
    n76 x--x n77
```
