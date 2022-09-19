T = int(input())
for tc in range(1, T+1):
    # 카운팅 정렬로 풀기 !!
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    one_to_nine = [1] * 9
    result = 1
    # 행/열 우선 순회
    for i in range(9):
        cnt_row = [0] * 10
        cnt_column = [0] * 10
        for j in range(9):
            cnt_row[puzzle[i][j]] += 1
            cnt_column[puzzle[j][i]] += 1
        if cnt_row[1:] != one_to_nine:
            result = 0
            break
        if cnt_column[1:] != one_to_nine:
            result = 0
            break

    # 3 * 3
    for r in range(0, 7, 3):
        for c in range(0, 7, 3):
            square_list = [0] * 10
            for di in range(3):
                for dj in range(3):
                    square_list[puzzle[r+di][c+dj]] += 1
            if square_list[1:] != one_to_nine:
                result = 0
                break
    print(f'#{tc} {result}')