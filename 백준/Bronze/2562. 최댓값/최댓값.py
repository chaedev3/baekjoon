from sys import stdin
arr = [int(stdin.readline()) for _ in range(9)]
maxV = 0
i = 0
for idx, number in enumerate(arr, start=1):
    if number > maxV:
        i, maxV = idx, number

print(maxV)
print(i)
