#sorting data in pandas
#SORTING DATA 1 column  sort_values()
#df.sort_values(by='column_name', ascending=True/False, inplace=True)

#SORTING DATA multiple columns
#df.sort_values(by=['col1', 'col2'], ascending=[True, False], inplace=True)

import pandas as pd

data = {
	"Name": ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
	"Age": [29, 27, 22, 32, 29],
	"Salary": [50000, 54000, 58000, 60000, 62000],
}

df = pd.DataFrame(data)
df.sort_values(by='Age', ascending=True, inplace=True)
print("Sorted by Age (Ascending):")
print(df)