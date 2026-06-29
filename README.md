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

# 🥈 Silver Layer Transformations

The Silver layer is responsible for cleaning, validating, and standardizing raw Bronze data before it is consumed by business models.

Implemented transformations include:

| Transformation | Purpose |
|---------------|---------|
| DISTINCT | Removes duplicate records |
| UPPER() | Standardizes text values |
| TRIM() | Removes leading/trailing spaces |
| COALESCE() | Replaces NULL values with default values |
| WHERE Filters | Removes invalid or incomplete records |
| Column Aliases | Uses business-friendly column names |
| Data Type Standardization | Ensures consistent datatypes |

---

# 🥇 Gold Layer

The Gold layer contains business-ready analytical models.

### Dimension Tables

- Walmart_Date_Dim
- Walmart_Store_Dim

### Fact Table

- Walmart_Fact_Table

The Gold layer is optimized for reporting and business analytics.

---

# 📊 Python Dashboard

The Python application connects directly to the Snowflake Gold layer using the Snowflake Connector.

It generates interactive Plotly dashboards, including:

- Top 10 Stores by Sales
- Top Departments by Sales
- Fuel Price vs Weekly Sales
- Temperature vs Weekly Sales
- CPI vs Weekly Sales
- Markdown Analysis
- Weekly Sales Distribution
- KPI Summary
  - Total Sales
  - Total Stores
  - Total Departments
  - Average Weekly Sales

---

# 🔄 Slowly Changing Dimensions

### SCD Type 1

Implemented using dbt models.

- Existing records are updated.
- Historical values are not preserved.

Used for:

- Store Dimension
- Date Dimension

### SCD Type 2

Implemented using dbt Snapshots.

- Historical versions are preserved.
- Tracks changes over time using version start and end dates.

Used for:

- Walmart Fact Table Snapshot

---

# 📂 Project Structure

```
walmart-analysis
│
├── models
├── macros
├── snapshots
├── tests
├── seeds
├── analyses
│
├── python
│   ├── connection_test.py
│   ├── dashboard_html.py
│   ├── sales_analysis.py
│   ├── local_to_aws_s3.py
│   ├── requirements.txt
│   ├── output
│   └── .env.example
│
├── dbt_project.yml
├── README.md
└── .gitignore
```

---

# 🔐 Security

Sensitive Snowflake credentials are **not stored** in the repository.

Credentials are managed using:

- `.env`
- `.gitignore`

An `.env.example` file is included as a template.

---

# 📈 Future Enhancements

- Automate ingestion using Snowpipe
- Orchestrate workflows using Apache Airflow
- Deploy dashboards using Streamlit Cloud
- Integrate CI/CD using GitHub Actions
- Add data quality monitoring using dbt tests

