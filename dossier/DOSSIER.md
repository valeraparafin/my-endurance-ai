# Athlete Training Dossier & Performance Roadmap

**Dossier Version:** v1.1.1  
**Protocol Compatibility:** Section 11 v11.6+  
**Date:** [2026-04-01]  
**Primary Source Systems:** Intervals.icu | Strava.com

This document serves as a reference template for endurance athletes using the deterministic AI-coaching framework defined in Section 11.

---

## Quick Start

1. Fill in your athlete profile (Section 1)
2. Document your equipment (Section 2)
3. Define your training schedule and goals (Section 3)
4. Enter your current performance metrics (Section 4)
5. Set up your nutrition/fueling protocol (Section 5)
6. Link this dossier to your JSON data mirror (see Section 11 for protocol)

---

## 1. Athlete Overview

### Athlete Profile

| Field | Value |
|-------|-------|
| Name | Artem |
| Age | 34 |
| Height | [168] |
| Current Weight | [69] |
| Target Weight | 68 |
| Location | Vladimir, Russia |

**Weigh-in Protocol:** [e.g., Once weekly, Friday morning, after bathroom, before food/drink]

### Medications & Supplements (Optional)

| Time | Items |
|------|-------|
| [Time] | [List medications/supplements] |
| [Time] | [List medications/supplements] |

### Sport Focus

| Type | Description |
|------|-------------|
| Primary | Cycling performance (Gravel/Endurance) |
| Secondary | Strength & Core stability |

### Goals

| Goal | Target Date |
|------|-------------|
| FTP 250W | 2026 |
| Consistent training year-round | Ongoin |
| Find my comfort and efficiency cadence  | 2026 |
| Find my self on some race someday | 2026 |

**Current Phase:** Aerobic base + outdoor transition (spring)  
**Training Style:** Mixed indoor/outdoor (~4-5h/week baseline)

---

## 2. Equipment & Environment

### Indoor Training Setup

| Component | Details |
|-----------|---------|
| Trainer/Bike | THINKRIDER XX PRO |
| Platform | MyWhoosh |
| Cooling | CYCPLUS |
| Sensors | HRM, power meter, cadence, EGR |
| Pedals | SHIMANO 540 |

### Outdoor Setup

| Component | Details |
|-----------|---------|
| Bike | Faraoll GT20 Frame, size-S] |
| Power Meter | Magene PES515  |
| Head Unit | Garmin Edge 130 Plus |
| HRM | THINKRIDER, Amazfit Bip 6 |

### Other Modalities

| Modality | Equipment | Purpose |
|----------|-----------|---------|
| Strength | Dumbbells (16kg, 4kg) | Core stability, injury prevention |

### Environment

| Factor | Details |
|--------|---------|
| Indoor | Room 5.5*3 m2 with window and fan |
| Outdoor | Vladimir city - limited training areas (parks muddy in spring), traffic challenges, temperature from -30 to +35 divided by seasons |
| Calibration | Power meter calibration via Garmin head unit |

---

## 3. Training Schedule & Framework

### Weekly Volume Target

**Baseline:** 4-6 hours/week (± 2 hours)  
**Peak phases:** Up to 8 hours (requires HRV ≥ 70ms, good recovery)

### Normal Weekly Schedule

| Day | Primary Session | Duration | Secondary |
|-----|-----------------|----------|-----------|
| Sunday | Outdoor ride / Rest | 1-2h / Rest | Chill ride |
| Monday | Rest or Z1 recovery or Volume | 40-60 min | Depends on day before |
| Tuesday | Z2 Endurance | 60 min | [Optional] |
| Wednesday | Strength + Core | 45 min | [Optional] |
| Thursday | Z2 / Threshold | [Duration] | [Optional] |
| Friday | Rest or Z1 | 40 min | [Optional] |
| Saturday | Outdoor ride (weather) | 1-3h | [Optional] |

### Session Details

