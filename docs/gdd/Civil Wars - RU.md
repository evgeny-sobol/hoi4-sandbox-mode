<!-- source: 2d17a6c7fd23a677998917138e92e99278b080bd -->
# Civil wars - RU

Гражданская война - самый дорогой способ страны сменить политику: она раскалывает тег, сжигает дивизии и втягивает соседей. В рандомизированном sandbox-мире несколько таких - это флавор. Дюжина сразу - это шум: игрок не расскажет историю по карте, которая и так горит.

Этот документ - про то, **как часто** ИИ их начинает. Он не перепроектирует ванильный civil-war контент (гражданская в Испании, Седильо, вапсы, вторая финская война). Эти скрипты остаются. Sandbox меняет только то, пойдет ли в них ИИ, и разрешено ли четвертой стране взорваться, пока горят три.

Гражданские войны - это **не**:
- Honor. Начало гражданской войны не стоит Honor; Honor - про обещания *другим* странам (`docs/gdd/Honor System.md`).
- Tyranny как значение. Чистка или путч могут поднять Tyranny; сама гражданская война - метод, а не источник Tyranny (`docs/gdd/Tyranny System.md`). Неконституционные фокусы, случайно начинающие войну, используют существующий tyranny-наклон.
- Замена революционным ивентам `political.21/22/23`. У тех уже есть AI-only мирный референдум; здесь их не трогать.

Sandbox-only: все правила ниже работают под `is_sandbox_mode_on()`. Исторический режим не меняется.

## Why this is needed - RU

`$ai_sandbox_modifier()` (`docs/gdd/National Focuses.md`) ставит каждому фокусу вес 40, а исторические AI-планы абортятся. Политические корни, которые ванильный ИИ почти не берет - `USA_america_first`, балтийские "разбить тишину" / вапсы, норвежские фашистский и коммунистический опенеры - теперь конкурируют с промышленностью. Факторы популярности партий тянут эти корни. К 1936-37 несколько ИИ завершают фокус, реально стреляющий `start_civil_war`, в одно окно.

Первый проход занулил `ai_will_do` на фокусах **поджига** при трех разных воюющих `original_tag`. Нагромождение это не остановило. Наблюдаемая sandbox-игра observer (v0.1.1, `historical=0`, по февраль 1938): `cw` дошел до **8**. После `cap=1` / `ignition_base=0` лишние войны шли как `cw_declare` от ребелов (AST, GRE, потом MEX, LIT, PER, POL, ITA) - миссии, MTTH/плот-ивенты, BoP, `on_daily` - а не тегированные фокусы (`cw_ignition` ни разу не стрельнул). Счетчик был честным; запал был не на фокусе.

Испания - скриптованная война 1936 года, ожидается при свободном слоте. Остальные - alt-history запалы, которые ванилла стреляет не спрашивая фокусный ИИ.

Что это нагромождение **не** вызывает (не трогать в этой итерации):
- Дженерик-решения `prepare_for_*_civil_war`: `ai_will_do = 0`.
- Революционные ивенты `political.21/22/23`: ИИ выбирает скрытый референдум.
- Шпионские путч-операции (`00_operations.txt`).

## Design goals - RU

1. Одновременно идет максимум горсть гражданских войн. Картина по умолчанию: Испания плюс две другие; четвертая ждет, пока одна из них кончится.
2. Фокус гражданской войны - редкий политический бит, а не ровня "строить гражданские фабрики". ИИ все еще может его взять, особенно высокотиранный правитель на идеологической ветке.
3. Взвешивать **корень** гражданской ветки, а не только последний фокус. Иначе ИИ год сидит на ветке и детонирует в момент освобождения слота.
4. Не отменять и не переписывать ванильные `start_civil_war`-пейлоады (стейты, идеология, OOB, раскол персонажей). Кап применяется к *новым* AI-начинаемым войнам из **любого** скрипта, зажигающего запал - фокус, ивент, миссия, решение, BoP-диапазон, `on_action`. Уже идущие войны продолжаются.
5. Войны, начатые игроком, без ограничений. Кап и фактор 0.25 - только для ИИ (`ai_will_do` / `ai_chance` / `is_ai = yes` на оверлее). Человеческая Испания все равно получает 1936; человеческая Мексика все равно получает Седильо, если даст миссии истечь.

