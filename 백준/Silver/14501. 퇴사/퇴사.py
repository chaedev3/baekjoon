# input 받기
N = int(input())
# 상담리스트에 시간, 금액을 추가해줌
consult_list = [[0, 0]]
for _ in range(N):
    time, amount = map(int, input().split())
    consult_list.append([time, amount])

# N의 최대값이 15까지이고 Ti의 최댓값이 5니까 최대로 나올 수 있는 값은 20이 된다
dp = [0] * 20

for i in range(1, N + 1):
    days = consult_list[i][0] - 1
    dp[i] = max(dp[i], dp[i-1])
    dp[i + days] = max(dp[i-1] + consult_list[i][1], dp[i + days])

print(dp[N])


