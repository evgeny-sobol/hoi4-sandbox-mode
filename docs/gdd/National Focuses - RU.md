<!-- source: bc3e20bd48e725a359235d89770b299217c948eb -->
# Common blocks - RU

## `ai_will_do` - RU

### Basic modifiers - RU

**Каждый** national focus:
```
    ai_will_do:
      +modifier:
        $ai_sandbox_modifier()
```

Каждый **root** в дереве нацфокусов:
```
      +modifier:
        $root_modifier()
```

**Взаимоисключающие** фокусы, которые:
- реально доступны одновременно (`N` - число конкурентных, а не размер списка `mutually_exclusive`)
- **опциональны** (доктрина, MIC, "улучшить истребители против бомбардировщиков"), а не политический или сюжетный бит
- еще не разбиты весами популярности партий
- еще не разбиты Tyranny-факторами (развилка "репрессии против реформ")
- еще не гейтятся `available`-проверкой популярности партии `> 0.5`
- еще не гейтятся конфликтующими проверками `has_government` (разные правящие идеологии одновременно не встречаются)
- **ни у одного** из конкурентных вариантов нет `FOCUS_FILTER_POLITICAL` или `FOCUS_FILTER_POLITICAL_CHARACTER` в `search_filters` (если хоть у одного сиблинга есть любой из фильтров - убрать `$crossroad_modifier` со всей эксклюзивной группы, например `GER_heed_von_neuraths_concerns` / `GER_reorganize_the_wehrmacht`)
```
      +modifier:
        $crossroad_modifier(N)
```

`$ai_sandbox_modifier()` - это `factor(0)` **и** `add(40)` в **одном** блоке `modifier`. Не разносить их по модификаторам: движок перемножает каждый `factor` в итоговый вес, так что отдельно стоящий `factor(0)` оставляет фокус на 0 в aiview даже после сработавшего позже `add(40)`. Чтобы гейтить корень на завершенный политический фокус, положить `factor(0)` + `add(N)` в один модификатор с триггером `has_completed_focus`, а отдельный `factor(0)` - только в комплементарный случай `NOT`.

### Party-popularity modifiers - RU

Взвешивать фокус через `mtth:democracy_factor`, `mtth:monarchy_factor`, `mtth:communism_factor` и/или `mtth:fascism_factor`, когда выбор ИИ - **политический путь**: опции стоят за разные правящие идеологии или партийные constituency. 

Эти факторы **не** использовать для доктринальных, MIC- или чисто дипломатических развилок.

Если `available` уже требует партию выше 50% (`democratic > 0.5`, `neutrality > 0.5`, `communism > 0.5` или `fascism > 0.5`), пропустить и `$crossroad_modifier`, и party-popularity фактор: игра уже отфильтровала выбор.

То же верно, когда эксклюзивные опции требуют разные правящие идеологии (`has_government`): они никогда не конкурентны, так что `$crossroad_modifier` не нужен, а party-popularity фактор под ту же идеологию ничего не добавляет.

**Неконституционные** фокусы смены правительства ("захватить власть", "запретить партию", "приостановить выборы", путчи) получают `$ai_high_tyranny_tilt()` из "Domestic-politics modifiers", чтобы деспоты предпочитали путч, а либералы ждали бюллетень. Задуманный Authoritarian-обход популярностного гейта (`docs/gdd/Tyranny System.md`, "Gating focuses by band") **отложен**: проверки популярности живут в ванильных блоках `available`, а include умеет только дописывать условия в существующий блок, а не оборачивать ванильное условие в `OR`. Не пытаться эмулировать через `+available:`; ждать replace-возможности в компиляторе.

Назначить каждой опции поддерживающие ее партии.

Отмасштабировать доли, чтобы эксклюзивный сет суммировался в `N` (каждая опция в среднем весит как синглтон). Убрать `$crossroad_modifier`.

