temperatures = [3.2, 3.4, 2.3, 4.3, 4.5, 2.3]

total = 0
for team in temperatures:
    total += team
    
average = total / len(temperatures)
print(average)    