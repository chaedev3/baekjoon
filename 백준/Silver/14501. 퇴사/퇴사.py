import sys
input = sys.stdin.readline

n = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)] 

dp = [0] * (20)

for i in range(1, n + 1):
    len, cost = arr[i]
    days = len - 1 
    dp[i] = max(dp[i], dp[i - 1]) 
    dp[i + days] = max(dp[i + days], dp[i - 1] + cost)
  
print(dp[n]) 
