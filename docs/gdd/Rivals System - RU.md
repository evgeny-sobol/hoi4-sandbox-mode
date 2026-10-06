<!-- source: 2d17a6c7fd23a677998917138e92e99278b080bd -->
# Rivals - RU

Rivals отвечают на один вопрос о стране: "**кого** она хочет бить?" Honor отвечает "как она держит обещания" (`docs/gdd/Honor System.md`), Tyranny - "как она правит дома" (`docs/gdd/Tyranny System.md`), Opinion - "как к ней относятся другие". В рандомизированном sandbox-мире rivalry - источник долгих читаемых конфликтов: они направляют агрессию ИИ и объясняют игроку, почему кто-то точит на него нож.

Rivalry - это **не**:
- Оправдание. Атака ривала под пактом или гарантией стоит столько же Honor, сколько атака кого угодно.
- Opinion. Rivalry *питает* opinion через два opinion-модификатора; opinion никогда не создает и не убирает ривала.
- Война. Война делает `$is_rival_of()` true для гейтов, но сама по себе не кладет страну в `rivals[]` (а вот объявление войны нам - кладет, см. "Event-driven rivals").

Sandbox-only: все правила ниже работают под `is_sandbox_mode_on()`.

## Where it lives - RU

- `common/scripted_effects/99_sandbox_scripted_effects.hsl`: selection (`select_major_rival`, `select_minor_rival`), slot discipline (`set_rival`, `clear_rival`, `reroll_leader_rival`, `add_rivalry_vs`, `become_event_rival`), monthly loop (`review_rivals`, `update_rivalry_monthly`, `fill_rival_vacancies`, `expire_former_rivals`), hooks (`apply_rivalry_on_declare_war`, `apply_rivalry_on_capitulation`, `clear_annexed_from_rivals`).
- `common/macros.hml`: `$add_rivalry`, `$rivalry_vs_into`, `$ai_rivalry_modifier`, `$ai_rivalry_modifier_max`, `$not_rival_of_PREV`, `$is_rival_of`, AI-plan macros `rival_base` / `rival_contain` / `rival_feud`.
- `common/scorers/country/99_sandbox_scorer.hsl`: `major_rivals_scorer` (from `global.majors`, ideology-driven), `minor_rivals_scorer` (from `global.countries`, geography-driven).
- `common/ai_strategy/99_sandbox_rivals_system.hsl`: three plans per tag (generated list).
- `common/opinion_modifiers/99_sandbox_opinion_modifiers.hsl`, `common/scripted_localisation/99_sandbox_scripted_localisation.hsl`, `localisation/english/99_sandbox_l_english.yml`.

Дефекты реализации до 2026-09, которые этот дизайн убрал: ривалы выбирались раз и навсегда; rivalry не доходил до opinion; `var:rival_ideology` никогда не ставился; единственный AI-план использовал `antagonize value(-200)` (ванилла использует положительные значения для враждебности); cooperation-фокусы, заблокированные ривалом, никогда не разблокировались.

## Model - RU

Три слота, как сейчас, разной природы:
- `rivals[0]` - **ruler's rival**. Всегда мажор. Привязан к персоне: перероллится при каждой смене правителя. Тултип "Dislikes X".
- `rivals[1]`, `rivals[2]` - **national rivals**. Соседи и региональные державы, привязаны к нации, переживают правителей.

Новый параллельный массив `rivalry[]` - **intensity** каждого слота, целое в `[0, 100]`, инициализируется 50 при заполнении слота.

Полосы:
- `< 25` **Cold** - остаточная неприязнь.
- `25-75` **Rival** - рабочее состояние.
- `>= 75` **Feud** - ИИ готовится к войне; фокусы против ривала получают большой бонус веса.

Один и тот же тег может занимать слот 0 и национальный слот сразу (Советский Союз для Финляндии); эффекты складываются.

Пустой слот держит `0` в обоих массивах.

## Design goals - RU

1. У rivalry есть начало, середина и конец. Каждого ривала можно потерять (разрядка, аннексия, альянс), и каждая потеря открывает слот для кого-то еще после паузы.
2. У rivalry есть зубы вне ИИ: opinion, war support, веса и гейты фокусов.
3. Мир двусторонний: ривалы склонны выбирать друг друга в ответ, победа охлаждает победителя и разогревает проигравшего.
4. Honor остается чистым: rivalry никогда не трогает `honor` и не снижает цену предательства.

