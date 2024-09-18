def minimumBribes(q):
    count = 0
    for i, num in enumerate(q):
        if num - i - 1 > 2:
            count = 'Too chaotic'
            break
        for j in range(max(0, num - 2), i):
            if q[j] > num:
                count += 1
    print(count)

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)