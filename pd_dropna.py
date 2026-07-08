import pandas as pd

df = pd.read_csv("house_prices.csv")

df.dropna(inplace=True)

print(df)

