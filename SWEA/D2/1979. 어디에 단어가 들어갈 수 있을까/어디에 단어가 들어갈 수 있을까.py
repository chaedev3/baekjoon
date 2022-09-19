T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 행 우선 순회
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            # 딱 K개만 필요하니까 (K보다 커도 작아도 안됨) 0인 경우에 그전까지 cnt가 3이면
            # result에 +1 하고 마지막 index의 경우는 거기까지 3이 안되면 끝인 거니까..
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                if puzzle[i][j] == 0:
                    # 초기화시켜줌
                    cnt = 0

    # 열 우선 순회
    for j in range(N):
        cnt = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or i == N-1:
                if cnt == K:
                    result += 1
                if puzzle[i][j] == 0:
                    # 초기화시켜줌
                    cnt = 0

    print(f'#{tc} {result}')