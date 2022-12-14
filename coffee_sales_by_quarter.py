import pandas as pd

df = pd.read_csv('data.csv')

iq12010 = ['1/1/2010', '2/1/2010', '3/1/2010']
iq22010 = ['4/1/2010', '5/1/2010', '6/1/2010']
iq32010 = ['7/1/2010', '8/1/2010', '9/1/2010']
iq42010 = ['10/1/2010', '11/1/2010', '12/1/2010']

iq12011 = ['1/1/2011', '2/1/2011', '3/1/2011']
iq22011 = ['4/1/2011', '5/1/2011', '6/1/2011']
iq32011 = ['7/1/2011', '8/1/2011', '9/1/2011']
iq42011 = ['10/1/2011', '11/1/2011', '12/1/2011']

q12010 = df[df["date"].isin(iq12010)]
q22010 = df[df["date"].isin(iq22010)]
q32010 = df[df["date"].isin(iq32010)]
q42010 = df[df["date"].isin(iq42010)]

q12011 = df[df["date"].isin(iq12011)]
q22011 = df[df["date"].isin(iq22011)]
q32011 = df[df["date"].isin(iq32011)]
q42011 = df[df["date"].isin(iq42011)]


category = "Coffee"
value = "sales"

q12010cat = q12010[q12010["category"] == category].reset_index(drop=True)
q22010cat = q22010[q22010["category"] == category].reset_index(drop=True)
q32010cat = q32010[q32010["category"] == category].reset_index(drop=True)
q42010cat = q42010[q42010["category"] == category].reset_index(drop=True)

q12011cat = q12011[q12011["category"] == category].reset_index(drop=True)
q22011cat = q22011[q22011["category"] == category].reset_index(drop=True)
q32011cat = q32011[q32011["category"] == category].reset_index(drop=True)
q42011cat = q42011[q42011["category"] == category].reset_index(drop=True)


q12010catsales = q12010cat['sales']
q22010catsales = q22010cat['sales']
q32010catsales = q32010cat['sales']
q42010catsales = q42010cat['sales']

q12011catsales = q12011cat['sales']
q22011catsales = q22011cat['sales']
q32011catsales = q32011cat['sales']
q42011catsales = q42011cat['sales']

# print(q12010catsales)


coffee_by_quarter = pd.DataFrame({
	'2010 Q1': q12010catsales,
	'2010 Q2': q22010catsales,
	'2010 Q3': q32010catsales,
	'2010 Q4': q42010catsales,
	'2011 Q1': q12011catsales,
	'2011 Q2': q22011catsales,
	'2011 Q3': q32011catsales,
	'2011 Q4': q42011catsales
	})

# print(coffee_by_quarter)
coffee_by_quarter.to_csv('coffee_by_quarter.csv', index=False)





