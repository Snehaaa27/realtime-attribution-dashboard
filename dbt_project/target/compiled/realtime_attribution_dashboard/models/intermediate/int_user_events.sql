-- models/intermediate/int_user_events.sql
SELECT
  user_id,
  event_name,
  source,
  medium,
  campaign,
  event_timestamp,
  ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_timestamp ASC) AS event_rank_asc,
  ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_timestamp DESC) AS event_rank_desc
FROM `assessment-476418`.`dbt_sneha_staging`.`stg_ga4_events`