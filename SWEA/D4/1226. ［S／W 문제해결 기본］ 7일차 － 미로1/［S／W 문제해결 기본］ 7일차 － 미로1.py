def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0


T = 10
for _ in range(T):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    N = 16
    sti = -1
    stj = -1
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sti = i
                stj = j
                break
        if sti != -1:
            break
    print(f'#{tc} {bfs(sti, stj, N)}')
