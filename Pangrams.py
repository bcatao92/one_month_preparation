#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alf = [" "]
    for char in alfabeto:
        alf.append(char)
    s = str.lower(s)
    for char in alf:
        if char not in s:
            return "not pangram"
    return "pangram"           


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
