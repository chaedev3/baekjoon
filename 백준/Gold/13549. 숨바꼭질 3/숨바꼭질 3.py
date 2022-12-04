import heapq, sys
input = sys.stdin.readline

INF = 10 ** 7
# N : 수빈이가 있는 위치
# K : 동생이 있는 위치
N, K = map(int, input().split())
visited = [INF] * 100001


def dijkstra(start, end):
    visited[start] = 0
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, start))

    while heap:
        cnt, s = heapq.heappop(heap)

        for next_num in [(s + 1, 1), (s - 1, 1), (s * 2, 0)]:
            if 0 <= next_num[0] < 100001 and visited[next_num[0]] > cnt + next_num[1]:
                visited[next_num[0]] = cnt + next_num[1]
                heapq.heappush(heap, (visited[next_num[0]], next_num[0]))
    print(visited[end])


dijkstra(N, K)






