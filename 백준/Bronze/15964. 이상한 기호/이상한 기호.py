def cir(a, b):
    return (a + b) * (a - b)


A, B = map(int, input().split())
print(cir(A, B))
