#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            if s[i+1:len(s)-i] == s[i+1:len(s)-i][::-1]:
                return i
            if s[i:len(s)-i-1] == s[i:len(s)-i-1][::-1]:
                return len(s) - 1 - i
    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
