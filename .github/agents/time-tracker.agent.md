---
name: time-tracker
description: Re-runs temporal analysis over time and reports changes.
argument-hint: dataset to monitor over time
tools:
  - execute
  - read
  - write
handoffs:
  - label: 📊 View Current Snapshot
    agent: temporal
    prompt: Run a single temporal analysis on config.json.
    send: false
  - label: 🔍 Analyze Trends
    agent: insights
    prompt: Summarize trends in this time-series and temperature-prime correlation.
    send: false
---

# Time-Series Tracker Agent

## Purpose
Re-run temporal analysis on a schedule, store snapshots, and report trend/flip events.

## Minimal Flow
1. Run baseline analysis and capture timestamp + Dallas temperature.
2. Append each run to `.github/tracking/temporal-analysis-log.jsonl`.
3. Track for each run: temperature, prime count, per-number prime status, entropy summary.
4. Detect changes since previous run (especially prime flips).
5. Produce compact timeline + notable events.

## Suggested Interval
- Stable weather: every 2-3h.
- Fast weather change: every 30-60m.

## Output
- Small table of recent snapshots.
- Flip report (which numbers changed prime status).
- Short trend summary and next check recommendation.
