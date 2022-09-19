T = 10
for _ in range(T):
    tc = int(input())
    que = list(map(int, input().split()))
    i = 1
    while True:
        if i > 5:
            i = 1
        pop_que = que.pop(0) - i
        if pop_que <= 0:
            que.append(0)
            break
        que.append(pop_que)
        i += 1
    print(f'#{tc}', *que)