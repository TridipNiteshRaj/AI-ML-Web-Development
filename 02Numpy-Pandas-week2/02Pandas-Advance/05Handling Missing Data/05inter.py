import pandas as pd
data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack' ,'Kathy', 'Leo', 'Mona'],
	'Age': [None, 27, 22, 32, 29, 23, 31, 28, 26, 30, 25, 34, 21],
	'Salary': [50000, None, 58000, 60000, 62000, 51000, 59000, 61000, 63000, 65000, 52000, 64000, 57000],
    "Department": ['HR', 'Finance', 'IT', 'Marketing', 'IT', 'HR', 'Finance', 'IT', 'Marketing', 'Finance', 'HR', 'IT', 'Marketing'],
    "PerformanceScore": [None, 90, 88, 92, 87, 80, 91, 89, 93, 86, 84, 95, 83]
}

df = pd.DataFrame(data)
print(df)

#linear, polynomial, time, etc.

df.interpolate(method= "linear", axis=0, inplace= True)
print(df)