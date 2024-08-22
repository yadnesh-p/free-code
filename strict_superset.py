if __name__ == '__main__':
    SET_A = set(map(int,input().split()))
    n = int(input())
    for i in range(n):
        SET_N = set(map(int,input().split()))
        result=False
        if SET_A.issuperset(SET_N):
            if len(SET_A)==len(SET_N):
                result = False
            else:
                result = True
        else:
            result=False
            break
print (result)