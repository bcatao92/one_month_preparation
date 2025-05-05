import math

a = [3, 9, 6]

b = [36, 72]

c = [12,45]
def mmc(arr):
    return math.lcm(*arr)
def mdc(arr):
    return math.gcd(*arr)
print(mmc(a))
print(mdc(b))
print(mmc(c))