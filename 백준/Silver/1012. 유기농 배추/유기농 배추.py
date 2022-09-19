def dfs(x, y):
    if visited[x][y] == 1:
        return 0
    stack = [x, y]
    while stack:
        y = stack.pop()
        x = stack.pop()
        if visited[x][y] == 0:
            visited[x][y] = 1
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < M and 0 <= ny < N:
                    if visited[nx][ny] == 0 and [nx, ny] in one_list:
                        stack.append(nx)
                        stack.append(ny)
    return 1


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    one_list = []
    for _ in range(K):
        a, b = map(int, input().split())
        one_list.append([a, b])
    visited = [[0] * (N) for _ in range(M)]
    cnt = 0
    for one in one_list:
        x, y = one[0], one[1]
        if dfs(x, y) == 1:
            cnt += 1
    print(cnt)