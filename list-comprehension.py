if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

import math
result = []
output = []
for X in range(x+1):
    for Y in range(y+1):
        for Z in range(z+1):
            if X+Y+Z != n:
                result = [X,Y,Z]
                output.append(result)
print(output)