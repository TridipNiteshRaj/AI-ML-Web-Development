import pandas as pd
data = {
    "Time": [1, 2, 3, 4, 5, 6],
	"Value": [10, None, None, 40, None, 60],
}

df = pd.DataFrame(data)
print('Befoure Interpolation:')
print(df)

df['Value'] = df['Value'].interpolate(method='linear')
print('\nAfter Interpolation:')
print(df)



""""
when to use linear interpolation:

1- timer series data with missing values
2-numeric data with a linear trend
3- small gaps in data
4- evenly spaced data points
5- when simplicity and speed are priorities
"""