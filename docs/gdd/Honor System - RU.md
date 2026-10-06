<!-- source: 2d17a6c7fd23a677998917138e92e99278b080bd -->
# Honor - RU

Honor - это репутация правителя в вопросе kept one's word (*pacta sunt servanda*). Она отвечает на один вопрос, который другие страны задают о лидере: "если мы что-то подпишем с ними, они это соблюдут?"

Honor - это **не**:
- Tyranny (внутренняя свобода против репрессий). Ядерки, чистки, призыв, аннексии Honor не трогают.
- Opinion (насколько конкретная страна нас любит). Honor питает opinion через черты лидера, никогда наоборот.
- Rivalry (с кем мы хотим воевать; см. `docs/gdd/Rivals System.md`). Ривал под пактом или гарантией защищен Honor как все остальные; rivalry никогда не снижает цену предательства.

Sandbox-only: все правила ниже работают под `is_sandbox_mode_on()`.

## Scale and bands - RU

`honor` - переменная страны в `[-100.0, 100.0]`, ограничивается через `$add_honor()` в `common/macros.hml`.

Полосы (существующие, `update_country_leader_traits()` в `common/scripted_effects/99_sandbox_scripted_effects.hsl`):
- `< -75` Treacherous (`treacherous_leader`, opinion -20)
- `< -25` Dishonorable (`dishonorable_leader`, opinion -10)
- `< 25` Inglorious (`inglorious_leader`, без модификаторов)
- `< 75` Honorable (`honorable_leader`, opinion +10)
- `>= 75` Righteous (`righteous_leader`, opinion +20)

Стартовое значение нового sandbox-лидера: `randi(-100, 100)` (существующее, `initialize_new_country_leader()`).

## Design goals - RU

1. Доверие теряется быстро и большими дискретными кусками; зарабатывается медленно и пассивно - реальным несением обязательств.
2. Honor двигают только поступки про обещания: пакты о ненападении, гарантии, фракции, призывы к оружию.
3. Числа настроены под полосы: одно предательство (-50) всегда роняет Inglorious-лидера минимум до Dishonorable; второе - до Treacherous. Подъем с Inglorious до Honorable честным поведением занимает примерно 3-5 игровых лет.
4. Репутация, не подкрепленная делами, затухает к нулю в обе стороны.

## Definitions - RU

Страна - наш **friend**, если выполняется `$is_friend_of()`: мы союзники (одна фракция), они нас гарантируют, или у нас пакт о ненападении. Это существующий макрос в `common/macros.hml`.

**Betrayal focus** - любой национальный фокус, разрывающий обещание другу (снимает пакт, выходит из фракции или дает варгол на друга). Сейчас это фокусы под гейтом `is_honored_leader(no)` / `can_PREV_get_wargoal_on_THIS()` (см. `docs/gdd/National Focuses.md`, "Antagonism").

## Honor losses (discrete events) - RU

Все значения применяются один раз за событие через `$add_honor(-X)` и показаны в тултипе эффекта-причины.

### Breaking a non-aggression pact by war: -50 - RU

Партнера по пакту атакуют (фокус снимает пакт через `diplomatic_relation ... active = no`, затем выдается варгол или объявляется война).

Реализация: макрос `break_non_aggression_pact_with(_tag_)` снимает пакт **и** применяет `$add_honor(-50)` в одном месте; используйте его в sandbox-фокусах вместо голого `diplomatic_relation`. Ванильные фокусы снимают пакты своим `diplomatic_relation` внутри `completion_reward`, который include-дельты заменить не могут, поэтому общий путь - `on_declare_war` (ROOT = атакующий, FROM = цель): снимать -50, если FROM в текущем или **прошлонедельном** снимке `na_pacts[]`, либо в **окне снятых обязательств** (ниже).

### Attacking a country we guarantee: -40 - RU

Начисляется в `on_declare_war`, когда `FROM` в текущем или прошлонедельном `guaranting[]`, либо в окне снятых обязательств (тогда -30, потому что -10 уже заплачены при отзыве гарантии). Если та же декларация заодно рвет пакт, применяется только больший штраф (-50), а не оба.

### Dropped-obligation window: 6 months - RU

ИИ обычно сначала снимает пакт или гарантию, *потом* неделями обосновывает варгол, *потом* объявляет войну. Недельный снимок это пропустит. Поэтому каждое снятое обязательство запоминается с месяцем снятия (`dropped_pacts[]` / `dropped_guarantees[]` плюс параллельные массивы `*_month[]`, счетчик `months_elapsed`). Война, объявленная этой стране в течение **6 месяцев**, тарифицируется как предательство; более старые записи чистятся ежемесячно.

