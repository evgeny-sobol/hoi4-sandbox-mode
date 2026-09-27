# ITA_air_innovations_bba

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n1(("ITA_air_innovations_bba"))
        n2["ITA_supermarina"]
    end
    subgraph tier_1["Tier 1"]
        n3["ITA_citta_dell_aria"]
        n4["ITA_expand_rome_flying_school"]
    end
    subgraph tier_2["Tier 2"]
        n5["ITA_diving_bombers"]
        n6["ITA_naval_air_coordination"]
        n7["ITA_reggianes_exports"]
        n8{"ITA_superaereo"}
    end
    subgraph tier_3["Tier 3"]
        n9["ITA_officers_of_the_service_role"]
        n10["ITA_specialization"]
        n11["ITA_standardization"]
    end
    subgraph tier_4["Tier 4"]
        n12["ITA_bomber_designs"]
        n13["ITA_fighter_designs"]
        n14["ITA_long_range_aircraft"]
        n15["ITA_multirole_aircraft"]
    end
    subgraph tier_5["Tier 5"]
        n16["ITA_supremacy_in_the_skies"]
    end
    n11 --> n12
    n10 --> n12
    n1 --> n3
    n3 --> n5
    n4 --> n5
    n1 --> n4
    n11 --> n13
    n10 --> n13
    n11 --> n14
    n10 --> n15
    n2 --> n6
    n4 --> n6
    n8 --> n9
    n4 --> n9
    n3 --> n7
    n8 --> n10
    n8 --> n11
    n3 --> n8
    n15 --> n16
    n14 --> n16
    n13 --> n16
    n12 --> n16
    n10 x--x n11
```

# ITA_army_primacy_bba

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17{"ITA_army_primacy_bba"}
        n18["ITA_fiocchi_munizioni"]
        n19["ITA_milan_comms_industry"]
    end
    subgraph tier_1["Tier 1"]
        n20["ITA_a_bandits_war"]
        n21["ITA_increase_artillery_production"]
        n22["ITA_preserve_army_traditions"]
    end
    subgraph tier_2["Tier 2"]
        n23["ITA_army_leaders"]
        n24["ITA_carica_di_isbuscenskij"]
        n25["ITA_italian_tankettes"]
        n26["ITA_moschettieri_del_duce"]
        n27["ITA_superesercito"]
        n28["ITA_vallo_alpino_del_littorio"]
    end
    subgraph tier_3["Tier 3"]
        n29["ITA_bersaglieri"]
        n30{"ITA_self_propelled_guns"}
    end
    subgraph tier_4["Tier 4"]
        n31["ITA_divisioni_alpine"]
        n32["ITA_end_fiat_ansaldo_duopoly"]
        n33["ITA_fanti_dell_aria"]
        n34["ITA_modernize_ansaldo_facilities"]
    end
    subgraph tier_5["Tier 5"]
        n35["ITA_ferrea_mole_ferreo_cuore"]
    end
    n17 --> n20
    n22 --> n23
    n20 --> n23
    n23 --> n29
    n27 --> n29
    n20 --> n24
    n29 --> n31
    n30 --> n32
    n29 --> n33
    n32 --> n35
    n34 --> n35
    n18 --> n21
    n17 --> n21
    n22 --> n25
    n20 --> n25
    n30 --> n34
    n22 --> n26
    n17 --> n22
    n27 --> n30
    n25 --> n30
    n22 --> n27
    n20 --> n27
    n19 --> n28
    n21 --> n28
    n20 x--x n22
    n32 x--x n34
```

# ITA_ethiopian_war_logistics_bba

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n36(("ITA_ethiopian_war_logistics_bba"))
        n37["ITA_italian_highways_bba"]
    end
    subgraph tier_1["Tier 1"]
        n38["ITA_ministry_of_italian_africa"]
    end
    subgraph tier_2["Tier 2"]
        n39["ITA_develop_eritrea"]
        n40["ITA_develop_ethiopia"]
        n41["ITA_develop_libya"]
        n42["ITA_develop_somaliland"]
    end
    subgraph tier_3["Tier 3"]
        n43{"ITA_regional_development"}
    end
    subgraph tier_4["Tier 4"]
        n44["ITA_litoranea_balbo"]
        n45["ITA_polizia_dell_africa_italiana"]
        n46["ITA_prospect_for_oil"]
        n47["ITA_strengthen_ascari_corps"]
    end
    subgraph tier_5["Tier 5"]
        n48["ITA_comandante_diavolo"]
        n49["ITA_libyan_railway"]
        n50["ITA_libyan_refineries"]
        n51["ITA_via_della_vittoria"]
    end
    n45 --> n48
    n47 --> n48
    n38 --> n39
    n38 --> n40
    n38 --> n41
    n38 --> n42
    n44 --> n49
    n46 --> n49
    n46 --> n50
    n43 --> n44
    n37 --> n38
    n36 --> n38
    n43 --> n45
    n43 --> n46
    n39 --> n43
    n41 --> n43
    n42 --> n43
    n40 --> n43
    n43 --> n47
    n44 --> n51
    n45 x--x n47
```

# ITA_italian_highways_bba

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n17["ITA_army_primacy_bba"]
        n36["ITA_ethiopian_war_logistics_bba"]
        n37{"ITA_italian_highways_bba"}
    end
    subgraph tier_1["Tier 1"]
        n18["ITA_fiocchi_munizioni"]
        n38["ITA_ministry_of_italian_africa"]
        n52["ITA_power_plants_in_terni"]
        n53["ITA_railway_innovations"]
        n54["ITA_steel_industry_in_terni"]
    end
    subgraph tier_2["Tier 2"]
        n55["ITA_brescia_small_arms_industry"]
        n39["ITA_develop_eritrea"]
        n40["ITA_develop_ethiopia"]
        n41["ITA_develop_libya"]
        n42["ITA_develop_somaliland"]
        n56["ITA_expand_foggia_farm_fields"]
        n21["ITA_increase_artillery_production"]
        n57{"ITA_industria_della_gomma_sintetica"}
        n58["ITA_investments_in_edison"]
        n19["ITA_milan_comms_industry"]
    end
    subgraph tier_3["Tier 3"]
        n59{"ITA_expand_national_universities"}
        n60["ITA_modernize_the_mezzogiorno"]
        n61{"ITA_redirect_alfa_romeo_production"}
        n43{"ITA_regional_development"}
        n62["ITA_strengthen_northern_industry"]
        n28["ITA_vallo_alpino_del_littorio"]
    end
    subgraph tier_4["Tier 4"]
        n63["ITA_increase_production"]
        n64["ITA_keep_specialization"]
        n44["ITA_litoranea_balbo"]
        n65["ITA_new_industrialization_program"]
        n45["ITA_polizia_dell_africa_italiana"]
        n46["ITA_prospect_for_oil"]
        n47["ITA_strengthen_ascari_corps"]
    end
    subgraph tier_5["Tier 5"]
        n48["ITA_comandante_diavolo"]
        n49["ITA_libyan_railway"]
        n50["ITA_libyan_refineries"]
        n66["ITA_thermojet_research"]
        n51["ITA_via_della_vittoria"]
    end
    n18 --> n55
    n45 --> n48
    n47 --> n48
    n38 --> n39
    n38 --> n40
    n38 --> n41
    n38 --> n42
    n53 --> n56
    n58 --> n59
    n37 --> n18
    n18 --> n21
    n17 --> n21
    n59 --> n63
    n61 --> n63
    n54 --> n57
    n52 --> n57
    n53 --> n58
    n59 --> n64
    n61 --> n64
    n44 --> n49
    n46 --> n49
    n46 --> n50
    n43 --> n44
    n18 --> n19
    n37 --> n38
    n36 --> n38
    n57 --> n60
    n62 --> n65
    n60 --> n65
    n59 --> n65
    n43 --> n45
    n37 --> n52
    n43 --> n46
    n37 --> n53
    n55 --> n61
    n19 --> n61
    n39 --> n43
    n41 --> n43
    n42 --> n43
    n40 --> n43
    n37 --> n54
    n43 --> n47
    n57 --> n62
    n63 --> n66
    n64 --> n66
    n19 --> n28
    n21 --> n28
    n44 --> n51
    n63 x--x n64
    n60 x--x n62
    n45 x--x n47
    n52 x--x n54
```

