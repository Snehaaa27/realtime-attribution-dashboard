-- models/mart/mart_attribution_last_click.sql
SELECT
  user_id,
  source AS last_source,
  medium AS last_medium,
  campaign AS last_campaign,
  event_timestamp AS last_click_time
FROM `assessment-476418`.`dbt_sneha_intermediate`.`int_user_events`
WHERE event_rank_desc = 1