import pandas as pd

data ={
	'Name': ['John', 'Anna', 'Peter', 'Linda'],
	'Age': [28, 24, 35, 32],
	'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

print(df)
df.to_csv('people.csv', index=False)
# df.to_excel('people.xlsx', index=False)
# df.to_json('people.json', orient='records')
# print("Data saved to people.csv, people.xlsx, and people.json")
