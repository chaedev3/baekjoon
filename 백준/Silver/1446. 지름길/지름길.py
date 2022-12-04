import heapq, sys
input = sys.stdin.readline

INF = 10 ** 7


def dijkstra(start):
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, start))
    visited[start] = 0

    while heap:
        d, n = heapq.heappop(heap)

        if d > visited[n]:
            continue

        for x in graph[n]:
            # x[1] 은 지름길의 길이임
            distance = d + x[1]
            if distance < visited[x[0]]:
                visited[x[0]] = distance
                heapq.heappush(heap, (distance, x[0]))


# N = 지름길의 개수, D = 고속도로의 길이
N, D = map(int, input().split())
graph = [[] for _ in range(D + 1)]
visited = [INF] * (D + 1)

for i in range(D):
    graph[i].append((i + 1, 1))

for _ in range(N):
    # 시작 위치, 도착 위치, 지름길의 길이
    s, e, w = map(int, input().split())
    if e > D:
        continue

    graph[s].append((e, w))

dijkstra(0)
print(visited[D])
