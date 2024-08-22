if __name__ == "__main__" :
    H = 0
    I = 0
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    SET_A = list(set(map(int,input().split())))
    SET_B = list(set(map(int,input().split())))
    '''for ele in arr:
        for i in range(m):
            if SET_A[i] == ele:
                H = H+1
            elif SET_B[i] == ele:
                H = H-1
            else:
                H = H
    '''
    I += sum(1 for ele in arr if ele in SET_A) #using list comprehension method for optimization
    I -= sum(1 for ele in arr if ele in SET_B)

    #optimized further more
    J=0
    for ele in arr:
        J += (1 if ele in SET_A else -1 if ele in SET_B else 0)
print(J)


         


    
    
