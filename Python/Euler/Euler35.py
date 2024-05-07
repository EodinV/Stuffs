import math

multisum = 0

for i in range(1000):
    if i % 3 == 0:
        multisum = multisum + i
    if i % 5 == 0:
        multisum = multisum + i

print('Sum of multiples is: ', multisum)
