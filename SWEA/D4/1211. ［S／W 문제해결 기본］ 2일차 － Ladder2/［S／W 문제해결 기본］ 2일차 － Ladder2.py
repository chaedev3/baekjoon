import copy


for tc in range(1, 11):
    N = int(input())
    ladder_list = [list(map(int, input().split())) for _ in range(100)]
    reverse = []
    for r in range(100):
        reverse.append([])
        for c in range(100):
            reverse[r].append(ladder_list[c][r])
    idx_list = []
    for a in range(100):
        if reverse[a] == [1] * 100:
            idx_list.append(a)

    # 하좌우
    di = [1, 0, 0]
    dj = [0, -1, 1]
    minV = 10000000
    for j in idx_list:
        i = 0
        cnt = 0
        copy_ladder = copy.deepcopy(ladder_list)
        b = j
        while i < 99:
            for d in range(3):
                row = i + di[d]
                col = j + dj[d]
                cnt += 1
                # 벗어나지 않도록 조건 설정
                if 0 <= row < 100 and 0 <= col < 100:
                    if copy_ladder[row][col] == 1:
                        i = row
                        j = col
                        # 그래서 지나는 길은 0으로 바꿔줌
                        copy_ladder[row][col] = 0
        else:
            if cnt < minV:
                minV = cnt
                result = b
    print(f'#{tc} {result}')