<!-- source: 2d17a6c7fd23a677998917138e92e99278b080bd -->
# Scenarios - RU

Sandbox-only директор, дающий каждой сессии кризис, в котором жить: на старте он выбирает одну **арку** (правдоподобный конфликт 1930-х), роллит ее target variant, сидит агрессора против целей и прогоняет трехрунговую лестницу, толкающую ИИ к войне. Игрок либо втягивается, либо смотрит, как горит мир. Система спроектирована переиспользовать остальные sandbox-механики (Honor, Tyranny, Rivals, Civil Wars, National Focuses), а не добавлять новые.

Это ванильный мод. Rt56-оверлей (`_sandbox-r56`) делит движок и большую часть документации; этот файл описывает специфичное для ваниллы.

## Design goals - RU

1. Make sessions alarming: an arc must, on a random draw, drive a major war. Сессия должна пугать: арка обязана при случайном ролле довести до большой войны.
2. Leave the player free: the director pushes AI, not the human; игрок может вступать, мутить воду или сидеть в стороне.
3. No new PM-level systems: переиспользовать существующие модификаторы и хуки.
4. Stay legible: every mechanism logs to `game.log` under `#sandbox` для observer-сессий.

## Selection - RU

Одна арка на сессию, выбирается на старте: пинится game rule или роллится случайно среди арок с существующим агрессором. Id арок фиксированы по мажорам (1 GER, 2 SOV, 3 JAP, 4 ITA, 5 ENG, 6 USA); id 7 - задокументированный гэп (Франция не content-portable; см. ниже). Пик роллит A/B target variant 50/50 и логирует `sc_pick` плюс `sc_variant`.

### Pool and selection - RU

- Случайные сессии выбирают из пула с равными весами среди арок с существующим агрессором. Pin-опции есть для всех шести.
- Derail перевыбирает следующую подходящую никогда не дерайлившуюся арку; дерайльнутая арка в том же сессии в пул не возвращается.
- Target variants роллятся на пике (50/50) и фиксируются на сессию.

### Excluded majors - RU

- **FRA**: бонапартистская ветка - только Rt56, реваншистская и Plan XIV ветки тоже отсутствуют. Французской арки, переносимой без замен, нет, так что id 7 оставлен задокументированным гэпом, а не забит substituted аркой.
- **HUN**: арка реставрации Габсбургов вне этого пула решением пользователя; ее ванильные фокусы существуют и пригодятся, если ее добавят позже.

## Arc schema - RU

Каждая арка описана одним TOML **arc spec** в `docs/scenarios/<id>.toml` (по одному на арку на мод). Общий тулинг читает спеки и выводит каталог, диаграммы фокусов, focus-boost замыкание и ожидаемые телеметрийные метки; scripted events и эффекты остаются рукописными в HSL-каталоге.

```toml
id = "axis_expansion"       # slug; identity and file name
number = 1                  # the director's arc id; written when the arc has code
status = "ready"            # ready (in the shipped pool) | draft (authored, not selected)
aggressor = "GER"           # a single tag
key = "axis"                # short slug for the pin trigger and pick label; optional

targets = { a = ["CZE", "POL"], b = ["FRA", "ENG"] }  # target variants, rolled 50/50

[ladder]                    # months from arc start
crises_at_month = 12
peak_at_month = 24
# Content rungs (optional pair): hand-written functions the tick calls.
# Both or neither; absent means the arc has no generated tick branch yet.
crises_func = "sandbox_fire_axis_crises"
peak_func = "sandbox_fire_axis_peak"

[joiners]                   # shared scorer, no per-arc parameters
select = "top_n_by_scorer"
n = 2

[gate]                      # optional; absent means no gate
ideology = "fascism"
at_phase = "crises"

# Ordered focus paths: each list runs from a branch entry to a war leaf.
paths = [
  ["GER_remilitarize_the_rhineland", "GER_anschluss", "GER_demand_sudetenland"],
]

notes = """
Free rationale prose, printed into the catalog beside the arc.
"""
```

Top-level ключи идут до заголовков `[table]`: в TOML все после заголовка принадлежит этой таблице. `id` должен совпадать с именем файла; `number` уникален и должен совпадать с диспетчером кода; `ready`-арке требуется `number`. Каждый key focus должен существовать в графе фокусов агрессора. Ladder content functions идут опциональной парой (`crises_func` + `peak_func` с именами рукописных rung-функций); отсутствие означает нет generated tick-ветки. Опциональный `key` именует суффикс pin-триггера и pick-метку; отсутствие означает нет generated pick-данных. Каждый вариант держит 1-4 цели (derail arms покрывают этот диапазон). Полей `type`, `block` и `content_refs` нет.

