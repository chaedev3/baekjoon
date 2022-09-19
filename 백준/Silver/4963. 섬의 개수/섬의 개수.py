dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]


def dfs(x, y):
    stack = [x, y]
    while stack:
        y = stack.pop()
        x = stack.pop()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and island[nx][ny] == 1:
                stack.append(nx)
                stack.append(ny)
                island[nx][ny] = 0


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * (h + 1) for _ in range(w + 1)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)

