M = int(input())
N = int(input())


num_list = list(range(M, N + 1))

# total = 0
# cnt = 0
a = []
for num in num_list:
    number = []
    for i in range(1, num+1):
        if num % i == 0:
            number.append(i)
    if len(number) == 2:
        a.append(i)

if not a:
    print(-1)
else:
    print(sum(a))
    print(a[0])