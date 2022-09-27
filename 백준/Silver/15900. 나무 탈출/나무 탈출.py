import sys
from collections import deque


def BFS(v):
    global cnt
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        # 연결된 게 하나라는 건 자식이 없다는 뜻 (리프노드라는 뜻)
        # 이미 방문 한 거면 > 0  크니까 !!
        if len(arr[v]) == 1 and visited[arr[v][0]]:
            cnt += visited[v] - 1
            continue

        for i in arr[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)

    return cnt


V = int(sys.stdin.readline())
E = V - 1
arr = [[] for _ in range(V + 1)]
for _ in range(E):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
cnt = 0
visited = [0] * (V + 1)
BFS(1)

if cnt % 2 == 0:
    print("No")
else:
    print("Yes")


