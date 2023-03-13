import sys 
input = sys.stdin.readline

def find_set(x):
    if x == p[x]: 
        return x 
    else: 
        return find_set(p[x]) 
    
def union(x, y):
    link(find_set(x), find_set(y)) 

def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x 
    else:
        p[x] = y

    if rank[x] == rank[y]: 
        rank[y] += 1 


# 집합의 개수 : N + 1, 입력으로 주어지는 연산의 개수 : M 개 
N, M = map(int, input().split())

p = [i for i in range(N + 1)] 
rank = [0 for _ in range(N + 1)] 

for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b) 
    else:
        if find_set(a) == find_set(b):
            print("YES") 
        else:
            print("NO")  