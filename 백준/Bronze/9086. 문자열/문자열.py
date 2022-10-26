T = int(input())

for tc in range(T):
    words = list(map(str, input()))
    print(words[0], end='')
    print(words[-1])
