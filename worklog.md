 Day 0 — Setup & Planning
- Created GitHub repository: `realtime-attribution-dashboard`
- Set up local project structure with folders for dbt, streaming demo, and docs.
- Initialized git and connected to remote.
- Currently waiting for BigQuery access (billing issue) and sent clarification to the company.
Day 1 - Project setup
- Initialized dbt project and BigQuery connection
- Created staging model for GA4 events

Day 2 - Intermediate & mart models
- Built int_user_events and mart_attribution_first_click
- Tested lineage and dependencies with dbt docs

Day 3 - Streaming demo
- Wrote Python script to stream 10 sample events into BigQuery
- Verified ingestion with dbt runs

Day 4 - Dashboard + Documentation
- Created Looker Studio dashboard
- Finalized README with architecture and monitoring notes
