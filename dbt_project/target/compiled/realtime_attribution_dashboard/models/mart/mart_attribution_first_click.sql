-- models/mart/mart_attribution_first_click.sql
SELECT
  user_id,
  source AS first_source,
  medium AS first_medium,
  campaign AS first_campaign,
  event_timestamp AS first_click_time
FROM `assessment-476418`.`dbt_sneha_intermediate`.`int_user_events`
WHERE event_rank_asc = 1