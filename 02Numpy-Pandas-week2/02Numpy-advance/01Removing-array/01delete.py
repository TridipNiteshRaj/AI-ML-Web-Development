""" 
np.delete(array, indices, axis=None)
flattern array
"""

import numpy as np

arr = np.array([10,20,30])
print(arr)
new_arr = np.delete(arr, 1)
print(new_arr)