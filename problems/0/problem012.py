# https://projecteuler.net/problem=12

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?
from math import ceil
def gettrianglenum():
    sum = 0
    counter = 1
    while True:
        sum += counter
        yield sum
        counter += 1

def getfactors(num):
    factors = set()
    for i in range(1, int(ceil(num**.5)) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return factors

def getnumwithfactors(target):
    for tnum in gettrianglenum():
        if len(getfactors(tnum)) > target:
            return tnum

num = getnumwithfactors(500)
print(num)