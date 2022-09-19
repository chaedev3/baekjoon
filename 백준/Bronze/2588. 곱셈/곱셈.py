num1 = int(input()) 
num2 = int(input())

a = num1 // 100 
b = (num1 - (a * 100)) // 10
c = num1 - (a * 100) - (b * 10) 


d = num2 // 100 
e = (num2 - (d * 100)) // 10
f = num2 - (d * 100) - (e * 10) 

print(num1 * f)
print(num1 * e)
print(num1 * d)
print(num1 * num2)