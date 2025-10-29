Realtime Attribution Dashboard
A near-real-time First Click / Last Click attribution pipeline built using BigQuery, dbt, and Looker Studio.

Overview
This project processes GA4 event data to compute First-Click and Last-Click attribution in near real time.
A lightweight streaming demo simulates live user events into BigQuery, automatically updating the dashboard.

Tools Used:

BigQuery – raw and mart data layers

dbt – data modeling and transformation

Looker Studio – real-time analytics dashboard

Python (stream_events.py) – event streaming demo

Flow:
GA4 Dataset → BigQuery (Raw) → dbt (stg_, int_, mart_) → BigQuery (Mart) → Looker Studio Dashboard

2. Architecture Overview
        ┌───────────────────────────┐
        │       GA4 Dataset         │
        │ (public analytics data)   │
        └────────────┬──────────────┘
                     │
                     ▼
        ┌───────────────────────────┐
        │     BigQuery (Raw Layer)  │
        │ Tables: stg_ga4_events     │
        │         sample_data.events │
        └────────────┬──────────────┘
                     │
                     ▼
        ┌───────────────────────────┐
        │           dbt             │
        │  ┌─────────────────────┐  │
        │  │ Staging Models (stg_)│  │ → clean & standardize GA4 data  
        │  │ Intermediate (int_) │  │ → session & user event ranking  
        │  │ Mart Models (mart_) │  │ → First/Last click attribution  
        │  └─────────────────────┘  │
        │ dbt run, test, docs       │
        └────────────┬──────────────┘
                     │
                     ▼
        ┌───────────────────────────┐
        │     BigQuery (Mart Layer) │
        │ Tables: mart_attribution_first_click │
        │          mart_attribution_last_click  │
        └────────────┬──────────────┘
                     │
                     ▼
        ┌───────────────────────────┐
        │      Looker Studio        │
        │ (Realtime Attribution     │
        │  Dashboard Visualization) │
        │   - First vs Last totals  │
        │   - 14-day trends         │
        │   - Channel breakdown     │
        │   - Live streamed events  │
        └────────────┬──────────────┘
                     │
                     ▼
        ┌───────────────────────────┐
        │     Streaming Demo Script │
        │ (load_to_bigquery.py)     │
        │  - streams sample events  │
        │  - handles dedupe logic   │
        │  - triggers dbt material. │
        └───────────────────────────┘

