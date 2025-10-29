
  
    

    create or replace table `assessment-476418`.`dbt_sneha_mart`.`mart_attribution_first_click`
      
    
    

    
    OPTIONS()
    as (
      -- mart_attribution_first_click.sql
-- Compute First-Click attribution

SELECT
  user_id,
  MIN(event_timestamp) AS first_click_time,
  ARRAY_AGG(source ORDER BY event_timestamp ASC LIMIT 1)[OFFSET(0)] AS first_source
FROM `assessment-476418`.`dbt_sneha_staging`.`stg_ga4_events`
WHERE event_name = 'page_view'
GROUP BY user_id
    );
  