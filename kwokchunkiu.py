# Exercise 1
height = 1.75
weight = 80.5

bmi = weight / (height ** 2)
if 18.5 <= bmi <= 25:
    print('healthy')
else:
    print('unhealthy')

# Exercise 2
num = 121
rev = 0
temp = num
while temp != 0:
    rem = num % 10
    rev = rem * 10 + rem
    temp = num // 10
if rev == num:
    print('The reverse is the same as the original.')
else:
    print('The reverse is not the same as the original.')

# Exercise 3
l = [1, 3, 4, 8, 9]
print(l.sum())
    
