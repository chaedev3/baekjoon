T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus_station = [0] * 5001
    for i in range(1, N+1):
        Ai, Bi = map(int, input().split())
        for j in range(Ai, Bi + 1):
            bus_station[j] += 1

    P = int(input())
    c_list = []
    for i in range(1, P+1):
        C = int(input())
        c_list.append(bus_station[C])

    print(f'#{tc}', *c_list)