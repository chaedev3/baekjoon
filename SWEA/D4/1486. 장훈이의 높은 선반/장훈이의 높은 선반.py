T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    height_list = list(map(int, input().split()))
    result = 100000000
    for i in range(1 << N):
        total = 0
        for j in range(N):
            if i & (1 << j):
                total += height_list[j]
        if total >= B:
            if result > total - B:
                result = total - B
    print(f'#{tc} {result}')