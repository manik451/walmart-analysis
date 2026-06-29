import os
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import streamlit as st
import plotly.express as px

load_dotenv()

st.set_page_config(page_title="Walmart Sales Dashboard", layout="wide")

@st.cache_data
def load_data():
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
    return df

df = load_data()

st.title("Walmart Sales Analytics Dashboard")

total_sales = df["STORE_WEEKLY_SALES"].sum()
total_stores = df["STORE_ID"].nunique()
avg_sales = df["STORE_WEEKLY_SALES"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Stores", total_stores)
col3.metric("Average Weekly Sales", f"${avg_sales:,.0f}")

st.divider()

top_stores = (
    df.groupby("STORE_ID", as_index=False)["STORE_WEEKLY_SALES"]
    .sum()
    .sort_values("STORE_WEEKLY_SALES", ascending=False)
    .head(10)
)

fig1 = px.bar(
    top_stores,
    x="STORE_ID",
    y="STORE_WEEKLY_SALES",
    title="Top 10 Stores by Sales"
)

st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(
    df,
    x="FUEL_PRICE",
    y="STORE_WEEKLY_SALES",
    title="Fuel Price vs Weekly Sales"
)

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(
    df,
    x="STORE_TEMPERATURE",
    y="STORE_WEEKLY_SALES",
    title="Temperature vs Weekly Sales"
)

st.plotly_chart(fig3, use_container_width=True)