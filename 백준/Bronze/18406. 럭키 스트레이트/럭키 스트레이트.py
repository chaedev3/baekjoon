import sys
input = sys.stdin.readline

N = list(map(int, input().strip()))

half = len(N) // 2 

first_half = sum(N[:half])

second_half = sum(N[half:])

if first_half == second_half:
    print("LUCKY")
else:
    print("READY")