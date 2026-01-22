list_1 = [1,2,3,4,5]
list_2 = list_1  # alias

list_2[0] = 100
print("list_1:", list_1)  # Output: [100, 2, 3, 4, 5]