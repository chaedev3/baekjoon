import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

V = int(input())
E = V - 1
parent = [-1] * (V + 1)
tree = [[] for _ in range(V + 1)]
for _ in range(E):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)


def DFS(node):
    for c in tree[node]:
        if parent[c] == -1:
            parent[c] = node
            DFS(c)

DFS(1)

for i in range(2, V + 1):
    print(parent[i])


