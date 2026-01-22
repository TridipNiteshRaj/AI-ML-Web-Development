#np.nan_to_nan(array, nan=value).default -0
import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 5])
cleaned_arr = np.nan_to_num(arr, nan=0)
print(cleaned_arr)