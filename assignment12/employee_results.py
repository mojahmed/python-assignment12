import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# SQL query to calculate total revenue per employee
query = """
SELECT last_name, 
       SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

# Load the data into a DataFrame
employee_results = pd.read_sql_query(query, conn)

# Cls the connection
conn.close()

# Plot revenue by employee
employee_results.plot(
    x="last_name",
    y="revenue",
    kind="bar",
color=["green"],
    title="Total Revenue by Employee"
)

plt.xlabel("Employee Last Name")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()
