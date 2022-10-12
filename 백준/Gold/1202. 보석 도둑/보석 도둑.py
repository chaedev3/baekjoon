import heapq
import sys

total_jewel_num, bag_num = map(int, sys.stdin.readline().split())

# 최소힙 배열 -> 보석의 무게를 기준으로 !!
min_heap = []
for _ in range(total_jewel_num):
    heapq.heappush(min_heap, list(map(int, sys.stdin.readline().split())))

# 가지고 있는 가방 -> 오름차순으로 배열
bag_weight_list = [int(sys.stdin.readline()) for _ in range(bag_num)]
bag_weight_list.sort()

max_heap = []
result = 0

for bag in bag_weight_list:
    while min_heap and min_heap[0][0] <= bag:
        heapq.heappush(max_heap, -heapq.heappop(min_heap)[1])
    if max_heap:
        result -= heapq.heappop(max_heap)
    elif not min_heap:
        break
print(result)








