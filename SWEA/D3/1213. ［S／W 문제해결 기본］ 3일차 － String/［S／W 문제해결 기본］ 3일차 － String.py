def bruteforce(pattern, text):
    cnt = 0
    for idx in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[idx+j] != pattern[j]:
                break
        else:
            cnt += 1
    return cnt


for i in range(10):
    T = int(input())
    a = input()
    b = input()

    print(f'#{T} {bruteforce(a, b)}')
