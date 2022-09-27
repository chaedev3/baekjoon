import sys
from collections import deque


# BFS 해서 리프 노드에서 간선의 개수를 셈
# 더한 값이 짝수면 성원이가 못이김
# 홀수면 성원이가 이길 수 있음

def BFS(v):
    global cnt
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        # 연결된 게 하나라는 건 자식이 없다는 뜻 (리프노드라는 뜻)
        # 이미 방문 한 거면 > 0  크니까 !!
        # 처음을 1로 시작해서 -1 해주기
        if len(arr[v]) == 1 and visited[arr[v][0]]:
            cnt += visited[v] - 1
            continue

        # 깊이에 따라 1씩 증가시켜주기
        for i in arr[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)

    return cnt


# 정점의 개수/ 간선의 수는 N - 1
V = int(sys.stdin.readline())
E = V - 1
arr = [[] for _ in range(V + 1)]

# 이렇게 받아오면 되는 건 줄 몰랐다.. 이렇게 또 하나 배웁니다
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