## Model - RU

### Active-war counter - RU

Глобальный, вне стран, `sandbox_civil_war_count`: число **разных `original_tag`**, у которых сейчас `has_civil_war = yes`.

Обе стороны одной войны делят `original_tag` (SPR и SPA, USA и CSA, балтийское правительство и его ребелы). Счет тегов, а не стран, означает: Испания - это 1, а не 2-4.

Перестраивать каждый `on_weekly` (и на `on_civil_war_end`, чтобы слот освобождался не дожидаясь недели). Также перестраивать на `on_declare_war`, когда **и** у ROOT, **и** у FROM есть `has_civil_war` (чтобы новый слот был виден в тот же день, но Италия, влезающая в Испанию, не считалась новой гражданской войной):

```
sandbox_civil_war_count = 0
seen[] cleared
every_country:
  if has_civil_war:
    t = original_tag
    if t not in seen[]:
      seen[].add(t)
      sandbox_civil_war_count += 1
```

**Cap: 3.** Scripted trigger `sandbox_civil_war_cap_reached`: `is_sandbox_mode_on()` и `sandbox_civil_war_count >= 3`.

Пока кап достигнут, ИИ не должен начинать новую гражданскую войну. Уже идущие продолжаются. Игрок все еще может поджечь еще одну.

AI-blocked хелпер (ивенты, миссии, on_actions, BoP - все, что не `ai_will_do`):

```
sandbox_civil_war_ai_blocked:
  is_ai = yes
  sandbox_civil_war_cap_reached()
```

В `sandbox_civil_war_cap_reached` уже требуется sandbox mode. Не складывать `is_ai` в кап-триггер: фокусный `ai_will_do` и так только для ИИ, а aiview должен показывать кап как country-level факт.

### Civil-war focus (definition) - RU

Фокус - это фокус **civil-war ignition**, если его `completion_reward` (или scripted effect / ивент, который он всегда зовет) может `start_civil_war` для ROOT.

Фокус - это **civil-war root**, если он первый взаимоисключающий выбор, фиксирующий дерево на ветке, чей позднейший ignition-фокус - нормальный исход (не редкий random_list). Примеры: `USA_america_first`, `USA_union_representation_act`, `FIN_the_second_finnish_civil_war`, `BALTIC_overthrow_the_government`, `EST_march_on_talinn` и его эксклюзивный опенер к вапсам, норвежские фашистский / коммунистический / "демократический к гражданской войне" опенеры.

Фокус, лишь *реагирующий* на чужую войну (`SPR_lessons_from_the_civil_war`, интервенция, волонтеры) - ни то ни другое. Не тегировать.

### Event and mission ignition (definition) - RU

**Event/mission ignition** - любой ванильный скрипт **вне** `completion_reward` нацфокуса, который может `start_civil_war` для ROOT (или для FROM / скриптованной цели) и тем занять новый слот `original_tag`.

Поверхности:
- Country events с MTTH / `trigger` (no-LaR `spain.1` / `spain.10`).
- `is_triggered_only`-ивенты, чьи `immediate` или единственный option всегда начинают войну (`mexico.1`, `PER_revolution_events.1`).
- Ивенты с AI-выбираемой опцией гражданской войны (`election.11.b` / `election.12.b`, некоторые GRE/BFTB опции).
- `complete_effect` решений / `timeout_effect` / `complete_effect` миссий (Седильо, польская крестьянская забастовка, AST-ветераны).
- `on_action` / `on_daily_TAG` (`on_daily_AST` - бунт ветеранов).
- BoP `on_activate`, стреляющий ивентом гражданской войны (итальянский великий совет, total-control диапазон -> `BBA_italy_civil_war.1`).

