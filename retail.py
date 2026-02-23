import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root123",  
    database="RetailDB"
)


df = pd.read_sql("SELECT * FROM Sales", conn)

df['Date'] = pd.to_datetime(df['Date'])
df['Units_Sold'] = df['Units_Sold'].astype(int)
df['Unit_Price'] = df['Unit_Price'].astype(float)
df['Revenue'] = df['Revenue'].astype(float)

category_revenue = df.groupby('Product_Category')['Revenue'].sum().reset_index()
print("Revenue by Category:\n", category_revenue)

top_products = df.groupby('Product_Name')['Revenue'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products:\n", top_products)

monthly_trend = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum()
print("\nMonthly Revenue Trend:\n", monthly_trend)

region_sales = df.groupby('Region')['Revenue'].sum()
print("\nRevenue by Region:\n", region_sales)