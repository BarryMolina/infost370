import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

types = ['Columbian', 'Decaf Irish Cream', 'Amaretto']

def get_type_profit(df, type):
	col = df[df["type"] == type].reset_index(drop=True)["profit"]
	col.name = type
	return col

def concat_types(df):
	type_profits = [get_type_profit(df, type) for type in types]
	return pd.concat(type_profits, axis=1)

# print(concat_types(df))
with pd.ExcelWriter('profit_by_type.xlsx') as writer:
	concat_types(df).to_excel(writer, sheet_name='profit type', index=False)


def normality():
	with open('coffee_type_normality.txt', 'w') as f:
		f.write('2010\tW\tP\n')
		for type in types:
			x = get_type_profit(df, type)
			(w, p) = stats.shapiro(x)
			f.write(f'{type}\t{w}\t{p}\n')


def hist():
	for type in types:
		plt.hist(get_type_profit(df, type), bins=20)
		plt.xlabel('Profit')
		plt.ylabel('Frequency')
		plt.title(f'{type} 2010')
		plt.savefig(f'type_year_hist/coffee_{type}_2010_hist.png')
		plt.clf()

# normality()
# hist()
	