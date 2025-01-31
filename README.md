# Анализ цен акций NVDA, TSLA, INTC, MSFT и IBM

## Описание проекта

В этом проекте анализируются цены акций компаний NVDA, TSLA, INTC, MSFT и IBM за период с 29 января 2024 года по 29 января 2025 года. Данные загружаются с Yahoo Finance с месячным интервалом. Основная цель анализа — изучение динамики цен, расчет месячных изменений и определение взаимосвязи между ценами акций.

## Выбор акций

Выбор этих акций обусловлен их значительным влиянием на технологический сектор и участием в сфере искусственного интеллекта (AI):

- **NVDA (NVIDIA)** — мировой лидер в производстве графических процессоров и AI-ускорителей, используемых для машинного обучения и обработки больших данных.
- **TSLA (Tesla)** — активно развивает технологии автономного вождения, внедряя AI в свои системы автопилота.
- **MSFT (Microsoft)** — ведущий разработчик облачных технологий и AI-решений, включая OpenAI и интеграцию AI в продукты Microsoft.
- **IBM (International Business Machines)** — крупный игрок в сфере облачных технологий и AI, включая Watson и решения для бизнес-аналитики.
- **INTC (Intel)** — один из крупнейших производителей процессоров, также разрабатывающий AI-решения и аппаратное ускорение вычислений, но с меньшим фокусом на AI по сравнению с остальными компаниями.

## Используемые инструменты

- **Python** — язык программирования для обработки и анализа данных.
- **yfinance** — библиотека для получения финансовых данных.
- **pandas** — библиотека для работы с таблицами и временными рядами.
- **matplotlib и seaborn** — библиотеки для визуализации данных.

## Построенные графики

1. **График изменения цен закрытия** — показывает динамику цен акций за исследуемый период.
2. **График месячных изменений (returns)** — отображает процентные изменения цен акций по месяцам.
3. **Тепловая карта корреляции** — иллюстрирует степень взаимосвязи между ценами закрытия различных акций.

## Вывод по графикам

### График изменения цен закрытия

![image](https://github.com/user-attachments/assets/d7551d3a-12e1-40ae-af42-52a0c8cfe9fd)

График показывает динамику котировок компаний, активно работающих в сфере AI, на протяжении года. Видно, что акции Tesla и NVIDIA демонстрируют наибольшую волатильность:

- **Tesla**: цена выросла с $201,88 в феврале до пика в $403,84 в декабре (+100%), но затем снизилась до $389,1 в январе. Рост может быть связан с анонсами новых AI-решений для автопилота, оптимистичными прогнозами аналитиков и повышением продаж электромобилей. Коррекция в январе объясняется волатильностью рынка.
- **NVIDIA**: с $79,09 в феврале акции выросли до $138,24 в ноябре (+74,8%) благодаря рекордному спросу на чипы для AI-моделей, но к январю скорректировались до $123,7 (-10,5%). Падение может быть связано с фиксацией прибыли инвесторами и ожиданиями новых регуляторных ограничений на экспорт чипов.
- **Microsoft** колебалась в пределах $387,16 — $445,26, увеличившись за год на 14,99%. Рост может объясняться развитием облачных сервисов Azure и интеграцией AI в экосистему Microsoft.
- **IBM**, стартовав с $178,58, завершила год на $228,63 (+28,03%). Компания активно инвестирует в AI и квантовые вычисления, что поддерживает интерес инвесторов.

### График месячных изменений

![image](https://github.com/user-attachments/assets/2c3a2355-3182-4e49-aa64-e25af34c1750)

Позволяет детально рассмотреть периоды значительного роста или падения:

- **NVIDIA** показала максимальный месячный прирост в мае (+26,89%), вероятно, на фоне сильной отчетности и анонса новых AI-ускорителей.
- **Tesla** зафиксировала самый сильный рост в ноябре (+38,15%), что может быть связано с новыми контрактами и усилением интереса к автономному вождению.
- **Intel** испытала самый резкий спад в августе (-28,3%), вероятно, из-за потери доли рынка и проблем с конкурентами (AMD и ARM).

### Тепловая карта корреляции

![image](https://github.com/user-attachments/assets/cec930a6-27e5-4eba-acd0-da3bd7595996)

Тепловая карта демонстрирует взаимосвязь между акциями:

- **Положительная корреляция (более 0.7)**:
  - Microsoft и NVIDIA: обе компании активно развивают AI, облачные вычисления и серверные решения, что делает их котировки схожими.
  - IBM и Microsoft: IBM развивает AI-решения в партнерстве с Microsoft, поэтому их динамика частично совпадает.
- **Отрицательная корреляция (менее -0.3)**:
  - Intel и Tesla: Tesla ориентирована на электромобили и автопилот, а Intel сталкивается с жесткой конкуренцией на рынке чипов, что приводит к разнонаправленным движениям котировок.
  - NVIDIA и Intel: несмотря на то, что обе компании производят чипы, NVIDIA сосредоточена на AI-ускорителях, а Intel теряет позиции на рынке процессоров, что создает разнонаправленные движения цен.

## Заключение

Этот анализ может быть полезен для инвесторов и аналитиков, желающих понять взаимосвязи между акциями и определить тенденции на рынке AI. Исследование демонстрирует влияние технологических инноваций на стоимость акций и помогает прогнозировать возможные тренды в будущем.
