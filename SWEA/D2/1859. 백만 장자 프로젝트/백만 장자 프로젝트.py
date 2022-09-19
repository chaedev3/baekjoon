T = int(input())
for tc in range(1, T + 1):
    # 원재쓰가 거래할 수 있는 날
    N = int(input())
    cost_list = list(map(int, input().split()))
    total = 0
    maxV = cost_list[-1]
    # 마지막은 maxV 에 이미 있으니까는 N-2 부터 -1씩 ..
    for i in range(N-2, -1, -1):
        if cost_list[i] > maxV:
            maxV = cost_list[i]
        else:
            total += (maxV - cost_list[i])
    print(f'#{tc} {total}')