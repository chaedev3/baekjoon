import sys
from collections import deque


def BFS(start, end):
    q = deque()
    q.append((start, 0))

    # set 으로 받아줌 (똑같은 값 안 받으려고)
    visited = set()
    visited.add(start)

    while q:
        start, cnt = q.popleft()
        # + 1 하는 경우 / -1 하는 경우 / * 2 하는 경우
        # 같아지면 cnt + 1
        if start == end:
            return cnt
        for next_num in (start + 1, start - 1, start * 2):
            if 0 <= next_num <= 100000 and next_num not in visited:
                visited.add(next_num)
                q.append((next_num, cnt + 1))


# input 받기
N, M = map(int, sys.stdin.readline().split())
print(BFS(N, M))
