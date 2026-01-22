"""  
reshape(row, column) specify new shape
if dimensions match
"""

import numpy as np
arr = np.reshape([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)