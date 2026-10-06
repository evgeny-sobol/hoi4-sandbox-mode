<!-- source: 2d17a6c7fd23a677998917138e92e99278b080bd -->
# Tyranny - RU

Tyranny - мера режима: насколько концентрирована и репрессивна власть правителя, насколько страной правят принуждением, а не согласием.

Tyranny - это компромисс, а не шкала "хорошо/плохо". Высокая Tyranny покупает контроль (защита от дрейфа партии, политвласть, твердая рука в войну) ценой открытости (наука, торговля, сопротивление на оккупированных землях). Низкая Tyranny - зеркально: открыто и продуктивно, но легко дестабилизировать извне.

Tyranny - это **не**:
- Honor (соблюдение обещаний другим странам; см. `docs/gdd/Honor System.md`). Оси ортогональны: либеральная демократия может быть вероломной, а деспот - человеком слова.
- Ideology. Идеология задает, где Tyranny естественно оседает, но любое правительство можно увести далеко от домашнего значения.
- Rivalry (с кем мы хотим воевать; см. `docs/gdd/Rivals System.md`). Единственная связь идет в обратную сторону: личное rivalry (`rivals[0]`) правителя Authoritarian или Despotic растет на +1 в месяц быстрее, правителя Libertarian или Liberal - на -1 медленнее.

Sandbox-only: все правила ниже работают под `is_sandbox_mode_on()`.

## Scale and bands - RU

`tyranny` - переменная страны в `[-100.0, 100.0]`, ограничивается через `$add_tyranny()` в `common/macros.hml`.

Полосы (те же пороги, что у Honor):
- `< -75` Libertarian (`libertarian_leader`)
- `< -25` Liberal (`liberal_leader`)
- `< 25` Moderate (`moderate_leader`, без модификаторов)
- `< 75` Authoritarian (`authoritarian_leader`)
- `>= 75` Despotic (`despotic_leader`)

Стартовое значение нового sandbox-лидера: `randi(min_tyranny, max_tyranny)` из таблицы правительство/идеология-лидера в `initialize_new_country_leader()` (`common/scripted_effects/99_sandbox_scripted_effects.hsl`). Таблица сохраняется как есть.

## Design goals - RU

1. Национальные фокусы - главный рычаг: репрессивные и либеральные фокусы ванильных деревьев двигают Tyranny дискретными шагами.
2. У институтов инерция: Tyranny дрейфует обратно к домашнему значению идеологии, так что разовый фокус оставляет след, затухающий годами, если ветку не продолжать.
3. Война и кризис толкают любой режим к контролю.
4. Полосы меняют, что лидеру можно делать внутри страны (зеркало гейта Honor на внешнее предательство) и как ИИ взвешивает репрессивные и либеральные ветки фокусов.

## Home value - RU

У каждого правительства есть естественный уровень Tyranny, `tyranny_home`, равный середине его стартового диапазона:

```
tyranny_home = (min_tyranny + max_tyranny) / 2
```

считается в той же функции, что роллит стартовое значение, из той же таблицы (например либеральная демократия `(-100 + -80) / 2 = -90`, фашизм `90`, центристский нейтралитет `-25`). Пересчитывается при каждой смене правящей партии.

## Band effects (leader traits) - RU

По трейту на полосу, меняются через `update_country_leader_traits()` ровно как Honor-трейты. Модификаторы:

- **Libertarian**: `research_speed_factor +0.05`, `trade_opinion_factor +0.10`, `drift_defence_factor -0.25`, `political_power_factor -0.10`, `foreign_subversive_activites +0.25` (vanilla spelling).
- **Liberal**: `research_speed_factor +0.02`, `trade_opinion_factor +0.05`, `drift_defence_factor -0.10`.
- **Moderate**: none.
- **Authoritarian**: `drift_defence_factor +0.10`, `political_power_factor +0.05`, `research_speed_factor -0.02`, `trade_opinion_factor -0.05`.
- **Despotic**: `drift_defence_factor +0.25`, `political_power_factor +0.10`, `research_speed_factor -0.05`, `trade_opinion_factor -0.10`, `resistance_growth +0.10`.

