T = int(input())

# 우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    # N * N 의 빈 리스트 만들어줌
    num_list = [[0] * N for _ in range(N)]
    # 초기값 설정 [i][j] 로 [0][0] 부터 시작
    i = 0
    j = 0
    idx = 0  # di, dj (우 하 좌 상)
    # 1~ N^2 의 값들을 할당하기 위함
    for n in range(1, N*N + 1):
        num_list[i][j] = n
        # di, dj 를 더해줌으로써 우측으로 이동할 수 있도록 0 0 -> 0 1 -> 0 2 -> 0 3..
        i += di[idx]
        j += dj[idx]
        # 3 * 3 으로 예를 들자면 0 3 까지 가면 안됨 - 만약 넘었으면 다시 빼주고 idx를 +1 해줌
        # % 4 를 한 이유는 계속 + 가 되기 때문에 0 1 2 3 에서만 돌도록 만들어주기 위함
        # 즉, 범위를 넘으면 다시 그 전으로 원상복귀하고 방향 바꿔서 더함
        if i < 0 or j < 0 or i >= N or j >= N or num_list[i][j] != 0:
            i -= di[idx]
            j -= dj[idx]
            idx = (idx + 1) % 4

            i += di[idx]
            j += dj[idx]

    print(f'#{tc}')
    for num in num_list:
        print(*num)

