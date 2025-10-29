-- models/staging/stg_ga4_events.sql
SELECT
  event_id,
  CAST(user_id AS STRING) AS user_id,
  event_name,
  source,
  medium,
  campaign,
  TIMESTAMP(event_timestamp) AS event_timestamp
FROM `assessment-476418`.`dbt_sneha_staging`.`raw_events`
WHERE user_id IS NOT NULL