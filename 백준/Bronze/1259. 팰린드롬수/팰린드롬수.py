import sys
input = sys.stdin.readline

while True:    
    N = int(input())

    if N == 0:
        break
    else:
        str_num = str(N)
        if str_num == str_num[::-1]:
            print('yes')
        else:
            print('no')
 