# Architecture Outline — Real-Time Attribution Dashboard

## Overview
This project simulates a real-time marketing attribution pipeline similar to a GA4 → BigQuery → dbt → Dashboard workflow.

---

## Components
1. **Data Source**
   - Using `ga4_events.csv` as simulated GA4 event data.
   - Columns: event_id, user_id, event_name, source, medium, campaign, event_timestamp.

2. **Data Ingestion**
   - In a production setup, GA4 exports data to BigQuery in near real-time.
   - Here, we’ll simulate ingestion using Python scripts that stream data rows into a BigQuery table (or print to console for demo).

3. **dbt Layer**
   - **stg_ models:** Clean and standardize event data.
   - **int_ models:** Derive session-level and user-level interaction metrics.
   - **mart_ models:** Build attribution tables:
     - `mart_first_click`
     - `mart_last_click`
   - Each model tested and documented using dbt tests and docs.

4. **Attribution Logic**
   - **First-click:** The earliest source/medium that brought a user before purchase.
   - **Last-click:** The most recent source/medium before purchase.

5. **Dashboard**
   - A **Streamlit** app (or Looker Studio mockup) showing:
     - First vs. Last attribution totals
     - 14-day trend line
     - Channel breakdown (source/medium)
     - Live panel displaying streamed events

6. **Streaming Demo**
   - Simple Python script to simulate new GA4 events being streamed.
   - Demonstrates deduplication, idempotency, and near real-time update of dashboard.

---

## Example Data Flow
