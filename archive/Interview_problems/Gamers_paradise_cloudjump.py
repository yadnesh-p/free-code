#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    Z = []
    list_min = [0]
    count = 0
    for j in range(n):
        if c[j] == 0:
            Z.append(j)
    while count < (n-1):
        if count+2 in Z:
            count = count + 2
            list_min.append(count)
        else:
            count = count + 1
            list_min.append(count)
    return (len(list_min)-1)

        



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print (result)

    #fptr.write(str(result) + '\n')

    #fptr.close()