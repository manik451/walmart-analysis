{{ config(
    materialized='incremental',
    unique_key=['STORE_ID', 'DEPT_ID'],
    schema='GOLD'
) }}

SELECT DISTINCT
    d.STORE_ID,
    d.DEPT_ID,
    s.STORE_TYPE,
    s.STORE_SIZE,
    CURRENT_TIMESTAMP() AS INSERT_DATE,
    CURRENT_TIMESTAMP() AS UPDATE_DATE
FROM {{ ref('stg_department') }} d
LEFT JOIN {{ ref('stg_stores') }} s
    ON d.STORE_ID = s.STORE_ID
WHERE d.STORE_ID IS NOT NULL
  AND d.DEPT_ID IS NOT NULL