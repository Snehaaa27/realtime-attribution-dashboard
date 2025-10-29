-- int_user_sessions.sql
-- Create user sessions per day

SELECT
  user_id,
  event_date,
  CONCAT(user_id, '_', event_date) AS session_id,
  COUNT(DISTINCT event_name) AS event_count,
  MIN(event_timestamp) AS session_start,
  MAX(event_timestamp) AS session_end
FROM `assessment-476418`.`dbt_sneha_staging`.`stg_ga4_events`
GROUP BY 1,2