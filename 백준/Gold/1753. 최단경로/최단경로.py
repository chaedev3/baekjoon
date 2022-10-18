import heapq, sys
input = sys.stdin.readline
# INF 정의
INF = 10 ** 7


# 다익스트라 정의
def dijkstra(start):
    # 처음 시작지점은 0으로 바꿔주기
    visited[start] = 0
    # heap 에 가중치(0), 시작점을 추가해줌
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, start))

    # heap이 빌 때까지
    while heap:
        # 가중치, 노드를 pop
        d, n = heapq.heappop(heap)
        # 노드와 연결된 점
        for nw, nn in graph[n]:
            if visited[nn] > visited[n] + nw:
                visited[nn] = visited[n] + nw
                heapq.heappush(heap, (visited[nn], nn))
    return


V, E = map(int, input().split())
K = int(input())
graph = {i: [] for i in range(1, V + 1)}

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
visited = [INF] * (V + 1)


dijkstra(K)

for i in range(1, V + 1):
    [print("INF") if visited[i] == INF else print(visited[i])]
