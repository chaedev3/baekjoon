# input 받기
N, M = map(int, input().split())


# 순서가 없는 복원 추출
def pick(n, picked, to_pick):
    if to_pick == 0:
        return print(*picked)

    if not picked:
        smallest = 1
    else:
        smallest = picked[-1]

    # smallest = 0 if not picked else picked[-1]

    for i in range(smallest, n + 1):
        picked.append(i)
        pick(n, picked, to_pick - 1)
        picked.pop()


pick(N, [], M)
