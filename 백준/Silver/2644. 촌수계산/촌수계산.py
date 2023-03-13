import sys
from collections import deque 
input = sys.stdin.readline

def bfs(s, e):  
    q = deque([s])  
    visited[s] = 1 
    while q:
        v = q.popleft()  
        for w in range(1, N + 1):  
            if graph[v][w] == 1 and not visited[w]:    
                q.append(w) 
                visited[w] = visited[v] + 1 
                
    return visited[e] - 1 

            
# N : 전체 사람의 수 
N = int(input())
start, end = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)] 
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    graph[b][a] = 1  
    graph[a][b] = 1 
visited = [0] * (N + 1)



print(bfs(start, end)) 