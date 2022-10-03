def f(i, N):
    global cnt
    # 부분집합이 다 만들어졌으면 부분집합의 합을 구해서 S와 같은지 아닌 지 확인 (같으면 cnt += 1)
    if i == N:
        total = 0  # 부분집합의 합
        for i in range(N):
            if bit[i]:
                total += A[i]
        if total == S:
            cnt += 1
    # 선택할 지 말지 결정 
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

# total = 0 이니까 S 가 0 인 경우에 하나씩 더 카운트됐었음 -> 0 인 경우에만 1 빼줌 
if S == 0:
    print(cnt - 1)
else:
    print(cnt)