Замысел: деспот держит правящую партию силой и быстрее проталкивает решения, но платит наукой, торговлей и сопротивлением на оккупированных территориях. Либертарий открыт и продуктивен, но партийную систему легко расшатать извне.

## Changes from national focuses (main source) - RU

Ванильные деревья фокусов тегируются `$add_tyranny(+/-X)` в `completion_reward`. Гайд по классификации:

- **+20**: чистки; тайная полиция; однопартийность; отмена выборов или конституции; военное положение; запрет партий; аресты оппозиции.
- **+10**: цензура и пропаганда; милитаризация общества; культ личности; централизация; подавление региональной автономии.
- **+5**: расширенные полномочия исполнительной власти; урезание профсоюзов; лоялистские назначения.
- **-5**: коалиционное правительство; частичная амнистия; смягчение цензуры.
- **-10**: свободные выборы; гражданские права; свобода прессы; легализация партий; региональная автономия.
- **-20**: новая демократическая конституция; роспуск тайной полиции; децентрализация; общая амнистия.

Калибровочные якоря:
- Демократии на -75 нужно пять фокусов +20, чтобы стать Authoritarian.
- Один фокус +20 съедается дрейфом примерно за 7 лет (см. ниже), так что разовые фокусы оставляют видимый, но временный след; lasting shift требует устойчивой ветки или смены правительства.
- Фокусам, уже меняющим правящую партию (например фашистская путч-ветка), Tyranny-награда не нужна: скачок покрывает правило смены лидера ниже.

## Systemic sources - RU

### War: +0.25 per month, +0.50 if core territory is occupied - RU

Любая война (`has_war()`) дает `+0.25` в месяц (чрезвычайные полномочия). Если хотя бы один кор-стейт контролируется врагом, ставка `+0.50` вместо этого (осадный менталитет). Наступательные и оборонительные войны считаются одинаково.

Это **заменяет** текущий `update_tyranny_gain_monthly_factor()` (наступление -0.25 / оборона +0.25), чей знак противоречит модели: агрессивная война не должна либерализовать агрессора.

### Low stability: +0.25 per month - RU

Пока `has_stability < 0.25`, режим закручивает гайки. Складывается с военной ставкой.

### Elections: -5 - RU

`on_new_term_election`: обновленный мандат ослабляет хватку. Стреляет только у стран с выборами, так что демократии получают периодический толчок вниз поверх дрейфа.

### Civil war and coup - RU

Без отдельного бонуса. Новый режим перероллится правилом смены лидера ниже.

## Drift toward home - RU

Каждый месяц Tyranny сдвигается на **0.25 к `tyranny_home`**, поверх системных источников:

```
drift = clamp(tyranny_home - tyranny, -0.25, 0.25)
tyranny_gain_monthly_factor = war_rate + stability_rate + drift
```

Следствия, которые сохранить при тюнинге:
- Институты тяготеют к норме своей идеологии; деспотическая демократия выживает, только пока ее что-то толкает (война, фокусы), а либерализованное фашистское государство откатывается без продолженных реформ.
- Дрейф и война складываются: демократия в долгой войне с оккупированными корами все равно растет на `0.50 - 0.25 = +0.25` чистыми в месяц.
- На домашнем значении без войны и при стабильном правительстве Tyranny плоская.

Тултип `LocKey_honor_tt` уже показывает `tyranny_gain_monthly_factor`; он должен показывать комбинированное значение.

## Leader change - RU

Tyranny - свойство режима больше, чем персоны, так что инерция сильнее, чем у Honor.

- Мирная смена правящей партии (`on_ruling_party_change`): `tyranny = 0.5 * tyranny + 0.5 * randi(min, max)` по строке нового правительства из таблицы; `tyranny_home` пересчитывается. Институты сохраняются, идеология меняет направление.
- Победа в гражданской войне (`on_civil_war_end`, ROOT = победитель): полный `randi(min, max)` под новое правительство. Старый аппарат снесен.
- Ребел-теги и путчистские режимы - новые страны: инициализируются лениво недельным `sandbox_initialized`-гейтом (см. `docs/gdd/Honor System.md`, "Leader change") и роллятся как стартовая страна. `on_coup_succeeded` не используется, потому что его ROOT - страна, против которой устроили путч.

