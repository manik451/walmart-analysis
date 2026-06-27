{{ config(
    materialized='incremental',
    unique_key='DATE_ID',
    schema='GOLD'
) }}

SELECT DISTINCT
    TO_NUMBER(TO_CHAR(STORE_DATE, 'YYYYMMDD')) AS DATE_ID,
    STORE_DATE,
    IS_HOLIDAY,
    CURRENT_TIMESTAMP() AS INSERT_DATE,
    CURRENT_TIMESTAMP() AS UPDATE_DATE
FROM {{ ref('stg_department') }}
WHERE STORE_DATE IS NOT NULL