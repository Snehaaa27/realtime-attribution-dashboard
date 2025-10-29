

  create or replace view `assessment-476418`.`dbt_sneha_staging`.`stg_ga4_events`
  OPTIONS()
  as SELECT
  event_id,
  user_id,
  event_name,
  source,
  medium,
  campaign,
  event_timestamp,
  DATE(event_timestamp) AS event_date,
  FORMAT_TIMESTAMP('%H', TIMESTAMP(event_timestamp)) AS event_hour
FROM `assessment-476418`.`dbt_sneha`.`stg_ga4_events`
WHERE event_name IS NOT NULL;

