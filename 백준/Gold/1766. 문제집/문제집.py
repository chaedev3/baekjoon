import heapq, sys
input = sys.stdin.readline

# N: 문제의 수, M: 정보의 개수
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

heap = []
heapq.heapify(heap)

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    node = heapq.heappop(heap)
    result.append(node)

    for n in graph[node]:
        indegree[n] -= 1
        if indegree[n] == 0:
            heapq.heappush(heap, n)

print(*result)