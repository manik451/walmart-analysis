{% snapshot store_snapshot %}

{{
    config(
        target_database='WALMART_DB',
        target_schema='SNAPSHOTS',
        unique_key='STORE_ID',
        strategy='check',
        check_cols=['STORE_TYPE', 'STORE_SIZE']
    )
}}

SELECT
    STORE_ID,
    STORE_TYPE,
    STORE_SIZE
FROM {{ ref('dim_store') }}

{% endsnapshot %}