import os
import snowflake.connector
from dotenv import load_dotenv

# Load values from .env
load_dotenv()

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA"),
    role=os.getenv("SNOWFLAKE_ROLE")
)

print("✅ Successfully connected to Snowflake!")

cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM WALMART_FACT_TABLE
""")

result = cursor.fetchone()

print(f"Total rows in WALMART_FACT_TABLE: {result[0]}")

cursor.close()
conn.close()

print("Connection closed.")