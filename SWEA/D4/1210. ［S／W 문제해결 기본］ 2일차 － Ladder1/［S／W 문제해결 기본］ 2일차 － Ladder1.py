for tc in range(1, 11):
    N = int(input())
    # 가로로 받아짐
    ladder_list = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점 X 의 index를 찾기
    for j in range(100):
        if ladder_list[99][j] == 2:
            break

    # X를 기준으로 따라서 올라오면 되지 않을까?!
    i = 99
    # 상좌우
    di = [-1, 0, 0]
    dj = [0, -1, 1]
    while i > 0:
        for d in range(3):
            row = i + di[d]
            col = j + dj[d]
            if 0 <= row < 100 and 0 <= col < 100:
                if ladder_list[row][col] == 1:
                    # 이렇게만 하면 문제가 생김 -> 계속 같은 곳을 맴돌게됨 .. 좌or 우로 이동을 했으면 그 다음에 또 좌우에 1이
                    # 있기 때문!!
                    i = row
                    j = col
                    ladder_list[row][col] = 0
    print(f'#{tc} {col-1}')