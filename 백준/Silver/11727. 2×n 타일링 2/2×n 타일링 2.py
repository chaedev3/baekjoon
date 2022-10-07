# f(n) = f(n - 1) + 2 * f(n - 2) 임

N = int(input())

dp = [0] * (N + 2)
dp[1] = 1
dp[2] = 3
for idx in range(3, N + 1):
    dp[idx] = dp[idx - 1] + 2 * dp[idx - 2]

print(dp[N] % 10007)