Не ignition (не оверлеить):
- Интервенция, волонтеры, "уроки гражданской войны в Испании".
- Персонажные/OOB-довески, идущие **после** уже true `has_civil_war`.
- `political.21/22/23` (у AI-опций гражданской войны уже `ai_chance = 0`).

Война Испании 1936 - event/mission ignition (no-LaR: `spain.1`; LaR: выборы `lar_spain.1`, затем военные-плот **миссии**). Она **не** exempt от капа. При свободном слоте стреляет как ванилла. При достигнутом капе AI-Испания ждет; слот она занимает уже после начала войны. Человеческая SPR никогда не задерживается.

Война, начатая **другим тегом** (решение ENG зажигает AST, ивент LIT зажигает POL) - все равно ignition для `original_tag` **цели**. Гейтить AI-актора. Игрок, принимающий это решение, не ограничен.

## AI weighting (focuses) - RU

Макросы в `common/macros.hml`, паттерны в `docs/gdd/National Focuses.md`. Без изменений с первого прохода.

**Ignition** (`$ai_civil_war_ignition_modifier()`), рядом с `$ai_sandbox_modifier()`:

```
macro ai_civil_war_ignition_modifier():
  factor(0.25)
  is_sandbox_mode_on()
```

Кап - **отдельным** модификатором, чтобы aiview показывал 0.25 при свободном капе:

```
      +modifier:
        $ai_civil_war_ignition_modifier()
      +modifier:
        factor(0)
        sandbox_civil_war_cap_reached()
```

`factor(0.25)` применяется даже при пустой карте: гражданская война - редкость, а не "только когда кап взят". Вместе с партийными/Tyranny-факторами ignition-фокус остается берущимся для фашистского/коммунистического деспота при пустом капе.

**Root** (`$ai_civil_war_root_modifier()`): те же 0.25, **без капа**. Блокировка корня, пока Испания воюет, заморозит каждую alt-history политическую ветку в 1936. Кап останавливает только спичку, зажигающую запал. Если ИИ прошел ветку при полном капе, он сидит на других доступных фокусах, пока слот не откроется, затем может взять ignition-фокус.

Tyranny: ignition-фокусы, которые заодно неконституционны, уже имеют `$ai_high_tyranny_tilt()` / fork-макросы. Оставить. Второй tyranny-фактор на тот же блок не добавлять.

## Event and mission overlays - RU

**Не** заворачивать `start_civil_war` в generic scripted effect: пейлоад (идеология, размер, стейты, персонажи) разный в каждой точке вызова. Оверлеить вокруг вызова. Откладывать, а не удалять запал.

`is_triggered_only`-ивенты и таймауты миссий часто ставят флаги "уже бунтовали" в `immediate` **до** `start_civil_war`. Если пропустить войну после этих флагов, бунт съеден навсегда. Гейтить **до** флага, либо рестартовать миссию / перестреливать ивент без установки флага.

### Pattern A - MTTH / daily trigger (Spain no-LaR) - RU

Ивент переоценивается ежедневно. Добавить `NOT sandbox_civil_war_ai_blocked()` в `trigger` (или эквивалент `OR = { is_ai = no NOT cap }`). Когда кап освободится, ванильный MTTH продолжится. Несработавший триггер логать не может: недельный `cw_defer spain` - вот что доказывает, что AI-Испания ждет. Когда ивент реально стреляет: `cw_event spain.1` / `spain.10`.

LaR-Испания: оверлеить **военные-плот миссии**, реально начинающие войну, а не только `lar_spain.1` (этот ивент - выборы 1936, он должен стрелять). Активные плот-миссии уже эмитят `cw_defer`.

### Pattern B - AI-choice option (elections, some country events) - RU

На опцию, зовущую `start_civil_war`:

```
ai_chance:
  +modifier:
    factor(0)
    sandbox_civil_war_cap_reached()
```