## Selecting a rival (scorer changes) - RU

Оба скорера (`FROM` - выбирающая страна, `THIS` - кандидат):
- `factor(0)`: `FROM == THIS`; та же фракция, что у `FROM`; сюзерен или субъект `FROM`; в `FROM.former_rivals[]` (кулдаун, см. "Losing a rival").
- `x0.25`: друзья по `$is_friend_of()` (пакт или гарантия). Ривал под пактом возможен, но редок.
- `x2`: `THIS` владеет кором `FROM`, или `FROM` владеет кором `THIS` (`any_owned_state: is_core_of(...)`). Главный "исторический" драйвер.
- `x2`: `THIS` уже держит `FROM` в своем `rivals[]`. Взаимность превращает односторонние неприязни в двусторонние конфликты.
- `x1000`: в войне с `FROM` (существующее).
- Заменить `has_government(var:FROM.rival_ideology)` на `has_enemy_ideology_with_FROM()` (уже в `99_sandbox_scripted_triggers.hsl`) и удалить мертвую ветку `rival_ideology` из `$ideology_factor`.

`major_rivals_scorer` сохраняет идеологическую логику (вражеская идеология +40, то же правительство x0.5); `minor_rivals_scorer` - географическую (субъект/сосед/континент +40, вне континента x0, если не война).

## Lifecycle - RU

### Initialisation - RU

Без изменений: `initialize_country_for_sandbox_mode()` заполняет все три слота на старте, а недельный `sandbox_initialized`-гейт покрывает поздно созданные страны (ребелы, релизнутые нации). Каждый заполненный слот получает `rivalry = 50`.

### Ruler change - RU

На `on_ruling_party_change` и победителю `on_civil_war_end`: `clear_rival(0)` без записи в кулдаун, затем сразу `select_major_rival()`. Национальные слоты не тронуты. У нового правителя, таким образом, всегда свежий личный враг, как в тултипе.

### Losing a rival - RU

Немедленная чистка, проверяется ежемесячно через `review_rivals()` и на хуках `on_annex`, `on_join_faction` / `on_join_allies`, `on_puppet`:
- ривал больше не существует;
- ривал в нашей фракции;
- ривал - наш сюзерен или наш субъект.

Известная задержка: ванильный `on_join_faction` не стреляет для эффекта `add_to_faction`, а `on_puppet` стреляет только из мирных конференций. Фокусные вхождения во фракции и паппетинг - обычный sandbox-путь - ловятся месячным ревью, так что ривал может до месяца сидеть в нашей фракции с opinion-модификатором -20.

Detente: `rivalry`, дошедший до 0, чистит слот.

При любой чистке (`clear_rival(slot)`): снять наши opinion-модификаторы в его сторону, обнулить оба массива на этом индексе и дописать тег с текущим `months_elapsed` в `former_rivals[]` / `former_rivals_month[]`. Кулдаун - **24 месяца**: в течение него страна скорит 0 в обоих скорерах. Записи старше 24 месяцев чистятся ежемесячно, тем же механизмом, что `dropped_pacts[]` в Honor.

### Filling a vacancy - RU

Ежемесячно, `fill_rival_vacancies()`:
- пустой национальный слот заполняется с вероятностью 1/6 (`randi(1, 6) == 1`), так что вакансия живет в среднем полгода - мир не находит замену врагу мгновенно;
- пустой слот 0 заполняется сразу после смены правителя (выше), иначе с тем же шансом 1/6.

### Event-driven rivals - RU

Страна, объявившая нам войну и не входящая в `rivals[]`, сразу становится национальным ривалом (`on_declare_war`, обрабатывается в скопе `FROM`): занимает пустой национальный слот с `rivalry = 75`; если пустого нет, вытесняет национальный слот с минимальным `rivalry`, при условии что значение `< 25`. Иначе ничего не происходит (война все равно считается через `$is_rival_of()`).

## Rivalry changes - RU

### Monthly (per slot, summed, then clamped to `[0, 100]`) - RU

