# f(n) = f(n - 1) + f(n - 2) + f(n - 3)

T = int(input())
for tc in range(T):
    N = int(input())
    # 처음에 dp의 크기를 N + 1 만큼 해줬는데 그러면 n 이 1, 2 일 때 문제가 생김 ! 
    dp = [0] * (max(4, N + 1)) 
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for idx in range(4, N + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2] + dp[idx -3]
    print(dp[N])
