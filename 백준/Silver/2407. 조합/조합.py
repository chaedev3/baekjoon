import sys
input = sys.stdin.readline

N, M = map(int, input().split())

total = 1
for i in range(N, N-M, -1):
    total *= i

for j in range(M, 0, -1):
    total //= j

print(total)
