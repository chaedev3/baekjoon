from itertools import permutations

N, M = map(int, input().split())
data = list(range(1, N+1))

y = list(permutations(data, M))

for idx in range(len(y)):
    print(*y[idx])