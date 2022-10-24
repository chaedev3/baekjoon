import sys
input = sys.stdin.readline


T = int(input())

for tc in range(T):
    N = int(input())
    zero_dp = [0] * max(2, (N + 1))
    one_dp = [0] * max(2, (N + 1))
    zero_dp[0] = 1
    zero_dp[1] = 0
    one_dp[0] = 0
    one_dp[1] = 1

    for i in range(2, N + 1):
        zero_dp[i] = zero_dp[i - 1] + zero_dp[i - 2]
        one_dp[i] = one_dp[i - 1] + one_dp[i - 2]

    print(zero_dp[N], one_dp[N])

