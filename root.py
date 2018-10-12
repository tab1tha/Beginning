#program to find the first perfect square when counting downwards from 99 to 0
from math import sqrt
for number in range(99,0,-1):
    n=sqrt(number)
    if n==int(n):
        print(number)
        break

