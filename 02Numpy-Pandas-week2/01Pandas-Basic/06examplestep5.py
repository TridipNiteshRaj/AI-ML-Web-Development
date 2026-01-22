import pandas as pd

data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
	'Age': [24, 27, 22, 32, 29],
	'Salary': [50000, 54000, 58000, 60000, 62000]
}
df = pd.DataFrame(data)


#display the dataframe
print(" Simple DataFrame:")
print(df)
print("Names (single column as Series):")
name =df['Name']
print(name)

#selecting multiple columns
sub = df[['Name', 'Salary']]
print("Subset with Name and Salary columns:")
print(sub)