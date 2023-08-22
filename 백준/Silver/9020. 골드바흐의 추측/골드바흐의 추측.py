import sys, math 
input = sys.stdin.readline 

# 소수 구하기
arr = [0] * 10001 
arr[1] = 1 
for i in range(2, int(math.sqrt(10001)) + 1):
    if arr[i] == 0:
        for j in range(i * 2, 10001, i):
            arr[j] = 1  



T = int(input()) 
for _ in range(T):
    n = int(input()) 
    for i in range(int(n // 2), 1, -1):
        if arr[i] == 0 and arr[n - i] == 0:
            print(f'{i} {n - i}') 
            break 
