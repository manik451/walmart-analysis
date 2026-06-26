{% macro copy_into_snowflake(table_nm) %}

{% if table_nm == 'STORES_RAW' %}

COPY INTO {{ var('target_db') }}.{{ var('target_schema') }}.STORES_RAW
(
    STORE,
    TYPE,
    SIZE
)
FROM (
    SELECT
        $1,
        $2,
        $3
    FROM @{{ var('stage_name') }}/stores.csv
)
FILE_FORMAT = (FORMAT_NAME = '{{ var("file_format_name") }}')
ON_ERROR = 'CONTINUE';

{% elif table_nm == 'DEPARTMENT_RAW' %}

COPY INTO {{ var('target_db') }}.{{ var('target_schema') }}.DEPARTMENT_RAW
(
    STORE,
    DEPT,
    DATE,
    WEEKLY_SALES,
    ISHOLIDAY
)
FROM (
    SELECT
        $1,
        $2,
        $3,
        $4,
        $5
    FROM @{{ var('stage_name') }}/department.csv
)
FILE_FORMAT = (FORMAT_NAME = '{{ var("file_format_name") }}')
ON_ERROR = 'CONTINUE';

{% elif table_nm == 'FACT_RAW' %}

COPY INTO {{ var('target_db') }}.{{ var('target_schema') }}.FACT_RAW
(
    STORE,
    DATE,
    TEMPERATURE,
    FUEL_PRICE,
    MARKDOWN1,
    MARKDOWN2,
    MARKDOWN3,
    MARKDOWN4,
    MARKDOWN5,
    CPI,
    UNEMPLOYMENT,
    ISHOLIDAY
)
FROM (
    SELECT
        $1,
        $2,
        $3,
        $4,
        $5,
        $6,
        $7,
        $8,
        $9,
        $10,
        $11,
        $12
    FROM @{{ var('stage_name') }}/fact.csv
)
FILE_FORMAT = (FORMAT_NAME = '{{ var("file_format_name") }}')
ON_ERROR = 'CONTINUE';

{% else %}

    {{ exceptions.raise_compiler_error("Invalid table name passed to copy_into_snowflake macro: " ~ table_nm) }}

{% endif %}

{% endmacro %}