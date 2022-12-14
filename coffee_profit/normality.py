import pandas as pd
from scipy import stats

df = pd.read_csv('coffee_profit_months.csv')

with open('coffee_normality.txt', 'w') as f:
	f.write('Month\tW\tP\n')
	for month in df:
		(w, p) = stats.shapiro(df[month])
		f.write(f'{month}\t{w}\t{p}\n')