import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    heap.append(int(input()))

heapq.heapify(heap)

total = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap) 
    total +=  a + b
    heapq.heappush(heap, a + b) 

print(total)