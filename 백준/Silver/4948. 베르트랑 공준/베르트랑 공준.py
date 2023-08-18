import sys, math
input = sys.stdin.readline 

while True: 
    n = int(input())
    if n == 0:
        break 
    else:
        array = [0] * (2 * n + 1) 
        for i in range(2, int(math.sqrt(n* 2)) + 1):
            if array[i] == 0: 
                for j in range(2 * i, 2 * n + 1, i):
                    array[j] = 1
    if n == 1:
        print(1) 
    else:
        arr = array[n + 1: 2 * n + 1]
        print(arr.count(0))  