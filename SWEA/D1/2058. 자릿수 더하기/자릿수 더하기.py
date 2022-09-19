a = int(input())
i = 0 
while a > 0:
    i += a % 10
    a = a //10 
print(i) 
