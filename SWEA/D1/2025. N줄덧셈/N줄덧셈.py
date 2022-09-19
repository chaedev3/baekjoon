num = int(input())
if num >= 10000:
    num = 0 

result = 0 
for i in range(num + 1):
    result = result + i 

print(result)  