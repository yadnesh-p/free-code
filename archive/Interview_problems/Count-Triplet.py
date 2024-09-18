#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the countTriplets function below.
def countTriplets(arr, r):
    '''
    sorted_arr = sorted(arr)
    combinations = list(itertools.combinations(sorted_arr,3))
    count = 0
    for a in combinations:
        if a[1]==a[0]*r and a[2]==a[0]*r**2:
            count +=1
    return count
    '''
    count = 0
    for ele in arr:
        if ele+r in arr and ele+2*r in arr:
            count += 1
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print (ans)

   # fptr.write(str(ans) + '\n')

   # fptr.close()
