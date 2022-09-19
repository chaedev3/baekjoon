arr = list(map(int, input().split()))
total = 0
for i in range(5):
    total += arr[i] ** 2
result = total % 10
print(result)