import sys
import heapq
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start, end):
    visited = {i: INF for i in range(1, N + 1)}
    visited[start] = 0
    distance = []
    heapq.heapify(distance)
    heapq.heappush(distance, (0, start))

    while distance:
        # d 는 거리 / n 은 node
        d, n = heapq.heappop(distance)

        # x에 저장된 최소비용이 현재 뽑힌 노드 (d, n) 보다 작으면
        # 노드가 저장된 이후 visited[x] 가 갱신된 것이므로 큐의 다음 노드로 넘어가게 됨
        if visited[n] < d:
            continue

        for nw, nn in graph[n]:
            nd = d + nw

            if visited[nn] > nd:
                visited[nn] = nd
                heapq.heappush(distance, (nd, nn))

    return visited[end]


N = int(input())
M = int(input())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

start, end = map(int, input().split())

print(dijkstra(start, end))



