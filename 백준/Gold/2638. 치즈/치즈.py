from collections import deque
import sys
input = sys.stdin.readline


# 모눈종이의 크기를 나타내는 두 정수 N, M
N, M = map(int, input().split())

# 치즈가 있으면 1, 없으면 0
cheeze = [list(map(int, input().split())) for _ in range(N)]

# 치즈가 모두 녹아 없어지는데 걸리는 시간
time = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 를 돌면서 주변 상하좌우 중 2변 이상이 공기와 접촉해야 녹기 때문에 공기와 접촉할 경우 +1 을 해주도록 함
def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if cheeze[nx][ny] >= 1:
                    cheeze[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


while True:
    visited = [[0] * M for _ in range(N)]
    bfs()
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 인접한 칸에 공기가 2개 이상일 경우 3 이상이 됨 -> 치즈가 녹았으니까 0 으로 바꿔줌  
            if cheeze[i][j] >= 3:
                cheeze[i][j] = 0
                cnt = 1
            # 아직 치즈가 안녹았으니까 1로 바꿔서 치즈를 유지해줌 
            elif cheeze[i][j] == 2:
                cheeze[i][j] = 1
    # cnt 가 1인 경우에는 치즈가 녹았다는 거니까 실제 걸리는 시간인 time 에 + 1 을 해줌 
    if cnt == 1:
        time += 1
    else:
        break

print(time)









