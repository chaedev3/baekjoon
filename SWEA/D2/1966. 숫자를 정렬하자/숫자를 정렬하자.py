T = int(input())


def bubblesort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    sorted_list = bubblesort(num_list, N)
    print(f'#{tc}', *sorted_list)