Затем `update_country_leader_traits()` как обычно.

## Gating focuses by band - RU

Honor позволяет лидеру предавать соседей; Tyranny позволяет лидеру топтать конституцию собственной страны.

- **Liberal or lower** (`tyranny < -25`): фокусы чисток и тайной полиции (класс `+20`) недоступны. Реализация: `is_liberal_leader(no)` в `available`.
- **Authoritarian or higher** (`tyranny >= 25`) - **deferred, blocked by tooling.** Замысел: неконституционные фокусы смены правительства ("захватить власть", "запретить партию", "приостановить выборы") становятся доступны без требования популярности партии `> 0.5`, которым гейтятся политические ветки. Эти требования живут в ванильных блоках `available`, а дельта-система `.include` умеет только *дописывать* условия в существующий блок (AND); обернуть или заменить ванильное условие в `OR` она не может. Пока компилятор не умеет заменять условие, правило выражено только через AI-наклон ниже (деспоты предпочитают путч-ветку, когда она им открыта). Триггер `is_authoritarian_leader` и его тултипы существуют и готовы под гейт.
- Despotic не получает дополнительных разрешений; его отличие - в модификаторах и весе ИИ.

Реализация: scripted triggers `is_authoritarian_leader` / `is_liberal_leader` с `custom_override_tooltip` в стиле `is_honored_leader`.

## AI weighting - RU

Используются существующие mtth-факторы в `common/mtth/99_sandbox_factors_mtth.hsl` с паттернами из `docs/gdd/National Focuses.md`:

- Развилка "репрессии против реформ" (обе опции mutually exclusive **друг с другом**): делим доли через `$ai_high_tyranny_fork()` / `$ai_low_tyranny_fork()` (`0.5 + factor`, так что Moderate-ИИ сохраняет вес) и убираем `$crossroad_modifier`; средний вариант берет `$ai_medium_tyranny_fork()`. Годятся только настоящие Tyranny-развилки; либеральный фокус, чей эксклюзивный сиблинг - *идеологический* выбор (например `GER_reestablish_free_elections` против `GER_revive_the_kaiserreich`), сохраняет наклон и партито-популярный раздел. Найдены пока: `SIA_an_absolute_monarchy` / `SIA_a_constitutional_monarchy`, `POL_codify_national_unity` / `POL_draft_a_new_constitution`.
- Одиночный репрессивный фокус без развилки: `$ai_high_tyranny_tilt()` (`1 + mtth:high_tyranny_factor`); одиночный либеральный: `$ai_low_tyranny_tilt()`.
- Неконституционные фокусы смены правительства: `$ai_high_tyranny_tilt()`, так что деспоты устраивают путчи, а либералы идут через выборы.

Совместить брейкпоинты факторов с полосами (сейчас ноль на +/-34, пик на +/-100):
- `low_tyranny_factor`: 1 при `tyranny <= -75`, линейно к 0 при `tyranny >= -25`.
- `high_tyranny_factor`: 1 при `tyranny >= 75`, линейно к 0 при `tyranny <= 25`.
- `medium_tyranny_factor`: 1 внутри `[-25, 25]`, линейно к 0 при `+/-75`.

## Implementation notes - RU

Хуки (из ванильного `common/on_actions/00_on_actions.txt`; скопы с пометкой "check" проверить):
- `on_new_term_election`: ROOT = страна с выборами.
- `on_ruling_party_change`, `on_civil_war_end` (ROOT победитель, FROM проигравший).
- `on_weekly` для пересчета месячного фактора и ленивой инициализации поздно созданных стран, `on_monthly` для применения фактора (существующее).
- Не используется: `on_coup_succeeded` (ROOT - жертва путча; новый режим - новый тег и ловится недельным гейтом инициализации).

