import pandas as pd

data = {
	'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack' ,'Kathy', 'Leo', 'Mona'],
	'Age': [24, 27, 22, 32, 29, 23, 31, 28, 26, 30, 25, 34, 21],
	'Salary': [50000, 54000, 58000, 60000, 62000, 51000, 59000, 61000, 63000, 65000, 52000, 64000, 57000],
}

df = pd.DataFrame(data)

#single condition filtering
high_salary = df[df['Salary'] > 60000]
print('Employees with Salary greater than 60000:')
print(high_salary)

#multiple condition filtering
age_salary_filter = df[(df['Age'] < 30) & (df['Salary'] > 55000)]
print('Employees with Age less than 30 and Salary greater than 55000:')
print(age_salary_filter)

#using isin() for filtering
selected_names = df[df['Name'].isin(['Alice', 'David', 'Mona'])]
print('Employees with names Alice, David, or Mona:')
print(selected_names)