import math

ran = 100

def sumsq():
    tot = 0
    for i in range(ran):
        num = (i+1) ** 2
        tot = tot + num
    print(tot)
    return tot

def sqsum():
    tot = 0
    for i in range(ran):
        num = (i+1)
        tot = tot + num
    sqtot = tot**2
    print(sqtot)
    return sqtot

diff = sqsum() - sumsq()

print("Difference is: ", diff)