| Session Type | Target Power/HR | Duration | Purpose |
|--------------|-----------------|----------|---------|
| VO₂Max | 110-120% | 5*5 | Anaerobic capacity |
| Endurance | 75-88% | 60 min | Aerobic base |
| Sweetspot | 88-100% | 2 * 20 min | LT Development  |
| Long Ride | 56-75%| 2h | Muscle stability |
| Recovery | 50-60% | 40-60 min| Activity Recover |
|Strength | Bodyweight + 16kg | 45 min | Muscle stability |

### Recovery Protocol

**Recovery Triggers (Auto-Deload):**
- HRV ↓ > 20% → Skip training, full rest
- RHR ↑ ≥ 5 bpm → Reduce intensity or rest
- Feel ≥ 4 →  Deload or rest day
- Two+ triggers → Full rest day

**Feel Scale:**
| Score | Meaning |
|-------|---------|
| 1 | Excellent (fully recovered) |
| 2 | Good (normal fatigue) |
| 3 | Moderate (manageable tiredness) |
| 4 | Fatigued (reduced readiness, deload trigger) |
| 5 | Exhausted (complete rest required) |

### Performance Objectives

| Year | Phase | Focus | Primary KPI |
|------|-------|-------|-------------|
|2026|Base + Build|FTP 215→230+W, Cadence 90+|FTP 230W+, HRV >80ms, LOW HR|
|2027|Development|FTP 230→250W, race readiness|FTP 250W, W/kg 3.6+|

---

## 4. Performance Metrics

### Current Power Zones

| Zone | % of FTP | Power (W) | Notes |
|------|----------|-----------|-------|
| Z1 | 0–55% | [Calculate] | Active Recovery |
| Z2 | 56–75% | [Calculate] | Endurance (Base) |
| Z3 | 76–90% | [Calculate] | Tempo |
| Z4 | 91–105% | [Calculate] | Threshold |
| Z5 | 106–120% | [Calculate] | VO₂max |
| Z6 | 121–150% | [Calculate] | Anaerobic |
| Z7 | 151%+ | [Calculate] | Neuromuscular |
| SS | 84–97% | [Calculate] | Sweetspot |

**Current FTP:** [W] (Indoor: [W])  
**Max HR:** [bpm]  
**Threshold HR:** [bpm]

### Current Fitness Markers

| Metric | Value | Notes |
|--------|-------|-------|
| FTP (Outdoor) | [W] | |
| FTP (Indoor) | [W] | Adjusted for indoor conditions |
| LT2 Power (MLSS) | [W] | ≈[%] of FTP |
| LT2 HR | [bpm] | |
| LT1 (AeT) | [W] | HR ≈[bpm] |
| VO₂max Interval Power | [W] | |
| Sweetspot Target | [W] | |
| Weekly Volume | [hours] | [TSS range] |

### Weight Tracking

**Protocol:** [Frequency, conditions]  
**Adjustment Control:** Weight adjustments only permitted during readiness-positive periods (DI ≥ 0.95, HR drift ≤ 3%, RI ≥ 0.8)

---

## 5. Nutrition / Fueling

### Training Fuel Recipe

```
[Your carb mix recipe]
```

**CHO per bottle:** [g]  
**Target absorption:** [g CHO/h]

### Recovery Drink Recipe

```
[Your recovery drink recipe]
```

### Fueling by Workout Type

| Workout Type | Duration | CHO Target | Setup |
|--------------|----------|------------|-------|
| Recovery / Z1–Z2 | < 1.5 h | [g/h] | [Description] |
| Endurance | 1.5–3 h | [g/h] | [Description] |
| Long Endurance | 3–6 h | [g/h] | [Description] |
| Threshold / SS | 1–2 h | [g/h] | [Description] |
| VO₂ / High Intensity | 1–1.5 h | [g/h] | [Description] |
| Race / Event | 4–6 h | [g/h] | [Description] |

### Hydration

**Target:** [ml/hour]  
**Sodium:** [mg/L] base, + [mg/h] additional for long/hot rides

---

## 6. Adaptation & Current Focus

### Current Adaptation Focus

