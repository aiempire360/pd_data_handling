import pandas as pd

df = pd.read_csv("house_prices.csv")

df.bfill(inplace=True)

print(df)