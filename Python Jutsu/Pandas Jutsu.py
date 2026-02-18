#%%
import pandas as pd
import numpy as np

# Create sample dataset
# %%
data = {
    "OrderID": [1001, 1002, 1003, 1004, 1005, 1006],
    "Customer": ["Alice", "Bob", "Alice", "David", "Bob", "Emma"],
    "City": ["New York", "Los Angeles", "New York", "Chicago", "Los Angeles", "Chicago"],
    "Sales": [250, 150, 400, 300, 200, 500],
    "Quantity": [2, 1, 4, 3, 2, 5],
    "OrderDate": pd.to_datetime([
        "2024-01-10", "2024-01-12", "2024-02-05",
        "2024-02-20", "2024-03-15", "2024-03-25"
    ])
}
# %%
df = pd.DataFrame(data)
print(df)

# %%
# Stealth Overview Functions
# Instant data scans from within the shadow
df.head()        # First 5 rows
df.tail()        # Last 5 rows
df.shape         # Rows & columns
df.info()        # Data types & null values
df.describe()    # Statistical summary
df.columns       # Column names
# %%
# Ninja Split
# Vanish unnecessary parts, keep what matters.

# Filter rows
df[df["Sales"] > 300]

# Multiple conditions
df[(df["City"] == "New York") & (df["Sales"] > 200)]

# Cleaner filtering using query()
df.query("Sales > 300 and City == 'Chicago'")
# %%
# Column Selection
# Keen eye for the elements that matter

# Multiple columns
df[["Customer", "Sales"]]

# Select numeric columns only
df.select_dtypes(include="number")
# %%
# Elemental Spawn
# New features appear silently in your data frame.
# Simple calculation
df["RevenuePerItem"] = df["Sales"] / df["Quantity"]

# Using apply()
df["SalesCategory"] = df["Sales"].apply(
    lambda x: "High" if x > 300 else "Low"
)
#%%
# Ninja Assemble
# Rally rows into their secret clans
# Total sales per city
df.groupby("City")["Sales"].sum()

# Multiple aggregations
df.groupby("Customer").agg({
    "Sales": ["sum", "mean"],
    "Quantity": "sum"
})
#%%
# Shadow Order
# Silently arrange everything by rank
# Sort values
df.sort_values(by="Sales", ascending=False)

# Rank sales
df["SalesRank"] = df["Sales"].rank(ascending=False)
#%%
# Ninja Burst
# Sudden surge of unstoppable speed
# Convert object to category for memory optimization
df["City"] = df["City"].astype("category")
#%%
# Shadow Dispatch
# Deliver your data silently and safely.
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)