[![Auto-Sync](https://github.com/valeraparafin/my-endurance-ai/actions/workflows/auto-sync.yml/badge.svg)](https://github.com/valeraparafin/my-endurance-ai/actions/workflows/auto-sync.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

# 🚴‍♂️ My Endurance AI

Section 11 endurance coaching protocol with automated Intervals.icu data sync and AI coach.

**Last successful sync:** _updated automatically by GitHub Actions_

## Stack

- **[Section 11](https://github.com/CrankAddict/section-11)** — AI coaching protocol (v11.23)
- **Intervals.icu** — training data source
- **GitHub Actions** — automated sync every 15 minutes
- **OpenClaw** — AI coach interface (local agent, Russian language)

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

## Repo Structure

| Path | Description |
|------|-------------|
| `dossier/` | Athlete profile (Artem, cycling, Section 11 v1.1) |
| `framework/` | Section 11 protocol and sync engine (local only) |
| `.github/workflows/` | GitHub Actions auto-sync |
| `sync.py` | Data sync engine (from Section 11) |
| `COMMANDS.md` | AI coach command reference |

## How It Works

```
Intervals.icu API ──→ GitHub Actions ──→ latest.json ──→ AI Coach
   (every 15 min)       (sync.py)      (this repo)     (OpenClaw agent)
```

1. **GitHub Actions** runs `sync.py` every 15 minutes
2. Pulls data from Intervals.icu (activities, wellness, intervals, power curves)
3. Commits JSON files to this repo (anonymized athlete ID, outdoor names redacted)
4. **AI coach** reads files directly → analyses → recommends

## Trigger Sync

[**Run workflow →**](https://github.com/valeraparafin/my-endurance-ai/actions/workflows/auto-sync.yml) — tap "Run workflow" for a fresh sync.

## Athlete Profile

- **Sport:** Cycling (gravel/endurance)
- **FTP:** 215W indoor / ~215W outdoor | eFTP: 220W | W/kg: 3.1
- **HR zones:** Empirical — Z1 <130, Z2 130–145, Z3 145–160, Z4 160–170, Z5 170+
- **Goals 2026:** FTP 230–250W, cadence 90+, Гонка: Покрова gravel finish
- **Phase:** Build (week 1 of 2026 season)

Full profile: [dossier/DOSSIER.md](dossier/DOSSIER.md)

## Local Setup

For local development, clone this repo and ensure:
- `framework/` is not published (it's a submodule of https://github.com/CrankAddict/section-11)
- `.sync_config.json` is in `.gitignore` (contains API credentials)

See [Section 11 README](https://github.com/CrankAddict/section-11) for full protocol documentation.

## License

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — Free for personal and non-commercial use. Attribution required.
