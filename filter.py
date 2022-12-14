import pandas as pd

df = pd.read_csv('data.csv')

iq1 = ['1/1/2010', '2/1/2010', '3/1/2010', '1/1/2011', '2/1/2011', '3/1/2011']
iq2 = ['4/1/2010', '5/1/2010', '6/1/2010', '4/1/2011', '5/1/2011', '6/1/2011']
iq3 = ['7/1/2010', '8/1/2010', '9/1/2010', '7/1/2011', '8/1/2011', '9/1/2011']
iq4 = ['10/1/2010', '11/1/2010', '12/1/2010', '10/1/2011', '11/1/2011', '12/1/2011']

q1 = df[df["date"].isin(iq1)]
q2 = df[df["date"].isin(iq2)]
q3 = df[df["date"].isin(iq3)]
q4 = df[df["date"].isin(iq4)]

def filter_quarter_value_by_column(quarter, column, column_value, value):
	return quarter[quarter[column] == column_value][value].reset_index(drop=True)

def filter_quarters(column, column_value, value):
	return pd.DataFrame({
		'Q1': filter_quarter_value_by_column(q1, column, column_value, value),
		'Q2': filter_quarter_value_by_column(q2, column, column_value, value),
		'Q3': filter_quarter_value_by_column(q3, column, column_value, value),
		'Q4': filter_quarter_value_by_column(q4, column, column_value, value),
	})

def filter_value_by_column(column, column_value, value):
	s =  df[df[column] == column_value][value].reset_index(drop=True)
	s.name = column_value
	return s

def get_categories():
	return df['category'].unique()

def get_category_types(category):
	return df[df['category'] == category]['type'].unique()

def filter_value_by_category_type(category, value):
	return pd.DataFrame([filter_value_by_column('type', t, value) for t in get_category_types(category)], index=get_category_types(category)).T



def filter_sales_by_categories():
	return pd.DataFrame([filter_value_by_column('category', cat, 'sales') for cat in df['category'].unique()], index=df['category'].unique()).T

def filter_sales_by_type():
	return pd.DataFrame([filter_value_by_column('type', t, 'sales') for t in df['type'].unique()], index=df['type'].unique()).T

def filter_profits_by_categories():
	return pd.DataFrame([filter_value_by_column('category', cat, 'profit') for cat in df['category'].unique()], index=df['category'].unique()).T

def filter_profits_by_type():
	return pd.DataFrame([filter_value_by_column('type', t, 'profit') for t in df['type'].unique()], index=df['type'].unique()).T

# def filter_sales_by_categories2():
# 	return pd.concat([filter_value_by_column('category', cat, 'sales') for cat in df['category'].unique()], axis=1)

def write_to_excel():
	with pd.ExcelWriter('sales_profit_by_type_and_category.xlsx') as writer:
		filter_sales_by_categories().to_excel(writer, sheet_name='sales_by_category', index=False)
		filter_profits_by_categories().to_excel(writer, sheet_name='profits_by_category', index=False)
		for cat in get_categories():
			filter_value_by_category_type(cat, 'sales').to_excel(writer, sheet_name='sales_by_type_' + cat, index=False)
			filter_value_by_category_type(cat, 'profit').to_excel(writer, sheet_name='profits_by_type_' + cat, index=False)

write_to_excel()
