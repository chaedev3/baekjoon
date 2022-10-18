'''
중복 가능
- visited 없어도 됨
'''


def recursion(depth):
    if depth == M:
        print(*result)
        return

    for i in range(1, N + 1):
        result.append(i)
        recursion(depth + 1)
        result.pop()


N, M = map(int, input().split())
result = []

recursion(0)
