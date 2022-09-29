def dijkstra(N, X, adj, d):
    U = [0] * (N + 1)
    U[X] = 1

    for r in range(N + 1):
        d[r] = adj[X][r]

    for _ in range(N):  # N개의 정점 중 출발을 제외한 정점 선택
        minV = INF
        w = 0
        for i in range(N + 1):
            if U[i] == 0 and d[i] < minV:    # 남은 노드 중 비용이 최소인 w
                minV = d[i]
                w = i
        U[w] = 1

        for v in range(1, N + 1):
            if 0 < adj[w][v] < INF:
                d[v] = min(d[v], d[w] + adj[w][v])


N, M, X = map(int, input().split())
INF = 100000
adj1 = [[INF] * (N + 1) for _ in range(N + 1)]
adj2 = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    adj1[i][i] = 0
    adj2[i][i] = 0

for _ in range(M):
    x, y, c = map(int, input().split())
    adj1[x][y] = c
    adj2[y][x] = c

d_out = [0] * (N + 1)
d_in = [0] * (N + 1)
dijkstra(N, X, adj1, d_out)
dijkstra(N, X, adj2, d_in)

result = 0
for idx in range(1, N + 1):
    if (d_in[idx] + d_out[idx]) > result:
        result = d_in[idx] + d_out[idx]
print(result)

