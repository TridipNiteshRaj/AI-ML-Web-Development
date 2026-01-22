import pandas as pd

data = {
	'Name': ['Alice', 'None', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack' ,'Kathy', 'Leo', 'Mona'],
	'Age': [24, None, 22, 32, 29, 23, 31, 28, 26, 30, 25, 34, 21],
	'Salary': [50000, 54000, None, 60000, 62000, 51000, 59000, 61000, 63000, 65000, 52000, 64000, 57000],
    "Department": ['HR', 'Finance', 'None', 'Marketing', 'IT', 'HR', 'Finance', 'IT', 'Marketing', 'Finance', 'HR', 'IT', 'Marketing'],
    "PerformanceScore": [85, 90, None, 92, 87, 80, 91, 89, 93, 86, 84, 95, 83]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull().sum())