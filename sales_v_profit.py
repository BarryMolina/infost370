import pandas as pd

df = pd.read_csv('data.csv')

coffee = df[df['category'] == 'Coffee'].reset_index(drop=True)
# drop everything but sales and profit
coffee = coffee.drop(columns=['region', 'caffeination', 'date', 'state', 'category', 'type'])
# print(coffee)

with pd.ExcelWriter(f'coffee.xlsx') as writer:
	coffee.to_excel(writer, sheet_name='coffee', index=False)