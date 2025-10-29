
  
    

    create or replace table `assessment-476418`.`dbt_sneha_mart`.`mart_attribution_last_click`
      
    
    

    
    OPTIONS()
    as (
      -- mart_attribution_last_click.sql
-- Compute Last-Click attribution

SELECT
  user_id,
  MAX(event_timestamp) AS last_click_time,
  ARRAY_AGG(source ORDER BY event_timestamp DESC LIMIT 1)[OFFSET(0)] AS last_source
FROM `assessment-476418`.`dbt_sneha_staging`.`stg_ga4_events`
WHERE event_name = 'page_view'
GROUP BY user_id
    );
  