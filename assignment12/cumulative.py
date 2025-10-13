import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# connect to the DB
conn = sqlite3.connect("../db/lesson.db")

## SQL 
query = """
SELECT o.order_id, 
       SUM(l.quantity * p.price) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# to load the results into a dataframe 
df = pd.read_sql_query(query, conn)
conn.close()

# Calculate cumulative revenue using cumsum() for better performance
df['cumulative'] = df['total_price'].cumsum()


## Plot cumulative revenue vs. order_id
df.plot(
    x="order_id",
    y="cumulative",
    kind="line",
    title="Cumulative Revenue by Order",
    color=["blue"]
)

plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.tight_layout()
plt.show()
