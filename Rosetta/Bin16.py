import sys
import os

arr = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
bin = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
num = int(input("Give me a Number: "))


for i in range(16):
    if num - arr[i] < 0:
        bin[i] = 0
    elif num - arr[i] >= 0:
        bin[i] = 1
        num = num - arr[i]
    
print(bin)


            