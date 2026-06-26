# Walmart Data Engineering Project (ETL with Snowflake, dbt, SCD Type 1 & Type 2)

## Objective

This project demonstrates an end-to-end modern data engineering pipeline using **AWS S3**, **Snowflake**, **dbt**, **Python**, and **Streamlit**.

The pipeline begins by manually uploading Walmart CSV datasets into an **AWS S3 bucket**. Snowflake securely accesses the files through an **External Stage**, and the data is loaded into the **Bronze layer** using the **COPY INTO** command.

Using **dbt**, the raw Bronze data is transformed into clean, standardized **Silver models** and business-ready **Gold dimensional models**, including fact and dimension tables. The project implements **Slowly Changing Dimension (SCD) Type 1** transformations through dbt models and **SCD Type 2** using **dbt snapshots** to preserve historical changes in dimension data.

To simulate incremental data ingestion, updated source files are uploaded to Amazon S3 using **Python** and **VS Code**, after which the pipeline is re-executed to process new and modified records.

Finally, the curated Gold-layer tables are queried using **Snowflake SQL** and **Snowflake CLI**, and interactive business insights are presented through a **Streamlit dashboard** for reporting and analytics.

## Technology Stack

* AWS S3
* Snowflake
* dbt
* Python
* Snowflake CLI
* Streamlit
* Git & GitHub

## Key Features

* End-to-end ETL pipeline
* Medallion Architecture (Bronze → Silver → Gold)
* Snowflake External Stage and COPY INTO
* dbt Models for data transformation
* SCD Type 1 implementation
* SCD Type 2 implementation using dbt Snapshots
* Incremental data processing
* Dimensional modeling (Fact & Dimension tables)
* Interactive analytics dashboard using Streamlit

