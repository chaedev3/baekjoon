import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1] 
t = 0 
while True:
    # n이 0이 입력되면 전체 입력 중단
    n = int(input())
    t += 1 
    if n == 0:
        break

    loopy_list = [list(map(int, input().split())) for _ in range(n)]

    # 최소 루피를 담는 리스트
    distance = [[INF] * n for _ in range(n)]

    # 시작점은 0,0 -> 끝 점은 n-1, n-1
    x, y = 0, 0
    q = [(loopy_list[x][y], x, y)]
    distance[x][y] = loopy_list[x][y]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = loopy_list[nx][ny] + dist
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    print(f'Problem {t}: {distance[n-1][n-1]}')