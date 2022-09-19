N = int(input())
command_list = [list(map(str, input().split())) for _ in range(N)]


queue = []
for idx in range(len(command_list)):
    if command_list[idx][0] == 'push':
        queue.append(command_list[idx][1])
    elif command_list[idx][0] == 'pop':
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif command_list[idx][0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif command_list[idx][0] == 'size':
        print(len(queue))
    elif command_list[idx][0] == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif command_list[idx][0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)