# ITA_naval_power_projection

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n4["ITA_expand_rome_flying_school"]
        n67(("ITA_naval_power_projection"))
    end
    subgraph tier_1["Tier 1"]
        n68["ITA_expand_naval_facilities"]
        n69["ITA_intensify_torpedo_manufacturing"]
        n70["ITA_oto_naval_guns"]
    end
    subgraph tier_2["Tier 2"]
        n71["ITA_forza_navale_especiale"]
        n72["ITA_improve_overseas_naval_bases"]
        n73["ITA_milizia_marittima_di_artiglieria"]
        n74["ITA_stockpile_fuel"]
        n2{"ITA_supermarina"}
    end
    subgraph tier_3["Tier 3"]
        n75["ITA_cooperation_programs"]
        n76["ITA_decima_flottiglia_mas"]
        n77["ITA_expand_naval_intelligence"]
        n78{"ITA_incrociatori_leggeri"}
        n79{"ITA_incrociatori_pesanti"}
        n6["ITA_naval_air_coordination"]
    end
    subgraph tier_4["Tier 4"]
        n80["ITA_cacciatorpediniere_di_scorta"]
        n81["ITA_cruiser_submarines"]
        n82["ITA_ispettorato_dei_mezzi_antisommergibili"]
        n83["ITA_midget_submarines"]
        n84["ITA_navi_da_battaglia"]
        n85["ITA_proper_carriers"]
        n86["ITA_refit_civilian_ships"]
    end
    subgraph tier_5["Tier 5"]
        n87["ITA_flotta_d_evasione"]
    end
    n78 --> n80
    n2 --> n75
    n78 --> n81
    n2 --> n76
    n67 --> n68
    n2 --> n77
    n82 --> n87
    n80 --> n87
    n84 --> n87
    n68 --> n71
    n68 --> n72
    n2 --> n78
    n2 --> n79
    n67 --> n69
    n78 --> n82
    n79 --> n82
    n78 --> n83
    n68 --> n73
    n2 --> n6
    n4 --> n6
    n79 --> n84
    n67 --> n70
    n79 --> n85
    n79 --> n86
    n68 --> n74
    n68 --> n2
    n81 x--x n83
    n78 x--x n79
    n85 x--x n86
