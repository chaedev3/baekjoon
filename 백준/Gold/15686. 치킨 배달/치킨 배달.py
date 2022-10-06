from itertools import combinations
# N : N * N 의 도시
# M : 남길 치킨집의 수
N, M = map(int, input().split())
city_list = [list(map(int, input().split())) for _ in range(N)]

# 집은 1, 치킨집은 2
chicken_list = []
house_list = []
for i in range(N):
    for j in range(N):
        if city_list[i][j] == 1:
            house_list.append([i, j])
        elif city_list[i][j] == 2:
            chicken_list.append([i, j])

# chicken_list 에서 M개의 남길 치킨집을 combination을 사용해 구하자
chickens = list(combinations(chicken_list, M))

# 최솟값을 구해보자
result = 10000
for chicken in chickens:
    total = 0
    for house in house_list:
        min_V = 100
        for idx in range(M):
            chicken_distance = abs(house[0] - chicken[idx][0]) + abs(house[1] - chicken[idx][1])
            if chicken_distance < min_V:
                min_V = chicken_distance
        total += min_V
    if result > total:
        result = total

print(result)


