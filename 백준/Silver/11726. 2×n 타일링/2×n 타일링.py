# 생각해보면 그냥 피보나치 구현 문제임
# bottom up
N = int(input())

d = [0] * (N + 2)
d[1] = 1
d[2] = 2
for idx in range(3, N + 1):
    d[idx] = d[idx-1] + d[idx-2]
# 문제에서 10007 로 나눈 나머지를 구하라고 했으니까 그대로 
print(d[N] % 10007)
