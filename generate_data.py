import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Ensure output folder exists
os.makedirs("data", exist_ok=True)

# 1. Customers
customers = []
for i in range(1, 51):
    customers.append({
        "customer_id": i,
        "first_name": f"First{i}",
        "last_name": f"Last{i}",
        "email": f"user{i}@example.com",
        "phone": f"99999{i:05d}",
        "created_at": (datetime.now() - timedelta(days=random.randint(1, 1000))).strftime("%Y-%m-%d")
    })

pd.DataFrame(customers).to_csv("data/customers.csv", index=False)

# 2. Products
products = []
for i in range(1, 51):
    products.append({
        "product_id": i,
        "product_name": f"Product{i}",
        "category": random.choice(["Electronics", "Clothes", "Home", "Sports", "Beauty"]),
        "price": round(random.uniform(10, 500), 2)
    })

pd.DataFrame(products).to_csv("data/products.csv", index=False)

# 3. Orders
orders = []
for i in range(1, 51):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 50),
        "order_date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
        "total_amount": 0  # will update later
    })

pd.DataFrame(orders).to_csv("data/orders.csv", index=False)

# 4. Order Items
order_items = []
for i in range(1, 101):
    order_id = random.randint(1, 50)
    product_id = random.randint(1, 50)
    quantity = random.randint(1, 3)

    # Get product price
    price = products[product_id - 1]["price"]
    line_total = round(price * quantity, 2)

    order_items.append({
        "item_id": i,
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity,
        "line_total": line_total
    })

pd.DataFrame(order_items).to_csv("data/order_items.csv", index=False)

# 5. Payments
payments = []
for i in range(1, 51):
    payments.append({
        "payment_id": i,
        "order_id": i,
        "payment_date": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
        "payment_method": random.choice(["Card", "UPI", "Wallet"]),
        "amount": round(random.uniform(20, 700), 2)
    })

pd.DataFrame(payments).to_csv("data/payments.csv", index=False)

print("All 5 CSV files created successfully in the 'data' folder!")