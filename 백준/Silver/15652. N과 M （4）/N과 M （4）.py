'''
중복 가능, 비내림차순(오름차순), 오름차순으로 출력
'''


def recursion(depth):
    if depth == M:
        print(*result)
        return

    for i in range(1, N + 1):
        if depth == 0 or result[-1] <= i:
            result.append(i)
            recursion(depth + 1)
            result.pop()


N, M = map(int, input().split())
result = []
recursion(0)

