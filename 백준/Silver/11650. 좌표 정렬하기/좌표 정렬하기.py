N = int(input())
xy_list = [tuple(map(int, input().split())) for _ in range(N)]

sorted_list = sorted(xy_list, key=lambda x: (x[0], x[1]))

for a, b in sorted_list:
    print(a, b)