```

# ITA_solid_progress

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n88{"ITA_conspiracies_in_the_shadows"}
        n89{"ITA_organize_strikes_in_the_north"}
        n90(("ITA_solid_progress"))
        n91["ITA_struggle_in_ethiopia"]
        n92["ITA_the_abyssinian_fiasco"]
        n93{"ITA_the_southern_farmlands"}
        n94["ITA_unite_the_opposition"]
    end
    subgraph tier_1["Tier 1"]
        n95["ITA_servizio_informazione_militare"]
    end
    subgraph tier_2["Tier 2"]
        n96{"ITA_triumph_in_africa_bba"}
    end
    subgraph tier_3["Tier 3"]
        n97["ITA_anglo_italian_agreements"]
        n98["ITA_convene_the_grand_council"]
        n99{"ITA_culto_del_duce"}
        n100["ITA_defy_the_duce"]
        n101["ITA_devaluate_the_lire"]
        n102{"ITA_foreign_affairs"}
        n103["ITA_liberate_gramsci"]
        n104["ITA_the_new_emperor_of_ethiopia"]
        n105["ITA_topple_amhara_rulers"]
    end
    subgraph tier_4["Tier 4"]
        n106["ITA_appeal_to_the_bourgeoisie"]
        n107{"ITA_balkan_ambition"}
        n108{"ITA_corpo_di_truppe_volontarie"}
        n109{"ITA_depose_mussolini"}
        n110["ITA_la_battaglia_del_grano"]
        n111["ITA_la_battaglia_per_la_terra"]
        n112["ITA_ministero_della_cultura_popolare"]
        n113{"ITA_potential_allies_in_the_balkans"}
        n114{"ITA_security_militias"}
        n115["ITA_seize_old_equipment"]
        n116{"ITA_the_ethiopian_question"}
        n117{"ITA_the_italian_republic"}
        n118{"ITA_the_man_of_providence"}
    end
    subgraph tier_5["Tier 5"]
        n119["ITA_abolish_the_colonies"]
        n120["ITA_albanian_occupation"]
        n121["ITA_battaglioni_d_assalto"]
        n122["ITA_believe_obey_fight"]
        n123["ITA_boost_the_grand_council_of_fascism"]
        n124["ITA_demand_balearic_islands_bba"]
        n125{"ITA_dino_grandi_focus"}
        n126["ITA_guarantee_austrian_independence"]
        n127{"ITA_italian_socialism"}
        n128{"ITA_italo_balbo_focus"}
        n129{"ITA_italy_first"}
        n130["ITA_la_battaglia_per_le_nascite"]
        n131["ITA_legge_bottai"]
        n132{"ITA_monarchia_d_italia"}
        n133["ITA_new_colonial_policies"]
        n134{"ITA_pact_of_steel"}
        n135["ITA_strengthen_the_blackshirts"]
        n136{"ITA_the_popular_front"}
        n137["ITA_to_live_as_a_lion"]
    end
    subgraph tier_6["Tier 6"]
        n138["ITA_a_leader_steps_forward"]
        n139["ITA_aid_for_the_spanish_republic"]
        n140["ITA_albanian_oil"]
        n141["ITA_banda_carita"]
        n142{"ITA_befriend_greece"}
        n143["ITA_befriend_japan"]
        n144{"ITA_common_ground"}
        n145["ITA_consolidate_power"]
        n146["ITA_cooperate_with_the_mafia"]
        n147["ITA_cooperatives_for_intensive_exploitation"]
        n148{"ITA_crush_the_mafia"}
        n149["ITA_empower_the_unions"]
        n150["ITA_extraction_industry"]
        n151["ITA_german_military_cooperation"]
        n152{"ITA_industrial_socialization"}
        n153["ITA_invite_france_to_military_partnership"]
        n154{"ITA_italian_irredentism"}
        n155["ITA_milizia_coloniale"]
        n156["ITA_negotiate_italian_claims"]
        n157["ITA_negotiations_with_albania"]
        n158{"ITA_power_to_the_king"}
        n159{"ITA_revoke_the_acerbo_law"}
        n160["ITA_seek_british_military_cooperation"]
        n161["ITA_spanish_italian_alliance"]
        n162{"ITA_stop_the_squandering"}
        n163{"ITA_strengthen_the_regime"}
        n164["ITA_support_albanian_irredentism"]
        n165["ITA_the_garibaldi_legion"]
        n166["ITA_the_italian_confederation"]
        n167["ITA_the_republics_leadership"]
        n168["ITA_treaty_with_germany"]
    end
    subgraph tier_7["Tier 7"]
        n169["ITA_a_new_era_for_the_red_shirts"]
        n170["ITA_albanian_fascist_militia"]
        n171["ITA_anglo_italian_pact"]
        n172["ITA_appease_the_military"]
        n173["ITA_banda_koch"]
        n174["ITA_befriend_portugal"]
        n175["ITA_bring_back_exiled_intellectuals"]
        n176["ITA_christian_democracy"]
        n177["ITA_condemn_colonialism"]
        n178["ITA_democratic_king"]
        n179{"ITA_devotion"}
        n180["ITA_disband_the_blackshirts"]
        n181["ITA_empower_the_carabinieri"]
        n182["ITA_enlist_the_bashkimi_kombetar"]
        n183["ITA_franco_italian_pact"]
        n184["ITA_gruppi_di_difesa_della_donna"]
        n185["ITA_institute_the_five_year_plan"]
        n186["ITA_mafia_abroad"]
        n187["ITA_new_corporations"]
        n188["ITA_planned_economy"]
        n189["ITA_political_commissars"]
        n190["ITA_prepare_for_the_coming_wars"]
        n191["ITA_production_lines"]
        n192["ITA_purge_the_party"]
        n193["ITA_ratify_the_stresa_front"]
        n194["ITA_reinforce_regia_aeronautica"]
        n195["ITA_reorganize_regio_esercito"]
        n196["ITA_reorganize_the_party"]
        n197["ITA_request_control_of_french_territories"]
        n198["ITA_sea_wolves_bba"]
        n199["ITA_secret_weapons"]
        n200["ITA_seek_papal_support"]
        n201["ITA_the_fight_overseas"]
        n202{"ITA_the_fourth_shore"}
        n203["ITA_the_path_to_progress"]
        n204["ITA_utilize_the_blackshirts"]
        n205["ITA_war_with_france"]
        n206{"ITA_war_with_greece"}
        n207["ITA_war_with_the_uk"]
    end
    subgraph tier_8["Tier 8"]
        n208["ITA_agents_of_the_church"]
        n209["ITA_army_modernization"]
        n210["ITA_ascari"]
        n211["ITA_befriend_turkey"]
        n212["ITA_bring_back_old_glories"]
        n213["ITA_claims_on_turkey_bba"]
        n214["ITA_compagnie_auto_avio_sahariane"]
        n215["ITA_cooperate_with_moderates"]
        n216["ITA_demand_ticino"]
        n217["ITA_economic_reforms"]
        n218["ITA_expand_intelligence_services"]
        n219["ITA_expand_the_royal_guard"]
        n220["ITA_irregulars"]
        n221["ITA_italys_destiny"]
        n222["ITA_joint_military_programs"]
        n223["ITA_liberate_the_workers_of_africa"]
        n224["ITA_meritocracy"]
        n225["ITA_mobilize_the_railway_guns"]
        n226["ITA_new_forms_of_weaponry"]
        n227["ITA_new_ricostruzione_industriale"]
        n228["ITA_oil_in_tripoli"]
        n229["ITA_proclaim_the_italian_empire"]
        n230["ITA_pugno_alzato"]
        n231{"ITA_social_stability"}
        n232["ITA_steel_in_tripoli"]
        n233{"ITA_the_fate_of_mussolini"}
        n234{"ITA_union_in_the_party"}
    end
    subgraph tier_9["Tier 9"]
        n235["ITA_a_greater_purpose"]
        n236["ITA_combined_land_and_air_warfare"]
        n237["ITA_crush_opposition"]
        n238["ITA_defend_the_land"]
        n239["ITA_divino_duce"]
        n240["ITA_follow_the_soviet_union"]
        n241["ITA_gloria_al_regno_d_italia"]
        n242["ITA_improve_the_industries"]
        n243["ITA_italia_libera"]
        n244["ITA_novus_ordo"]
        n245["ITA_paramilitary_training"]
        n246["ITA_reestablish_old_alliances"]
        n247["ITA_strengthen_the_papacy"]
        n248["ITA_the_eastern_threat"]
    end
    subgraph tier_10["Tier 10"]
        n249{"ITA_blackshirt_loyalty"}
        n250["ITA_european_democracies"]
        n251["ITA_expanded_corporatism"]
        n252["ITA_military_agreements"]
        n253["ITA_military_cooperation"]
        n254["ITA_raise_the_peoples"]
        n255["ITA_scientific_cooperation"]
        n256{"ITA_setting_course"}
        n257["ITA_special_brigades"]
        n258["ITA_spreading_the_eagles_wings"]
        n259["ITA_the_fight_against_stalinism"]
        n260["ITA_the_papacy_reborn"]
        n261["ITA_united_anarchist_confederations"]
    end
    subgraph tier_11["Tier 11"]
        n262["ITA_bring_down_fascist_strongholds"]
        n263["ITA_catholic_action"]
        n264["ITA_combined_research_effort"]
        n265["ITA_defense_against_capitalism"]
        n266["ITA_deus_vult"]
        n267["ITA_italian_hegemony"]
        n268["ITA_mare_nostrum_bba"]
        n269["ITA_peace_preservation"]
        n270["ITA_secure_the_borders"]
        n271["ITA_the_enemies_of_capitalism"]
        n272{"ITA_towards_a_greater_italy"}
    end
    subgraph tier_12["Tier 12"]
        n273["ITA_a_time_for_war"]
        n274["ITA_auxiliaries"]
        n275["ITA_bend_the_bars"]
        n276["ITA_capo_supremo"]
        n277["ITA_heroes_of_the_nation"]
        n278["ITA_iberian_protection"]
        n279["ITA_il_sol_dell_avvenire"]
        n280["ITA_il_vento_aureo"]
        n281["ITA_new_roman_citizens"]
        n282["ITA_the_holy_lands"]
        n283["ITA_the_italian_legions"]
    end
    subgraph tier_13["Tier 13"]
        n284["ITA_all_roads_lead_to_rome"]
        n285["ITA_masters_of_the_aegean"]
        n286["ITA_south_american_alliances"]
        n287["ITA_subdue_the_sentinels"]
        n288["ITA_the_catholic_dominion"]
    end
    subgraph tier_14["Tier 14"]
        n289["ITA_a_colonial_empire"]
        n290["ITA_caligulas_pride"]
        n291["ITA_masters_of_the_mediterranean"]
        n292["ITA_modern_musculus"]
        n293["ITA_the_king_of_the_skies"]
    end
    subgraph tier_15["Tier 15"]
        n294["ITA_by_blood_alone"]
    end
    n287 --> n289
    n233 --> n235
    n136 --> n138
    n165 --> n169
    n266 --> n273
    n116 --> n119
    n200 --> n208
    n127 --> n139
    n164 --> n170
    n113 --> n120
    n107 --> n120
    n120 --> n140
    n283 --> n284
    n96 --> n97
    n160 --> n171
    n100 --> n106
    n144 --> n172
    n172 --> n209
    n189 --> n209
    n181 --> n209
    n201 --> n210
    n268 --> n274
    n102 --> n107
    n122 --> n141
    n141 --> n173
    n114 --> n121
    n129 --> n142
    n134 --> n143
    n129 --> n143
    n161 --> n174
    n124 --> n174
    n206 --> n211
    n142 --> n211
    n112 --> n122
    n272 --> n275
    n239 --> n249
    n118 --> n123
    n167 --> n175
    n190 --> n212
    n255 --> n262
    n289 --> n294
    n284 --> n290
    n272 --> n276
    n179 --> n276
    n260 --> n263
    n159 --> n176
    n206 --> n213
    n142 --> n213
    n214 --> n236
    n253 --> n264
    n136 --> n144
    n127 --> n144
    n195 --> n214
    n194 --> n214
    n147 --> n177
    n128 --> n145
    n125 --> n145
    n96 --> n98
    n88 --> n98
    n176 --> n215
    n178 --> n215
    n127 --> n146
    n119 --> n147
    n102 --> n108
    n215 --> n237
    n218 --> n237
    n136 --> n148
    n127 --> n148
    n96 --> n99
    n234 --> n238
    n253 --> n265
    n89 --> n100
    n93 --> n100
    n96 --> n100
    n108 --> n124
    n205 --> n216
    n197 --> n216
    n159 --> n178
    n98 --> n109
    n260 --> n266
    n96 --> n101
    n137 --> n179
    n123 --> n179
    n163 --> n179
    n109 --> n125
    n158 --> n180
    n159 --> n180
    n233 --> n239
    n196 --> n217
    n148 --> n181
    n127 --> n149
    n157 --> n182
    n243 --> n250
    n178 --> n218
    n176 --> n218
    n180 --> n219
    n204 --> n219
    n224 --> n251
    n242 --> n251
    n132 --> n150
    n234 --> n240
    n96 --> n102
    n88 --> n102
    n153 --> n183
    n134 --> n151
    n219 --> n241
    n178 --> n241
    n165 --> n184
    n113 --> n126
    n107 --> n126
    n272 --> n277
    n179 --> n277
    n268 --> n278
    n266 --> n278
    n264 --> n279
    n254 --> n279
    n266 --> n280
    n217 --> n242
    n136 --> n152
    n152 --> n185
    n125 --> n153
    n132 --> n153
    n201 --> n220
    n231 --> n243
    n258 --> n267
    n134 --> n154
    n129 --> n154
    n117 --> n127
    n109 --> n128
    n113 --> n129
    n107 --> n129
    n193 --> n221
    n193 --> n222
    n99 --> n110
    n99 --> n111
    n110 --> n130
    n111 --> n130
    n118 --> n131
    n94 --> n103
    n96 --> n103
    n201 --> n223
    n146 --> n186
    n256 --> n268
    n163 --> n268
    n249 --> n268
    n275 --> n285
    n285 --> n291
    n196 --> n224
    n192 --> n224
    n246 --> n252
    n240 --> n253
    n121 --> n155
    n135 --> n155
    n99 --> n112
    n98 --> n112
    n190 --> n225
    n284 --> n292
    n109 --> n132
    n126 --> n156
    n119 --> n157
    n133 --> n157
    n116 --> n133
    n150 --> n187
    n190 --> n226
    n185 --> n227
    n268 --> n281
    n232 --> n244
    n228 --> n244
    n202 --> n228
    n113 --> n134
    n107 --> n134
    n219 --> n245
    n204 --> n245
    n250 --> n269
    n166 --> n188
    n152 --> n189
    n102 --> n113
    n132 --> n158
    n150 --> n190
    n171 --> n229
    n183 --> n229
    n149 --> n191
    n184 --> n230
    n169 --> n230
    n145 --> n192
    n162 --> n192
    n238 --> n254
    n156 --> n193
    n231 --> n246
    n128 --> n194
    n162 --> n194
    n128 --> n195
    n162 --> n195
    n125 --> n196
    n145 --> n196
    n134 --> n197
    n154 --> n197
    n132 --> n159
    n243 --> n255
    n246 --> n255
    n151 --> n198
    n151 --> n199
    n255 --> n270
    n99 --> n114
    n98 --> n114
    n125 --> n160
    n132 --> n160
    n158 --> n200
    n100 --> n115
    n90 --> n95
    n92 --> n95
    n91 --> n95
    n241 --> n256
    n237 --> n256
    n247 --> n256
    n175 --> n231
    n278 --> n286
    n108 --> n161
    n129 --> n161
    n240 --> n257
    n238 --> n257
    n235 --> n258
    n202 --> n232
    n128 --> n162
    n125 --> n162
    n114 --> n135
    n208 --> n247
    n130 --> n163
    n275 --> n287
    n120 --> n164
    n273 --> n288
    n282 --> n288
    n221 --> n248
    n252 --> n271
    n100 --> n116
    n192 --> n233
    n238 --> n259
    n147 --> n201
    n166 --> n201
    n128 --> n202
    n162 --> n202
    n136 --> n165
    n266 --> n282
    n133 --> n166
    n268 --> n283
    n100 --> n117
    n284 --> n293
    n99 --> n118
    n96 --> n104
    n247 --> n260
    n138 --> n203
    n117 --> n136
    n127 --> n167
    n118 --> n137
    n96 --> n105
    n163 --> n272
    n249 --> n272
    n256 --> n272
    n134 --> n168
    n95 --> n96
    n203 --> n234
    n238 --> n261
    n158 --> n204
    n154 --> n205
    n154 --> n206
    n129 --> n207
    n154 --> n207
    n235 x--x n239
    n119 x--x n133
    n172 x--x n181
    n172 x--x n189
    n107 x--x n113
    n121 x--x n135
    n142 x--x n206
    n211 x--x n213
    n123 x--x n137
    n276 x--x n277
    n176 x--x n178
    n98 x--x n99
    n98 x--x n100
    n146 x--x n148
    n99 x--x n100
    n238 x--x n240
    n124 x--x n161
    n125 x--x n128
    n125 x--x n132
    n180 x--x n204
    n181 x--x n189
    n126 x--x n129
    n126 x--x n134
    n153 x--x n160
    n243 x--x n246
    n127 x--x n136
    n128 x--x n132
    n129 x--x n134
    n110 x--x n111
    n268 x--x n272
    n228 x--x n232
    n158 x--x n159
    n194 x--x n195
    n197 x--x n205
    n90 x--x n91
    n90 x--x n92
```

