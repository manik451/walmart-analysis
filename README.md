# Walmart Data Engineering Project
### End-to-End ETL Pipeline using AWS S3, Snowflake, dbt, Python & Plotly

## 📌 Project Overview

This project demonstrates an end-to-end modern data engineering pipeline built using **AWS S3**, **Snowflake**, **dbt**, **Python**, and **Plotly**.

The pipeline begins by uploading Walmart CSV datasets into an **Amazon S3 bucket**. Snowflake securely accesses the files using an **External Stage**, and the raw data is loaded into the **Bronze layer** using the **COPY INTO** command.

Using **dbt**, the raw Bronze data is transformed into clean, standardized **Silver models**, followed by business-ready **Gold dimensional models** consisting of fact and dimension tables.

The project implements:

- **SCD Type 1** using dbt models (latest values overwrite previous records)
- **SCD Type 2** using dbt snapshots to preserve historical changes

To simulate incremental data ingestion, updated source files are uploaded to Amazon S3 using **Python**, and the pipeline is re-executed to process new and modified records.

Finally, curated Gold-layer tables are queried from Snowflake using **Python**, and interactive business dashboards are generated using **Plotly**.

---

# 🏗️ Architecture

```
CSV Files
    │
    ▼
AWS S3
    │
    ▼
Snowflake External Stage
    │
    ▼
COPY INTO
    │
    ▼
Bronze Layer
    │
    ▼
dbt Silver Layer
    │
    ▼
dbt Gold Layer
    │
    ▼
Python + Plotly Dashboard
```

---

# 🛠️ Technology Stack

- AWS S3
- Snowflake
- dbt
- SQL
- Python
- Pandas
- Plotly
- Snowflake Connector for Python
- Git & GitHub

---

# 🚀 Key Features

- End-to-End ETL Pipeline
- Medallion Architecture (Bronze → Silver → Gold)
- Snowflake External Stage
- COPY INTO Data Loading
- Data Cleaning & Standardization
- dbt Models
- SCD Type 1 Implementation
- SCD Type 2 using dbt Snapshots
- Incremental Data Processing
- Star Schema (Fact & Dimension Modeling)
- Python-based Analytics
- Interactive Plotly Dashboard
- Environment Variable Management using `.env`

---

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
