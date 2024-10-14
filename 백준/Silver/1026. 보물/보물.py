import sys
input = sys.stdin.readline

n = int(input())
a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())))

total = 0
for i in range(n):
    total += a_list[i] * b_list[n - i - 1]

print(total)

