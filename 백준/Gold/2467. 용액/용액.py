import sys
input = sys.stdin.readline

# N: 전체 용액의 수
N = int(input())
fluids = list(map(int, input().split()))

minV = 2e+10 

start = 0
end = N - 1
answer = []
while start < end:
    startV = fluids[start]
    endV = fluids[end]
    if abs(startV + endV) < minV:
        minV = abs(startV + endV)
        answer = [startV, endV]

    if startV + endV == 0:
        break

    elif startV + endV < 0:
        start += 1

    else:
        end -= 1

print(*answer)


