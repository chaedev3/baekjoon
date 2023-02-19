from collections import deque
import sys
input = sys.stdin.readline

# N : 가수의 수, M : 보조 PD의 수
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    A, *singer_list = map(int, input().split())

    for i in range(A - 1):
        graph[singer_list[i]].append(singer_list[i + 1])
        indegree[singer_list[i + 1]] += 1

que = deque([])
for i in range(1, N + 1):
    if indegree[i] == 0:
        que.append(i)
result = []
while que:
    node = que.popleft()
    result.append(node)
    for n in graph[node]:
        indegree[n] -= 1
        if indegree[n] == 0:
            que.append(n)

if len(result) == N:
    for r in result:
        print(r)
else:
    print(0) 

