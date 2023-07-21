import sys
input = sys.stdin.readline 


def find_set(x):
    if x != p[x]:
        # 부모를 바꾸고
        p[x] = find_set(p[x])
    # 부모를 출력
    return p[x]

def union(x, y):
    parent_x = find_set(x) 
    parent_y = find_set(y) 

    if parent_x < parent_y:
        p[parent_y] = parent_x 
    else:
        p[parent_x] = parent_y

# 도시의 수 N
N = int(input())

# 여행 계획에 속한 도시들의 수 M 
M = int(input())

# 0 이면 연결되지 않은 것, 1이면 연결된 것 
p = [i for i in range(N)] 


for i in range(N):
    connect_info = list(map(int, input().split())) 
    for j in range(N):
        if connect_info[j] == 1:
            union(i, j) 

parent = [-1] + p 


# 마지막 줄에는 여행 계획!! 
trip_info = list(map(int,input().split())) 

for i in range(1, M):
    if parent[trip_info[i]] != parent[trip_info[0]]:
        print("NO")
        break 
else:
    print("YES") 

