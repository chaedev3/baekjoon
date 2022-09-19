T = 10
for tc in range(1, T+1):
    N = int(input())
    word = input()
    stack = []
    result = ''
    for token in word:
        if token.isdecimal():
            result += token
        else:
            if token == "(":
                stack.append(token)
            elif token == ")":
                while stack and stack[-1] != "(":
                    result += stack.pop()
                stack.pop()
            elif token == "*":
                while stack and stack[-1] == "*":
                    result += stack.pop()
                stack.append(token)
            elif token == "+":
                while stack and stack[-1] != "(":
                    result += stack.pop()
                stack.append(token)
    while stack:
        result += stack.pop()

    for r in result:
        if r.isdecimal():
            stack.append(int(r))
        else:
            p1 = stack.pop()
            p2 = stack.pop()
            if r == "+":
                stack.append(p2 + p1)
            elif r == "*":
                stack.append(p2 * p1)
    print(f'#{tc} {stack[-1]}')