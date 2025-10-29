# Realtime Attribution Dashboard

## 1. Overview
The **Realtime Attribution Dashboard** is a prototype that demonstrates how GA4 event data can be processed in near real-time to model marketing attribution (first-click and last-click).  
The project uses a combination of **Python**, **BigQuery**, **dbt**, and **Streamlit** to build a complete data pipeline from ingestion to visualization.

## 2. Architecture Overview
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


**Data Flow:**
GA4 Events (CSV / Stream)
↓
Python Processing (ETL, cleanup, sessionization)
↓
BigQuery (staging → intermediate → mart)
↓
dbt Transformations (models, tests, lineage)
↓
Streamlit Dashboard (visualization)


## 3. Tools and Components

| Layer | Tool | Purpose |
|-------|------|----------|
| Data Source | GA4 Sample CSV | Input event data |
| Data Storage | BigQuery | Central analytical database |
| Transformation | dbt | Data modeling (`stg_`, `int_`, `mart_`) |
| Processing | Python | Cleansing, ingestion, streaming demo |
| Visualization | Streamlit | Realtime dashboard prototype |
| Monitoring | BigQuery logs, dbt tests | Quality checks, observability |


## 4. Dataset / Table Names
| Layer | Table | Description |
|-------|--------|-------------|
| **staging** | `stg_ga4_events` | Raw event data cleaned and standardized |
| **intermediate** | `int_user_sessions` | Sessionized event data per user |
| **mart** | `mart_attribution_first_click`, `mart_attribution_last_click` | Aggregated attribution results |



## 5. Assumptions
- Lookback window: **14 days**
- Identity resolution: Based on `user_id`
- Tie-breaking: Latest timestamp wins
- Latency: <5 seconds expected for streaming updates


## 6. Diagram (to be added)



## 7. Implementation Steps (coming next)
This section will explain:
- How to process the GA4 events in Python  
- How to load data into BigQuery  
- How to run dbt transformations  
- How to visualize results in Streamlit  


## 8. Folder Structure (example)

