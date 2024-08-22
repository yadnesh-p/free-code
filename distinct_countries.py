if __name__ == "__main__" :
    N = int(input())
    S = set()
    for i in range(N):
        new=str(input())
        S.add(new)
    print(len(S))
