#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
from collections import Counter

def sockMerchant(n, ar):
    # Write your code here
    arr = set(ar)
    occ = 0
    for i in arr:
        count = Counter(ar)
        occ = occ+count[i]//2
        print(count)
    print(occ)


                

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