# ITA_struggle_in_ethiopia

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n89{"ITA_organize_strikes_in_the_north"}
        n90["ITA_solid_progress"]
        n91(("ITA_struggle_in_ethiopia"))
        n92["ITA_the_abyssinian_fiasco"]
        n93{"ITA_the_southern_farmlands"}
        n94["ITA_unite_the_opposition"]
    end
    subgraph tier_1["Tier 1"]
        n95["ITA_servizio_informazione_militare"]
        n295["ITA_undermine_the_duce"]
    end
    subgraph tier_2["Tier 2"]
        n88{"ITA_conspiracies_in_the_shadows"}
        n96{"ITA_triumph_in_africa_bba"}
    end
    subgraph tier_3["Tier 3"]
        n97["ITA_anglo_italian_agreements"]
        n98["ITA_convene_the_grand_council"]
        n99{"ITA_culto_del_duce"}
        n100["ITA_defy_the_duce"]
        n101["ITA_devaluate_the_lire"]
        n102{"ITA_foreign_affairs"}
        n103["ITA_liberate_gramsci"]
        n104["ITA_the_new_emperor_of_ethiopia"]
        n105["ITA_topple_amhara_rulers"]
    end
    subgraph tier_4["Tier 4"]
        n106["ITA_appeal_to_the_bourgeoisie"]
        n107{"ITA_balkan_ambition"}
        n108{"ITA_corpo_di_truppe_volontarie"}
        n109{"ITA_depose_mussolini"}
        n110["ITA_la_battaglia_del_grano"]
        n111["ITA_la_battaglia_per_la_terra"]
        n112["ITA_ministero_della_cultura_popolare"]
        n113{"ITA_potential_allies_in_the_balkans"}
        n114{"ITA_security_militias"}
        n115["ITA_seize_old_equipment"]
        n116{"ITA_the_ethiopian_question"}
        n117{"ITA_the_italian_republic"}
        n118{"ITA_the_man_of_providence"}
    end
    subgraph tier_5["Tier 5"]
        n119["ITA_abolish_the_colonies"]
        n120["ITA_albanian_occupation"]
        n121["ITA_battaglioni_d_assalto"]
        n122["ITA_believe_obey_fight"]
        n123["ITA_boost_the_grand_council_of_fascism"]
        n124["ITA_demand_balearic_islands_bba"]
        n125{"ITA_dino_grandi_focus"}
        n126["ITA_guarantee_austrian_independence"]
        n127{"ITA_italian_socialism"}
        n128{"ITA_italo_balbo_focus"}
        n129{"ITA_italy_first"}
        n130["ITA_la_battaglia_per_le_nascite"]
        n131["ITA_legge_bottai"]
        n132{"ITA_monarchia_d_italia"}
        n133["ITA_new_colonial_policies"]
        n134{"ITA_pact_of_steel"}
        n135["ITA_strengthen_the_blackshirts"]
        n136{"ITA_the_popular_front"}
        n137["ITA_to_live_as_a_lion"]
    end
    subgraph tier_6["Tier 6"]
        n138["ITA_a_leader_steps_forward"]
        n139["ITA_aid_for_the_spanish_republic"]
        n140["ITA_albanian_oil"]
        n141["ITA_banda_carita"]
        n142{"ITA_befriend_greece"}
        n143["ITA_befriend_japan"]
        n144{"ITA_common_ground"}
        n145["ITA_consolidate_power"]
        n146["ITA_cooperate_with_the_mafia"]
        n147["ITA_cooperatives_for_intensive_exploitation"]
        n148{"ITA_crush_the_mafia"}
        n149["ITA_empower_the_unions"]
        n150["ITA_extraction_industry"]
        n151["ITA_german_military_cooperation"]
        n152{"ITA_industrial_socialization"}
        n153["ITA_invite_france_to_military_partnership"]
        n154{"ITA_italian_irredentism"}
        n155["ITA_milizia_coloniale"]
        n156["ITA_negotiate_italian_claims"]
        n157["ITA_negotiations_with_albania"]
        n158{"ITA_power_to_the_king"}
        n159{"ITA_revoke_the_acerbo_law"}
        n160["ITA_seek_british_military_cooperation"]
        n161["ITA_spanish_italian_alliance"]
        n162{"ITA_stop_the_squandering"}
        n163{"ITA_strengthen_the_regime"}
        n164["ITA_support_albanian_irredentism"]
        n165["ITA_the_garibaldi_legion"]
        n166["ITA_the_italian_confederation"]
        n167["ITA_the_republics_leadership"]
        n168["ITA_treaty_with_germany"]
    end
    subgraph tier_7["Tier 7"]
        n169["ITA_a_new_era_for_the_red_shirts"]
        n170["ITA_albanian_fascist_militia"]
        n171["ITA_anglo_italian_pact"]
        n172["ITA_appease_the_military"]
        n173["ITA_banda_koch"]
        n174["ITA_befriend_portugal"]
        n175["ITA_bring_back_exiled_intellectuals"]
        n176["ITA_christian_democracy"]
        n177["ITA_condemn_colonialism"]
        n178["ITA_democratic_king"]
        n179{"ITA_devotion"}
        n180["ITA_disband_the_blackshirts"]
        n181["ITA_empower_the_carabinieri"]
        n182["ITA_enlist_the_bashkimi_kombetar"]
        n183["ITA_franco_italian_pact"]
        n184["ITA_gruppi_di_difesa_della_donna"]
        n185["ITA_institute_the_five_year_plan"]
        n186["ITA_mafia_abroad"]
        n187["ITA_new_corporations"]
        n188["ITA_planned_economy"]
        n189["ITA_political_commissars"]
        n190["ITA_prepare_for_the_coming_wars"]
        n191["ITA_production_lines"]
        n192["ITA_purge_the_party"]
        n193["ITA_ratify_the_stresa_front"]
        n194["ITA_reinforce_regia_aeronautica"]
        n195["ITA_reorganize_regio_esercito"]
        n196["ITA_reorganize_the_party"]
        n197["ITA_request_control_of_french_territories"]
        n198["ITA_sea_wolves_bba"]
        n199["ITA_secret_weapons"]
        n200["ITA_seek_papal_support"]
        n201["ITA_the_fight_overseas"]
        n202{"ITA_the_fourth_shore"}
        n203["ITA_the_path_to_progress"]
        n204["ITA_utilize_the_blackshirts"]
        n205["ITA_war_with_france"]
        n206{"ITA_war_with_greece"}
        n207["ITA_war_with_the_uk"]
    end
    subgraph tier_8["Tier 8"]
        n208["ITA_agents_of_the_church"]
        n209["ITA_army_modernization"]
        n210["ITA_ascari"]
        n211["ITA_befriend_turkey"]
        n212["ITA_bring_back_old_glories"]
        n213["ITA_claims_on_turkey_bba"]
        n214["ITA_compagnie_auto_avio_sahariane"]
        n215["ITA_cooperate_with_moderates"]
        n216["ITA_demand_ticino"]
        n217["ITA_economic_reforms"]
        n218["ITA_expand_intelligence_services"]
        n219["ITA_expand_the_royal_guard"]
        n220["ITA_irregulars"]
        n221["ITA_italys_destiny"]
        n222["ITA_joint_military_programs"]
        n223["ITA_liberate_the_workers_of_africa"]
        n224["ITA_meritocracy"]
        n225["ITA_mobilize_the_railway_guns"]
        n226["ITA_new_forms_of_weaponry"]
        n227["ITA_new_ricostruzione_industriale"]
        n228["ITA_oil_in_tripoli"]
        n229["ITA_proclaim_the_italian_empire"]
        n230["ITA_pugno_alzato"]
        n231{"ITA_social_stability"}
        n232["ITA_steel_in_tripoli"]
        n233{"ITA_the_fate_of_mussolini"}
        n234{"ITA_union_in_the_party"}
    end
    subgraph tier_9["Tier 9"]
        n235["ITA_a_greater_purpose"]
        n236["ITA_combined_land_and_air_warfare"]
        n237["ITA_crush_opposition"]
        n238["ITA_defend_the_land"]
        n239["ITA_divino_duce"]
        n240["ITA_follow_the_soviet_union"]
        n241["ITA_gloria_al_regno_d_italia"]
        n242["ITA_improve_the_industries"]
        n243["ITA_italia_libera"]
        n244["ITA_novus_ordo"]
        n245["ITA_paramilitary_training"]
        n246["ITA_reestablish_old_alliances"]
        n247["ITA_strengthen_the_papacy"]
        n248["ITA_the_eastern_threat"]
    end
    subgraph tier_10["Tier 10"]
        n249{"ITA_blackshirt_loyalty"}
        n250["ITA_european_democracies"]
        n251["ITA_expanded_corporatism"]
        n252["ITA_military_agreements"]
        n253["ITA_military_cooperation"]
        n254["ITA_raise_the_peoples"]
        n255["ITA_scientific_cooperation"]
        n256{"ITA_setting_course"}
        n257["ITA_special_brigades"]
        n258["ITA_spreading_the_eagles_wings"]
        n259["ITA_the_fight_against_stalinism"]
        n260["ITA_the_papacy_reborn"]
        n261["ITA_united_anarchist_confederations"]
    end
    subgraph tier_11["Tier 11"]
        n262["ITA_bring_down_fascist_strongholds"]
        n263["ITA_catholic_action"]
        n264["ITA_combined_research_effort"]
        n265["ITA_defense_against_capitalism"]
        n266["ITA_deus_vult"]
        n267["ITA_italian_hegemony"]
        n268["ITA_mare_nostrum_bba"]
        n269["ITA_peace_preservation"]
        n270["ITA_secure_the_borders"]
        n271["ITA_the_enemies_of_capitalism"]
        n272{"ITA_towards_a_greater_italy"}
    end
    subgraph tier_12["Tier 12"]
        n273["ITA_a_time_for_war"]
        n274["ITA_auxiliaries"]
        n275["ITA_bend_the_bars"]
        n276["ITA_capo_supremo"]
        n277["ITA_heroes_of_the_nation"]
        n278["ITA_iberian_protection"]
        n279["ITA_il_sol_dell_avvenire"]
        n280["ITA_il_vento_aureo"]
        n281["ITA_new_roman_citizens"]
        n282["ITA_the_holy_lands"]
        n283["ITA_the_italian_legions"]
    end
    subgraph tier_13["Tier 13"]
        n284["ITA_all_roads_lead_to_rome"]
        n285["ITA_masters_of_the_aegean"]
        n286["ITA_south_american_alliances"]
        n287["ITA_subdue_the_sentinels"]
        n288["ITA_the_catholic_dominion"]
    end
    subgraph tier_14["Tier 14"]
        n289["ITA_a_colonial_empire"]
        n290["ITA_caligulas_pride"]
        n291["ITA_masters_of_the_mediterranean"]
        n292["ITA_modern_musculus"]
        n293["ITA_the_king_of_the_skies"]
    end
    subgraph tier_15["Tier 15"]
        n294["ITA_by_blood_alone"]
    end
    n287 --> n289
    n233 --> n235
    n136 --> n138
    n165 --> n169
    n266 --> n273
    n116 --> n119
    n200 --> n208
    n127 --> n139
    n164 --> n170
    n113 --> n120
    n107 --> n120
    n120 --> n140
    n283 --> n284
    n96 --> n97
    n160 --> n171
    n100 --> n106
    n144 --> n172
    n172 --> n209
    n189 --> n209
    n181 --> n209
    n201 --> n210
    n268 --> n274
    n102 --> n107
    n122 --> n141
    n141 --> n173
    n114 --> n121
    n129 --> n142
    n134 --> n143
    n129 --> n143
    n161 --> n174
    n124 --> n174
    n206 --> n211
    n142 --> n211
    n112 --> n122
    n272 --> n275
    n239 --> n249
    n118 --> n123
    n167 --> n175
    n190 --> n212
    n255 --> n262
    n289 --> n294
    n284 --> n290
    n272 --> n276
    n179 --> n276
    n260 --> n263
    n159 --> n176
    n206 --> n213
    n142 --> n213
    n214 --> n236
    n253 --> n264
    n136 --> n144
    n127 --> n144
    n195 --> n214
    n194 --> n214
    n147 --> n177
    n128 --> n145
    n125 --> n145
    n295 --> n88
    n96 --> n98
    n88 --> n98
    n176 --> n215
    n178 --> n215
    n127 --> n146
    n119 --> n147
    n102 --> n108
    n215 --> n237
    n218 --> n237
    n136 --> n148
    n127 --> n148
    n96 --> n99
    n234 --> n238
    n253 --> n265
    n89 --> n100
    n93 --> n100
    n96 --> n100
    n108 --> n124
    n205 --> n216
    n197 --> n216
    n159 --> n178
    n98 --> n109
    n260 --> n266
    n96 --> n101
    n137 --> n179
    n123 --> n179
    n163 --> n179
    n109 --> n125
    n158 --> n180
    n159 --> n180
    n233 --> n239
    n196 --> n217
    n148 --> n181
    n127 --> n149
    n157 --> n182
    n243 --> n250
    n178 --> n218
    n176 --> n218
    n180 --> n219
    n204 --> n219
    n224 --> n251
    n242 --> n251
    n132 --> n150
    n234 --> n240
    n96 --> n102
    n88 --> n102
    n153 --> n183
    n134 --> n151
    n219 --> n241
    n178 --> n241
    n165 --> n184
    n113 --> n126
    n107 --> n126
    n272 --> n277
    n179 --> n277
    n268 --> n278
    n266 --> n278
    n264 --> n279
    n254 --> n279
    n266 --> n280
    n217 --> n242
    n136 --> n152
    n152 --> n185
    n125 --> n153
    n132 --> n153
    n201 --> n220
    n231 --> n243
    n258 --> n267
    n134 --> n154
    n129 --> n154
    n117 --> n127
    n109 --> n128
    n113 --> n129
    n107 --> n129
    n193 --> n221
    n193 --> n222
    n99 --> n110
    n99 --> n111
    n110 --> n130
    n111 --> n130
    n118 --> n131
    n94 --> n103
    n96 --> n103
    n201 --> n223
    n146 --> n186
    n256 --> n268
    n163 --> n268
    n249 --> n268
    n275 --> n285
    n285 --> n291
    n196 --> n224
    n192 --> n224
    n246 --> n252
    n240 --> n253
    n121 --> n155
    n135 --> n155
    n99 --> n112
    n98 --> n112
    n190 --> n225
    n284 --> n292
    n109 --> n132
    n126 --> n156
    n119 --> n157
    n133 --> n157
    n116 --> n133
    n150 --> n187
    n190 --> n226
    n185 --> n227
    n268 --> n281
    n232 --> n244
    n228 --> n244
    n202 --> n228
    n113 --> n134
    n107 --> n134
    n219 --> n245
    n204 --> n245
    n250 --> n269
    n166 --> n188
    n152 --> n189
    n102 --> n113
    n132 --> n158
    n150 --> n190
    n171 --> n229
    n183 --> n229
    n149 --> n191
    n184 --> n230
    n169 --> n230
    n145 --> n192
    n162 --> n192
    n238 --> n254
    n156 --> n193
    n231 --> n246
    n128 --> n194
    n162 --> n194
    n128 --> n195
    n162 --> n195
    n125 --> n196
    n145 --> n196
    n134 --> n197
    n154 --> n197
    n132 --> n159
    n243 --> n255
    n246 --> n255
    n151 --> n198
    n151 --> n199
    n255 --> n270
    n99 --> n114
    n98 --> n114
    n125 --> n160
    n132 --> n160
    n158 --> n200
    n100 --> n115
    n90 --> n95
    n92 --> n95
    n91 --> n95
    n241 --> n256
    n237 --> n256
    n247 --> n256
    n175 --> n231
    n278 --> n286
    n108 --> n161
    n129 --> n161
    n240 --> n257
    n238 --> n257
    n235 --> n258
    n202 --> n232
    n128 --> n162
    n125 --> n162
    n114 --> n135
    n208 --> n247
    n130 --> n163
    n275 --> n287
    n120 --> n164
    n273 --> n288
    n282 --> n288
    n221 --> n248
    n252 --> n271
    n100 --> n116
    n192 --> n233
    n238 --> n259
    n147 --> n201
    n166 --> n201
    n128 --> n202
    n162 --> n202
    n136 --> n165
    n266 --> n282
    n133 --> n166
    n268 --> n283
    n100 --> n117
    n284 --> n293
    n99 --> n118
    n96 --> n104
    n247 --> n260
    n138 --> n203
    n117 --> n136
    n127 --> n167
    n118 --> n137
    n96 --> n105
    n163 --> n272
    n249 --> n272
    n256 --> n272
    n134 --> n168
    n95 --> n96
    n91 --> n295
    n203 --> n234
    n238 --> n261
    n158 --> n204
    n154 --> n205
    n154 --> n206
    n129 --> n207
    n154 --> n207
    n235 x--x n239
    n119 x--x n133
    n172 x--x n181
    n172 x--x n189
    n107 x--x n113
    n121 x--x n135
    n142 x--x n206
    n211 x--x n213
    n123 x--x n137
    n276 x--x n277
    n176 x--x n178
    n98 x--x n99
    n98 x--x n100
    n146 x--x n148
    n99 x--x n100
    n238 x--x n240
    n124 x--x n161
    n125 x--x n128
    n125 x--x n132
    n180 x--x n204
    n181 x--x n189
    n126 x--x n129
    n126 x--x n134
    n153 x--x n160
    n243 x--x n246
    n127 x--x n136
    n128 x--x n132
    n129 x--x n134
    n110 x--x n111
    n268 x--x n272
    n228 x--x n232
    n158 x--x n159
    n194 x--x n195
    n197 x--x n205
    n90 x--x n91
    n91 x--x n92
