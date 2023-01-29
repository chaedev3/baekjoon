import sys
input = sys.stdin.readline


def bellmanFord(start):
    distance[start] = 0
    for i in range(N):
        for j in range(1, N + 1):
            for next_node, cost in graph[j]:
                if distance[next_node] > distance[j] + cost:
                    distance[next_node] = distance[j] + cost
                    if i == N - 1:
                        return True
    return False


# T : 테스트케이스의 개수
T = int(input())
for _ in range(T):
    # N: 지점의 수 ,M: 도로의 개수 ,W: 웜홀의 개수
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    INF = 10 ** 7 + 1 
    distance = [INF] * (N + 1)
    for _ in range(M):
        start, end, time = map(int, input().split())
        graph[start].append([end, time])
        graph[end].append([start, time])

    for _ in range(W):
        start, end, time = map(int, input().split())
        graph[start].append([end, -time])

    isNegative = bellmanFord(1)
    if isNegative:
        print("YES")
    else:
        print("NO")


