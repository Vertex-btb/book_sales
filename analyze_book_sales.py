import pandas as pd
df = pd.read_csv("book_sales.csv")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("book_sales.csv")

# Top 5 best-selling books
top_sellers = df.sort_values(by="sales", ascending=False).head(5)
print("Top 5 Best-Selling Books:\n", top_sellers)

# Genre with highest average sales
genre_avg_sales = df.groupby("genre")["sales"].mean().sort_values(ascending=False)
print("\nGenre with Highest Average Sales:\n", genre_avg_sales.index[0])

# Most profitable author
df["revenue"] = df["price"] * df["sales"]
author_revenue = df.groupby("author")["revenue"].sum().sort_values(ascending=False)
print("\nMost Profitable Author:\n", author_revenue.index[0])

# Scatter plot of price vs. sales
plt.scatter(df["price"], df["sales"])
plt.xlabel("Price")
plt.ylabel("Sales")
plt.title("Price vs. Sales")
plt.show()