- `+2` мы воюем с ривалом.
- `+2` ривал владеет нашим кором или мы владеем его кором.
- `+1` вражеская идеология (`has_enemy_ideology_with`); `-1` то же правительство.
- `+1` ривал воюет хотя бы с одним нашим другом (`$is_friend_of()`); один раз, не за каждого друга. Реализовано из скопа ривала как `any_enemy_country->is_friend_of_ROOT()`, так что `update_rivalry_monthly()` можно звать только с ROOT = страна (как делает `on_monthly`).
- Только слот 0: `+1`, если наш правитель Authoritarian или Despotic (режиму нужен внешний враг); `-1`, если Libertarian или Liberal. Это единственное пересечение с Tyranny.
- `-1` у нас пакт о ненападении с ривалом.
- `-1` базовый дрейф, применяется только если ни одно `+`-условие выше не выполнено.

Итог: неподпитываемая rivalry угасает с 50 до 0 примерно за четыре года; коры плюс война дотягивают до Feud за год.

### Discrete events - RU

- `+25` ривал объявляет нам войну (`on_declare_war`: ROOT атакующий, FROM цель; применяется в скопе FROM на слот с ROOT).
- `+15` ривал объявляет войну нашему другу.
- `-50` ривал капитулирует нам (`on_capitulation`: ROOT капитулирующий, FROM победитель; применяется в скопе FROM). Победа утоляет.
- `+25` мы капитулируем ривалу (применяется в скопе ROOT). Реваншизм. Если победителя нет в нашем `rivals[]`, он входит по event-driven правилу выше.

Пара намеренно асимметрична: после войны победитель остывает, а проигравший держит обиду.

Все изменения идут через `$add_rivalry(slot, value)` с клампом и детенте-чисткой на 0. Лукапы слотов по тегу - через `rival_slot_of(tag)` (темп `rival_slot`, `-1` если нет).

## Effects - RU

### Opinion - RU

Два opinion-модификатора в `common/opinion_modifiers/99_sandbox_opinion_modifiers.hsl`, вешаются через `add_opinion_modifier` (цель = ривал) из `set_rival(slot, tag)` и снимаются через `clear_rival(slot)`:
- `national_rival` -20 (слоты 1-2),
- `leaders_rival` -10 (слот 0).

Складываются до -30, когда один тег в обоих. Через opinion rivalry течет в каждый существующий `$ai_antagonism_modifier` / `$ai_cooperation_modifier`, не трогая файлы фокусов.

### AI strategies - RU

`99_sandbox_rivals_system.hsl` растет с одного до трех планов на тег, включаемых по `rivalry` слота с тегом:
- любой ривал: `antagonize 200` (знак исправлен), `alliance -200`, `befriend -200`;
- полоса Rival и выше (`rivalry >= 25`): `contain 100`;
- Feud (`rivalry >= 75`): `conquer 100`, `prepare_for_war 100`.

Пер-теговый макрос `country_is_rival(_country_)` становится тремя макросами (`rival_base`, `rival_contain`, `rival_feud`) или одним макросом на три плана; генератор, выпустивший список тегов, сохраняется.

### National focuses - RU

Паттерны - в `docs/gdd/National Focuses.md`, "Diplomacy modifiers":
- cooperation-фокусы с **одним-двумя** именованными партнерами гейтятся: `available: $not_rival_of_PREV($TAG)` (alias-safe форма `$TAG->is_rival_of_PREV(no)`) и `factor(0)` на `$TAG in rivals[]`;
- cooperation-фокусы, зовущие **трех и больше** стран (фокусы строительства фракций вроде `USA_hemisphere_defense`, `ITA_south_american_alliances`, балтийские и балканские приглашения) **не** гейтятся и `factor(0)` не получают. Национальных ривалов набирают из соседей и своего континента, так что один из многих приглашенных почти всегда ривал, и гейт заблокирует фокус навсегда; ривальские opinion-модификаторы уже снижают усредненный cooperation-фактор, а ИИ самого ривала отказывает в альянсе (`alliance -200`);
- antagonism-фокусы дописывают `$ai_rivalry_modifier($TAG)` рядом с `$ai_antagonism_modifier($TAG)`: `factor(1 + rivalry_vs / 50)`, где `rivalry_vs` - максимальный `rivalry` по слотам с `TAG` (x1 для не-ривала, x2 на 50, x3 на Feud); две цели используют `$ai_rivalry_modifier_max($TAG1, $TAG2)`; три и больше целей расписывают тот же модификатор по одной строке `$rivalry_vs_into($TAG)` на цель (паттерн в `docs/gdd/National Focuses.md`);
- макросы считают `rivalry_vs` внутри модификатора темп-переменными и `if`-триггерами по трем слотам (`ai_will_do` - триггерный контекст, так что scripted effect вызвать нельзя); файлы фокусов никогда не индексируют `rivalry[]` напрямую;
- покрытие полное: каждый `$ai_antagonism_modifier` и каждый мультитаргетный блок `antagonism = ...`, включая общие деревья (`baltic_shared`, `china_shared*`, `indonesia_joint`, `TSR_*`), имеет rivalry-модификатор;
- алиасы тегов следуют правилу `country_exists`-гейта из того же документа.

