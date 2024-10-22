import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * n for _ in range(n)]
for i in range(n):
    a_list = list(map(int, input().split()))
    for j in range(len(a_list)):
        arr[i][j] = a_list[j]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            arr[i][j] += arr[i - 1][j]
        elif j == i:
            arr[i][j] += arr[i - 1][j - 1] 
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - 1]) + arr[i][j]
    
print(max(arr[n - 1])) 