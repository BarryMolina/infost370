import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('coffee_profit_months.csv')

for month in df:
	plt.hist(df[month], bins=20)
	plt.xlabel('Profit')
	plt.ylabel('Frequency')
	plt.title(f'{month}')
	plt.savefig(f'coffee_profit/coffee_{month}_hist.png')
	plt.clf()


