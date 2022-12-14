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


def get_quarter_sales(quarter, category):
	value = "sales"
	quarter_cat = quarter[quarter["category"] == category].reset_index(drop=True)
	return quarter_cat[value]

category = "Espresso"
q1_espresso_sales = get_quarter_sales(q1, category)
q2_espresso_sales = get_quarter_sales(q2, category)
q3_espresso_sales = get_quarter_sales(q3, category)
q4_espresso_sales = get_quarter_sales(q4, category)

espresso_by_quarter = pd.DataFrame({
	'Q1': q1_espresso_sales,
	'Q2': q2_espresso_sales,
	'Q3': q3_espresso_sales,
	'Q4': q4_espresso_sales,
})

# print(espresso_by_quarter)
espresso_by_quarter.to_excel('infographic.xlsx', sheet_name='espresso', index=False)





