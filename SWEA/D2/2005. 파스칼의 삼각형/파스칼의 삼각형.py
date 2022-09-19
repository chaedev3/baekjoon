# 테스트케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # N * N 짜리 빈 배열 만들어줌
    arr = [[0] * N for _ in range(N)]
    # 양 끝에는 1, 중앙 값은 위의 있는 두개의 합
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    # 한 줄씩 출력
    print(f'#{tc}')
    # 0이 아닌 값들만 출력
    for lst in arr:
        result = [x for x in lst if x]
        print(*result)