Мирная / другая опция остается. Игрок по-прежнему видит обе. Если **каждая** опция начинает войну (ITA `BBA_italy_civil_war.1`), этот паттерн не спасет - применять C на **вызывающем** (BoP `on_activate`, фокус, миссия). `ai_chance = 0` пропуск логать не может; civil-war опция логирует `cw_event` когда взята.

### Pattern C - Forced fuse (immediate, timeout, on_daily, BoP) - RU

```
if:
  sandbox_civil_war_ai_blocked()
  # defer: activate_mission again, or country_event = { id = X days = 7 }, or skip this on_daily tick
  log("#sandbox ... cw_defer ...")
else:
  # vanilla start_civil_war / country_event unchanged
```

Для `on_daily_AST` ветеранов: добавить `NOT sandbox_civil_war_ai_blocked()` в существующий `if`-лимит. На следующий день, если стабильность все еще низкая и слот свободен, стрельнет. Не чистить `AST_veterans_revolt_active` на отложенном тике.

Для ITA BoP: не стрелять `BBA_italy_civil_war.1` пока blocked; проверять снова, пока диапазон активен и кап освободился (недельно / следующий `on_activate`, если диапазон ретриггерится; если нет - короткий скрытый ивент на `on_weekly`, пока диапазон активен).

### Pattern D - Decisions the AI can take - RU

Как фокусы: `ai_will_do` `factor(0)`, когда `sandbox_civil_war_cap_reached()`. `available` без изменений (игрок). Включая ENG-решения, `start_civil_war`-ящие домиинион.

## Coverage - RU

### Focuses (first pass, keep) - RU

Тегировать каждый ванильный фокус, чья награда содержит `start_civil_war` (или `effect_tooltip` такого, который потом выполняет реальная награда). Известный список в `common/national_focus/*.txt` на 1.19:

- Прямой `start_civil_war` в фокусе: `AFG_the_faqirs_revolt`, `AFG_return_of_the_emir`, `AFG_parliamentary_democracy`, `AFG_socialist_coup`, `ARG_viva_la_revolucion`, `BALTIC_overthrow_the_government`, `BALTIC_arm_baltic_reds`, `BRA_ban_political_parties`, `BRA_launch_the_revolution`, `BUL_overthrow_the_tsar`, `BUL_abolish_the_monarchy`, `BUL_depose_the_tsar`, `CHL_avenge_the_pacification_of_araucania`, `COG_strike_while_the_rion_is_hot`, `COG_uniao_dos_povos_do_norte_de_angola`, `CZE_kohler_faction`, `DEN_seize_power`, `DEN_ask_for_support`, `EST_march_on_talinn`, `FIN_the_second_finnish_civil_war`, `FIN_a_fascist_regime`, `FRA_destroy_the_counter_revolution`, `wuw_HUN_reviving_the_spirit_of_1848`, `RAJ_give_me_blood_and_i_will_grant_you_freedom`, `RAJ_indian_peoples_army`, `RAJ_indian_national_army`, `IRQ_kurdish_revolt`, `JAP_cast_the_die`, `JAP_pre_emptive_coup`, `PER_strengthen_iranian_parliament`, `PER_force_abdication`, `PER_iranian_socialist_revolution`, `PER_march_on_saadabad`, `POR_reorganization_of_the_communist_party`, `lar_portugal_iberian_workers_united`, `POR_allow_free_elections`, `POR_ditadura_militar`, `POR_restoration_of_the_monarchy`, `SIA_the_kings_gambit`, `SIA_and_spring_the_trap`, `SIA_unseat_the_government`, `SAF_support_the_german_coup`, `AAT_Sweden_nationalists`, `TUR_restack_the_officer_corps`.

