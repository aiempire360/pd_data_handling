import pandas as pd

df = pd.read_csv('house_prices.csv')
df.fillna( 0, inplace=True)
df.fillna( {
   'Price':df.Price.mean()
},
   inplace=True)



print(df)

