import pandas as pd

iq1 = ['1/1', '2/1', '3/1']
iq2 = ['4/1', '5/1', '6/1']
iq3 = ['7/1', '8/1', '9/1']
iq4 = ['10/1', '11/1', '12/1']

quarters = [iq1, iq2, iq3, iq4]

df = pd.read_csv('data.csv')

df = df[df['category'] == 'Coffee'].reset_index(drop=True).drop(columns=['category'])

profit_2010 = df[df["date"].str.contains("2010")].reset_index(drop=True).drop(columns=["sales", "region", "caffeination"])
profit_2011 = df[df["date"].str.contains("2011")].reset_index(drop=True).drop(columns=["sales", "region", "caffeination"])

profit_2010['date'] = profit_2010['date'].str[:-5]
profit_2011['date'] = profit_2011['date'].str[:-5]

# print(profit_2010)
# print(profit_2011)

def get_quarter(df, quarter):
	q = df[df['date'].isin(quarter)].reset_index(drop=True)
	# add the index of the quarter to the dataframe
	q['quarter_idx'] = q['date'].apply(lambda x: quarter.index(x))
	# drop the date column
	q = q.drop(columns=['date'])
	return q
	# return df[df['date'].isin(quarter)].reset_index(drop=True)

def merge_quarters(df):
	q1 = get_quarter(df, iq1)
	q2 = get_quarter(df, iq2)
	q3 = get_quarter(df, iq3)
	q4 = get_quarter(df, iq4)

	merged = pd.merge(q1, q2, on=['state', 'type', 'quarter_idx'], suffixes=['_q1', '_q2'])
	merged = pd.merge(merged, q3, on=['state', 'type', 'quarter_idx'], suffixes=['', '_q3'])
	merged = pd.merge(merged, q4, on=['state', 'type', 'quarter_idx'], suffixes=['_q3', '_q4'])

	# add index for two-factor ANOVA
	merged['index'] = merged.index

	ordered = merged[['quarter_idx', 'state', 'type', 'index', 'profit_q1', 'profit_q2', 'profit_q3', 'profit_q4']]

	return ordered

def write_excel():
	q_2010 = merge_quarters(profit_2010)
	q_2011 = merge_quarters(profit_2011)
	with pd.ExcelWriter('quarter_year.xlsx') as writer:
		q_2010.to_excel(writer, sheet_name='profit quarter 2010', index=False)
		q_2011.to_excel(writer, sheet_name='profit quarter 2011', index=False)

write_excel()
# print(get_quarter(profit_2010, iq1))
# print(merge_quarters(profit_2010))