```

# ITA_the_abyssinian_fiasco

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n88{"ITA_conspiracies_in_the_shadows"}
        n90["ITA_solid_progress"]
        n91["ITA_struggle_in_ethiopia"]
        n92(("ITA_the_abyssinian_fiasco"))
    end
    subgraph tier_1["Tier 1"]
        n95["ITA_servizio_informazione_militare"]
        n94{"ITA_unite_the_opposition"}
    end
    subgraph tier_2["Tier 2"]
        n89{"ITA_organize_strikes_in_the_north"}
        n93{"ITA_the_southern_farmlands"}
        n96{"ITA_triumph_in_africa_bba"}
    end
    subgraph tier_3["Tier 3"]
        n97["ITA_anglo_italian_agreements"]
        n98["ITA_convene_the_grand_council"]
        n99{"ITA_culto_del_duce"}
        n100["ITA_defy_the_duce"]
        n101["ITA_devaluate_the_lire"]
        n102{"ITA_foreign_affairs"}
        n103["ITA_liberate_gramsci"]
        n104["ITA_the_new_emperor_of_ethiopia"]
        n105["ITA_topple_amhara_rulers"]
    end
    subgraph tier_4["Tier 4"]
        n106["ITA_appeal_to_the_bourgeoisie"]
        n107{"ITA_balkan_ambition"}
        n108{"ITA_corpo_di_truppe_volontarie"}
        n109{"ITA_depose_mussolini"}
        n110["ITA_la_battaglia_del_grano"]
        n111["ITA_la_battaglia_per_la_terra"]
        n112["ITA_ministero_della_cultura_popolare"]
        n113{"ITA_potential_allies_in_the_balkans"}
        n114{"ITA_security_militias"}
        n115["ITA_seize_old_equipment"]
        n116{"ITA_the_ethiopian_question"}
        n117{"ITA_the_italian_republic"}
        n118{"ITA_the_man_of_providence"}
    end
    subgraph tier_5["Tier 5"]
        n119["ITA_abolish_the_colonies"]
        n120["ITA_albanian_occupation"]
        n121["ITA_battaglioni_d_assalto"]
        n122["ITA_believe_obey_fight"]
        n123["ITA_boost_the_grand_council_of_fascism"]
        n124["ITA_demand_balearic_islands_bba"]
        n125{"ITA_dino_grandi_focus"}
        n126["ITA_guarantee_austrian_independence"]
        n127{"ITA_italian_socialism"}
        n128{"ITA_italo_balbo_focus"}
        n129{"ITA_italy_first"}
        n130["ITA_la_battaglia_per_le_nascite"]
        n131["ITA_legge_bottai"]
        n132{"ITA_monarchia_d_italia"}
        n133["ITA_new_colonial_policies"]
        n134{"ITA_pact_of_steel"}
        n135["ITA_strengthen_the_blackshirts"]
        n136{"ITA_the_popular_front"}
        n137["ITA_to_live_as_a_lion"]
    end
    subgraph tier_6["Tier 6"]
        n138["ITA_a_leader_steps_forward"]
        n139["ITA_aid_for_the_spanish_republic"]
        n140["ITA_albanian_oil"]
        n141["ITA_banda_carita"]
        n142{"ITA_befriend_greece"}
        n143["ITA_befriend_japan"]
        n144{"ITA_common_ground"}
        n145["ITA_consolidate_power"]
        n146["ITA_cooperate_with_the_mafia"]
        n147["ITA_cooperatives_for_intensive_exploitation"]
        n148{"ITA_crush_the_mafia"}
        n149["ITA_empower_the_unions"]
        n150["ITA_extraction_industry"]
        n151["ITA_german_military_cooperation"]
        n152{"ITA_industrial_socialization"}
        n153["ITA_invite_france_to_military_partnership"]
        n154{"ITA_italian_irredentism"}
        n155["ITA_milizia_coloniale"]
        n156["ITA_negotiate_italian_claims"]
        n157["ITA_negotiations_with_albania"]
        n158{"ITA_power_to_the_king"}
        n159{"ITA_revoke_the_acerbo_law"}
        n160["ITA_seek_british_military_cooperation"]
        n161["ITA_spanish_italian_alliance"]
        n162{"ITA_stop_the_squandering"}
        n163{"ITA_strengthen_the_regime"}
        n164["ITA_support_albanian_irredentism"]
        n165["ITA_the_garibaldi_legion"]
        n166["ITA_the_italian_confederation"]
        n167["ITA_the_republics_leadership"]
        n168["ITA_treaty_with_germany"]
    end
    subgraph tier_7["Tier 7"]
        n169["ITA_a_new_era_for_the_red_shirts"]
        n170["ITA_albanian_fascist_militia"]
        n171["ITA_anglo_italian_pact"]
        n172["ITA_appease_the_military"]
        n173["ITA_banda_koch"]
        n174["ITA_befriend_portugal"]
        n175["ITA_bring_back_exiled_intellectuals"]
        n176["ITA_christian_democracy"]
        n177["ITA_condemn_colonialism"]
        n178["ITA_democratic_king"]
        n179{"ITA_devotion"}
        n180["ITA_disband_the_blackshirts"]
        n181["ITA_empower_the_carabinieri"]
        n182["ITA_enlist_the_bashkimi_kombetar"]
        n183["ITA_franco_italian_pact"]
        n184["ITA_gruppi_di_difesa_della_donna"]
        n185["ITA_institute_the_five_year_plan"]
        n186["ITA_mafia_abroad"]
        n187["ITA_new_corporations"]
        n188["ITA_planned_economy"]
        n189["ITA_political_commissars"]
        n190["ITA_prepare_for_the_coming_wars"]
        n191["ITA_production_lines"]
        n192["ITA_purge_the_party"]
        n193["ITA_ratify_the_stresa_front"]
        n194["ITA_reinforce_regia_aeronautica"]
        n195["ITA_reorganize_regio_esercito"]
        n196["ITA_reorganize_the_party"]
        n197["ITA_request_control_of_french_territories"]
        n198["ITA_sea_wolves_bba"]
        n199["ITA_secret_weapons"]
        n200["ITA_seek_papal_support"]
        n201["ITA_the_fight_overseas"]
        n202{"ITA_the_fourth_shore"}
        n203["ITA_the_path_to_progress"]
        n204["ITA_utilize_the_blackshirts"]
        n205["ITA_war_with_france"]
        n206{"ITA_war_with_greece"}
        n207["ITA_war_with_the_uk"]
    end
    subgraph tier_8["Tier 8"]
        n208["ITA_agents_of_the_church"]
        n209["ITA_army_modernization"]
        n210["ITA_ascari"]
        n211["ITA_befriend_turkey"]
        n212["ITA_bring_back_old_glories"]
        n213["ITA_claims_on_turkey_bba"]
        n214["ITA_compagnie_auto_avio_sahariane"]
        n215["ITA_cooperate_with_moderates"]
        n216["ITA_demand_ticino"]
        n217["ITA_economic_reforms"]
        n218["ITA_expand_intelligence_services"]
        n219["ITA_expand_the_royal_guard"]
        n220["ITA_irregulars"]
        n221["ITA_italys_destiny"]
        n222["ITA_joint_military_programs"]
        n223["ITA_liberate_the_workers_of_africa"]
        n224["ITA_meritocracy"]
        n225["ITA_mobilize_the_railway_guns"]
        n226["ITA_new_forms_of_weaponry"]
        n227["ITA_new_ricostruzione_industriale"]
        n228["ITA_oil_in_tripoli"]
        n229["ITA_proclaim_the_italian_empire"]
        n230["ITA_pugno_alzato"]
        n231{"ITA_social_stability"}
        n232["ITA_steel_in_tripoli"]
        n233{"ITA_the_fate_of_mussolini"}
        n234{"ITA_union_in_the_party"}
    end
    subgraph tier_9["Tier 9"]
        n235["ITA_a_greater_purpose"]
        n236["ITA_combined_land_and_air_warfare"]
        n237["ITA_crush_opposition"]
        n238["ITA_defend_the_land"]
        n239["ITA_divino_duce"]
        n240["ITA_follow_the_soviet_union"]
        n241["ITA_gloria_al_regno_d_italia"]
        n242["ITA_improve_the_industries"]
        n243["ITA_italia_libera"]
        n244["ITA_novus_ordo"]
        n245["ITA_paramilitary_training"]
        n246["ITA_reestablish_old_alliances"]
        n247["ITA_strengthen_the_papacy"]
        n248["ITA_the_eastern_threat"]
    end
    subgraph tier_10["Tier 10"]
        n249{"ITA_blackshirt_loyalty"}
        n250["ITA_european_democracies"]
        n251["ITA_expanded_corporatism"]
        n252["ITA_military_agreements"]
        n253["ITA_military_cooperation"]
        n254["ITA_raise_the_peoples"]
        n255["ITA_scientific_cooperation"]
        n256{"ITA_setting_course"}
        n257["ITA_special_brigades"]
        n258["ITA_spreading_the_eagles_wings"]
        n259["ITA_the_fight_against_stalinism"]
        n260["ITA_the_papacy_reborn"]
        n261["ITA_united_anarchist_confederations"]
    end
    subgraph tier_11["Tier 11"]
        n262["ITA_bring_down_fascist_strongholds"]
        n263["ITA_catholic_action"]
        n264["ITA_combined_research_effort"]
        n265["ITA_defense_against_capitalism"]
        n266["ITA_deus_vult"]
        n267["ITA_italian_hegemony"]
        n268["ITA_mare_nostrum_bba"]
        n269["ITA_peace_preservation"]
        n270["ITA_secure_the_borders"]
        n271["ITA_the_enemies_of_capitalism"]
        n272{"ITA_towards_a_greater_italy"}
    end
    subgraph tier_12["Tier 12"]
        n273["ITA_a_time_for_war"]
        n274["ITA_auxiliaries"]
        n275["ITA_bend_the_bars"]
        n276["ITA_capo_supremo"]
        n277["ITA_heroes_of_the_nation"]
        n278["ITA_iberian_protection"]
        n279["ITA_il_sol_dell_avvenire"]
        n280["ITA_il_vento_aureo"]
        n281["ITA_new_roman_citizens"]
        n282["ITA_the_holy_lands"]
        n283["ITA_the_italian_legions"]
    end
    subgraph tier_13["Tier 13"]
        n284["ITA_all_roads_lead_to_rome"]
        n285["ITA_masters_of_the_aegean"]
        n286["ITA_south_american_alliances"]
        n287["ITA_subdue_the_sentinels"]
        n288["ITA_the_catholic_dominion"]
    end
    subgraph tier_14["Tier 14"]
        n289["ITA_a_colonial_empire"]
        n290["ITA_caligulas_pride"]
        n291["ITA_masters_of_the_mediterranean"]
        n292["ITA_modern_musculus"]
        n293["ITA_the_king_of_the_skies"]
    end
    subgraph tier_15["Tier 15"]
        n294["ITA_by_blood_alone"]
    end
    n287 --> n289
    n233 --> n235
    n136 --> n138
    n165 --> n169
    n266 --> n273
    n116 --> n119
    n200 --> n208
    n127 --> n139
    n164 --> n170
    n113 --> n120
    n107 --> n120
    n120 --> n140
    n283 --> n284
    n96 --> n97
    n160 --> n171
    n100 --> n106
    n144 --> n172
    n172 --> n209
    n189 --> n209
    n181 --> n209
    n201 --> n210
    n268 --> n274
    n102 --> n107
    n122 --> n141
    n141 --> n173
    n114 --> n121
    n129 --> n142
    n134 --> n143
    n129 --> n143
    n161 --> n174
    n124 --> n174
    n206 --> n211
    n142 --> n211
    n112 --> n122
    n272 --> n275
    n239 --> n249
    n118 --> n123
    n167 --> n175
    n190 --> n212
    n255 --> n262
    n289 --> n294
    n284 --> n290
    n272 --> n276
    n179 --> n276
    n260 --> n263
    n159 --> n176
    n206 --> n213
    n142 --> n213
    n214 --> n236
    n253 --> n264
    n136 --> n144
    n127 --> n144
    n195 --> n214
    n194 --> n214
    n147 --> n177
    n128 --> n145
    n125 --> n145
    n96 --> n98
    n88 --> n98
    n176 --> n215
    n178 --> n215
    n127 --> n146
    n119 --> n147
    n102 --> n108
    n215 --> n237
    n218 --> n237
    n136 --> n148
    n127 --> n148
    n96 --> n99
    n234 --> n238
    n253 --> n265
    n89 --> n100
    n93 --> n100
    n96 --> n100
    n108 --> n124
    n205 --> n216
    n197 --> n216
    n159 --> n178
    n98 --> n109
    n260 --> n266
    n96 --> n101
    n137 --> n179
    n123 --> n179
    n163 --> n179
    n109 --> n125
    n158 --> n180
    n159 --> n180
    n233 --> n239
    n196 --> n217
    n148 --> n181
    n127 --> n149
    n157 --> n182
    n243 --> n250
    n178 --> n218
    n176 --> n218
    n180 --> n219
    n204 --> n219
    n224 --> n251
    n242 --> n251
    n132 --> n150
    n234 --> n240
    n96 --> n102
    n88 --> n102
    n153 --> n183
    n134 --> n151
    n219 --> n241
    n178 --> n241
    n165 --> n184
    n113 --> n126
    n107 --> n126
    n272 --> n277
    n179 --> n277
    n268 --> n278
    n266 --> n278
    n264 --> n279
    n254 --> n279
    n266 --> n280
    n217 --> n242
    n136 --> n152
    n152 --> n185
    n125 --> n153
    n132 --> n153
    n201 --> n220
    n231 --> n243
    n258 --> n267
    n134 --> n154
    n129 --> n154
    n117 --> n127
    n109 --> n128
    n113 --> n129
    n107 --> n129
    n193 --> n221
    n193 --> n222
    n99 --> n110
    n99 --> n111
    n110 --> n130
    n111 --> n130
    n118 --> n131
    n94 --> n103
    n96 --> n103
    n201 --> n223
    n146 --> n186
    n256 --> n268
    n163 --> n268
    n249 --> n268
    n275 --> n285
    n285 --> n291
    n196 --> n224
    n192 --> n224
    n246 --> n252
    n240 --> n253
    n121 --> n155
    n135 --> n155
    n99 --> n112
    n98 --> n112
    n190 --> n225
    n284 --> n292
    n109 --> n132
    n126 --> n156
    n119 --> n157
    n133 --> n157
    n116 --> n133
    n150 --> n187
    n190 --> n226
    n185 --> n227
    n268 --> n281
    n232 --> n244
    n228 --> n244
    n202 --> n228
    n94 --> n89
    n113 --> n134
    n107 --> n134
    n219 --> n245
    n204 --> n245
    n250 --> n269
    n166 --> n188
    n152 --> n189
    n102 --> n113
    n132 --> n158
    n150 --> n190
    n171 --> n229
    n183 --> n229
    n149 --> n191
    n184 --> n230
    n169 --> n230
    n145 --> n192
    n162 --> n192
    n238 --> n254
    n156 --> n193
    n231 --> n246
    n128 --> n194
    n162 --> n194
    n128 --> n195
    n162 --> n195
    n125 --> n196
    n145 --> n196
    n134 --> n197
    n154 --> n197
    n132 --> n159
    n243 --> n255
    n246 --> n255
    n151 --> n198
    n151 --> n199
    n255 --> n270
    n99 --> n114
    n98 --> n114
    n125 --> n160
    n132 --> n160
    n158 --> n200
    n100 --> n115
    n90 --> n95
    n92 --> n95
    n91 --> n95
    n241 --> n256
    n237 --> n256
    n247 --> n256
    n175 --> n231
    n278 --> n286
    n108 --> n161
    n129 --> n161
    n240 --> n257
    n238 --> n257
    n235 --> n258
    n202 --> n232
    n128 --> n162
    n125 --> n162
    n114 --> n135
    n208 --> n247
    n130 --> n163
    n275 --> n287
    n120 --> n164
    n273 --> n288
    n282 --> n288
    n221 --> n248
    n252 --> n271
    n100 --> n116
    n192 --> n233
    n238 --> n259
    n147 --> n201
    n166 --> n201
    n128 --> n202
    n162 --> n202
    n136 --> n165
    n266 --> n282
    n133 --> n166
    n268 --> n283
    n100 --> n117
    n284 --> n293
    n99 --> n118
    n96 --> n104
    n247 --> n260
    n138 --> n203
    n117 --> n136
    n127 --> n167
    n94 --> n93
    n118 --> n137
    n96 --> n105
    n163 --> n272
    n249 --> n272
    n256 --> n272
    n134 --> n168
    n95 --> n96
    n203 --> n234
    n92 --> n94
    n238 --> n261
    n158 --> n204
    n154 --> n205
    n154 --> n206
    n129 --> n207
    n154 --> n207
    n235 x--x n239
    n119 x--x n133
    n172 x--x n181
    n172 x--x n189
    n107 x--x n113
    n121 x--x n135
    n142 x--x n206
    n211 x--x n213
    n123 x--x n137
    n276 x--x n277
    n176 x--x n178
    n98 x--x n99
    n98 x--x n100
    n146 x--x n148
    n99 x--x n100
    n238 x--x n240
    n124 x--x n161
    n125 x--x n128
    n125 x--x n132
    n180 x--x n204
    n181 x--x n189
    n126 x--x n129
    n126 x--x n134
    n153 x--x n160
    n243 x--x n246
    n127 x--x n136
    n128 x--x n132
    n129 x--x n134
    n110 x--x n111
    n268 x--x n272
    n228 x--x n232
    n89 x--x n93
    n158 x--x n159
    n194 x--x n195
    n197 x--x n205
    n90 x--x n92
    n91 x--x n92
```

