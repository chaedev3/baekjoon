T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    bar = 0
    cnt = 0
    i = 0
    while i < len(arr):
        if arr[i] == "(" and arr[i+1] == ")":
            cnt += bar
            i += 2
        elif arr[i] == "(":
            bar += 1
            i += 1
        elif arr[i] == ")":
            bar -= 1
            cnt += 1
            i += 1
    print(f'#{tc} {cnt}')