### Leaving a faction: -30 at war, -10 in peace - RU

`on_leave_faction` (ROOT = выходящая страна, FROM = лидер фракции). "At war" значит, что лидер фракции `has_war()` в момент выхода.

Исключение: штрафа нет, если выходящая страна - субъект, покидающий фракцию сюзерена по причине релиза, либо фракция распадается из-за капитуляции лидера.

### Faction leader expels a member at war: -15 to the leader - RU

Тот же хук; лидер - это FROM. При реализации проверить, стреляет ли экспульсия в `on_leave_faction`. Если добровольный выход неотличим, фокусы/решения экспульсии должны ставить флаг страны (например `expelled_by_leader`) на члена до удаления, а хук читает этот флаг.

### Withdrawing a guarantee without war: -10 - RU

Детектируется в недельном апдейте диффом `guaranting[]` против снимка прошлой недели; отозвать гарантию может только гарант, так что штраф атрибуируем. Пропустить, если партнер исчез по независящим от нас причинам: аннексирован, капитулировал, стал нашим субъектом, вступил в нашу фракцию, либо мы уже с ним воюем (этот случай - -40 выше).

Отмена пакта о ненападении **немедленного штрафа не несет**: отменить могла любая сторона, а игра не сообщает кто. Снятие все равно пишется в 6-месячное окно, так что последующая война тарифицируется полными -50. Известное ограничение: партнер, который отменил пакт и атакует *нас*, тарифицируется своим `on_declare_war`; с нас ничего не снимается.

### Justifying a wargoal on a friend: -2 per 30 pulses - RU

`on_justifying_wargoal_pulse` (ROOT = обосновывающий, FROM = цель) стреляет **ежедневно** в ванилле. Считаем пульсы против друга в `honor_justify_pulses` и снимаем -2 каждые 30 штук (~= -2 за месяц обоснования). Это телеграфирует грядущее предательство: соседи видят сползание лидера к Dishonorable до начала войны, но одна обосновка не сносит всю полосу целиком.

### Ignoring obligations (monthly): -5 / -3 per case - RU

Проверяется в `on_monthly` по каждой другой стране:
- Страна под нашей гарантией ведет оборонительную войну против X, а мы не воюем с X: **-5 за такую страну в месяц**.
- Союзник по фракции воюет с X, X не наш субъект/союзник, и мы не воюем с X (отклоненный или проигнорированный призыв): **-3 за такого союзника в месяц**.

Льготный период: первый полный месяц войны бесплатный, чтобы не наказывать страну, которую просто еще не призвали. Реализация: сравнение со снимком прошлого месяца; наказываем, только если то же неисполненное обязательство было в обоих снимках.

Субъекты exempt: они не могут объявлять войны сами, так что войны сюзерена - не их нарушенные обещания.

У отказа от призыва нет on_action, так что месячная проверка - единственный надежный детектор.

## Honor gains - RU

### Passive gain for obligations carried (monthly) - RU

Расширяет существующий `update_honor_gain_monthly_factor()`:
- `+0.20` за каждую гарантируемую страну
- `+0.05` за пакт о ненападении
- `+0.05` за союзника по фракции (остальные члены нашей фракции)
- Сумма **ограничена +1.00 в месяц**

Обоснование капа: мажор с десятью союзниками и несколькими гарантиями иначе дойдет до Righteous за год.

### Honoring a guarantee: +15 - RU

Мы вступаем в войну на стороне гарантируемой страны после атаки на нее: либо отвечая на призыв (`on_join_allies`, FROM = призывающий, `FROM->is_guaranteed_by(ROOT)`), либо объявляя войну сами стране, которая воюет с гарантируемой в оборонительной войне (`on_declare_war`, else-ветка после проверок предательства). Один раз за войну.

### Answering a call to arms: +10 - RU

`on_join_allies` (ROOT = вступающая страна, FROM = призывающий). Один раз за войну. Если применимы и этот бонус, и бонус гарантии, выдается только больший (+15).

"Один раз за войну" трекается в `honor_answered_call[]` (по записи на страну, за которую вступились); список чистится в `on_monthly`, когда мы в мире, так что за того же союзника можно снова получить награду в следующей войне.

### Releasing a nation as independent: +5 - RU

`on_release_as_free` и `on_liberate`, начисляется отпускающей/освобождающей стране. Паппетинг и аннексия не дают ничего.

### Natural pact expiry: 0 - RU

Мирно истекший пакт уже вознагражден ежемесячным пассивным гейном.

## Drift toward zero - RU

