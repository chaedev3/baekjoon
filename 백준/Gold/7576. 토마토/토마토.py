import sys
from collections import deque
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(queue):
    max_v = 0
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    queue.append([nx, ny])
    for r in range(N):
        for c in range(M):
            if tomato[r][c] == 0:
                return -1
            else:
                if tomato[r][c] > max_v:
                    max_v = tomato[r][c]
    return max_v - 1


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i, j])

print(BFS(q))




