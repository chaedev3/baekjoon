import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

minV = 100001
i, j = 0, 0
partSum = numbers[0]

while i < N:
    if partSum >= S:
        minV = min(minV, j - i + 1)
        partSum -= numbers[i]
        i += 1
    else:
        j += 1
        if j == N:
            break
        partSum += numbers[j]

if minV == 100001:
    print(0)
else:
    print(minV)