**Непересекающиеся** партийные наборы (ни одна партия не поддерживает больше одной опции): сумма поддерживающих факторов, умножить на `N`:

```
      +modifier:
        f = (mtth:democracy_factor + mtth:communism_factor) * 2
        factor(f)
        is_sandbox_mode_on()
```

```
      +modifier:
        f = (mtth:monarchy_factor + mtth:fascism_factor) * 2
        factor(f)
        is_sandbox_mode_on()
```

**Пересекающиеся** партийные наборы (одна и та же партия поддерживает больше одной опции): поддерживающие партии в числитель; в знаменателе посчитать каждую партию по разу за каждую claiming ее опцию; умножить на `N`:

```
      +modifier:
        f = (mtth:democracy_factor + mtth:communism_factor) /
          (mtth:democracy_factor + 2 * mtth:monarchy_factor + mtth:communism_factor + mtth:fascism_factor) * 3
        factor(f)
        is_sandbox_mode_on()
```

Фокус, только **клонящий** к партии, без раздела развилки, использует boost вместо доли. Не добавлять `$crossroad_modifier` на тот же эксклюзивный сет: `1 + factor` и так на синглтон-весе или выше.

```
      +modifier:
        f = 1 + mtth:communism_factor
        factor(f)
        is_sandbox_mode_on()
```

### Diplomacy modifiers - RU

**Кооперация** с *одной* страной (для фокусов, ведущих к альянсам). Ривалы (`docs/gdd/Rivals System.md`) блокируют кооперацию: гейт в `available` использует `$not_rival_of_PREV($TAG)` - `$is_rival_of()` (в войне, или любая сторона держит другую в `rivals[]`), обернутый в `country_exists`-гейт для безопасности алиасов тегов - а вес ИИ зануляется, когда цель в нашем `rivals[]`. Ривальские opinion-модификаторы (-20/-10) уже снижают `$ai_cooperation_modifier`, так что отдельный rivalry-фактор здесь не нужен.
```
    available:
      $not_rival_of_PREV($TAG)
    ai_will_do:
      +modifier:
        $ai_cooperation_modifier($TAG)
      +modifier:
        factor(0)
        $TAG in rivals[]
        is_sandbox_mode_on()
```
Использовать `+available:`, если у ванильного фокуса нет блока `available`.

**Кооперация** с *двумя* странами:
```
    available:
      $not_rival_of_PREV($TAG1)
      $not_rival_of_PREV($TAG2)
    ai_will_do:
      +modifier:
        cooperation = 1 + ($opinion_factor($TAG1) + $opinion_factor($TAG2)) / 2
        factor(cooperation)
        is_sandbox_mode_on()
      +modifier:
        factor(0)
        or:
          $TAG1 in rivals[]
          $TAG2 in rivals[]
        is_sandbox_mode_on()
```

**Кооперация** с *тремя и больше* странами (приглашения строительства фракций вроде `USA_hemisphere_defense`, `ITA_south_american_alliances`, `GER_safeguard_the_baltic`, `SOV_our_slavic_commitments`): **без** rival-гейта и **без** `factor(0)`. Национальных ривалов набирают из соседей и своего континента, так что при многих приглашенных один из них почти всегда ривал, и гейт запретит фокус навсегда и игроку, и ИИ. Оставить только усредненный cooperation-фактор; ривальские opinion-модификаторы его тянут вниз, а ИИ самого ривала отклоняет альянс (`alliance -200`).
```
    ai_will_do:
      +modifier:
        cooperation = 1 + ($opinion_factor($TAG1) + $opinion_factor($TAG2) +
          $opinion_factor($TAG3)) / 3
        factor(cooperation)
        is_sandbox_mode_on()
```

