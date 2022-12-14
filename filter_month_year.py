import pandas as pd

df = pd.read_csv('data.csv')

profit_2010 = df[df["date"].str.contains("2010")].reset_index(drop=True).drop(columns=["sales", "region", "caffeination"])
profit_2011 = df[df["date"].str.contains("2011")].reset_index(drop=True).drop(columns=["sales", "region", "caffeination"])

profit_2010['date'] = profit_2010['date'].str[:-5]
profit_2011['date'] = profit_2011['date'].str[:-5]


print(profit_2010)
print(profit_2011)

merged = pd.merge(profit_2010, profit_2011, on=['date', 'state', 'category', 'type'], suffixes=['_2010', '_2011'])
ordered = merged[['date', 'state', 'category', 'type', 'profit_2010', 'profit_2011']]
print(ordered)
# profit_by_year = pd.DataFrame({
# 	'2010': profit_2010,
# 	'2011': profit_2011,
# })

# print(profit_by_year)
with pd.ExcelWriter('profit_by_year.xlsx') as writer:
	ordered.to_excel(writer, sheet_name='profit', index=False)

# print(profit_2010)
# print(profit_2011)