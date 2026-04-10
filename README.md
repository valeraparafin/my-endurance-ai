[![Auto-Sync](https://github.com/valeraparafin/my-endurance-ai/actions/workflows/auto-sync.yml/badge.svg)](https://github.com/valeraparafin/my-endurance-ai/actions/workflows/auto-sync.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

# 🚴‍♂️ My Endurance AI

Section 11 endurance coaching protocol with automated Intervals.icu data sync and AI coach.

**Last successful sync:** _updated automatically by GitHub Actions_

## Stack

- **[Section 11](https://github.com/CrankAddict/section-11)** — AI coaching protocol (v11.25)
- **Intervals.icu** — training data source  
- **GitHub Actions** — automated sync 3× daily
- **OpenClaw** — AI coach interface

## Quick Links

- 📊 **Live data** — [latest.json](https://raw.githubusercontent.com/valeraparafin/my-endurance-ai/main/latest.json)
- 📈 **History** — [history.json](https://raw.githubusercontent.com/valeraparafin/my-endurance-ai/main/history.json)
- 📋 **Commands reference** — [COMMANDS.md](COMMANDS.md)
- 🏃‍♂️ **Athlete dossier** — [dossier/DOSSIER.md](dossier/DOSSIER.md)

## Data Files (auto-generated)

| File | URL |
|------|-----|
| `latest.json` | [View](https://raw.githubusercontent.com/valeraparafin/my-endurance-ai/main/latest.json) |
| `history.json` | [View](https://raw.githubusercontent.com/valeraparafin/my-endurance-ai/main/history.json) |
| `intervals.json` | [View](https://raw.githubusercontent.com/valeraparafin/my-endurance-ai/main/intervals.json) |
| `ftp_history.json` | [View](https://raw.githubusercontent.com/valeraparafin/my-endurance-ai/main/ftp_history.json) |
| `routes.json` | [View](https://raw.githubusercontent.com/valeraparafin/my-endurance-ai/main/routes.json) |

## How It Works

1. GitHub Actions runs `sync.py` 3× daily (15:30, 19:30, 23:30 MSK)
2. Data is pulled from Intervals.icu API — activities, wellness, metrics
3. JSON files are committed to this repo (anonymized)
4. AI coach reads files directly and provides analysis & recommendations

```
Intervals.icu ──→ GitHub Actions ──→ JSON files ──→ AI Coach
   (API)         (sync.py 3×/day)   (this repo)    (OpenClaw)
```

## Trigger Sync

[**Run workflow →**](https://github.com/valeraparafin/my-endurance-ai/actions/workflows/auto-sync.yml) — tap "Run workflow" for a fresh sync.

## Dossier

See [dossier/DOSSIER.md](dossier/DOSSIER.md) for the complete athlete profile.

---

[Section 11](https://github.com/CrankAddict/section-11) · [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