- Event / scripted-effect ignition **из фокуса**: все равно тегировать **root + ignition** на NOR / EST / LAT / LIT / POL / USA / MEX. Кап фокуса сохраняется; этот проход также оверлеит ивент/миссию, которую стреляет фокус, так что фокус, завершенный игроком при капе, войну все равно начинает, а фокус, завершенный ИИ, не проскочит мимо капа через ивент.
- Не тегировать intervention / "lessons from the Spanish Civil War" / volunteer-фокусы.

### Events, missions, decisions, on_actions (this pass) - RU

Пройти ванильный `start_civil_war` вне `common/national_focus/`. Оверлеить каждый ignition. Известные дыры из плейтеста v0.1.1 плюс скрипты того же семейства:

- **Spain**: no-LaR `spain.1` / `spain.10`; LaR military-plot миссии (не ивент выборов).
- **Mexico**: `MEX_mission_cedillos_rebellion` timeout -> `mexico.1`; миссии Cristiada / второй революции -> `mexico.28` / `mexico.30`.
- **Australia**: `on_daily_AST` - бунт ветеранов; таймаут миссии `AST_veterans_revolt`; TAOG-ветки, зовущие `AST_instigate_civil_war_in_target` на сам AST.
- **Greece**: BFTB-ивенты, `start_civil_war`-ящие (`bftb_greece.105` через `bftb_greece.100` else_if + недельный ретрай, `.218` из `.207.b` Pattern B - не опции "начать войну в Турции", если слот цели не TUR).
- **Poland**: таймауты крестьянской забастовки / санационных миссий и civil-war эффекты `POL_scripted_effects`.
- **Baltic**: LIT/LAT/EST решения и NSB-ивенты, начинающие войну в ROOT (и LIT-ивенты, начинающие в POL - гейтить актора, считать цель). `EST_vaps_down_effect` (тот же паттерн, что Iron Wolf). Триггер `EST_events.7` + недельный ретрай. `LAT_events.8` (обе опции - война; миссия `available` + триггер ивента). `LIT_events.10` / `EST_events.9` Pattern B.
- **Persia**: `PER_revolution_events.1` (триггер ивента + недельный ретрай) и ignition на `PER_revive_old_ways`; задержка миссии `PER_civil_war_imminent`.
- **Italy**: BoP `ITA_grand_council_total_control_range` -> `BBA_italy_civil_war.1` (триггер ивента + недельный ретрай). Оверлеи используют `sandbox_civil_war_ai_allowed()` (`= yes`), а не `scripted_trigger = no`.
- **Ethiopia**: BoP total-control диапазоны -> `BBA_ethiopia_balance_of_power_events.01`; недельный ретрай, пока диапазон жив.
- **Siam**: `siam.8` (Songsuradet, отложен из `siam.7`); миссия `SIA_war_fervor_coup`.
- **Soviets**: ignition-фокусы `SOV_left_opposition_coup` / `SOV_coup_detat` / `SOV_the_hands_do` плюс ивенты, которые они ставят в очередь.
- **Lithuania**: `LIT_iron_wolf_partisans` / `LIT_iron_wolf_down_effect` (тик идеи Iron Wolf на bad_4). `EST_vaps_down_effect` - то же семейство.
- **Elections**: `election.11.b` / `election.12.b` - Pattern B.
- **UK/dominions**: ENG-решения, `start_civil_war`-ящие CAN/SAF/AST/NZL.

Если неясно, может ли `random_list` пропустить войну, - все равно оверлеить: кап только задерживает ИИ, награду не удаляет.

## Honor, Tyranny, Rivals - RU

Без изменения Honor при старте гражданской войны. Победитель все равно роллит Honor/Tyranny на `on_civil_war_end` как обычно.

Rivals: `on_civil_war_end` уже переролливает личного ривала победителя. Без дополнительных правил. Противник по гражданской войне автоматически ривалом не становится (они воюют; `$is_rival_of()` и так считает это rivalry для гейтов).

## Implementation notes - RU

