import sys
from collections import deque
input = sys.stdin.readline


def bfs(a, b, group):
    q = deque([])
    q.append([a, b])
    zero_list[a][b] = group

    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if wall[nx][ny] == 0 and not visited[nx][ny]:
                    zero_list[nx][ny] = group
                    cnt += 1
                    q.append([nx, ny])
                    visited[nx][ny] = 1
        info[group] = cnt


N, M = map(int, input().split())
wall = [list(map(int, input().rstrip())) for _ in range(N)]
zero_list = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
group = 1
info = {}
info[0] = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 먼저 0 인 곳들을 묶어서 표시해줌
# dict 에 몇 개씩 있는 지 저장해줌
for i in range(N):
    for j in range(M):
        if wall[i][j] == 0 and not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j, group)
            group += 1

for i in range(N):
    for j in range(M):
        if zero_list[i][j] == 0:
            total = set()
            result = 1
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < M and zero_list[ni][nj] > 0:
                    total.add(zero_list[ni][nj])
            for t in total:
                result += info[t]
            wall[i][j] = result % 10

for i in range(N):
    for j in range(M):
        print(wall[i][j], end='')
    print()


