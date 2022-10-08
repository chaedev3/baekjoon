import heapq
import sys

# input 받기, min_heap/ max_heap / 삭제한건지를 표시하는 visited 를 정의해줌
T = int(sys.stdin.readline())
for tc in range(T):
    k = int(sys.stdin.readline())
    min_heap, max_heap = [], []
    visited = [0] * k
    for i in range(k):
        calc_str, number = map(str, sys.stdin.readline().split())

        # I 면 추가해주는 것
        if calc_str == "I":
            heapq.heappush(min_heap, (int(number), i))
            heapq.heappush(max_heap, (-int(number), i))
            visited[i] = 1
        else:
            if number == "1":
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)

            elif number == "-1":
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
                    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if len(min_heap) == 0 or len(max_heap) == 0:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])


