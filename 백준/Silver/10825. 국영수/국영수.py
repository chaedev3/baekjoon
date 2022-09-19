N = int(input())
score_list = [tuple(map(str, input().split())) for _ in range(N)]
sorted_list = sorted(score_list, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for idx in range(N):
    print(sorted_list[idx][0])