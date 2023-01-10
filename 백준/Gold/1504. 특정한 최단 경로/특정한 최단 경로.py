import sys, heapq
input = sys.stdin.readline 

# N : 정점의 개수, E: 간선의 개수 
N, E = map(int, input().split())

INF = 10 ** 7 + 1 
graph = {i: [] for i in range(1, N + 1)}

for _ in range(E):
    # a번 정점에서 b번 정점까지 양방향 길이 존재, 그 거리가 c라는 뜻 
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c))
    graph[b].append((a, c)) 

# 두 개의 서로 다른 정점 번호 v1, v2 가 주어짐 
v1, v2 = map(int, input().split()) 



def dijkstra(start):
    visited = {i: INF for i in range(1, N + 1)} 
    visited[start] = 0 
    heap = [(0, start)]  
    heapq.heapify(heap) 

    while heap:
        distance, node = heapq.heappop(heap) 

        if visited[node] < distance:
            continue 

        for nn, nd in graph[node]: 
            cost = distance + nd 
            if visited[nn] > cost:
                visited[nn] = cost
                heapq.heappush(heap, (cost, nn)) 
    
    return visited  

real_visited = dijkstra(1) 
v1_visited = dijkstra(v1) 
v2_visited = dijkstra(v2)

v1_path = real_visited[v1] + v1_visited[v2] + v2_visited[N] 
v2_path = real_visited[v2] + v1_visited[N] + v2_visited[v1] 

result = min(v1_path, v2_path)

if result >= INF:
    print(-1) 
else:
    print(result)
