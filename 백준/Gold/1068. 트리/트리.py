import sys

N = int(sys.stdin.readline())
parent_list = list(map(int, sys.stdin.readline().split()))
remove_node = int(sys.stdin.readline())

def dfs(v):
    parent_list[v] = -2
    for i in range(N):
        if parent_list[i] == v:
            dfs(i)

dfs(remove_node)

# 자식 -> 연결 리스트
adjL = [[] for _ in range(N)]

for idx in range(N):
    if parent_list[idx] == -1:
        pass
    elif parent_list[idx] == -2:
        adjL[idx].append(-2)
    else:
        adjL[parent_list[idx]].append(idx)
cnt = 0
for i in range(N):
    if adjL[i] == []:
        cnt += 1
print(cnt)










