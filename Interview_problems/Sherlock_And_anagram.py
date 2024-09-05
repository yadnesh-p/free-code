#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    for caseNo in range(q):

        n = len(s)
        res = 0
        for l in range(1, n):
            cnt = {}
            for i in range(n - l + 1):
                subs = list(s[i:i + l])
                subs.sort()
                subs = ''.join(subs)
                print (subs)
                if subs in cnt:
                    cnt[subs] += 1
                else:
                    cnt[subs] = 1
                res += cnt[subs] - 1
        print (cnt)        
        return res


if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print (result)

   #     fptr.write(str(result) + '\n')

   # fptr.close()
