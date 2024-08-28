#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    

    for idx in range(n):
        while arr[idx]-1 != idx:
            ele = arr[idx]
            arr[ele-1], arr[idx] = arr[idx], arr[ele-1]
            swaps += 1
    return swaps
    '''
    new_arr = []
    for i, num in enumerate(arr):
        if num  == i+1 :
            continue
        else:
            new_arr.append(num)
        
    print (new_arr)
    return len(new_arr)-1
    '''
 
if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print (res)

#    fptr.write(str(res) + '\n')

#    fptr.close()