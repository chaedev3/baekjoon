A, B = map(int, input().split())

cnt = 1
while A < B:
    if str(B)[-1] == '1':
        B = (B // 10)
        cnt += 1
    else:
        if B % 2 != 0:
            break
        else:
            B = (B // 2)
            cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)