Изменения существующего кода:
- `update_country_leader_traits()` сейчас обрабатывает только Honor-трейты, хотя `$add_tyranny` его вызывает. Добавить параллельную ветку под гейтом `tyranny != prev_tyranny`, меняющую пять Tyranny-трейтов.
- `update_tyranny_gain_monthly_factor()` переписывается на war rate + stability rate + drift.
- `initialize_new_country_leader()` дополнительно хранит `tyranny_home`; та же таблица должна быть переиспользуема для реролла смены лидера (вынести вычисление диапазона в отдельный эффект).
- Тултип `LocKey_honor_tt` форматирует Tyranny через `|.2-`, а Honor через `|.2+`; унифицировать, чтобы положительный знак читался как "репрессивнее" и для Tyranny тоже.

Все изменения Tyranny идут через `$add_tyranny()`, чтобы трейты и тултипы оставались консистентны. Не писать `&tyranny` напрямую вне инициализации и правила смены лидера.

## Acceptance checklist - RU

- [x] A liberal democracy starts in `[-100, -80]`, `tyranny_home = -90`, trait Libertarian; other countries see no opinion change (opinion is out of scope for this iteration).
- [x] A fascist state at 90, at peace, stable: monthly factor 0.00.
- [ ] A democracy at -90 (its home value, so drift is 0) enters a war: factor `+0.25`; after an enemy occupies a core state the factor is `+0.50`. Once it has climbed to -70 with cores still occupied, drift kicks in and the factor is `+0.50 - 0.25 = +0.25`.
- [ ] A country at -70 with `tyranny_home = -90`, no war, stability 60%: factor `-0.25`, reaches -90 in 80 months and then stays flat.
- [x] Completing a +20 focus shows "Tyranny +20" in the focus tooltip, moves the value by exactly 20 (clamped), and swaps the trait if a band boundary is crossed.
- [x] Stability drops below 25% in peacetime: factor gains `+0.25`; it disappears the week stability recovers to 25% or more.
- [x] A democracy holds an election: -5 applied once, tooltip visible in the election event chain if one is shown.
- [x] Peaceful party change from democracy (-80) to fascism: new value is `0.5 * (-80) + 0.5 * randi(80, 100)`, i.e. in `[0, 10]`, trait Moderate, `tyranny_home = 90`, then climbs at 0.25 per month toward 90.
- [x] A fascist rebel tag created by a coup or civil war has, by the end of its first week, a value in `[80, 100]` and the Despotic trait; the country it split from keeps its own values.
- [ ] (Deferred with the Authoritarian gate) A leader at 30 can take a "seize power" focus with ruling party at 35% popularity; a leader at 20 cannot until popularity exceeds 50%.
- [ ] A leader at -30 cannot take a purge focus; at -20 the focus is available.
- [ ] In the `SIA_an_absolute_monarchy` / `SIA_a_constitutional_monarchy` fork a Despotic AI weighs the options 1.5 : 0.5, a Libertarian AI 0.5 : 1.5, a Moderate AI 0.5 : 0.5; no `$crossroad_modifier` is applied on top.
- [ ] With the aligned breakpoints, `high_tyranny_factor` is 0 at 25, 0.5 at 50, 1 at 75; `low_tyranny_factor` mirrors it; `medium_tyranny_factor` is 1 at 0, 0.5 at +/-50, 0 at +/-75.

## Second iteration (not blocking) - RU

- **Liberal focus coverage.** The first tagging pass is skewed toward repression (+20 x37, +10 x41 against -10 x16, -20 x5, -5 x1; the +/-5 classes are almost unused). Democracies can therefore move down only through drift and elections. A content pass over the vanilla trees for elections, constitutions, civil rights, press freedom, amnesties, and autonomy focuses is needed to tag the liberal side, and the `+5` / `-5` classes should be used for the softer items in the classification table.
- **Authoritarian gate** once the include system can replace a vanilla condition (see "Gating focuses by band").
- Opinion by band distance between two countries: same band +5, one band apart 0, two apart -5, three apart -10, opposite extremes -20. Gives democracies and despotisms a natural mutual dislike independent of ideology.
- Linking Tyranny to laws (total mobilisation, universal conscription) through `on_idea_added`, if that hook is confirmed to exist.

## Out of scope for this iteration - RU

- Opinion, trade, or intel effects beyond the trait modifiers listed above.
- Tyranny effects on subjects or overlords.
- Player-facing decisions to raise or lower Tyranny outside focus trees.
- Historical-mode behaviour: everything here is sandbox-only.