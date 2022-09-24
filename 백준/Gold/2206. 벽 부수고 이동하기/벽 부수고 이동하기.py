from collections import deque
import copy

dx = [0, 0, 0, 0]
dy = [-1, 1, 0, 0]
dz = [0, 0, -1, 1]


def BFS(start, end):
    if start == end:
        return 1
    q = deque([start])
    while q:
        x, y, z = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < 2 and 0 <= ny < N and 0 <= nz < M:
                if wall_list[nx][ny][nz] == 0:
                    wall_list[nx][ny][nz] = wall_list[x][y][z] + 1
                    q.append([nx, ny, nz])
                if wall_list[nx][ny][nz] == 1:
                    if nx == 0:
                        nx = nx + 1
                        wall_list[nx][ny][nz] = wall_list[x][y][z] + 1
                        q.append([nx, ny, nz])
    if wall_list[end[0]][end[1]][end[2]] in one_zero and wall_list[end[0] + 1][end[1]][end[2]] in one_zero:
        return -1
    elif wall_list[end[0]][end[1]][end[2]] in one_zero or wall_list[end[0] + 1][end[1]][end[2]] in one_zero:
        return max(wall_list[end[0]][end[1]][end[2]], wall_list[end[0] + 1][end[1]][end[2]]) + 1
    else:
        return min(wall_list[end[0]][end[1]][end[2]], wall_list[end[0] + 1][end[1]][end[2]]) + 1


N, M = map(int, input().split())
wall_list = []
wall = [list(map(int, input())) for _ in range(N)]
w = copy.deepcopy(wall)
wall_list.append(wall)
wall_list.append(w)
one_zero = [0, 1]

s = [0, 0, 0]
e = [0, N-1, M-1]
print(BFS(s, e))




