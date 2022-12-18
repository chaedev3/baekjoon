import sys
input = sys.stdin.readline

N, K = map(int, input().split())

cnt = 0
while bin(N).count('1') > K:
    bottles = 1 << bin(N)[::-1].index('1')
    cnt += bottles
    N += bottles

print(cnt)