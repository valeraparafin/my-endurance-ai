[![Auto-Sync](https://github.com/valeraparafin/my-endurance-ai/actions/workflows/auto-sync.yml/badge.svg)](https://github.com/valeraparafin/my-endurance-ai/actions/workflows/auto-sync.yml)

# Training Data + AI Coach

Section 11 endurance coaching protocol with automated Intervals.icu data sync.

**Last successful sync:** 2026-04-02 12:17:41 UTC

## Stack

- **[Section 11](https://github.com/CrankAddict/section-11)** — AI coaching protocol
- **Intervals.icu** — training data source
- **GitHub Actions** — automated sync every 15 minutes
- **OpenClaw** — AI coach interface

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
| `section11/` | AI coaching protocol (framework) |
| `dossier/` | Athlete profile (Artem, cycling) |
| `.github/workflows/` | Auto-sync workflow |
| `sync.py` | Data sync engine |

## Trigger Sync

[**Run workflow →**](https://github.com/valeraparafin/my-endurance-ai/actions/workflows/auto-sync.yml) — tap "Run workflow" for a fresh sync.

## License

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
