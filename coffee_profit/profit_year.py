import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df_2010 = df[df["date"].str.contains("2010")].reset_index(drop=True).drop(columns=["sales", "region", "caffeination"])
df_2011 = df[df["date"].str.contains("2011")].reset_index(drop=True).drop(columns=["sales", "region", "caffeination"])

df_2010['date'] = df_2010['date'].str[:-5]
df_2011['date'] = df_2011['date'].str[:-5]

coffee_2010 = df_2010[df_2010['category'] == 'Coffee'].reset_index(drop=True).drop(columns=['category'])
coffee_2011 = df_2011[df_2011['category'] == 'Coffee'].reset_index(drop=True).drop(columns=['category'])

dates = df_2010['date'].unique()

# print(df_2010)
# print(df_2011)

# print(coffee_2010)
# print(coffee_2011)

merged = coffee_2010.merge(coffee_2011, on=['state', 'type', 'date'], suffixes=('_2010', '_2011'))

# rearange columns
ordered = merged[['date', 'state', 'type', 'profit_2010', 'profit_2011']]

with pd.ExcelWriter('profit_year.xlsx') as writer:
	ordered.to_excel(writer, sheet_name='profit_year', index=False)

# print(ordered)