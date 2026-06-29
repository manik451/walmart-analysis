import os
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import plotly.express as px

load_dotenv()

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
    SUM(STORE_WEEKLY_SALES) AS TOTAL_SALES
FROM WALMART_FACT_TABLE
GROUP BY STORE_ID
ORDER BY TOTAL_SALES DESC
"""

# Read data into a DataFrame
df = pd.read_sql(query, conn)

# Print the data (optional)
print(df)

# Close the connection
conn.close()

# -----------------------------
# Create the chart
# -----------------------------
fig = px.bar(
    df,
    x="STORE_ID",
    y="TOTAL_SALES",
    title="Total Sales by Store"
)

# Display the chart
import os

os.makedirs("output", exist_ok=True)

fig.write_html("output/total_sales_by_store.html")
print("✅ Chart saved to output/total_sales_by_store.html")