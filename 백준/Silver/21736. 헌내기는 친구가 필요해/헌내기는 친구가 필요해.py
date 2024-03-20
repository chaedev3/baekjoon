import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]  

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] 

def bfs(x, y):
    q = [(x, y)]
    visited[x][y] = 1 
    result = 0 
    while q:
        start_x, start_y = q.pop(0)
        for i in range(4):
            sx = start_x + dx[i]
            sy = start_y + dy[i]
            if 0 <= sx < N and 0 <= sy < M and not visited[sx][sy]:
                visited[sx][sy] = 1 
                if arr[sx][sy] == 'P': 
                    result += 1
                    q.append((sx, sy)) 
                elif arr[sx][sy] == 'O':
                    q.append((sx, sy)) 
    return result 



for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            answer = bfs(i, j)
            if answer > 0:
                print(answer)
            else:
                print('TT')