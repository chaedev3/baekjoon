import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    r, c = map(int, input().split())
    x = max(r, c)
    y = min(r, c)
    answer = []

    if y == 1:
        print(x, x-1)

    else:
        if y == x:
            answer.append(((y*(y+1)*(2*y+1))//6)*2 - y*y)
            answer.append(((y*(y+1)*(2*y+1))//6)*2 - y*y - y)

        else:
            answer.append(((y*(y+1)*(2*y+1))//6)*2 - y*y + (y*y)*(x-y))
            answer.append(((y*(y+1)*(2*y+1))//6)*2 - y*y - y + (y*y)*(x-y))

        print(int(max(answer)), int(min(answer)))