Фокусы, ведущие к войне против **друга** (союзник, гарант или партнер по пакту о ненападении; `$is_friend_of()`), - это **betrayal-фокусы**. Никогда не гейтить их напрямую через `is_honored_leader(no)`: он игнорирует Honor-тиры. Два макроса в `macros.hml` несут AI-сторону (`docs/gdd/Honor System.md`, "AI weighting"); фактор - `clamp((25 - honor) / 125, 0, 1)`, так что Treacherous-ИИ предает на полном весе, а Inglorious-ИИ около 25 - почти никогда. Фокус, чьи цели не друзья, не затрагивается, потому что триггер падает и модификатор не применяется:
```
macro ai_betrayal_modifier():
  betrayal = clamp((25 - honor) / 125, 0, 1)
  factor(betrayal)
  is_sandbox_mode_on()

macro ai_betrayal_modifier_vs(_tag_):
  $ai_betrayal_modifier()
  country_exists(_tag_)
  _tag_->is_friend_of_PREV()
```

Сам Honor-штраф никогда не пишется в блоке фокуса. Ванильные фокусы снимают пакты своим `diplomatic_relation`, который include заменить не может; -50 charged by `on_declare_war` через недельный снимок и 6-месячное dropped-obligation окно (`docs/gdd/Honor System.md`, "Honor losses"). Только sandbox-авторские фокусы, снимающие пакт, используют `$break_non_aggression_pact_with($TAG)`, который применяет `$add_honor(-50)` напрямую. Войны на гарантируемые страны и выходы из фракций аналогично charged by on_actions.

**Антагонизм** с *одной* страной (для фокуса, ведущего к войнам). `can_PREV_get_wargoal_on_THIS` тирирован по Honor (см. `docs/gdd/Honor System.md`): NAP требует Inglorious или хуже, гарантия - Dishonorable или хуже, союзник по фракции - Treacherous; не-друг разрешен всегда.
```
    available:
      $TAG->can_PREV_get_wargoal_on_THIS()
    ai_will_do:
      +modifier:
        $ai_war_support_modifier()
      +modifier:
        $ai_antagonism_modifier($TAG)
      +modifier:
        $ai_rivalry_modifier($TAG)
      +modifier:
        $ai_betrayal_modifier_vs($TAG)
```
Использовать `+available:`, если у ванильного фокуса нет блока `available`.

`$ai_rivalry_modifier($TAG)` (`docs/gdd/Rivals System.md`, "National focuses") - это `factor(1 + rivalry_vs / 50)`, где `rivalry_vs` - максимальный `rivalry` по нашим слотам с `TAG` (0 для не-ривала): x1 для stranger, x2 для ривала на 50, x3 на Feud. Стоит рядом, а не вместо `$ai_antagonism_modifier`: ривальские opinion-модификаторы уже поднимают antagonism, а rivalry-фактор добавляет интенсивность, которую opinion выразить не может.

**Антагонизм** с *несколькими* странами:
```
    available:
      $TAG1->can_PREV_get_wargoal_on_THIS()
      $TAG2->can_PREV_get_wargoal_on_THIS()
    ai_will_do:
      +modifier:
        $ai_war_support_modifier()
      +modifier:
        antagonism = 1 - ($opinion_factor($TAG1) + $opinion_factor($TAG2)) / 2
        factor(antagonism)
        is_sandbox_mode_on()
      +modifier:
        $ai_rivalry_modifier_max($TAG1, $TAG2)
      +modifier:
        $ai_betrayal_modifier()
        or:
          $TAG1->is_friend_of_PREV()
          $TAG2->is_friend_of_PREV()
```
Использовать `+available:`, если у ванильного фокуса нет блока `available`. `$ai_rivalry_modifier_max` берет максимальный `rivalry` по обеим целям, так что фокус против одного ривала и одного stranger весит как фокус против одного ривала.

