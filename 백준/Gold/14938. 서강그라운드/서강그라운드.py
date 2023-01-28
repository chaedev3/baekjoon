import sys
input = sys.stdin.readline

# n: 지역의 개수, m: 수색범위, r: 길의 개수
n, m, r = map(int, input().split())

# 아이템의 수를 담은 list
items_count = list(map(int, input().split()))

graph = [[0] * n for _ in range(n)]

for _ in range(r):
    start, end, length = map(int, input().split())
    graph[start - 1][end - 1] = length
    graph[end - 1][start - 1] = length

INF = float('inf')
result = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            result[i][j] = 0
        elif graph[i][j] > 0:
            result[i][j] = graph[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            result[i][j] = min(result[i][j], result[i][k] + result[k][j])


total_list = []
for i in range(n):
    total = 0
    for j in range(n):
        if result[i][j] <= m:
            total += items_count[j]
    total_list.append(total)

print(max(total_list))

