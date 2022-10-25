import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    for num in list(map(int, input().split())):
        heapq.heappush(heap, num)
        if len(heap) > N:
            heapq.heappop(heap)

print(heap[0])