## Ladder - RU

| Rung | Fires at | Releases |
|---|---|---|
| smolder | month 0 | seed only |
| crises | month 12 | crisis events (claims, incidents) |
| peak | month 24 | ultimatums to targets, join offers |

Шаблонный календарь (smolder 36.1.1 / crises 37.1.1 / peak 38.1.1) - то, на чем стоят ванильные арки; позднейшие арки могут сдвигать ранги.

## Levers - RU

**Rivals and antagonism**: директор сидит каждую пару агрессор-цель как national rival на 65 и впрыскивает rivalry на фазе crises, так что существующие AI-веса толкают военное планирование. Rivalry - главный рычаг; нового AI-кода нет.

**Focus weights**: `$ai_scenario_focus_boost()` (x5, только живой агрессор) сплайсится на war-фокусы арки и корни их веток, чтобы ИИ реально шел по военной ветке (урок s10: буст за небустнутой развилкой мертв). Какие фокусы бустит каждая арка, нарисовано поарково в `docs/gdd/Scenarios Catalog.md`.

**Join levers**: на peak два топ-скорера из outsiders (`scenario_join_scorer`) получают приглашение в блок. Скорер гейтится на идеологию и враждебность, скорит силу плюс goodwill; джойнер сначала выходит из старой фракции (без Honor charge).

## Lifecycle - RU

Арка кончается на **ignition**: любая война между declared scenario enemies, в любую сторону, детектированная на объявлении или месячным ongoing-war свипом. Ignition логирует `sc_ignite` + `sc_success` + `sc_end`.

**Derail** паркует мертвую арку на phase 3: агрессор gone, капитулировал или сидит в затяжной гражданской войне (12 месяцев); жизнеспособных целей не осталось; либо арка просидела на peak 12 месяцев без ignition (`peak_timeout`). На random derail перевыбирает; пикатированные сессии тихо гаснут.

## Hooks and telemetry - RU

- Tick: `on_startup` (selection) плюс `on_weekly` / `on_monthly`. `on_monthly` идет по странам, так что ladder tick стреляет ровно в одном хосте в месяц: HAI - primary host с fallback-цепочкой через мажоров.
- Reactions: `on_declare_war` (ignition), `on_annex` / `on_capitulation` (derail), `on_join_allies` / `on_join_faction` (joiner tracking).
- Telemetry: `sc_pick`, `sc_variant`, `sc_seed`, `sc_phase`, `sc_crisis`, `sc_target`, `sc_power`, `sc_goal`, `sc_justify`, `sc_goal_end`, `sc_focus`, `sc_offer`, `sc_ignite`, `sc_success`, `sc_join`, `sc_end`, `sc_derail`, `sc_repick`. Per-actor строки гейтятся на `is_scenario_actor` (агрессор или declared target), так что чужой фокус не pollute-ит арку.

### Sampling cadence - RU

Повторяющееся состояние сэмплируется по расписанию; переход логируется когда случается. s7 diagnostic package следует этому правилу:

| Line | Cadence |
| --- | --- |
| `sc_power` | monthly per live actor |
| `sc_goal` | monthly per declared pair with a held wargoal or an active justification |
| `sc_justify` | monthly per declared pair with an active justification |
| `sc_goal_end` | on wargoal expiry (transition) |

`sc_justify` раньше ездил на daily justification pulse (строка в день на justification); с issue 15 это месячный сэмпл как остальной s7, так что долгая justification стоит строк в месяц, а не в день.

### Telemetry label convention - RU

`sc_goal` и `sc_justify` несут по одной метке на пару агрессор/цель, всегда `<aggressor>_on_<target>` в **lowercase** (`ger_on_cze`, `hun_on_rom`). Каталог пишет оба набора меток руками в s7-телеметрии; оба должны совпадать точно, иначе одна арка читается как два ключа при грепе сессии.

- `sc_goal` логирует варголы в **обе** стороны, так что держит и `<target>_on_<aggressor>`-метки (`cze_on_ger`); `sc_justify` покрывает только justifications агрессора.
- Каждый тег цели в метке должен быть реальным тегом, который сидит арка (`sandbox_set_targets`). Румыния - это `ROM`, никогда `ROU`.

### Join lever - RU

