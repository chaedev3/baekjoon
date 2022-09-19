def is_not_diagonal(picked, i):
    for idx, num in enumerate(picked):
        if abs(num - i) == abs(idx - len(picked)):
        # if abs(int((num - i) / (idx - len(picked)))) == 1:
            return False
    return True


def pick(n, picked, to_pick):
    global cnt
    if to_pick == 0:
        cnt += 1
        return

    for i in range(n):
        if i not in picked:
            if is_not_diagonal(picked, i):
                picked.append(i)
                pick(n, picked, to_pick - 1)
                picked.pop()


N = int(input())
cnt = 0
pick(N, [], N)
print(cnt)
