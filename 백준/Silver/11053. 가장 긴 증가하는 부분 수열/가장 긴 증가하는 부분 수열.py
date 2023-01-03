import sys 
input = sys.stdin.readline 

# N : 수열의 크기 
N = int(input())

arr = list(map(int, input().split())) 
dp = [0 for _ in range(N)] 

# arr을 하나씩 차례대로 돌면서 
for i in range(N):
    # i 보다 전에 있는 것들과 비교한다. 
    for j in range(i):
        # 만약 증가하고 있고 아직 증가한 게 반영되지 않았다면 같게 해준다. 
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j] 
    # 아무것도 증가하지 않은 경우에도 1이니까 +=1 을 해주는 것임 
    dp[i] += 1
   
print(max(dp)) 