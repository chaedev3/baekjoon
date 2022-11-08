# bottom-up
import sys
input = sys.stdin.readline

# N : 물품의 수
# K : 버틸 수 있는 무게
N, K = map(int, input().split())

arr = [[0, 0]]
for _ in range(N):
    # weight, value 순임
    arr.append(list(map(int, input().split())))

dp = [[0] * (K + 1) for _ in range(N + 1)]

# i = 1 일 때,
for a in range(1, N + 1):
    for b in range(1, K + 1):
        if arr[a][0] > b:
            dp[a][b] = dp[a - 1][b]
        else:
            dp[a][b] = max(dp[a-1][b-arr[a][0]] + arr[a][1], dp[a - 1][b])

print(dp[N][K])