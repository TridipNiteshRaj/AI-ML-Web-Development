'''  
slicing 
array[start:stop:step]

arr[start:end] #slicing from start to end-1

negative step, -1 reverse the array
'''
import numpy as np
arr = np.array([20,63,34,12,42])
print(arr[0:5]) #slicing from index 0 to 2
print(arr[:3]) #index 0 to 2
print(arr[::2]) #every 2nd element
print(arr[::-1]) #reverse the array #negative step