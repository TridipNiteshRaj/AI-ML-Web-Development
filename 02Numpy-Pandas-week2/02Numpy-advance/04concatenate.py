"""
np. concatenate((array1, array2, ...), axis=0)

axis 0 > vertical stacking (row-wise)
axis 1 > horizontal stacking (column-wise) 
"""

import numpy as np
arr1 = np.array([10,20,25])
arr2 = np.array([30,40,50])
new_arr = np.concatenate((arr1, arr2), axis=0)
print(new_arr)
