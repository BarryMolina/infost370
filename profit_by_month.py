import pandas as pd

df = pd.read_csv('data.csv')

profit_2010 = df[df["date"].str.contains("2010")].reset_index(drop=True).drop(columns=["sales", "region", "caffeination"])
profit_2011 = df[df["date"].str.contains("2011")].reset_index(drop=True).drop(columns=["sales", "region", "caffeination"])

profit_2010['date'] = profit_2010['date'].str[:-5]
profit_2011['date'] = profit_2011['date'].str[:-5]

# print(profit_2010)
# print(profit_2011)

def filter_by_date(date, df):
	by_date = df[df['date'] == date].reset_index(drop=True)
	return by_date.drop(columns=['date'])

# jan_2010 = filter_by_date('1/1', profit_2010)

# print(jan_2010)

def join_dates(df):
	jan = filter_by_date('1/1', df)
	feb = filter_by_date('2/1', df)
	mar = filter_by_date('3/1', df)
	apr = filter_by_date('4/1', df)
	may = filter_by_date('5/1', df)
	jun = filter_by_date('6/1', df)
	jul = filter_by_date('7/1', df)
	aug = filter_by_date('8/1', df)
	sep = filter_by_date('9/1', df)
	oct = filter_by_date('10/1', df)
	nov = filter_by_date('11/1', df)
	dec = filter_by_date('12/1', df)
	merged = pd.merge(jan, feb, on=['state', 'category', 'type'], suffixes=['_jan', '_feb'])
	merged = pd.merge(merged, mar, on=['state', 'category', 'type'], suffixes=['', '_mar'])
	merged = pd.merge(merged, apr, on=['state', 'category', 'type'], suffixes=['', '_apr'])
	merged = pd.merge(merged, may, on=['state', 'category', 'type'], suffixes=['', '_may'])
	merged = pd.merge(merged, jun, on=['state', 'category', 'type'], suffixes=['', '_jun'])
	merged = pd.merge(merged, jul, on=['state', 'category', 'type'], suffixes=['', '_jul'])
	merged = pd.merge(merged, aug, on=['state', 'category', 'type'], suffixes=['', '_aug'])
	merged = pd.merge(merged, sep, on=['state', 'category', 'type'], suffixes=['', '_sep'])
	merged = pd.merge(merged, oct, on=['state', 'category', 'type'], suffixes=['', '_oct'])
	merged = pd.merge(merged, nov, on=['state', 'category', 'type'], suffixes=['', '_nov'])
	merged = pd.merge(merged, dec, on=['state', 'category', 'type'], suffixes=['', '_dec'])
	return merged

# print(join_dates(profit_2010))

def write_to_excel():
	months_2010 = join_dates(profit_2010)
	months_2011 = join_dates(profit_2011)
	with pd.ExcelWriter(f'profit_by_month.xlsx') as writer:
		months_2010.to_excel(writer, sheet_name='profit_by_month_2010', index=False)
		months_2011.to_excel(writer, sheet_name='profit_by_month_2011', index=False)

write_to_excel()