Каждый месяц Honor сдвигается на **0.25 к 0** вне зависимости от знака, поверх пассивного гейна:

```
drift = -0.25 if honor > 0, +0.25 if honor < 0, 0 if |honor| < 0.25
honor_gain_monthly_factor = clamp(obligation_gain, 0, 1.0) + drift
```

Следствия, которые сохранить при тюнинге:
- Лидер Treacherous без новых предательств восстанавливается до Dishonorable примерно за 8 лет.
- Righteous стабилен только у лидера, реально несущего обязательства: одна гарантия примерно компенсирует дрейф; две и больше - растят Honor.
- Без дрейфа каждый невоюющий за несколько лет стал бы Honorable, и полосы потеряли бы смысл.

Тултип `LocKey_honor_tt` уже показывает `honor_gain_monthly_factor`; он должен показывать комбинированное значение (гейн + дрейф).

## Leader change - RU

Honor принадлежит правителю, а не государству. На `on_ruling_party_change`:

```
honor = 0.5 * honor + randi(-50, 50)
```

Половина наследуется как дипломатическая репутация государства, половина - личный нрав нового правителя. Затем `update_country_leader_traits()` как обычно.

Победитель гражданской войны (`on_civil_war_end`, ROOT = победитель): правитель получает свежий `randi(-100, 100)`; ничего не наследуется.

Ребел-теги, путчистские режимы и релизнутые нации созданы после стартапа и не видели `on_startup`. Они инициализируются лениво: `on_weekly` прогоняет `initialize_country_for_sandbox_mode()` для любой страны без флага `sandbox_initialized`, который роллит Honor/Tyranny ровно как стартовой стране. `on_coup_succeeded` сознательно не используется: его ROOT - страна, *против* которой устроили путч, а не новый режим.

## Gating betrayal focuses by band - RU

Заменить одиночный гейт `is_honored_leader(no)` тирами, чтобы у каждой полосы был свой смысл:

- **Inglorious or worse** (`honor < 25`): может рвать пакт о ненападении.
- **Dishonorable or worse** (`honor < -25`): может дополнительно атаковать гарантируемую страну.
- **Treacherous** (`honor < -75`): может дополнительно выходить из фракции ради атаки бывшего союзника.

Реализация: `can_PREV_get_wargoal_on_THIS` в `common/scripted_triggers/99_sandbox_scripted_triggers.hsl` становится tier-aware: требуемая полоса зависит от того, чем нам приходится цель (пакт -> Inglorious, гарантия -> Dishonorable, фракция -> Treacherous). Добавить scripted triggers `is_dishonorable_leader` / `is_treacherous_leader` с тултипами по аналогии с `is_honored_leader`. Паттерны "Antagonism" в `docs/gdd/National Focuses.md` (single target, multiple targets, state owners) при шипе перевести на тирный триггер.

## AI weighting - RU

Каждый betrayal-фокус получает betrayal-фактор рядом с существующим antagonism-модификатором: `clamp((25 - honor) / 125, 0, 1)`, применяется только пока хотя бы одна цель - друг. Упаковано как `$ai_betrayal_modifier()` (голый фактор, триггер дружбы дает вызывающий) и `$ai_betrayal_modifier_vs($TAG)` (одна фиксированная цель) в `macros.hml`; точные фокусные паттерны для single, multiple и state-owner целей - в `docs/gdd/National Focuses.md`, "Antagonism".

Treacherous-ИИ (honor -100) предает на полном весе; Inglorious-ИИ на 24 - почти никогда. Вместе с тирным гейтом это держит предательства редкими, но возможными для средних лидеров.

Остальные страны реагируют через opinion-модификаторы черт лидера (-20/-10/+10/+20); дополнительной AI-стратегии на эту итерацию не требуется.

## Implementation notes - RU

Хуки и скопы (из ванильного `common/on_actions/00_on_actions.txt`; скопы с пометкой "check" проверить в игре):
- `on_declare_war`: ROOT атакующий, FROM цель. Несет все штрафы предательства и +15 "declared on the aggressor".
- `on_leave_faction`: ROOT выходящая страна, FROM лидер фракции.
- `on_join_allies`: ROOT вступающая страна, FROM призывающий (check).
- `on_justifying_wargoal_pulse`: ROOT обосновывающий, FROM цель; **ежедневно**.
- `on_release_as_free`, `on_liberate`: ROOT отпущенная страна, FROM отпускающая страна (check).
- `on_ruling_party_change`, `on_civil_war_end` (ROOT победитель), `on_monthly`, `on_weekly`.
- Не используются: `on_coup_succeeded` (ROOT - жертва путча), `on_war_relation_added` (дубль `on_declare_war`).

