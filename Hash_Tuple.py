import _hashlib
if __name__ == '__main__':
    N = int(input())
    L = tuple(map(int,input().split()))
    print(hash(L))
    
    