from sys import stdin
N = int(stdin.readline())
height_list = list(map(int, stdin.readline().split()))
stack = [0]
result = [0] * len(height_list)

for idx in range(1, N):
    if height_list[stack[-1]] < height_list[idx]:
        stack.pop()
        if len(stack) > 0:
            for i in range(len(stack)):
                if height_list[stack[-1]] < height_list[idx]:
                    stack.pop()
                else:
                    result[idx] = stack[-1] + 1
                    break
        else:
            stack.append(idx)
        stack.append(idx)
    else:
        result[idx] = stack[-1] + 1
        stack.append(idx)

print(*result)