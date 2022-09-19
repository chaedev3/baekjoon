n = int(input())
num = n
result = 0  

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    result += 1 
    if(num == n):
        break

print(result)  