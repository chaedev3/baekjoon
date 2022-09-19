T = int(input())


def bruteforce(pattern, text):
    result = 0
    cnt = 0
    for idx in range(len(text) - len(pattern) + 1):
        if text[cnt:len(pattern)+cnt] == pattern:
            result += 1
            cnt = len(pattern) + cnt - 1
        cnt += 1
    return len(text) - result * len(pattern) + result


for tc in range(1, T+1):
    A, B = map(str, input().split())
    print(f'#{tc} {bruteforce(B, A)}')
