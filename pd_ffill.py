import pandas as pd

df = pd.read_csv("house_prices.csv")

df.ffill(inplace=True)

print(df)