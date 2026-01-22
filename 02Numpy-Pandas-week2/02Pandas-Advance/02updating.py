import pandas as pd

data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack' ,'Kathy', 'Leo', 'Mona'],
	'Age': [24, 27, 22, 32, 29, 23, 31, 28, 26, 30, 25, 34, 21],
	"Salary": [50000, 54000, 58000, 60000, 62000, 51000, 59000, 61000, 63000, 65000, 52000, 64000, 57000],
    "Department": ['HR', 'Finance', 'IT', 'Marketing', 'IT', 'HR', 'Finance', 'IT', 'Marketing', 'Finance', 'HR', 'IT', 'Marketing'],
    "PerformanceScore": [85, 90, 88, 92, 87, 80, 91, 89, 93, 86, 84, 95, 83]
}

df = pd.DataFrame(data)
print(df)


# .loc[]
# df.loc[row_indexer, "col_indexer"] = new_value
df.loc[0, "Salary"] = 60000
print(df)