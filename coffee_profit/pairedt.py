import pandas as pd
from scipy import stats

df = pd.read_csv('coffee_profit_months.csv')

jan = df['profit_jan']
aug = df['profit_aug']

(t, p) = stats.ttest_rel(jan, aug)



with open('coffee_pairedt.txt', 'w') as f:
	f.write('var1\tvar2\tt\tp\n')
	# loop through all unique pairs of months
	for i in range(len(df.columns)):
		for j in range(i+1, len(df.columns)):
			var1 = df.columns[i]
			var2 = df.columns[j]
			(t, p) = stats.ttest_rel(df[var1], df[var2])
			significant = p < 0.05
			result = f"p {'<' if significant else '>'} 0.05"
			interpret = "Reject the null hypothesis, the means are not equal" if significant else "Fail to reject the null hypothesis, the means are equal"

			f.write(f'{var1}\t{var2}\t{t}\t{p}\t{result}\t{interpret}\n')
		f.write('\n')

		