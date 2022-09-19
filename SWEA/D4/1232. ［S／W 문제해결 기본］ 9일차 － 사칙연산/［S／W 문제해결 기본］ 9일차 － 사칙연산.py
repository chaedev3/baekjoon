def postorder(n):
    global order_list
    if n > 0:
        postorder(ch1[n])
        postorder(ch2[n])
        order_list.append(n)


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    calc_list = [0] * (N + 1)
    for idx in range(N):
        if len(arr[idx]) == 2:
            calc_list[int(arr[idx][0])] = int(arr[idx][1])
        elif len(arr[idx]) == 4:
            calc_list[int(arr[idx][0])] = arr[idx][1]
            ch1[int(arr[idx][0])] = int(arr[idx][2])
            ch2[int(arr[idx][0])] = int(arr[idx][3])
    order_list = []
    postorder(1)
    calc = []
    for order in order_list:
        calc.append(str(calc_list[order]))
    stack = []
    # 이제 후위 계산 고고싱
    for char in calc:
        if char.isnumeric():
            stack.append(int(char))
        else:
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)
    print(f'#{tc} {int(stack[-1])}')












































































