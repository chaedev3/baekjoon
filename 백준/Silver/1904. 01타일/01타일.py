import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * max(3, N + 1)
dp[1] = 1
dp[2] = 2

for idx in range(3, N + 1):
    dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 15746

print(dp[N])
