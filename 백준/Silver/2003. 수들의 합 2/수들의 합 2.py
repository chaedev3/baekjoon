import sys 
input = sys.stdin.readline

# N:수열의 개수, M  
N, M = map(int, input().split())

arr = list(map(int, input().split()))
sum_arr = [0] 
for a in arr:
    sum_arr.append(a + sum_arr[-1]) 

a, b = 0, 1 
result = 0 
while b < N + 1:  
    gap = sum_arr[b] - sum_arr[a] 
    if gap > M:
        a += 1 
    elif gap < M:
        b += 1  
    else:
        result += 1
        b += 1

print(result)