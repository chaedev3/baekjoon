import sys
input = sys.stdin.readline
N, K = map(int, input().split())
date_list = list(map(int, input().split()))

k_days = [sum(date_list[:K])]
for i in range(1, N - K + 1):
    result = k_days[-1] + date_list[i+K-1] - date_list[i-1]
    k_days.append(result)
print(max(k_days))