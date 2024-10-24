# 뱀이 벽 or 자기 자신의 몸과 부딪히면 게임이 끝남
# N * N 몇 몇 칸에는 사과 
# 벽으로 둘러싸여 있음
# 뱀의 길이 1 (0, 0) 에 O
# 1) 뱀 길이 1 늘림 -> 머리를 다음칸에 위치시킴
# 2) 이동한 칸에 사과 O, 사과 없어지고 꼬리는 그대로
# 3) 사과 없으면, 꼬리 하나 비워줌 (몸 길이 1되는 거) 
import sys
from collections import deque
input = sys.stdin.readline

# 순서대로 
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0] 

# N: 보드의 크기, K: 사과의 개수
n = int(input())
k = int(input())

apples = []
# K 줄 -> 사과의 위치 (행, 열) (0, 0) 에는 사과 없음
for _ in range(k):
    a, b = map(int, input().split())
    apples.append((a - 1, b - 1)) 


# 뱀의 방향 변환 횟수 L 
l = int(input())
# L 개의 줄, 뱀의 방향 변환 정보 (x, c)
# x 초가 끝난 뒤에 방향으로 90도 회전 시킨다는 뜻 (L - 왼쪽, D - 오른쪽)
directions = []
for _ in range(l):
    a, b = map(str, input().split())
    directions.append([int(a), b])
# 1) -> 인 경우에 (i, j) 오른쪽 회전 (i + 1, j), 3 왼쪽 회전 (i - 1, j), 4
# 2) <- 인 경우에 (i, j) 오른쪽 회전 (i - 1, j), 4 왼쪽 회전 (i + 1, j), 3
# 3) 아래인 경우에 (i, j) 오른쪽 회전 (i, j - 1), 2 왼쪽 회전 (i, j + 1), 1
# 4) 위인 경우에 (i, j) 오른쪽 회전 (i, j + 1), 1 왼쪽 회전 (i, j - 1), 2 
# flag = 0, 1, 2, 3
# 1) flag가 0일 때 -> D 2, L 3 
# 2) flag가 1일 때 -> D 3, L 2
# 3) flag가 2일 때 -> D 1, L 0 
# 4) flag가 3일 때 -> D 0, L 1 

# 시작 
x, y = 0, 0

q = deque()
q.append((x, y))  
# flag 처음엔 오른쪽
flag = 0
result = 0
while True:
    x, y = x + dx[flag], y + dy[flag]
    result += 1
    if 0 > x or x >= n or 0 > y or y >= n:
        break
    if (x, y) in q:
        break

    q.append((x, y))

    if (x, y) in apples:
        apples.remove((x, y))

    elif (x, y) not in apples:
        q.popleft()

    for direction in directions:
        a, b = direction
        if result == a:
            if flag == 0:
                if b == 'D':
                    flag = 2
                else:
                    flag = 3
            elif flag == 1:
                if b == 'D':
                    flag = 3
                else:
                    flag = 2
            elif flag == 2:
                if b == 'D':
                    flag = 1
                else:
                    flag = 0
            elif flag == 3:
                if b == 'D':
                    flag = 0
                else:
                    flag = 1

print(result)