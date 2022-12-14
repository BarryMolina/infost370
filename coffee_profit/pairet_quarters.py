import pandas as pd
from scipy import stats

df = pd.read_clipboard()

with open('paired_quarters_2011.txt', 'w') as f:
	f.write('var1\tvar2\tvar1_mean\tvar2_mean\tt\tp\n')
	# loop through all unique pairs of months
	for i in range(len(df.columns)):
		for j in range(i+1, len(df.columns)):
			var1 = df.columns[i]
			var2 = df.columns[j]
			var1_mean = df[var1].mean()
			var2_mean = df[var2].mean()
			(t, p) = stats.ttest_rel(df[var1], df[var2])
			significant = p < 0.05
			result = f"p {'<' if significant else '>'} 0.05"
			interpret = "Reject the null hypothesis, the means are not equal" if significant else "Fail to reject the null hypothesis, the means are equal"

			f.write(f'{var1}\t{var2}\t{var1_mean}\t{var2_mean}\t{t}\t{p}\t{result}\t{interpret}\n')
		f.write('\n')

		