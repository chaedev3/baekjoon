T = int(input())
for tc in range(1, T+1):
    dal, P = map(int, input().split())
    P_list = [0] * P
    for i in range(P):
        P_list[i] = dal // P

    for j in range(P):
        if dal - P * (dal // P) > 0:
            P_list[j] += 1
            if sum(P_list) == dal:
                break

    total = P_list[0]
    for idx in range(1, P):
        total = total * P_list[idx]

    print(f'#{tc} {total}')