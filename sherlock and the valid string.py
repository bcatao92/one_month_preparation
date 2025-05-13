#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):  
    a = list(s)
    b = set(a)
    dici=[]
    for letra in b:
        dici.append(a.count(letra))
    dici.sort(reverse=True)

    
    c = set(dici)
    #print(c)
    if(len(c)) == 1: return "YES"
    if len(c) > 2: return "NO"
    if max(c)-min(c) > 1 and min(c) != 1: return "NO"

    aux = dici
    aux[0] -= 1
    
    if len(set(aux)) == 1: return "YES"
    aux[0] += 1
    dici[-1] -=1
    if dici[-1] == 0:
        del(dici[-1])
    if len(set(dici)) == 1: return "YES"    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