- Счетчик и `seen[]` живут в глобальном скопе. `seen[]` - темп-перестройка, а не персистентный список старых войн. Дедупликация через `every_country_with_original_tag` / `original_tag_to_check = THIS` - не биндить loop-переменную, компилирующую `THIS` в недельный ROOT.
- `sandbox_civil_war_cap_reached` - scripted trigger, чтобы файлы фокусов не читали переменную сырым `compare`. Ванильный оверлей в блоках `limit` / `trigger` использует `sandbox_civil_war_ai_allowed()` (`NOT` от `sandbox_civil_war_ai_blocked`). Не писать `sandbox_civil_war_ai_blocked = no`: кастомный `scripted_trigger = no` инвертируется ненадежно.
- `$ai_civil_war_ignition_modifier` **не должен** складывать `factor(0)` капа в тот же блок, что `factor(0.25)`: если кап-триггер упадет, весь модификатор пропустится и 0.25 пропадут. Два модификатора, как в сниппете выше.
- `$ai_sandbox_modifier()` на этих фокусах сохраняется. Порядок: sandbox 40, затем 0.25, затем кап, затем party/Tyranny как обычно.
- Перестраивать счетчик на `on_weekly`, `on_civil_war_end` и civil-war `on_declare_war`. Не ждать неделю после конца Испании, чтобы открыть слот.
- `original_tag` ребела обычно родительский. Если динамический тег `Dxx` покажет `has_civil_war` со своим original_tag - считать отдельным слотом; принять.
- Пустые `t*` в `#sandbox`-пульсах часто печатают pulse ROOT (HAI), когда слот массива пуст. Доверять `cw=`, а не уникальным тегам `t*`.
- Компилировать после тегирования `.include`-файлов (`compile-after-hsl` rule), включая оверлеи `events/` и `common/decisions/`.

## How to read `game.log` - RU

Первая строка - версия (`#sandbox Mode Overhaul v0.1.2`). Дальше `sandbox_start historical=0` или `historical=1`.

| Token | When | What to read |
| --- | --- | --- |
| `cw_pulse` | weekly, HAI | Census. Use `cw=` and `cap=`. The `N->N` arrow is the post-rebuild snapshot, not a weekly delta. Ignore `t*` for identity. |
| `cw_count` | counter actually changed | Same fields; the arrow *is* the delta. |
| `cw_declare` | civil-war `on_declare_war` | Slot taken. Arrow should be `N->N+1` (Spain is 1, not SPR+SPA). `ai=0` if **either** ROOT or FROM is human (ROOT is often a Dxx rebel). `other=` is the other side - use that, not Dxx, to name the war. |
| `cw_end` | `on_civil_war_end` | Slot freed the same day. Then a waiting fuse may fire that day or within a week. |
| `cw_ignition` / `cw_root` | focus `completion_reward` | `ai=0` is the player. Root has no cap; ignition must not complete while `cap=1` for an AI. |
| `cw_defer` | Pattern C skip this week | Tag + fuse id (`spain`, mission id, `BBA_italy_civil_war.1`, `on_daily_AST`). Proves the AI is waiting, not that vanilla has not rolled yet. |
| `cw_event` | fuse actually fired | `spain.1` / `spain.10`, `election.11.b` / `12.b`, ITA retry. `ai=` is THIS (the country running the event), not a rebel. |

**Fail the cap** if any `cw_pulse` / `cw_count` has `cw=` **greater than 3**, or an AI (`ai=1`) `cw_declare` whose arrow is `3->4`. A `2->3` line with `cap=1` is the third war, not a fail. A player (`ai=0`) may push `cw` above 3; that is allowed.

**Name an ungated fuse:** an AI `cw_declare` that raises the count with no `cw_ignition`, `cw_event`, or `cw_defer` for that original_tag in the days before it. v0.1.1 playtest extras (AST, GRE, MEX, LIT, PER, POL, ITA) must now show `cw_defer` or `cw_event` first. A new extra without those tokens is a hole (NSB events, `bftb_greece.105` from `.100`, `bftb_greece.218`).

