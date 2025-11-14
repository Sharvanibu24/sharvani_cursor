import sqlite3
import pandas as pd
import os

# Create database connection
conn = sqlite3.connect("ecommerce.db")

# Folder where CSVs are stored
folder = "data"

# Read and insert each CSV file
tables = {
    "users": "users.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "payments": "payments.csv"
}

for table, file in tables.items():
    df = pd.read_csv(os.path.join(folder, file))
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"Inserted → {table}")

print("\nAll tables successfully loaded into ecommerce.db!")

conn.close()