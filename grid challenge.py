grid = ["dca", "ade", "efg"]
n = len(grid)

for el in range(len(grid)):
    grid[el] = list(grid[el])
    grid[el].sort()
print(grid)

for i in range(n):
    aux = []
    for j in range(n):
        aux.append(grid[j][i])

    if sorted(aux) != aux:
        print("NO")
    else:
        print("YES")
        
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here 
    s_grid = [sorted(_) for _ in grid]

    return 'YES' if [list(i) for i in zip(*s_grid)] == [sorted(list(i)) for i in zip(*s_grid)] else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
