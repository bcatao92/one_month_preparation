#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    binario = str(bin(n))
    binario = str(binario[2:])
    while len(binario) < 32:
        binario = '0'+binario
    alterado = ''
    for c in binario:
        if c == '0':
            alterado+='1'
        else:
            alterado+='0'
    alterado = int(alterado,2)
    return alterado
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
