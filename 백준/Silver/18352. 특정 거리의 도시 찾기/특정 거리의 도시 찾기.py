import heapq, sys
input = sys.stdin.readline


def dijkstra(start):
    visited[start] = 0
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, start)

    while heap:
        n = heapq.heappop(heap)
        for node in graph[n]:
            if visited[node] > visited[n] + 1:
                visited[node] = visited[n] + 1
                heapq.heappush(heap, node)
    return


# N : 도시의 개수 / M : 도로의 개수 / K : 거리 정보 / X: 출발 도시의 번호
N, M, K, X = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    # A -> B
    A, B = map(int, input().split())
    graph[A].append(B)
INF = 10 ** 7
visited = [INF] * (N + 1)

dijkstra(X)

if K not in visited:
    print(-1)
else:
    for idx in range(len(visited)):
        if visited[idx] == K:
            print(idx)

