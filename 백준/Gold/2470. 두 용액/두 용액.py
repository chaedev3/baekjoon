import sys 
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

maxV = 10 ** 10 
result = [] 

a = 0 
b = N - 1 

while a < b:
    if abs(arr[a] + arr[b]) <= maxV:
        maxV = abs(arr[a] + arr[b])
        result = [arr[a], arr[b]]
    if arr[a] + arr[b] > 0:
        b -= 1 
    elif arr[a] + arr[b] < 0: 
        a += 1 
    else: 
        break 

print(*result)