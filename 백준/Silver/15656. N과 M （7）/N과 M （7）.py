'''
중복 가능
중복되는 수열 여러 번 출력하면 안됨
사전 순으로 증가하는 ..
'''


def recursion(depth):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        result.append(number_list[i])
        recursion(depth + 1)
        result.pop()


N, M = map(int, input().split())
number_list = sorted(list(set(map(int, input().split()))))
result = []

recursion(0)