**Антагонизм** с *тремя и больше* странами: макросы фиксированной арности, так что расписать тот же модификатор по одной строке `$rivalry_vs_into($TAG)` на цель (макрос только поднимает `rivalry_vs`, так что строки складываются):
```
      +modifier:
        rivalry_vs = 0
        $rivalry_vs_into($TAG1)
        $rivalry_vs_into($TAG2)
        $rivalry_vs_into($TAG3)
        f = 1 + rivalry_vs / 50
        factor(f)
        is_sandbox_mode_on()
```
Каждый `$ai_antagonism_modifier` и каждый мультитаргетный блок `antagonism = ...` должен иметь рядом rivalry-модификатор, общие деревья (`*_shared`, `*_joint`, `TSR_*`) включены.

**Антагонизм** с *владельцами перечисленных стейтов* (страны - не фиксированные теги). Еженедельный `update_<TAG>_national_focuses()` хранит **по одному владельцу на стейт** (одна и та же страна может встретиться несколько раз, так что тултип фокуса называет каждого владельца стейта). AI-фактор усредняет только уникальных владельцев-чужих. Затем фокус использует эти слоты как `SOV_the_rightful_heir_to_the_empire` / `GER_demand_slovenia`:

```
    available:
      var:focus_targets[0]->can_PREV_get_wargoal_on_THIS()
      var:focus_targets[1]->can_PREV_get_wargoal_on_THIS()
    ai_will_do:
      +modifier:
        $ai_war_support_modifier()
      +modifier:
        factor(focus_antagonism)
        is_sandbox_mode_on()
      +modifier:
        $ai_betrayal_modifier()
        any_other_country:
          THIS in ROOT.focus_targets[]
          is_friend_of_ROOT()
```

Если возможен только один владелец, достаточно одного `var:focus_targets[0]->can_PREV_get_wargoal_on_THIS()`. Использовать `+available:`, если у ванильного фокуса нет блока `available`. State-owner фокусы учитывают rivalry только через opinion; rivalry-фактор по динамическим целям - follow-up (`docs/gdd/Rivals System.md`, "Out of scope").

**Антагонизм** с *алиасом тега*. Некоторые теги ванильных деревьев фокусов - не страны, а алиасы из `common/country_tag_aliases/tag_aliases.txt` (`SPA`, `SPB`, `SPC`, `SPD`, `VIC`, `SOU`, `SOB`, `SOS`, `SOT`, `SOP`, `BUF`, `BUZ`, `FGR`, `FNO`, `MOT`, `RDS`, `RSI`, `SB1`-`SB4`). Алиас резолвится в страну, только пока держится его триггер (например `SOS` - сталинистская половина советской гражданской войны); иначе это `None`, и вход в него как в скоп (`$SOS->...`) логирует `Invalid Scope` в `error.log` при каждом вычислении блока. Обычные теги безопасны, даже если страны нет на карте. Для алиасов никогда не входить в скоп без гейта:
```
    available:
      $can_get_wargoal_on($ALIAS)         # OR: NOT country_exists / ALIAS->can_PREV_get_wargoal_on_THIS
    ai_will_do:
      +modifier:
        $ai_betrayal_modifier_vs($ALIAS)  # already checks country_exists before the scope
      +modifier:
        $ai_betrayal_modifier()
        or:
          $TAG1->is_friend_of_PREV()
          and:
            country_exists($ALIAS)
            $ALIAS->is_friend_of_PREV()
```
Формы значений (`$opinion_factor($ALIAS)`, `has_war_with = ALIAS`) в скоп не входят и гейта не требуют. Триггерные блоки вычисляются по порядку и останавливаются на первом падающем (`and`) или проходящем (`or`) триггере, так что `country_exists` должен стоять **до** скопа.

### Domestic-politics modifiers (Tyranny) - RU

Репрессивные и либеральные фокусы тегируются `$add_tyranny(+/-X)` в `completion_reward` по классификации из `docs/gdd/Tyranny System.md` ("Changes from national focuses"); гейты и веса ниже - фокусная сторона-партнер. Mtth-факторы `low_tyranny_factor`, `medium_tyranny_factor` и `high_tyranny_factor` пикируют в полосах Libertarian / Moderate / Despotic и доходят до нуля на полосу в сторону.

