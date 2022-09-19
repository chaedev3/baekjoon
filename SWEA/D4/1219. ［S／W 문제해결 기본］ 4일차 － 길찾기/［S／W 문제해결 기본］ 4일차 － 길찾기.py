def DFS(start, end):
    stack = [start]
    visited = [0 for _ in range(100)]
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            for w in range(100):
                if arr[v][w] == 1 and visited[w] == 0:
                    stack.append(w)
    return visited[end]

T = 10
for _ in range(1, T+1):
    tc, N = map(int, input().split())
    arr = [[0] * 100 for _ in range(100)]
    num_list = list(map(int, input().split()))
    for i in range(N):
        a, b = num_list[i * 2], num_list[i * 2 + 1]
        arr[a][b] = 1
    n, m = 0, 99
    result = 1
    if not DFS(n, m):
        result = 0

    print(f'#{tc} {result}')
