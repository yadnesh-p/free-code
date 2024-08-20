from collections import Counter
K = int(input())
SET_K = list(map(int, input().split()))
unique_K = set(SET_K)

result = [key for key, count in Counter(SET_K).items() if count == 1]
print(result[0])