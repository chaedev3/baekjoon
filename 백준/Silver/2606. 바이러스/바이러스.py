import sys
input = sys.stdin.readline

# N 은 컴퓨터의 수
N = int(input())
# M 은 컴퓨터 쌍의 수 
M = int(input()) 

arr = [[] for _ in range(N + 1)]  
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a) 

visited= [0 for _ in range(N + 1)]

def bfs(v):
    queue = [v]
    visited[v] = 1
    result = 0 
    while queue:
        start = queue.pop(0)
        for w in range(1, N + 1):
            if visited[w] == 0 and w in arr[start]:
                queue.append(w)
                visited[w] = 1
                result += 1 
    return result

print(bfs(1))
