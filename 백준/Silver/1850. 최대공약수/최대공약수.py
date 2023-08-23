import sys
input = sys.stdin.readline 

def gcd(x, y): 
    while y != 0:
        x, y = y, x % y 
    return x 

A, B = map(int, input().split()) 
print('1' * gcd(A, B)) 
