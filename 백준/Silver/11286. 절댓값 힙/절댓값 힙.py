import heapq
import sys

N = int(sys.stdin.readline())
heap = []
heapq.heapify(heap)
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if not heap:
            print(0)
        else:
            pop_num = heapq.heappop(heap)[1]
            print(pop_num)
    else:
        heapq.heappush(heap, (abs(num), num))

