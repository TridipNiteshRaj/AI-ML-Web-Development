
age = int(input('enter your age ='))
if (age >= 18 and age < 101): #True
    print('you can vote!')

elif age >= 101:
    print('Greater then 101')

elif age <=0:
    print('invalid age')


else:
    print('error occurred')