### War support - RU

- Объявление войны ривалу с `rivalry >= 50`: `add_war_support(0.05)` один раз (популярная война).
- Ривал объявляет войну нам: `add_war_support(0.10)` один раз.

### Honor and Tyranny - RU

Honor: без изменений. `can_PREV_get_wargoal_on_THIS` и штрафы предательства игнорируют rivalry. Rivalry касается Honor лишь косвенно: друзья - маловероятные ривалы (x0.25), а пакт охлаждает существующую rivalry (-1 в месяц).

Tyranny: только месячный член слота 0 выше.

## Tooltips and localisation - RU

- `LocKey_personality_tt` показывает полосу по слотам: "Dislikes [leader] ([flag] [name], Feud). [Adjective] citizens dislike [flag] [name] (Rival), [flag] [name] (Cold)." Пустые слоты опускаются (нужны три варианта или scripted-loc хелпер; решает middle designer).
- Opinion-модификаторы: `national_rival` "National rival", `leaders_rival` "Personal rival of the ruler".
- `LocKey_is_rival_of_PREV_tt` / `_NOT` существуют; добавить `LocKey_is_rival_of_ROOT_tt` / `_NOT`, если `is_rival_of_ROOT` используется в тултип-контексте.

## Implementation notes - RU

Массивы и переменные (скоп страны): `rivals[]` (3), `rivalry[]` (3), `former_rivals[]`, `former_rivals_month[]`; штампы по существующему счетчику `months_elapsed`.

Эффекты в `99_sandbox_scripted_effects.hsl` (scripted effects не принимают параметров; аргументы едут в темп-переменных `rival_slot`, `rival_tag`, `rival_intensity`, `rivalry_delta`):
- `set_rival()`: пишет оба массива, вешает opinion-модификатор под тип слота (только если страна существует), сбрасывает `rival_intensity` в 50.
- `clear_rival()`: снимает opinion-модификатор, зануляет оба массива, дописывает в `former_rivals[]`, если не стоит one-shot флаг `sandbox_clear_rival_no_cooldown` (реролл при смене правителя).
- `$add_rivalry(slot, value)` (макро): кламп, детенте-проверка. Та же дисциплина, что у `$add_honor()`: `&rivalry[i]` больше нигде не писать. `add_rivalry_vs()` применяет `rivalry_delta` к каждому слоту с `rival_tag`.
- `review_rivals()`, `update_rivalry_monthly()`, `fill_rival_vacancies()`, `expire_former_rivals()`: monthly.
- `select_major_rival()` / `select_minor_rival()`: unchanged weighted-random body; зовут `set_rival()` вместо записи `&rivals[i]`, чтобы вешался opinion-модификатор.

Кросс-скоп чтения темп-переменных (`var:PREV.some_temp`) нигде в системе не используются; где нужно состояние другой страны, эффект входит в ее скоп и возвращается через `PREV` или `ROOT`.

Хуки (`common/on_actions/99_sandbox_on_actions.hsl`):
- `on_monthly`: четыре месячных эффекта выше, после `months_elapsed += 1`.
- `on_ruling_party_change`, `on_civil_war_end` (ROOT победитель): реролл слота 0.
- `on_declare_war` (ROOT атакующий, FROM цель): сторона атакующего - war-support бонус против ривала; сторона цели - `+25`, event-driven ривал, war-support бонус; каждая остальная страна - `+15`, если цель ее друг, а атакующий в ее `rivals[]`.
- `on_capitulation` (ROOT капитулирующий, FROM победитель; скопы проверить в игре): `-50` для FROM, `+25` / event-driven ривал для ROOT.
- `on_annex` (ROOT аннексирующий, FROM аннексированный): `every_country: if FROM in rivals[]: clear_rival(...)`.
- `on_join_faction` / `on_join_allies`, `on_puppet`: прогоняют `review_rivals()` для обеих сторон.

Скореры не читают темп-переменные селектора; кулдаун-тест - это `THIS in FROM.former_rivals[]`.

