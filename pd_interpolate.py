import pandas as pd

df = pd.read_csv("house_prices.csv")

# Numeric columns interpolation
numeric_cols = df.select_dtypes(include="number").columns

df[numeric_cols] = df[numeric_cols].interpolate()

print(df)
print(df.dtypes)