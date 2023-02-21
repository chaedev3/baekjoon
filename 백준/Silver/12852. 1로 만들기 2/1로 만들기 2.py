import sys 
input = sys.stdin.readline 

N = int(input())
INF = 10 ** 7 + 1 
dp = [INF] * (N + 1)
dp[N] = 0 
for i in range(N, 1, -1):
    if i % 2 == 0: 
        dp[i // 2] = min(dp[i // 2], dp[i] + 1) 
    if i % 3 == 0:
        dp[i // 3] = min(dp[i // 3], dp[i] + 1) 
    
    dp[i - 1] = min(dp[i - 1], dp[i] + 1) 

i = dp[1]
j = 1  
result = [1] 
while i > 0:
    if j * 3 < N + 1 and dp[j * 3] + 1 == dp[j]:
        j = j * 3 
        result.append(j) 
    elif j * 2 < N + 1 and dp[j * 2] + 1 == dp[j]:
        j = j * 2
        result.append(j) 
    elif dp[j + 1] + 1 == dp[j]:  
        j = j + 1 
        result.append(j)
    i -= 1 
result = result[::-1]

print(dp[1])  
print(*result)




