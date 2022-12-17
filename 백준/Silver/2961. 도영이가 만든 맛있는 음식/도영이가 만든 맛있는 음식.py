from itertools import combinations
import sys
input = sys.stdin.readline

# 1. 비트 마스킹을 사용하지 않은 경우

# input 받기
# N : 재료의 개수
N = int(input())
# 신맛과 쓴맛이 담긴 리스트
taste_list = [list(map(int, input().split())) for _ in range(N)]
combs = [combinations(taste_list, i) for i in range(1, N + 1)]

diff = 10 ** 7 + 1

for comb in combs:
    for c in comb:
        sour_result = 1
        bitter_result = 0
        for s, b in c:
            sour_result *= s
            bitter_result += b
        if abs(sour_result - bitter_result) < diff:
            diff = abs(sour_result - bitter_result)
print(diff)






