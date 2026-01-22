"""
vertically 
horizontally

vstack() row wise stacking
hstack() column wise stacking
"""

import numpy as np	

arr1 = np.array([10,20,30],)
arr2 = np.array([70,80,90],)

print(np.vstack((arr1, arr2)))  # vertical stacking
print("-----")
print(np.hstack((arr1, arr2)))  # horizontal stacking