#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
def isPower2(n):
    s = bin(n)[2:]
    s = list(str(s))
    count = 0
    for char in s:
        if char == "1":
            count += 1
        if count == 2:
            return False
    return True


def findPower2(n):
    aux = 0
    baux = 1
    while aux < n:
        aux = 2**baux
        baux += 1
    return int(aux / 2)


def divide(n):
    conta = 0
    while n > 1:
        conta += 1
        n = n / 2
    return conta


def counterGame(n):
    conta = 0
    if isPower2(n):
        conta = divide(n)
        if (conta - 1) % 2 != 0:
            return "Richard"
        else:
            return "Louise"
    else:
        while n > 1:
            n = n - findPower2(n)
            conta += 1
        print(conta)
        if (conta - 1) % 2 != 0:
            return "Richard"
        else:
            return "Louise"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
