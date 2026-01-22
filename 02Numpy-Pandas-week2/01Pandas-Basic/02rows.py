#head() , #tail() , #sample()
#head() - first n rows -5
#tail() - last n rows -5
#sample() - random n rows -5

import pandas as pd
df = pd.read_csv("sales_data_sample.csv" , encoding='latin1')

print('First 5 rows using head():')
print(df.head(10))

print('Last 5 rows using tail():')
print(df.tail(10))