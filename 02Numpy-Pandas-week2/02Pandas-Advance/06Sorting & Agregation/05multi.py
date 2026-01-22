#multiple column grouping and aggregation in pandas
#df.groupby(['col1', 'col2']).agg({'value_column': ['sum',
import pandas as pd

data = {
	"Name": ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
	"Age": [29, 27, 22, 32, 29],
	"Salary": [50000, 54000, 58000, 60000, 62000],
}

df = pd.DataFrame(data)
grouped = df.groupby(['Age', 'Name'])["Salary"].sum()
print(grouped)