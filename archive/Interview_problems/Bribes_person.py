#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    count = 0
    for i in range(len(q)):
        a = [num for num in q[i+1:] if num < q[i] ]
        print (a)
        if len(a) > 2:
            count = 'Too chaotic'
            break
        else :
            count += len(a) 

    print (count)

    
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
