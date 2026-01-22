import numpy as np

arr_2d = np.array([[10,20,], [40,50]])
print(arr_2d)
#insert a new column,row at index 2
new_arr_2d = np.insert(arr_2d, 2, [70,80], axis=1)
print(new_arr_2d)