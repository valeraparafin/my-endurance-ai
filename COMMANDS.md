# 🚴‍♂️ Endurance Coach — Command Reference

> Quick reference for querying your AI coach. Just copy-paste or speak naturally.

---

## 🟢 Daily / Pre-Ride

| Query | Coach does |
|-------|-----------|
| `Готовность?` | Readiness assessment (HRV, RHR, sleep, TSB, ACWR) + Go/Modify/Skip |
| `Как я сегодня?` | Same as above, plus context on recent fatigue/trends |
| `Что делать сегодня?` | Readiness + phase + weather → workout recommendation |
| `Погода для катания?` | Weather check (Vladimir) — only if conditions meet thresholds |

## 📊 Current Status

| Query | Coach does |
|-------|-----------|
| `Форма?` | CTL, ATL, TSB, eFTP, W', phase |
| `Как тренированность?` | Full current status + trend indicators |
| `Какой мой FTP?` | Indoor/outdoor FTP, eFTP from API, W/kg |
| `Мои зоны?` | Power zones + HR zones from current setup |

## 📈 Weekly Analysis

| Query | Coach does |
|-------|-----------|
| `Как неделя?` | Weekly summary: TSS, hours, activities, compliance |
| `Поляризация?` | Seiler TID, polarization index, gray zone % |
| `Нагрузка в норме?` | ACWR, monotony, strain, hard days count |
| `Сколько TSS за неделю?` | Weekly TSS breakdown by type (indoor/outdoor) |

## 🔬 Deep Dive

| Query | Coach does |
|-------|-----------|
| `Анализируй последнюю тренировку` | Latest activity details: zones, compliance, cardiac drift, efficiency |
| `Анализируй активность от [дата]` | Specific activity from intervals.json (structured sessions only) |
| `Как меняется мой FTP?` | FTP history trends (if available), W' changes, power curve shifts |
| `Покажи power curve` | 5锚点 power curve evolution: 5s, 60s, 300s, 1200s, 3600s |
| `Как моя выносливость?` | Durability metrics, efficiency factor trend, HRRc recovery |

## 📊 Long-Term Analysis

| Query | Coach does |
|-------|-----------|
| `Анализируй последний месяц` | history.json → daily/weekly trends, CTL/ATL, missed sessions |
| `Анализируй последние 3 месяца` | Full longitudinal analysis: phases, progression, plateaus |
| `Анализируй последние 6 месяцев` | Same + seasonal comparison, long-term adaptations |
| `Сравни этот месяц с прошлым` | Month-over-month comparison across all metrics |
| `Покажи тренды CTL/ATL/TSB` | Fitness/fatigue/freshness trends from history.json |

## 🎯 Planning

| Query | Coach does |
|-------|-----------|
| `Анализируй 3 месяца → план на месяц` | Deep history analysis → structured training plan |
| `Составь план на неделю` | Phase-appropriate weekly plan aligned with DOSSIER goals |
| `Составь план тренировки на сегодня` | Specific session plan based on readiness + phase |
| `План подготовки к гонке [дата]` | Taper schedule, peak week, race-week protocol |
| `Какая сейчас фаза?` | Phase detection + what it means for training |
| `Когда тест на FTP?` | Recommended timing based on phase + last test |

## 🏁 Race / Event

| Query | Coach does |
|-------|-----------|
| `Сколько до гонки?` | Countdown to Гонка: Покрова + readiness check |
| `Режим гонки?` | Race week protocol (carb loading, opener, TSB targets) |
| `Как готовиться к gravel?` | Sport-specific advice + equipment check |

## 💬 Conversational

| Query | Coach does |
|-------|-----------|
| `Почему так?` | Detailed explanation of any metric/recommendation |
| `Что улучшить?` | Targeted improvement recommendations |
| `У меня [симптом]` | Context-aware health/adjustment advice |
| `Совет по питанию?` | Fueling strategy based on workout type |
| `Совет по каденсу?` | Cadence analysis vs goals (current: 85-87 indoor → target 90+) |

## ⚙️ System / Config

| Query | Coach does |
|-------|-----------|
| `Проверь sync` | GitHub Actions status, last run result |
| `Когда был последний sync?` | Data freshness check |
| `Обнови данные` | Trigger GitHub Actions workflow manually |
| `Запиши это` | Save important note to memory file |

---

## Tips

- **Be specific:** "Analyze my 3-month trend → 4-week build plan" works better than "help me train"
- **Reference dates:** "Анализируй тренировку 30 марта" pulls exact interval data
- **Ask "почему" any time:** Get detailed explanations for any metric
- **Russian or English:** Both work. Coach defaults to your language.
- **Don't hold context in your head:** Say "запиши" → it survives any restart
