import sys, heapq
input = sys.stdin.readline


def dijkstra(start, end):
    heap = [(0, start)]
    heapq.heapify(heap)

    while heap:
        cost, node = heapq.heappop(heap)

        if visited[node] < cost:
            continue

        for nn, nc in graph[node]:
            nd = nc + cost

            if visited[nn] > nd:
                visited[nn] = nd
                prev[nn] = node
                heapq.heappush(heap, (nd, nn))

    return visited[end]


# n : 도시의 개수, m : 버스의 개수
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    # 순서대로 출발 도시의 번호 / 도착지의 도시 번호 / 버스 비용
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())


visited = [float('inf')] * (n + 1)
prev = [-1] * (n + 1)
print(dijkstra(start, end))

result = [end]
r = end
while r != start:
    result.append(prev[r])
    r = prev[r]

print(len(result))
print(*result[::-1])




