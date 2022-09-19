N = 10
num_list = []
for idx in range(N):
    num_list.append(input())
result = []
for i in range(N):
    result.append(int(num_list[i]) % 42)

print(len(set(result)))