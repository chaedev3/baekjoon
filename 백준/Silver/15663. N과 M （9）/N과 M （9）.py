from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
result_list = sorted(set(permutations(num_list, M)))

for result in result_list:
    for r in result:
        print(r, end=' ')
    print()