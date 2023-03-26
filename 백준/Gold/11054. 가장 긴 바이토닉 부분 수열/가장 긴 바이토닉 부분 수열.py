import sys 
input = sys.stdin.readline


N = int(input()) 
numbers = list(map(int, input().split()))
reverse_numbers = numbers[::-1] 

dp_one = [0 for _ in range(N)]
dp_two = [0 for _ in range(N)] 
for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j] and dp_one[i] < dp_one[j]:
            dp_one[i] = dp_one[j] 
        elif reverse_numbers[i] > reverse_numbers[j] and dp_two[i] < dp_two[j]:
            dp_two[i] = dp_two[j] 
    dp_one[i] += 1 

for i in range(N):
    for j in range(i):
        if reverse_numbers[i] > reverse_numbers[j] and dp_two[i] < dp_two[j]:
            dp_two[i] = dp_two[j] 
    dp_two[i] += 1 

result = 0 
for i in range(N):
    if dp_one[i] + dp_two[N - i - 1] - 1 > result: 
        result = dp_one[i] + dp_two[N - i - 1] - 1 

print(result) 