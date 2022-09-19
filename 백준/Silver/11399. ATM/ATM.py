N = int(input())
person = list(map(int, input().split()))

sorted_list = sorted(person)
total = 0
result = 0
for num in sorted_list:
    total += num
    result += total
print(result)