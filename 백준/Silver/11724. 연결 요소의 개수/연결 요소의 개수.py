import sys
input = sys.stdin.readline


def bfs(x):
    q = [x]  
    visited[x] = 1
    while q:
        s = q.pop(0) 
        for w in range(1, N + 1):
            if visited[w] == 0 and arr[s][w] == 1:
                q.append(w)
                visited[w] = 1     

N, M = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u][v] = 1 
    arr[v][u] = 1 

result = 0 
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i) 
        result += 1 
    
print(result)