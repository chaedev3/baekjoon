import sys
input = sys.stdin.readline

# 집의 개수
n = int(input())
house_list = list(map(int, input().split())) 

# 오름차순으로 정렬
house_list.sort()

def add_house(k):
    total = 0
    for house in house_list:
        total += abs(k - house)
    return total 

# 중앙값 찾아!
if n % 2 == 0:
    middle1 = house_list[n // 2]
    middle2 = house_list[(n // 2) - 1]
    if add_house(middle1) >= add_house(middle2):
        middle = middle2
    else:
        middle = middle1 
else:
    middle = house_list[n // 2] 

print(middle)