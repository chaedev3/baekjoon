N, M = map(int, input().split())
chess_list = [list(map(str, input())) for _ in range(N)]

chess1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
chess2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

cnt1_list = []
cnt2_list = []

for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for a in range(8):
            for b in range(8):
                if chess_list[i + a][j + b] != chess1[a][b]:
                    cnt1 += 1
                if chess_list[i + a][j + b] != chess2[a][b]:
                    cnt2 += 1
        cnt1_list.append(cnt1)
        cnt2_list.append(cnt2)


print(min(min(cnt1_list), min(cnt2_list)))
