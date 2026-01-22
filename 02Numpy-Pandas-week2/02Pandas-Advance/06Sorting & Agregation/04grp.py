import pandas as pd

data = {
	"Name": ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
	"Age": [29, 27, 22, 32, 29],
	"Salary": [50000, 54000, 58000, 60000, 62000],
}

df = pd.DataFrame(data)
grouped = df.groupby('Age').agg({'Salary': ['sum', 'mean', 'count']})
print(grouped)

"""
dr.grouped("Age")
age = 22 > [45000] =
age = 27 > [54000]
age = 29 > [112000]

[salary].sum()
age = 22 > [48000] =
age = 28 [50000,480000] = 530000
age = 30 [60000,62000] = 122000"""