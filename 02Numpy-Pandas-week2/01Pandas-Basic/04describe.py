import pandas as pd

data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
	'Age': [24, 27, 22, 32, 29],
	'Salary': [50000, 54000, 58000, 60000, 62000]
}
df = pd.DataFrame(data)
print(" Simple DataFrame:")
print(df)


print('Description of DataFrame:')
print(df.describe())