Дипломатические действия без хуков (отмена гарантии, отмена пакта, отказ от призыва) детектятся снимками:
- Еженедельно: держать `prev_guaranting[]` / `prev_na_pacts[]` до перестройки `guaranting[]` / `na_pacts[]`; дропы уходят в `dropped_guarantees[]` / `dropped_pacts[]` со штампами `months_elapsed`.
- Ежемесячно: `months_elapsed += 1`, чистка дропов старше 6 месяцев, держать прошлый месяц списка неисполненных обязательств ради льготного периода, чистить `honor_answered_call[]` в мире.

Поздно созданные страны: `on_weekly` инициализирует любую страну без `sandbox_initialized` (флаг ставится внутри `initialize_country_for_sandbox_mode()`).

Одноразовые флаги: `sandbox_honor_skip_leave_faction` (ставится через `on_release_as_free`, чтобы автоматический выход релизнутой нации из фракции не считался предательством) чистится каждую неделю, чтобы не проглотить поздний настоящий выход. `expelled_by_leader` должен ставиться экспульсирующим фокусом/решением прямо перед удалением.

Макросы с параметром `_country_`, строящие ключ тултипа (`$is_friend_of(FROM)` -> `LocKey_is_friend_of_FROM_tt`), требуют этот ключ в локализации даже при использовании внутри hidden effect.

Исторический дефект, закрытый этим изменением: `update_honor_gain_monthly_factor()` не чистил `guaranting[]` / `na_pacts[]` в недельном прогоне, так что месячный фактор инфлировал линейно со временем. Оба массива теперь чистятся (после копирования в `prev_`-снимки) перед наполнением.

Все изменения Honor идут через `$add_honor()`, чтобы трейт, opinion-модификаторы и тултип оставались консистентны. Не писать `&honor` напрямую вне `initialize_new_country_leader()` и правила смены лидера.

## Acceptance checklist - RU

- [ ] A leader at Honor 20 with a pact partner completes a betrayal focus against it: Honor becomes -30, trait becomes Dishonorable, all other countries get the -10 opinion modifier, and the focus tooltip showed "Honor -50".
- [ ] The same leader betrays a second pact: Honor -80, Treacherous.
- [ ] A vanilla focus removes a pact; the AI justifies for 3 months and then declares war: no penalty at removal, -50 at the declaration (window), nothing more afterwards. If it declares after 7 months instead, nothing is charged.
- [ ] A guarantee is withdrawn: -10 the same week; war on that country 2 months later adds -30 (total -40). Two guarantees withdrawn in one week: -20.
- [ ] Justifying a wargoal on a pact partner for 90 days costs -6 (three batches of 30 daily pulses), not -180.
- [x] A rebel tag spawned by a civil war has Honor/Tyranny traits by the end of its first week; the coup victim's values are untouched.
- [x] A subject whose overlord fights a war the subject has not joined loses nothing for "ignoring" it.
- [ ] A country at Honor 0 with no obligations and no events stays at 0 indefinitely.
- [ ] A country at Honor 60 with no obligations declines to 30 after 10 years (0.25 x 120 months).
- [ ] A country at Honor 0 guaranteeing two minors and in a pact with one more gains `0.20*2 + 0.05 - 0.25 = +0.20` per month and reaches Honorable (25) after ~10.5 years; with four guarantees it reaches it in ~3.5 years.
- [x] Passive gain never exceeds +1.00 before drift, regardless of how many allies/guarantees exist.
- [ ] A guarantor that ignores a guaranteed country's defensive war loses 5 per month starting from the second month, and stops losing the moment it declares on the aggressor, gaining +15 once.
- [x] After a peaceful ruling-party change, Honor equals half the old value plus a random offset in [-50, 50], clamped.
- [ ] A leader at Honor -30 can take a "break pact" and "attack guaranteed" focus but not a "leave faction to attack ally" focus; at -80 all three are available.
- [x] The monthly factor shown in `LocKey_honor_tt` does not grow week over week when the diplomatic situation is unchanged (regression test for the array-clear bug).

## Out of scope for this iteration - RU

- Honor effects on trade, licensing, and opinion beyond the existing trait modifiers.
- Player-facing decisions to "restore honor" (apologies, reparations).
- Honor for subjects toward their overlord (a puppet leaving its overlord's faction is not a betrayal).
- Attributing a cancelled non-aggression pact to the side that cancelled it (the game does not expose it; see "Withdrawing a guarantee without war").
- Historical-mode behaviour: everything here is sandbox-only.