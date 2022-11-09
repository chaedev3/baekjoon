import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_value = [int(input()) for _ in range(n)]
coin_value.sort()

dp = [0] * (k + 1)
dp[0] = 1
for coin in coin_value:
    for idx in range(1, k + 1):
        if idx - coin >= 0:
            dp[idx] = dp[idx] + dp[idx - coin]

print(dp[k])
