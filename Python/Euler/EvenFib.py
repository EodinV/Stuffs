import math

n1 = 0
n2 = 1
nnext = 0

for i in range(10000):
    n1 = n2
    n2 = nnext
    nnext = n1 + n2
    if nnext % 2 == 0:
        print(nnext)
    if nnext >= 4000000:
        break