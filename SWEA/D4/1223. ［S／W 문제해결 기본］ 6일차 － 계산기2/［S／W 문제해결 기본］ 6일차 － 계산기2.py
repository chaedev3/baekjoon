T = 10
for tc in range(1, T+1):
    # 총 길이
    N = int(input())
    infix = input()
    stack1 = []
    stack2 = []
    result = ''
    for i in range(N):
        if infix[i].isdecimal():
            result += infix[i]
        else:
            if not stack1:
                stack1.append(infix[i])
            elif infix[i] == "*":
                while stack1 and stack1[-1] == "*":
                    result += stack1.pop()
                stack1.append(infix[i])
            elif infix[i] == "+":
                while stack1:
                    result += stack1.pop()
                stack1.append(infix[i])
    while stack1:
        result += stack1.pop()

    for r in result:
        if r.isdecimal():
            stack2.append(int(r))
        else:
            p1 = stack2.pop()
            p2 = stack2.pop()
            if r == "+":
                stack2.append(p2 + p1)
            elif r == "*":
                stack2.append(p2 * p1)
    print(f'#{tc} {stack2[-1]}')