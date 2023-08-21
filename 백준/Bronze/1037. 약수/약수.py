import sys, math  
input = sys.stdin.readline 

# N : 진짜 약수의 개수 
N = int(input())
divisors = sorted(list(map(int, input().split())))

print(divisors[0] * divisors[-1]) 