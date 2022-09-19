bingo_list = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부를 number -> 2차원에서 1차원으로 변경
call_list = [list(map(int, input().split())) for _ in range(5)]
call = sum(call_list, [])
# 결과가 될 사회자가 부른 횟수
result = 0


def bingo_count(a_list):
    bingo = 0
    for i in range(5):
        if sum(a_list[i]) == 0:
            bingo += 1
    for j in range(5):
        if sum(b[j] for b in a_list) == 0:
            bingo += 1
    if a_list[1][1] + a_list[2][2] + a_list[3][3] + a_list[4][4] + a_list[0][0] == 0:
        bingo += 1
    if a_list[0][4] + a_list[1][3] + a_list[2][2] + a_list[3][1] + a_list[4][0] == 0:
        bingo += 1
    return bingo


for num in call:
    for i in range(5):
        for j in range(5):
            if bingo_list[i][j] == num:
                bingo_list[i][j] = 0
                result += 1
                bingo = bingo_count(bingo_list)
                if bingo >= 3:
                    print(result)
                    exit()