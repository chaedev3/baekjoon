from collections import deque

N = int(input())
command_list = [list(map(str, input().split())) for _ in range(N)]
q = deque()
for idx in range(len(command_list)):
    if command_list[idx][0] == 'push_front':
        q.appendleft(command_list[idx][1])
    elif command_list[idx][0] == 'push_back':
        q.append(command_list[idx][1])
    elif command_list[idx][0] == 'pop_front':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif command_list[idx][0] == 'pop_back':
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)
    elif command_list[idx][0] == 'size':
        print(len(q))
    elif command_list[idx][0] == 'empty':
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif command_list[idx][0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif command_list[idx][0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)

