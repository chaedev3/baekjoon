import sys, math 
input = sys.stdin.readline

T = int(input())

arr = [0] * 1299710 
arr[1] = 1 
for i in range(2, len(arr)):
    if arr[i] == 0:
        for j in range(i * 2, len(arr), i):
            arr[j] = 1  

for _ in range(T):
    k = int(input()) 
    if arr[k] == 0:
        print(0) 
    else:
        i = k
        j = k 
        result = 0
        while True:
            i -= 1 
            if arr[i] == 0:
                result += 1
                break 
            else:
                result += 1 
        
        while True: 
            j += 1 
            if arr[j] == 0:
                result += 1
                break 
            else: 
                result += 1
        print(result) 

