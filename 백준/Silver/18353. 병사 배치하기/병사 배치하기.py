import sys
input = sys.stdin.readline

n = int(input())
power_list = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i + 1, n): 
        if power_list[i] > power_list[j]:
            dp[j] = max(dp[i] + 1, dp[j])


print(n - max(dp)) 