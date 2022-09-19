import sys
input = sys.stdin.readline

x, y = map(int, input().split())
cut = int(input())
garo = [0]
sero = [0]
for _ in range(cut):
    a, b = map(int, input().split())
    if a == 0:
        garo.append(b)
    else:
        sero.append(b)
garo.append(y)
garo.sort()
sero.append(x)
sero.sort()

result = []
for g in range(len(garo)-1):
    for s in range(len(sero)-1):
        result.append((garo[g+1] - garo[g]) * (sero[s+1] - sero[s]))

print(max(result))
