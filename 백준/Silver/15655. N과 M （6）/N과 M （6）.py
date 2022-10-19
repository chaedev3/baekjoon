'''
중복 불가능
오름차순으로 출력해야됨
'''


def recursion(depth):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        if visited[i] == 0:
            if depth == 0 or result[-1] <= number_list[i]:
                result.append(number_list[i])
                visited[i] = 1
                recursion(depth + 1)
                result.pop()
                visited[i] = 0


N, M = map(int, input().split())
number_list = sorted(list(map(int, input().split())))
visited = [0] * (N + 1)
result = []

recursion(0)