Арифметика, передаваемая в макросы, сначала считается в темп-переменную (ограничение компилятора `MATH`, см. Honor implementation notes).

Ограничения движка, найденные на первом запуске (`error.log` 2026-09-06):
- `add_opinion_modifier` / `remove_opinion_modifier` отвергают `target = var:x` ("Malformed token"). `set_rival()` / `clear_rival()` входят в скоп ривала (`var:rival_tag:`) и возвращаются с `PREV:`, чтобы цель писалась как `PREV`.
- Элементы массива внутри матблока (`clamp(rivalry[i] + d, ...)`) сначала читаются в темп (`cur_rivalry = rivalry[i]`); за malformed-token ошибками выше шли ошибки "math expression" на каждое следующее выражение в файле, так что их держат раздельно ради атрибуции лога.

Проверить в игре (не прогонялось после реализации; доказательства - `error.log` и тултипы):
- Теги и скопы как значения переменных: `check_variable = { rivals^0 = GER }` в 2 475 AI-планах и `set_temp_variable = { rival_tag = ROOT }` в хуках. Тот же механизм, что давний `is_in_array = { rivals = SOV }`, но `enable`-блоки планов целиком на нем держатся.
- Вложенная scripted localisation: `LocKey_personality_tt` -> `[GetSandboxLeaderRivalText]` -> ключ, внутри которого `[?rivals^0.GetLeader]` и `[GetSandboxRivalBand0]`. Тултип трейта не должен показывать сырые скобки, а `LocKey_empty` (пустая строка) не должен светить именем ключа.
- Скопы `on_capitulation` (FROM = победитель) в фракционных войнах.
- Цена AI-планов: три на тег с проверками переменных в `enable`. Если тики ИИ просядут, слить три тира в один план на тег с гейтами `contain`/`conquer` по `rivalry` внутри плана.
- `has_government = <scope>` (используется в `update_rivalry_monthly` и `major_rivals_scorer`) валиден: ванильный `USA_hemisphere_defense` использует `has_government = ROOT`.

## Acceptance checklist - RU

- [ ] A new Soviet ruler gets a new personal rival within the same day; the two national rivals are unchanged.
- [ ] Romania is Hungary's national rival at `rivalry` 50; Romania joins Hungary's faction: the slot is cleared, Hungary's -20 opinion modifier toward Romania disappears, and Romania cannot be selected again for 24 months.
- [ ] The Soviet Union owns Finnish cores: Finland's `rivalry` toward it rises by >=2 per month and reaches Feud within ~13 months; the Soviet AI (if it lists Finland) gets `conquer`.
- [ ] A country with a rival it shares no cores, wars, or ideology conflict with: `rivalry` falls from 50 to 0 in ~50 months, the slot empties, and is refilled after ~6 months on average.
- [x] Y declares war on Z without being Z's rival: Y occupies a free national slot of Z with `rivalry` 75 the same day, Z gains +10 war support.
- [x] Z capitulates to Y: Y's `rivalry` toward Z drops by 50; Z's toward Y rises by 25.
- [ ] A pact partner is also a rival at `rivalry` 40: declaring war costs the usual -50 Honor; monthly growth is reduced by 1.
- [ ] `USA_us_ussr_economic_cooperation` is unavailable while SOV is in USA's `rivals[]` or USA in SOV's, and its AI weight is 0.
- [ ] With a rival at Feud, the antagonism focus against it weighs three times its non-rival weight; a focus against several countries of which one is at Feud weighs the same.
- [ ] `USA_hemisphere_defense` stays available and keeps a non-zero AI weight while Mexico is a US national rival; `USA_liberty_for_the_philippines` is unavailable while the Philippines are.
- [ ] A rival at war with one, two, or five of our friends gains exactly +1 per month from that term.
- [x] No `Invalid Scope` lines in `error.log` from rival effects when a rival slot holds a country that has ceased to exist mid-month.

## Out of scope for this iteration - RU

- Player decisions "declare rival" / "seek detente" (`common/decisions` is empty; add once the AI loop is tuned).
- Targeted ideas per rival (`targeted_modifier`: `attack_bonus_against`, `generate_wargoal_tension_against`); requires per-tag generation like the AI-strategy file.
- News events and notifications about rivalry changes.
- Opinion by Tyranny band distance (listed under "Second iteration" in `docs/gdd/Tyranny System.md`; independent of rivals).
- Historical-mode behaviour: everything here is sandbox-only.