import sys 
input = sys.stdin.readline

T = int(input())

def dynamic(N):
    dp[0] = 0 
    dp[1] = 1 
    dp[2] = 2
    dp[3] = 3 
    if N > 3:
        for i in range(4, N + 1): 
            if i % 3 == 0:
                dp[i] = dp[i-1] + dp[i - 2] - dp[i - 3] + 1 
            else: 
                dp[i] = dp[i -1] + dp[i - 2] - dp[i - 3]  

num_list = [int(input()) for _ in range(T)]
maxV = max(num_list)
dp = [0] * max(maxV + 1, 4)   
dynamic(maxV) 

for num in num_list:
    print(dp[num])
