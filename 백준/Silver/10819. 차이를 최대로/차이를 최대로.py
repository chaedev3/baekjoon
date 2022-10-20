N = int(input())
number_list = list(map(int, input().split()))
visited = [0] * (N + 1)
result = []
maxV = 0


def abs_minus(arr):
    total = 0
    for i in range(N - 1):
        total += abs(arr[i] - arr[i + 1])
    return total


def recursion(depth):
    global maxV
    if depth == N:
        if abs_minus(result) > maxV:
            maxV = abs_minus(result)
        return

    for i in range(N):
        if not visited[i]:
            result.append(number_list[i])
            visited[i] = 1
            recursion(depth + 1)
            result.pop()
            visited[i] = 0


recursion(0)
print(maxV)