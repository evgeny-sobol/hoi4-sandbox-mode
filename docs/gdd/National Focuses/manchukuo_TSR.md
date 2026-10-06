# MAN_tsr_pacify_the_countryside

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("MAN_tsr_pacify_the_countryside"))
    end
    subgraph tier_1["Tier 1"]
        n2{"MAN_tsr_army_modernization"}
        n3["MAN_tsr_invite_japanese_settlers"]
        n4{"MAN_tsr_trade_delegation"}
    end
    subgraph tier_2["Tier 2"]
        n5["MAN_tsr_assertiveness"]
        n6["MAN_tsr_collective_farms"]
        n7["MAN_tsr_expand_the_textile_industry"]
        n8["MAN_tsr_mukden_military_academy"]
        n9["MAN_tsr_obedience"]
    end
    subgraph tier_3["Tier 3"]
        n10["MAN_tsr_expand_the_navy"]
        n11["MAN_tsr_first_five_year_plan"]
        n12["MAN_tsr_hoankyoku"]
        n13["MAN_tsr_law_university"]
        n14{"MAN_tsr_request_control_of_the_railways"}
    end
    subgraph tier_4["Tier 4"]
        n15["MAN_tsr_alliance_with_the_kwantung_army"]
        n16{"MAN_tsr_five_equal_peoples"}
        n17["MAN_tsr_invite_japanese_investors"]
        n18["MAN_tsr_mukden_arsenal"]
        n19["MAN_tsr_research_and_education_department"]
        n20{"MAN_tsr_staff_the_court_with_manchus"}
        n21["MAN_tsr_trading_illicit_goods"]
    end
    subgraph tier_5["Tier 5"]
        n22["MAN_tsr_bolster_nationalism"]
        n23["MAN_tsr_empower_the_legislative_council"]
        n24["MAN_tsr_expand_showa_steel_works"]
        n25["MAN_tsr_expand_the_imperial_guards"]
        n26["MAN_tsr_expand_the_railways"]
        n27["MAN_tsr_further_mobilization"]
        n28["MAN_tsr_mamc"]
        n29["MAN_tsr_question_the_emperors_authority"]
        n30["MAN_tsr_request_dalian"]
        n31["MAN_tsr_strengthen_the_manchukuo_imperial_army"]
        n32["MAN_tsr_strengthen_ties_with_nissan"]
        n33["MAN_tsr_white_russian_advisers"]
    end
    subgraph tier_6["Tier 6"]
        n34["MAN_tsr_bandit_recruitment"]
        n35["MAN_tsr_develop_aluminum_sources"]
        n36["MAN_tsr_expand_xingan_army"]
        n37["MAN_tsr_five_people_armies"]
        n38["MAN_tsr_local_arms_procurement"]
        n39["MAN_tsr_mangyo"]
        n40["MAN_tsr_purge_the_general_affairs_council"]
        n41["MAN_tsr_social_research_unit"]
        n42{"MAN_tsr_the_question_of_leadership"}
    end
    subgraph tier_7["Tier 7"]
        n43{"MAN_tsr_a_new_dawn_over_manchuria"}
        n44["MAN_tsr_ally_bandit_leaders"]
        n45["MAN_tsr_chinese_leadership"]
        n46["MAN_tsr_empire_of_manchukuo"]
        n47{"MAN_tsr_independence_war"}
        n48["MAN_tsr_persuade_the_IMPRP"]
        n49["MAN_tsr_reform_the_civil_service"]
        n50["MAN_tsr_second_five_year_plan"]
    end
    subgraph tier_8["Tier 8"]
        n51["MAN_tsr_a_new_constitution"]
        n52{"MAN_tsr_depose_puyi"}
        n53["MAN_tsr_embrace_state_shintoism"]
        n54["MAN_tsr_imperial_divinity"]
        n55["MAN_tsr_national_cooperation_government"]
        n56["MAN_tsr_national_defense_state"]
        n57["MAN_tsr_vassalize_mengukuo"]
    end
    subgraph tier_9["Tier 9"]
        n58["MAN_tsr_division_of_power"]
        n59["MAN_tsr_promote_manchu_identity"]
        n60["MAN_tsr_reclaim_our_lost_possessions"]
        n61["MAN_tsr_reestablish_the_qing_army"]
        n62["MAN_tsr_the_new_beiyang_government"]
        n63["MAN_tsr_the_two_emperors"]
        n64["MAN_tsr_work_with_the_kempeitai"]
        n65["MAN_tsr_zhao_shangzhis_coup"]
    end
    subgraph tier_10["Tier 10"]
        n66["MAN_tsr_ally_the_soviet_republic"]
        n67["MAN_tsr_beiyang_university"]
        n68["MAN_tsr_claim_outer_manchuria"]
        n69["MAN_tsr_raise_the_yong_ying"]
        n70{"MAN_tsr_reclaim_the_empire"}
        n71["MAN_tsr_reform_the_army"]
        n72["MAN_tsr_the_southern_expedition"]
    end
    subgraph tier_11["Tier 11"]
        n73["MAN_tsr_assert_our_authority"]
        n74["MAN_tsr_imperial_university"]
        n75["MAN_tsr_offer_vassalization"]
        n76["MAN_tsr_proclaim_the_republic_of_china"]
        n77["MAN_tsr_research_cooperation"]
        n78["MAN_tsr_soviet_aid"]
        n79["MAN_tsr_the_long_march_south"]
    end
    subgraph tier_12["Tier 12"]
        n80["MAN_tsr_a_new_self_strengthening_movement"]
        n81["MAN_tsr_an_industrial_power"]
        n82["MAN_tsr_finish_off_the_japanese_threat"]
        n83["MAN_tsr_move_capitals"]
        n84["MAN_tsr_proclaim_the_peoples_republic"]
        n85["MAN_tsr_reestablish_the_gansu_braves"]
        n86["MAN_tsr_request_our_lost_territories"]
    end
    subgraph tier_13["Tier 13"]
        n87["MAN_tsr_claim_the_mandate_of_heaven"]
    end
    n47 --> n51
    n34 --> n43
    n73 --> n80
    n75 --> n80
    n11 --> n15
    n34 --> n44
    n65 --> n66
    n76 --> n81
    n1 --> n2
    n70 --> n73
    n4 --> n5
    n29 --> n34
    n62 --> n67
    n20 --> n22
    n16 --> n22
    n42 --> n45
    n59 --> n68
    n64 --> n68
    n83 --> n87
    n3 --> n6
    n43 --> n52
    n24 --> n35
    n51 --> n58
    n46 --> n53
    n42 --> n46
    n16 --> n23
    n17 --> n24
    n20 --> n25
    n9 --> n10
    n17 --> n26
    n4 --> n7
    n31 --> n36
    n76 --> n82
    n9 --> n11
    n14 --> n16
    n33 --> n37
    n15 --> n27
    n9 --> n12
    n47 --> n54
    n70 --> n74
    n40 --> n47
    n11 --> n17
    n1 --> n3
    n6 --> n13
    n8 --> n13
    n7 --> n13
    n25 --> n38
    n18 --> n28
    n32 --> n39
    n24 --> n39
    n26 --> n39
    n73 --> n83
    n75 --> n83
    n11 --> n18
    n2 --> n8
    n45 --> n55
    n50 --> n56
    n2 --> n9
    n70 --> n75
    n34 --> n48
    n79 --> n84
    n72 --> n76
    n53 --> n59
    n22 --> n40
    n16 --> n29
    n61 --> n69
    n54 --> n60
    n61 --> n70
    n73 --> n85
    n75 --> n85
    n54 --> n61
    n51 --> n61
    n62 --> n71
    n40 --> n49
    n5 --> n14
    n15 --> n30
    n66 --> n86
    n79 --> n86
    n13 --> n19
    n66 --> n77
    n39 --> n50
    n26 --> n41
    n66 --> n78
    n14 --> n20
    n15 --> n31
    n17 --> n32
    n66 --> n79
    n52 --> n62
    n31 --> n42
    n27 --> n42
    n62 --> n72
    n57 --> n63
    n55 --> n63
    n1 --> n4
    n11 --> n21
    n45 --> n57
    n16 --> n33
    n53 --> n64
    n52 --> n65
    n51 x--x n52
    n51 x--x n54
    n73 x--x n75
    n5 x--x n9
    n22 x--x n29
    n45 x--x n46
    n52 x--x n54
    n16 x--x n20
    n62 x--x n65
```
