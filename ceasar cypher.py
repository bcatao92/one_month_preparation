#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto = list(alfabeto)
    cesar = {}
    i=0
    aux=''
    for letra in alfabeto:
        cesar[letra] = alfabeto[(i + k) % 26]
        i+=1
    for char in s:
        dummy = char.lower()
        if dummy not in alfabeto:
            aux+=dummy
        elif char.isupper():
            aux+=(cesar[dummy]).upper()
        else:
            aux+=cesar[char] 
    return(aux)    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
