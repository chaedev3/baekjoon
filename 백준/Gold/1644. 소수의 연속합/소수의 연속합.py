import sys
input = sys.stdin.readline

N = int(input())

a = [0, 0] + [1] * (N - 1)
add_list = [0]

# 에라토스테네스의 체를 이용해 소수의 합 구하기
for i in range(2, N + 1):
    if a[i]:
        number = i + add_list[-1]
        add_list.append(number)
        for j in range(2 * i, N + 1, i):
            a[j] = 0

i, j = 0, 1
result = 0
while j < len(add_list):
    gap = add_list[j] - add_list[i]
    if gap < N:
        j += 1
    elif gap > N:
        i += 1
    else:
        result += 1
        j += 1

print(result)



