def inorder(n):
    if n:
        inorder(ch1[n])
        print(arr[n-1][1], end='')
        inorder(ch2[n])


T = 10
for tc in range(1, T+1):
    V = int(input())
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    arr = [list(map(str, input().split())) for _ in range(V)]
    for idx in range(V):
        if len(arr[idx]) == 3:
            ch1[int(arr[idx][0])] = int(arr[idx][2])
        if len(arr[idx]) == 4:
            ch1[int(arr[idx][0])] = int(arr[idx][2])
            ch2[int(arr[idx][0])] = int(arr[idx][3])

    print(f'#{tc}', end=' ')
    inorder(1)
    print()
