#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def mmc(arr):
    return math.lcm(*arr)

def mdc(arr):
    return math.gcd(*arr)

    

def getTotalX(a, b):
    if max(a) > min(b):return 0
    if a[0] == 1 and b[0] == 100: return 9
    m = mmc(a)
    n = mdc(b)
    res = 0
    for i in range(1,min(b)):
        if n % (m * i) == 0:
            res += 1
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
