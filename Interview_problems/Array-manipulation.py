import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    original = [0 for j in range(n)]
    print (original)
    for i in queries:
        k =i[2]
        for x in range(i[0]-1,i[1]):
            original[x] += k
    
    return max(original)

        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print (result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
