import math

def new(a,b):
    print (a//b)
    print (a%b)
    print (divmod(a,b))
    

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    new(a,b)