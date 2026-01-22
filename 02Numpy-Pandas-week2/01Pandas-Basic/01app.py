import pandas as pd

#Read data from CSV file into a DataFrame

df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# df = pd.read_excel("sales_data_sample.xlsx")
# df = pd.read_json("sales_data_sample.json")

print(df)