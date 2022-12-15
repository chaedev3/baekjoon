from collections import deque
import sys
input = sys.stdin.readline

# N : 건물의 종류 수
N = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
time_list = [0] * (N + 1)
dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    building_time, *precede_list, end = map(int, input().split())
    time_list[i] = building_time

    for p in precede_list:
        graph[p].append(i)
        indegree[i] += 1

que = deque([])
for i in range(1, N + 1):
    if indegree[i] == 0:
        que.append(i)
        dp[i] = time_list[i]


while que:
    node = que.popleft()

    for n in graph[node]:
        indegree[n] -= 1
        dp[n] = max(dp[n], dp[node] + time_list[n])
        if indegree[n] == 0:
            que.append(n)


for i in range(1, N + 1):
    print(dp[i])









