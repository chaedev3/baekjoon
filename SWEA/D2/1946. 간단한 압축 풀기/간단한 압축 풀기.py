T = int(input())

for tc in range(1, T+1):
    N = int(input())
    txt = ''
    for n in range(N):
        a, num = input().split()
        txt += a*int(num)
    print('#{}'.format(tc))
    for i in range(1, len(txt)+1, 10):
        print(txt[i-1:i+10-1]) 