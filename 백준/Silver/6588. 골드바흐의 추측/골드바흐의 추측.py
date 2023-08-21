import sys, math 
input = sys.stdin.readline

arr = [0] * 1000001
arr[1] = 1 
for i in range(2, int(math.sqrt(1000001)) + 1): 
    if arr[i] == 0:
        for j in range(i * 2, len(arr), i):
            arr[j] = 1  

while True:
    n = int(input())
    if n == 0: 
        break 
    else:   
        for i in range(3, int(n / 2) + 1, 2):
            if arr[i] == 0 and arr[n - i] == 0: 
                print(f'{n} = {i} + {n - i}') 
                break 
        else:
            print("Goldbach's conjecture is wrong.")