N = int(input())

member_list = [tuple(map(str, input().split())) for _ in range(N)]

sorted_list = sorted(member_list, key=lambda x: int(x[0]))

for age, name in sorted_list:
    print(age, name)