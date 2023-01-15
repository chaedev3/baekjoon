import sys
input = sys.stdin.readline


def pipe(x, y):
    # 대각선 파이프를 추가
    # 파이프가 지나가는 길에 벽이 없는지 확인
    if graph[x - 1][y] == 0 and graph[x][y - 1] == 0 and graph[x][y] == 0:
        dp[x][y][1] = sum(dp[x - 1][y - 1])
        # dp[x][y][1] = dp[x - 1][y - 1][0] + dp[x - 1][y - 1][1] + dp[x - 1][y - 1][2]

    # 가로, 세로 파이프 추가
    if graph[x][y] == 0:
        # 가로로 올 수 있는 건 가로/ 대각선
        dp[x][y][0] = dp[x][y - 1][0] + dp[x][y - 1][1]
        # 세로로 올 수 있는 건 세로, 대각선
        dp[x][y][2] = dp[x - 1][y][1] + dp[x - 1][y][2]

    # 가로에서는 가로 / 대각선만 가능
    # 세로에서는 세로 / 대각선만 가능
    # 대각선에서는 가로 / 세로 / 대각선 다 가능


N = int(input())
# 3차원 그래프 생성
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
# [0, 0, 0] -> 첫번째는 가로 / 두번째는 대각선 / 세번째는 대각선으로 하자

# (0, 1) 자리에는 가로로 오는 게 하나 있기 때문에 1로 해줌
dp[0][1][0] = 1

# 0 번째 행의 경우 세로/ 대각선에서 올 수 없으므로 갈 수 있는 만큼 이동해줌
for idx in range(2, N):
    if graph[0][idx] == 0:
        dp[0][idx][0] = dp[0][idx - 1][0]

# 0 행은 이미 처리해줬고 0 열은 아무것도 오지 않을 거기 때문에 1행, 1열부터 시작해줌
for i in range(1, N):
    for j in range(1, N):
        pipe(i, j)


print(sum(dp[N - 1][N - 1]))