Рычаг шлет `sc_offer` топ-2 кандидатам пула. Принятие - Honor-free (`sandbox_honor_skip_leave_faction`), дает **взаимный military access** с агрессором и opinion-модификатор `scenario_ally`, логирует `sc_join`. **Фракция не образуется.** Превращение агрессора в лидера фракции лочит его от его же war-фокусов, нескольким из которых требуется `is_in_faction = no` (`ITA_pact_of_steel`, `ITA_italy_first`, `GER_integrate_czechoslovakia`, `JAP_sea_pressure_siam`); observer-сессия показала Италию, дошедшую до `ITA_foreign_affairs` и вставшую на шесть лет, не в силах открыть путь `italian_irredentism` к войне.

## Acceptance checklist - RU

Log-first. Observer sandbox. Tick only when the grep holds.

- [ ] Startup: exactly one `sc_pick` naming one pool arc, plus one `sc_variant`.
- [ ] Ladder phases logged on schedule: `sc_phase smolder`, `crises`, `peak`.
- [ ] At peak each target logs one `sc_target` status line.
- [ ] Ignition: `sc_ignite` + `sc_success` + `sc_end` when a war fires between declared enemies (direct or ongoing).
- [ ] Derail: `sc_derail` + `sc_end` with a reason; random repicks.
- [ ] No `error.log` lines attributable to scenario files.

Observer note (first vanilla session, `italian` / variant a / YUG+GRE): фазы шли по расписанию, выпавший вариант был honored, join lever стрельнул (`sc_offer` -> `sc_join`). Затем арка висела на peak целый год без `sc_ignite`, `sc_success` или `sc_derail`: оба ультиматума были defied, а defy-опция добавляет только war support, так что ignition зависит от того, обоснует ли ИИ сам. Betrayal exemption (F1) и телеметрия `sc_justify` / `sc_goal_end` / `sc_focus` отсутствовали в ванильном порту и теперь wired; peak, переживший лестницу, все еще недетектим и остается open item.

Observer note (second vanilla session, `japanese` / variant a / CHI+PHI): новая `sc_focus`-телеметрия показала, что Япония завершила **ноль** war-фокусов за четыре года, пока арка сидела на peak. Причина: порт бустил только war-листья и один-два корня, так что почти каждый лист сидел за небустнутым prerequisite (идеологическая развилка `JAP_sea_purge_the_kodoha_faction` XOR `JAP_revere_the_emperor_destroy_the_traitors` для Японии, африканская ветка для Италии, `reorganize_the_wehrmacht` для Германии, `the_comintern` для СССР, `no_further_appeasement` для Британии, `intervention_in_asia` для США). ИИ никогда не коммитится в гейт, так что лист никогда не *доступен* и буст на нем ничего не делает. `boost_focus_ancestors.py` теперь бустит транзитивное ancestor-замыкание каждого key focus (63 фокуса), а `sc_focus`-логирование расширено под стать, так что мертвый гейт виден в логе, а не молчит.

Observer note (third vanilla session, `japanese` -> `axis` repick): peak timeout сработал как designed. Япония держалась на peak с 1938.1, оба ультиматума были submitted, join lever стрельнул (GER и SOV joined), и на 1939.1 арка дерайльнулась с `sc_derail peak_timeout` и перевыбралась в `axis`. Затем axis-арка сжала лестницу (crises и peak на соседних тиках) и дошла до peak с CZE/POL ультиматумами и JAP/HUN joiners за месяц. `sc_focus` показал ноль строк: гейт `is_scenario_actor` звал aggressor-ветку без скобок, так что компилятор ее дропнул и логировать могли только цели; fixed.

l10n note: `99_sandbox_l_english.yml` должен оставаться UTF-8 **with BOM**. HOI4 молча дропает файл локализации без него, и каждая строка откатывается к сырому ключу (tell - тултип leader-personality). Генератор event-ключей поэтому пишет с `utf-8-sig`. Отдельно: каждый ключ, на который указывает движок, должен существовать: opinion-модификатора `scenario_ally` не хватало, и он светился сырым ключом в тултипе дипломатии. Game-rule `option = sandbox_<arc>` ids - не l10n-ключи и записи не требуют.

## Out of scope for this iteration - RU

- Flip and imperial arcs (DLC-gated focus branches in vanilla; they live in the Rt56 overlay).
- The full 28-arc catalog: only the content-portable subset ships here.
- Player-facing scenario UI beyond the pinning game rule.
- Concurrent arcs.
- Scenario behaviour in historical mode: sandbox-only.