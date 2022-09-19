# stack으로 하나씩 append하면서 top과 append하려는 게 같으면 top pop 시키고 append 하지 않음
T = 10
for tc in range(1, T+1):
    N, numbers = map(str, input().split())

    stack1 = []
    for idx in range(len(numbers)):
        # stack1 이 비었는지 아닌지 확인 - 비었으면 그냥 추가해
        if len(stack1) != 0:
            if stack1[-1] == numbers[idx]:
                stack1.pop()
            else:
                stack1.append(numbers[idx])
        else:
            stack1.append(numbers[idx])
    result = ''.join(stack1)
    print(f'#{tc} {result}')