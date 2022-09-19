texts = []
while True:
    words = input()
    if words == '.':
        break
    else:
        texts.append(words)


for words in texts:
    stack = []
    for word in words:
        if word == "[" or word == "(":
            stack.append(word)
        elif word == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(word)
                break
        elif word == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(word)
                break

    if len(stack) == 0:
        result = 'yes'
    else:
        result = 'no'

    print(result)
