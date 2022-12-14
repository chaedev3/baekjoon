from collections import deque
import sys
input = sys.stdin.readline


# T : 테스트 케이스의 개수
T = int(input())
for _ in range(T):
    # N : 건물의 개수(건물의 번호는 1~N), K : 건설순서 규칙의 총 개수
    N, K = map(int, input().split())
    # 각 건물당 건설에 걸리는 시간
    time_list = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)    # 진입차수
    dp = [0 for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1
    # W: 백준이가 승리하기 위해 건설해야 할 건물의 번호
    W = int(input())

    que = deque([])
    for i in range(1, N + 1):
        if indegree[i] == 0:
            que.append(i)
            dp[i] = time_list[i]

    while que:
        node = que.popleft()
        for n in graph[node]:
            indegree[n] -= 1
            dp[n] = max(dp[node] + time_list[n], dp[n])
            if indegree[n] == 0:
                que.append(n)
    print(dp[W])




