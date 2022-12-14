import pandas as pd

df = pd.read_csv('data.csv')


profit_2010 = df[df["date"].str.contains("2010")].reset_index(drop=True).drop(columns=["sales", "region", "caffeination"])
profit_2011 = df[df["date"].str.contains("2011")].reset_index(drop=True).drop(columns=["sales", "region", "caffeination"])

profit_2010['date'] = profit_2010['date'].str[:-5]
profit_2011['date'] = profit_2011['date'].str[:-5]

dates = profit_2010['date'].unique()

# print(dates)

def filter_col_by_date(date, col, col_value, df):
	by_date = df[df['date'] == date].reset_index(drop=True)
	col_by_date = by_date[by_date[col] == col_value].reset_index(drop=True)
	return col_by_date.drop(columns=[col, 'date'])
	
# jan_espresso = filter_col_by_date('1/1', 'category', 'Espresso', profit_2010)
# print(jan_espresso)
# espresso_profits_jan = jan_espresso['profit']
# espresso_profits_jan.name = '1/1'
# print(espresso_profits_jan)

def filter_category(category, df):
	on = ['state', 'type']
	jan = filter_col_by_date('1/1', 'category', category, df)
	feb = filter_col_by_date('2/1', 'category', category, df)
	mar = filter_col_by_date('3/1', 'category', category, df)
	apr = filter_col_by_date('4/1', 'category', category, df)
	may = filter_col_by_date('5/1', 'category', category, df)
	jun = filter_col_by_date('6/1', 'category', category, df)
	jul = filter_col_by_date('7/1', 'category', category, df)
	aug = filter_col_by_date('8/1', 'category', category, df)
	sep = filter_col_by_date('9/1', 'category', category, df)
	oct = filter_col_by_date('10/1', 'category', category, df)
	nov = filter_col_by_date('11/1', 'category', category, df)
	dec = filter_col_by_date('12/1', 'category', category, df)

	merged = jan.merge(feb, on=on, suffixes=['_jan', '_feb']).merge(mar, on=on, suffixes=['', '_mar']).merge(apr, on=on, suffixes=['', '_apr']).merge(may, on=on, suffixes=['', '_may']).merge(jun, on=on, suffixes=['', '_jun']).merge(jul, on=on, suffixes=['', '_jul']).merge(aug, on=on, suffixes=['', '_aug']).merge(sep, on=on, suffixes=['', '_sep']).merge(oct, on=on, suffixes=['', '_oct']).merge(nov, on=on, suffixes=['', '_nov']).merge(dec, on=on, suffixes=['', '_dec'])
	return merged

# espresso = filter_category('Espresso', profit_2010)
# print(espresso)

def write_to_excel(df, filename):
	with pd.ExcelWriter(filename) as writer:
		for category in df['category'].unique():
			filtered = filter_category(category, df)
			filtered.to_excel(writer, sheet_name=category, index=False)

write_to_excel(profit_2010, 'profit_by_month_category.xlsx')



# for date in dates:
# 	print(filter_col_by_date(date, 'category', 'Espresso', profit_2010))

