"""  
np.insert(array, index, values, axis=None)
array - original array 
index -
value -
axis = 0, row-wise insertion
axis = 1, column-wise insertion
"""

import numpy as np

arr = np.array([10,20,30,40,50])
print(arr)
new_arr = np.insert(arr, 2, 100)
print(new_arr)