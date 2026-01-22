#np.isinf(array) 10*1000
#1/0


import numpy as np
arr = np.array([1, 2, np.inf, 4, -np.inf, 5])

print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, nan=1000, posinf=1000)

print(cleaned_arr)