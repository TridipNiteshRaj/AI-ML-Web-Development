#pd.merge(df1, df2, on="Column_Name", how="type_of_join")
import pandas as pd

#customer dataframe
df_customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4],
	"CustomerName": ["Sourabh", "gautam", "Dabbu", "Ankit"]
})

#orders dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 4, 3, 5],
	'OrderAmount': [101, 102, 103, 104, 105]
})


#merge

df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="outer")
print("Outer Join:")
print(df_merged)



""" """