**Гейт**: фокусы чисток и тайной полиции (класс `+20`) недоступны лидерам Liberal-or-lower (`docs/gdd/Tyranny System.md`, "Gating focuses by band"):

```
    available:
      +is_liberal_leader(no)
```

Authoritarian-обход для неконституционных фокусов смены правительства отложен (см. "Party-popularity modifiers"); такие фокусы получают только наклон ниже.

### Civil-war focuses - RU

Alt-history ветки, начинающие гражданскую войну, взвешиваются отдельно (`docs/gdd/Civil Wars.md`). `$ai_sandbox_modifier()` по-прежнему применяется. Поверх него:

**Ignition** (фокус, чья награда или всегда вызываемый им ивент может `start_civil_war` для ROOT):
```
      +modifier:
        $ai_civil_war_ignition_modifier()   # factor 0.25 in sandbox
      +modifier:
        factor(0)
        sandbox_civil_war_cap_reached()     # 3 distinct original_tags already in a civil war
```

**Root** такой ветки (первый эксклюзивный выбор, фиксирующий ее): только `$ai_civil_war_root_modifier()` (те же 0.25, **без** капа - иначе Испания-1936 заморозит каждое alt-history дерево).

Ивенты, миссии, решения, BoP-диапазоны и `on_action`, зовущие `start_civil_war`, капятся так же (`docs/gdd/Civil Wars.md`, "Event and mission overlays"). Не дублировать эти паттерны здесь.

Не тегировать intervention / "lessons from the Spanish Civil War" фокусы. Оставить существующие Tyranny-наклоны на неконституционных ignition; второй tyranny-фактор не стакать. Player `ai_will_do` - единственная поверхность: `available` без изменений.

**Развилка** "репрессии против реформ": обе опции mutually exclusive *друг с другом* и различаются репрессивностью, а не идеологией (`SIA_an_absolute_monarchy` / `SIA_a_constitutional_monarchy`, `POL_codify_national_unity` / `POL_draft_a_new_constitution`). Убрать `$crossroad_modifier`. **Не** умножать на `N` как party-popularity доли: между -25 и 25 оба внешних фактора нулевые, так что у Moderate-ИИ вообще не будет веса; `0.5 +` внутри макросов держит развилку открытой (Despotic 1.5 : 0.5, Moderate 0.5 : 0.5).

```
      +modifier:
        $ai_high_tyranny_fork()
```

```
      +modifier:
        $ai_low_tyranny_fork()
```

С третьим, серединным вариантом дать ему `$ai_medium_tyranny_fork()` (голый `mtth:medium_tyranny_factor`; какой-то фактор тогда всегда ненулевой, так что `0.5 +`-варианты не нужны, а крайние опции используют голые факторы).

Либеральный фокус, чей эксклюзивный сиблинг - **идеологический** выбор (`GER_reestablish_free_elections` против `GER_revive_the_kaiserreich`, `PER_free_elections` против `PER_islamic_restoration`) - не Tyranny-развилка: оставить party-popularity раздел и наклон.

**Наклон**: одиночный репрессивный фокус без развилки или неконституционный фокус смены правительства:

```
      +modifier:
        $ai_high_tyranny_tilt()
```

Одиночный либеральный фокус использует `$ai_low_tyranny_tilt()`. Макросы - это `1 + mtth:high_tyranny_factor` / `1 + mtth:low_tyranny_factor`.

**Не** комбинировать Tyranny-факторы с party-popularity факторами на одной развилке, если опции не различаются и идеологией, и репрессивностью одновременно; в этом случае перемножить две доли.

### Military-industrial complex modifiers - RU

```
      +modifier:
        $ai_mic_modifier()
```