**Silent by design:** Pattern B skip (`ai_chance` 0) and Pattern D (`ai_will_do` 0) do not log. Prove them by the fail rule above, not by a defer line.

Historical: after `sandbox_start historical=1` the rest of the log must not contain `cw_`. Overlay files still exist; their gates require sandbox mode, so they are no-ops.

## Acceptance checklist - RU

Log-first. Observer sandbox unless the item says human or aiview. Tick only when the grep holds (compound items split so a partial pass is visible).

- [x] First `#sandbox` line is the current version; next is `sandbox_start historical=0`.
- [x] Spain 1936 with `cw<3`: `cw_event spain.1` / `spain.10` / `lar_spain.2` then `cw_count` whose arrow is `N->N+1` (not +2 for SPA/SPB).
- [ ] AI Spain while `cap=1` and no SCW yet: weekly `cw_defer spain` (and `cw_defer SPA_military_plot_nationalists` / `SPR_military_plot_republicans` if LaR missions are already ticking). No `cw_event spain.1` until a `cw_end` drops `cap` to 0.
- [ ] Human SPR at `cap=1`: no `cw_defer spain`; `cw_event spain.1` with `ai=0`; `cw_declare` `ai=0`.
- [x] After Spain, a second and a third AI war may start (`cw=` 2 then 3) from focus (`cw_ignition`), event (`cw_event`), or mission (`cw_defer` then `cw_declare`).
- [x] No AI `cw_declare` with arrow `3->4` or `cw=` 4 on a pulse. v0.1.1 hit 8 via event/mission after `cap=1`; that must not recur through 1938.
- [ ] Capped ITA BoP: `cw_defer BBA_italy_civil_war.1` weekly while the range is active; after `cw_end`, `cw_event BBA_italy_civil_war.1` (same week or next).
- [x] Capped Cedillo / peasants / veterans with the mission already ticking: `cw_defer MEX_mission_cedillos_rebellion` (or `POL_peasants_strike` / `AST_veterans_revolt` / `on_daily_AST`); after `cw_end`, the timeout may fire within a week (no more defer, then `cw_declare`).
- [ ] `cw_root USA_america_first` may appear while `cap=1`. `cw_ignition USA_ally_with_the_silver_shirts` / `USA_union_representation_act` must not appear for an AI (`ai=1`) while `cap=1`.
- [ ] Human USA ignition or human Mexico Cedillo timeout at `cap=1`: `cw_ignition` / `cw_declare` with `ai=0`; no `cw_defer` from that player tag.
- [ ] Historical: `sandbox_start historical=1`, then no `cw_` lines. Vanilla Spain 1936 still happens in-game.
- [ ] aiview (in-game, not the log) on an ignition focus, cap free: sandbox 40 x 0.25 = 10, times party/Tyranny. Cap reached: 0.

## Out of scope for this iteration - RU

- Rewriting Spain, Cedillo, or any `start_civil_war` payload (states, ideology, OOBs).
- Player decisions "start / join a civil war" besides applying the same AI gate as other decisions.
- Spy coup operations (`00_operations.txt`).
- Stability-crisis civil wars (`stability.3`) unless a playtest shows they cluster; then use Pattern C on that mission.
- News events / notifications about the cap.
- A game rule for the cap (3 vs 2). Hard-code 3; promote to a rule only if testers want it tighter.

## Second iteration (not blocking) - RU

- If the 1936 cluster is still too hot because many AIs *finish* the branch the week Spain starts: lower root 0.25, or delay ignition with `days = 30` only when the cap is reached (hidden event) - that second option is a content change, not a weight change, and needs a separate pass.
- Reserve a slot for Spain so 1936 always fires even if two others went first - only if testers want Spain guaranteed rather than "up to three including Spain".
- Count "player's civil war" toward the cap or not (currently it does, which is what we want: the player's Spanish playthrough still occupies a slot for the AI).
- `stability.3` if wartime crises start clustering.