import sys, heapq
input = sys.stdin.readline
INF = int(1e9) 

# 최소 스패닝 트리 문제?
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) 
    return parent[x] 

def add_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())

parent = [0] * (n + 1)

# 자기 자신
for i in range(1, n + 1):
    parent[i] = i

x = []
y = []
z = [] 
# 거리를 저장해야댐!!
for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

edges = [] 

for i in range(n - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))     
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1])) 
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1])) 

result = 0

edges.sort()

for edge in edges:
    dist, x, y = edge 
    if find_parent(parent, x) != find_parent(parent, y):
        result += dist
        add_parent(parent, x, y)

print(result) 