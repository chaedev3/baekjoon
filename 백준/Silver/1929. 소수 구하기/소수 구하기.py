import sys, math
input = sys.stdin.readline 

M, N = map(int, input().split()) 

array = [0] * (N + 1) 

for i in range(2, int(math.sqrt(N)) + 1):
    if array[i] == 0:
        for j in range(i * 2, N + 1, i):
            array[j] = 1 
    

for i in range(M, N + 1): 
    if array[i] == 0  and i != 1: 
        print(i) 