# ITA_the_italian_liberation_war

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n296(("ITA_the_italian_liberation_war"))
    end
    subgraph tier_1["Tier 1"]
        n297{"ITA_fronte_militare_clandestino"}
    end
    subgraph tier_2["Tier 2"]
        n298["ITA_corpo_volontari_della_liberta"]
        n299["ITA_the_carabinieri"]
    end
    subgraph tier_3["Tier 3"]
        n300["ITA_gappisti"]
        n301["ITA_partisan_republics"]
        n302["ITA_the_kings_finest"]
    end
    subgraph tier_4["Tier 4"]
        n303["ITA_grande_rivolta_rurale"]
    end
    subgraph tier_5["Tier 5"]
        n304["ITA_liberation_or_death"]
    end
    subgraph tier_6["Tier 6"]
        n305["ITA_independence_rds"]
    end
    n297 --> n298
    n296 --> n297
    n298 --> n300
    n301 --> n303
    n300 --> n303
    n302 --> n303
    n304 --> n305
    n303 --> n304
    n298 --> n301
    n299 --> n301
    n297 --> n299
    n299 --> n302
    n298 x--x n299
```

# ITA_the_italian_social_republic

```mermaid
swimlane-beta TD
    subgraph tier_0["Tier 0"]
        n306(("ITA_the_italian_social_republic"))
    end
    subgraph tier_1["Tier 1"]
        n307["ITA_guardia_nazionale_repubblicana"]
    end
    subgraph tier_2["Tier 2"]
        n308["ITA_all_within_the_state"]
        n309["ITA_battaglioni_m"]
        n310["ITA_integrate_polizia_dell_africa_italiana"]
    end
    subgraph tier_3["Tier 3"]
        n311["ITA_anti_partisan_measures"]
        n312["ITA_reinforce_the_gustav_line"]
    end
    subgraph tier_4["Tier 4"]
        n313["ITA_the_social_republic_prevails"]
    end
    subgraph tier_5["Tier 5"]
        n314["ITA_independence_rsi"]
    end
    n307 --> n308
    n310 --> n311
    n307 --> n309
    n306 --> n307
    n313 --> n314
    n307 --> n310
    n309 --> n312
    n311 --> n313
    n308 --> n313
    n312 --> n313
```
