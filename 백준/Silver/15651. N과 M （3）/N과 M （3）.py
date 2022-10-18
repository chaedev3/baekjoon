from itertools import product

N, M = map(int, input().split())
num_list = list(range(1, N + 1))
result = list(product(num_list, repeat=M))
for r in result:
    print(*r)

