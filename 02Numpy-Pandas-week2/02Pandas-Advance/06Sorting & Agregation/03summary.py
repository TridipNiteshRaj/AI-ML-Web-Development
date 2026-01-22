"""
Summary of Sorting and Aggregation in Pandas:
1. Sorting:
   - Single column: df.sort_values(by='column_name', ascending=True/False, inplace=True)
   - Multiple columns: df.sort_values(by=['col1', 'col2'], ascending=[True, False], inplace=True)

2. Aggregation:
   - Basic functions: df['column'].sum(), df['column'].mean(), df['column'].count()
   - Grouping: df.groupby('group_column').agg({'value_column': ['sum', 'mean']})
   - Custom aggregations: df.groupby('group_column')['value_column'].apply(custom_function)
"""

""" 
df["column_name"].mean()
df["column_name"].sum()
df["column_name"].count()
df["column_name"].min()
df["column_name"].max()
df["column_name"].std()
df["column_name"].var()
df["column_name"].median()
"""

import pandas as pd

data = {
	"Name": ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
	"Age": [29, 27, 22, 32, 29],
	"Salary": [50000, 54000, 58000, 60000, 62000],
}

df = pd.DataFrame(data)

avg_salary = df['Salary'].mean()
print(avg_salary)