import sys
sys.setrecursionlimit(100001)

N = int(input())

dp = [0] * max(3, (N + 1))
# 점화식 dp[n] = 2 * dp[n - 1] + dp[n - 2]
dp[1] = 3
dp[2] = 7

if N < 3:
    pass
else:
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901

print(dp[N])
