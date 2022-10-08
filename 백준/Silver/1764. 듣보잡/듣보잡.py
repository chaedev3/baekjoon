N, M = map(int, input().split())
not_listen_list = [input() for _ in range(N)]
not_see_list = [input() for _ in range(M)]

not_see_and_listen = list(set(not_listen_list) & set(not_see_list))

print(len(not_see_and_listen))
for i in sorted(not_see_and_listen):
    print(i)