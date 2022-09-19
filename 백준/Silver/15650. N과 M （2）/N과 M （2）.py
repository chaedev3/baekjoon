def pick(n, picked, to_pick):
    if to_pick == 0:
        return print(*picked)
    if not picked:
        smallest = 1
    else:
        smallest = picked[-1]

    for i in range(smallest, n+1):
        if i not in picked:
            picked.append(i)
            pick(n, picked, to_pick - 1)
            picked.pop()


N, M = map(int, input().split())
num_list = list(range(1, N+1))
pick(N, [], M)