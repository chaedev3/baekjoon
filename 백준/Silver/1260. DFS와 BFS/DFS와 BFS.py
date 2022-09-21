def DFS(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, V + 1):
        if arr[v][w] == 1 and visited[w] == 0:
            DFS(w)


def BFS(v):
    queue = [v]
    visited1[v] = 1
    print(v, end=' ')
    while queue:
        v = queue.pop(0)
        for w in range(1, V+1):
            if arr[v][w] == 1 and visited1[w] == 0:
                queue.append(w)
                visited1[w] = 1
                print(w, end=' ')


V, E, v = map(int, input().split())
arr = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
visited = [0 for _ in range(V+1)]
visited1 = [0 for _ in range(V+1)]
DFS(v)
print()
BFS(v)
