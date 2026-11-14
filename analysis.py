import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

df["Revenue"] = df["Quantity"] * df["Price"]

# Product-wise chart
product_sales = df.groupby("Product")["Revenue"].sum()

plt.figure(figsize=(8, 5))
plt.bar(product_sales.index, product_sales.values)
plt.title("Product Wise Sales")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Region-wise chart
region_sales = df.groupby("Region")["Revenue"].sum()

plt.figure(figsize=(8, 5))
plt.bar(region_sales.index, region_sales.values)
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

print("Sales Analysis Completed!")