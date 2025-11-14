import sqlite3
import pandas as pd

conn = sqlite3.connect("ecom.db")

query = """
SELECT 
    o.order_id,
    u.user_name,
    u.email,
    p.product_name,
    oi.quantity,
    oi.price,
    o.order_date,
    pay.payment_method,
    pay.amount
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN payments pay ON o.order_id = pay.order_id
LIMIT 20;
"""

df = pd.read_sql_query(query, conn)
print(df)

conn.close()