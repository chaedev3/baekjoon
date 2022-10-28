import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())


def recursion(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        result = recursion(a, b // 2, c)
        return (result*result) % c
    elif b % 2 == 1:
        result = recursion(a, b // 2, c)
        return (result*result*a) % c


print(recursion(A, B, C))