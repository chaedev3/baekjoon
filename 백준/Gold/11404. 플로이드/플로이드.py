import sys
input = sys.stdin.readline
# n: 도시의 개수, m: 버스의 개수
n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    # 똑같은 루트인데 더 비용이 적은 경우가 있기 때문에 이렇게 처리해줌 
    if 0 < graph[start - 1][end - 1] < cost:
        pass
    else:
        graph[start - 1][end - 1] = cost

INF = float('inf')

result = [[INF] * n for _ in range(n)]
# 출발지와 도착지가 같은 경우는 0, 비용이 있는 경우에는 그 비용으로 초기 세팅해줌 
for i in range(n):
    for j in range(n):
        if i == j:
            result[i][j] = 0
        elif graph[i][j] != 0:
            result[i][j] = graph[i][j]

# k를 중간에 거치는 루트로 해서 더 적은 비용으로 갱신해줌 
for k in range(n):
    for i in range(n):
        for j in range(n):
            result[i][j] = min(result[i][j], result[i][k] + result[k][j])

# INF 로 처리된 부분을 0으로 바꿔주고 결과를 출력해줌 
for i in range(n):
    for j in range(n):
        if result[i][j] == INF:
            result[i][j] = 0
        print(result[i][j], end=' ')
    print()

