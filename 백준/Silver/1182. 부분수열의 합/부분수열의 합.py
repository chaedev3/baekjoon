def f(i, N):
    global cnt
    if i == N:
        s = 0  # 부분집합의 합
        for i in range(N):
            if bit[i]:
                s += A[i]
        if s == S:
            cnt += 1
    else:
        candidate = [0, 1]
        for x in candidate:
            bit[i] = x
            f(i+1, N)


N, S = map(int, input().split())
A = list(map(int, input().split()))
bit = [0] * N
cnt = 0
f(0, N)
if S == 0:
    print(cnt - 1)
else:
    print(cnt)