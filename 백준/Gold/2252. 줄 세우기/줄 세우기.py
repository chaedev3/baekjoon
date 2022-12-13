from collections import deque
import sys
input = sys.stdin.readline

# N : 학생들의 수, M: 키를 비교한 회수
N, M = map(int, input().split())
# 연결된 간선의 정보를 담을 리스트
graph = [[] for _ in range(N + 1)]
# 자신에게 들어오는 간선의 수를 담는 indegree 리스트
indegree = [0] * (N + 1)


for _ in range(M):
    # A 학생은 항상 B 학생의 앞에 서 있어야 함
    A, B = map(int, input().split()) 
    # 모든 간선의 정보를 담으면서 indegree 테이블을 채워줌 
    graph[A].append(B)
    indegree[B] += 1

que = deque([])
for i in range(1, N + 1):
    # indegree가 0인 정점들을 큐에 넣어줌 
    if indegree[i] == 0:
        que.append(i)

result = []
# 큐가 빌 때까지 반복해줌 
while que: 
    # que에서 정점을 꺼내어 위상 정렬 결과에 추가 
    node = que.popleft()
    result.append(node)
    # 해당 정점으로부터 연결된 모든 정점의 indegree 값ㅇ르 1 감소시키고 
    # 이 때 indegree가 0이 되었다면 그 정점을 큐에 추가해줌 
    for n in graph[node]:
        indegree[n] -= 1
        if indegree[n] == 0:
            que.append(n)

print(*result)





