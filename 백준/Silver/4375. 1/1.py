import sys 
input = sys.stdin.readline 

while True:
    try:
        N = int(input())
        k = 0
        num = 1 
        while True: 
            if num % N == 0:
                print(len(str(num)))
                break
            else:
                k += 1 
                num += 10 ** k 
    except:
        break 

