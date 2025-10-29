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
FROM {{ ref('stg_ga4_events') }}
