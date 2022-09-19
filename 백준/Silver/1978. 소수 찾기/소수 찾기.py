N = int(input())

num_list = list(map(int, input().split()))

cnt = 0
for num in num_list:
    number = []
    for i in range(1, num+1):
        if num % i == 0:
            number.append(i)
    if len(number) == 2:
        cnt += 1
print(cnt)