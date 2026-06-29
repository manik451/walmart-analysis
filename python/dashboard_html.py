import os
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import plotly.express as px

load_dotenv()
os.makedirs("output", exist_ok=True)

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
    role=os.getenv("SNOWFLAKE_ROLE")
)

query = """
SELECT
    STORE_ID,
    DEPT_ID,
    DATE_ID,
    STORE_WEEKLY_SALES,
    FUEL_PRICE,
    STORE_TEMPERATURE,
    UNEMPLOYMENT,
    CPI,
    MARKDOWN1,
    MARKDOWN2,
    MARKDOWN3,
    MARKDOWN4,
    MARKDOWN5
FROM WALMART_FACT_TABLE
"""

df = pd.read_sql(query, conn)
conn.close()

total_sales = df["STORE_WEEKLY_SALES"].sum()
total_stores = df["STORE_ID"].nunique()
total_departments = df["DEPT_ID"].nunique()
avg_weekly_sales = df["STORE_WEEKLY_SALES"].mean()

top_stores = (
    df.groupby("STORE_ID", as_index=False)["STORE_WEEKLY_SALES"]
    .sum()
    .sort_values("STORE_WEEKLY_SALES", ascending=False)
    .head(10)
)

top_departments = (
    df.groupby("DEPT_ID", as_index=False)["STORE_WEEKLY_SALES"]
    .sum()
    .sort_values("STORE_WEEKLY_SALES", ascending=False)
    .head(10)
)

df["TOTAL_MARKDOWN"] = (
    df["MARKDOWN1"]
    + df["MARKDOWN2"]
    + df["MARKDOWN3"]
    + df["MARKDOWN4"]
    + df["MARKDOWN5"]
)

markdown_by_store = (
    df.groupby("STORE_ID", as_index=False)[["TOTAL_MARKDOWN", "STORE_WEEKLY_SALES"]]
    .sum()
    .sort_values("STORE_WEEKLY_SALES", ascending=False)
    .head(10)
)

fig1 = px.bar(top_stores, x="STORE_ID", y="STORE_WEEKLY_SALES", title="Top 10 Stores by Sales")
fig2 = px.bar(top_departments, x="DEPT_ID", y="STORE_WEEKLY_SALES", title="Top 10 Departments by Sales")
fig3 = px.scatter(df, x="FUEL_PRICE", y="STORE_WEEKLY_SALES", title="Fuel Price vs Weekly Sales")
fig4 = px.scatter(df, x="STORE_TEMPERATURE", y="STORE_WEEKLY_SALES", title="Temperature vs Weekly Sales")
fig5 = px.scatter(df, x="CPI", y="STORE_WEEKLY_SALES", title="CPI vs Weekly Sales")
fig6 = px.bar(markdown_by_store, x="STORE_ID", y="TOTAL_MARKDOWN", title="Total Markdown by Top Stores")
fig7 = px.histogram(df, x="STORE_WEEKLY_SALES", title="Weekly Sales Distribution")

html = f"""
<html>
<head>
    <title>Walmart Sales Dashboard</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f7f9fc;
        }}
        h1 {{
            color: #1f2937;
        }}
        .kpi-container {{
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
        }}
        .kpi-card {{
            background: white;
            padding: 20px;
            border-radius: 12px;
            width: 24%;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}
        .kpi-title {{
            color: #6b7280;
            font-size: 14px;
        }}
        .kpi-value {{
            color: #111827;
            font-size: 24px;
            font-weight: bold;
        }}
        .chart-card {{
            background: white;
            margin-bottom: 30px;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}
    </style>
</head>
<body>

<h1>Walmart Sales Analytics Dashboard</h1>
<p>This dashboard analyzes Walmart Gold-layer data from Snowflake using Python and Plotly.</p>

<div class="kpi-container">
    <div class="kpi-card">
        <div class="kpi-title">Total Sales</div>
        <div class="kpi-value">${total_sales:,.0f}</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-title">Total Stores</div>
        <div class="kpi-value">{total_stores}</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-title">Total Departments</div>
        <div class="kpi-value">{total_departments}</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-title">Avg Weekly Sales</div>
        <div class="kpi-value">${avg_weekly_sales:,.0f}</div>
    </div>
</div>

<div class="chart-card">{fig1.to_html(full_html=False, include_plotlyjs='cdn')}</div>
<div class="chart-card">{fig2.to_html(full_html=False, include_plotlyjs=False)}</div>
<div class="chart-card">{fig3.to_html(full_html=False, include_plotlyjs=False)}</div>
<div class="chart-card">{fig4.to_html(full_html=False, include_plotlyjs=False)}</div>
<div class="chart-card">{fig5.to_html(full_html=False, include_plotlyjs=False)}</div>
<div class="chart-card">{fig6.to_html(full_html=False, include_plotlyjs=False)}</div>
<div class="chart-card">{fig7.to_html(full_html=False, include_plotlyjs=False)}</div>

</body>
</html>
"""

with open("output/walmart_sales_dashboard.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Enhanced dashboard saved to output/walmart_sales_dashboard.html")