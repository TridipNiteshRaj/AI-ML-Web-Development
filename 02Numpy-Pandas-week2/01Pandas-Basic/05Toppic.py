""" 
1- how big is the dataframe
2- what is the mean, min, max, std, etc of each column

shape and columns description
 
"""

import pandas as pd

data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
	'Age': [24, 27, 22, 32, 29],
	'Salary': [50000, 54000, 58000, 60000, 62000]
}
df = pd.DataFrame(data)
print(" Simple DataFrame:")
print(df)

print(f'shape: {df.shape}')
print(f'column names: {df.columns}')

"""  
10000,20
4,6
"""