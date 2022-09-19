for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 최대값 
    maxV = 0
    # 대각선의 합 구하기
    diagonal = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                diagonal += arr[i][j] 
    # 대각선의 합이 더 크다면 최대값 바꿈 
    if diagonal > maxV:
        maxV = diagonal


    # 반대쪽 대각선
    diagonal_reverse = 0
    for i in range(100):
        for j in range(100):
            if i == 99 - j:
                diagonal_reverse += arr[i][j]
    if diagonal_reverse > maxV:
        maxV = diagonal_reverse


    # 행의 합, 열의 합
    for i in range(100):
        sum_row = 0
        sum_column = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_column += arr[j][i]
        if sum_row > maxV:
            maxV = sum_row
        if sum_column > maxV:
            maxV = sum_column
    print(f'#{N} {maxV}')