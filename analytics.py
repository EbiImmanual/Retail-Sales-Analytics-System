import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
# Load dataset
df = pd.read_csv("sales_data.csv", encoding='latin1')

# Display first 5 rows
print(df.head())

print("\n========================")

# Total sales
total_sales = df['Sales'].sum()

print("Total Sales =", total_sales)

# Total profit
total_profit = df['Profit'].sum()

print("Total Profit =", total_profit)

# Average sales
average_sales = df['Sales'].mean()

print("Average Sales =", average_sales)

# Highest sale
highest_sale = df['Sales'].max()

print("Highest Sale =", highest_sale)

# Lowest sale
lowest_sale = df['Sales'].min()

print("Lowest Sale =", lowest_sale)

print("\n========================")
print("CATEGORY-WISE SALES")

category_sales = df.groupby('Category')['Sales'].sum()

print(category_sales)
print("\n========================")

best_category = category_sales.idxmax()

print("Best Performing Category =", best_category)

print("\n========================")
print("REGION-WISE SALES")

region_sales = df.groupby('Region')['Sales'].sum()

print(region_sales)

print("\n========================")

best_region = region_sales.idxmax()

print("Best Performing Region =", best_region)

print("\n========================")
print("TOP 10 SELLING PRODUCTS")

top_products = df.groupby('Product Name')['Sales'].sum()

top_products = top_products.sort_values(ascending=False)

print(top_products.head(10))

print("\nGenerating Category Sales Chart...")

category_sales.plot(kind='bar')

plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.savefig("charts/category_sales.png")
plt.show()
print("\nGenerating Region Sales Chart...")

region_sales.plot(kind='bar')

plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.savefig("charts/region_sales.png")
plt.show()
# Convert order date into proper date format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract month
df['Month'] = df['Order Date'].dt.month

# Group sales by month
monthly_sales = df.groupby('Month')['Sales'].sum()

print("\n========================")
print("MONTHLY SALES")

print(monthly_sales)

print("\nGenerating Monthly Sales Trend Graph...")

monthly_sales.plot(kind='line', marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("charts/monthly_sales.png")
plt.show()


print("\n========================")
print("CREATING SQL DATABASE")

conn = sqlite3.connect("sales.db")

print("Database Created Successfully")

# Store dataframe into SQL table
df.to_sql("sales", conn, if_exists='replace', index=False)

print("Data inserted into SQL database successfully")

print("\n========================")
print("SQL QUERY RESULTS")

query = """
SELECT Region, SUM(Sales) AS TotalSales
FROM sales
GROUP BY Region
ORDER BY TotalSales DESC
"""

sql_result = pd.read_sql(query, conn)

print(sql_result)

print("\n========================")
print("TOP 5 PRODUCTS USING SQL")

query2 = """
SELECT "Product Name", SUM(Sales) AS TotalSales
FROM sales
GROUP BY "Product Name"
ORDER BY TotalSales DESC
LIMIT 5
"""

top_products_sql = pd.read_sql(query2, conn)

print(top_products_sql)

print("\n========================")
print("FINAL BUSINESS INSIGHTS")

# Best region
best_region = region_sales.idxmax()
print("Best Performing Region:", best_region)

# Best category
best_category = category_sales.idxmax()
print("Best Performing Category:", best_category)

# Highest selling product
top_product = top_products.idxmax()
print("Highest Selling Product:", top_product)

# Total revenue
print("Total Revenue Generated:", total_sales)

# Total Profit
print("Total Profit Generated:", total_profit)