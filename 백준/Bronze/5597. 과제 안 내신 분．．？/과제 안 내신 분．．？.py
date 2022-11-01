num_list = list(range(1, 31))

for _ in range(28):
    N = int(input())
    num_list.remove(N)


for i in range(2):
    print(num_list[i])

