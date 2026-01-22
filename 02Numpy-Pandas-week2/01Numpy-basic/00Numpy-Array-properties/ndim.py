import numpy as np

arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3],[4, 5, 6]])
arr_3d = np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9]]]) 

print(arr_1d.ndim)  # Output: 1
print(arr_2d.ndim)  # Output: 2
print(arr_3d.ndim)  # Output: 3