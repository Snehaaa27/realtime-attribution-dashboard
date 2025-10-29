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