- [ ] [Focus item 1]
- [ ] [Focus item 2]
- [ ] [Focus item 3]
- [ ] [Focus item 4]

### Next-Phase Options

[Description of upcoming phase transition criteria and options]

---

## 7. Outdoor Transition Plan (if applicable)

### Transition Timeline

| Month | Changes | Notes |
|-------|---------|-------|
| [Month] | [Transition step] | [Details] |
| [Month] | [Transition step] | [Details] |
| [Month] | [Transition step] | [Details] |

**General Rules:**
- Outdoor rides replace indoor 1:1
- HR < 85% of threshold = aerobic
- Use HR to guide intensity early season

---

## 8. Long-Term Performance Roadmap

### Primary Objective

[Your main goal with target time/performance]

### Progression Overview

| Year | Focus | FTP Target | W/kg Target | Key Metrics |
|------|-------|------------|-------------|-------------|
| [Year] | [Focus] | [W] | [W/kg] | [Metrics] |
| [Year] | [Focus] | [W] | [W/kg] | [Metrics] |
| [Year] | [Focus] | [W] | [W/kg] | [Metrics] |

### Event-Specific Targets (Optional)

| Event/Segment | Year | Priority | Target Time | Target Power |
|---------------|------|----------|-------------|--------------|
| [Event] | [Year] | [A/B/C] | [Time] | [W] |
| [Event] | [Year] | [A/B/C] | [Time] | [W] |

> **Race tagging for automated protocol activation:** Tag races in Intervals.icu as `RACE_A`, `RACE_B`, or `RACE_C` using the event category selector. The race-week protocol (Section 11A) activates automatically for A and B races within 7 days. C races are training races — no taper adjustments. For best results, also set expected duration (`moving_time`) in the event to enable event-type modifiers (carb loading, opener intensity, TSB targets).

---

## 9. Coach Notes

[Space for coach observations, athlete-specific considerations, or important reminders]

---

## 10. Operational & Data Integrity Log

### Training Timeline & Event Log

| Date | Event | Notes |
|------|-------|-------|
| [Date] | [Event] | [Details] |
| [Date] | [Event] | [Details] |

### Calibration & Data Log

| Date | Item | Action |
|------|------|--------|
| [Date] | [Equipment] | [Action taken] |
| [Date] | [Equipment] | [Action taken] |

---

## Data Mirror Configuration

### JSON Endpoint (for AI coaches)

**URL:** `https://raw.githubusercontent.com/[username]/[repo]/main/latest.json`

**Archive:** `https://github.com/[username]/[repo]/tree/main/archive`

**— OR (GitHub connector) —**

**Repo:** `[username]/[repo]` (connected via platform's GitHub integration — AI reads files directly, no URLs needed)

> **Tip:** If you commit `DOSSIER.md` to your data repo alongside `latest.json`, `history.json`, and `intervals.json`, connecting the repo gives the AI both your data and your profile in one connection. The only remaining piece is `SECTION_11.md`, which the AI can fetch from the public CrankAddict/section-11 repo or a second connector.

**— OR (local setup) —**

**Path:** `latest.json` (data directory root, alongside this dossier)

**History:** `history.json` (data directory root)

**Intervals:** `intervals.json` (data directory root — on-demand, for structured session analysis)

**Data Path (optional):** `[/path/to/training-data/]`
Only needed if the AI agent's working directory is different from where data files live (e.g., OpenClaw workspace is `~/clawd/` but data is in `~/training-data/`). Leave blank if they are the same directory.

For local setups where sync.py runs on the same machine as the AI agent, files are read directly from the filesystem — no URLs needed. See `examples/json-local-sync/SETUP.md` for the complete local pipeline.

This endpoint provides synchronized Intervals.icu metrics for deterministic AI parsing. See **Section 11** for the full AI Coach Guidance Protocol.

---

## Protocol Reference

This dossier follows the **Section 11 A/B AI Coach Guidance Protocol** for AI integration.

**Protocol Location:** [Link to your Section 11 document or repo]

---

## Changelog

### v1.0 ([Date])
- Initial dossier creation

