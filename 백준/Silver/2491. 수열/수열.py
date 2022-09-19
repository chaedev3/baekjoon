N = int(input())
num_list = list(map(int, input().split()))
result = 1
increasing_v = 1
decreasing_v = 1
for i in range(N-1):
    if num_list[i] <= num_list[i+1]:
        increasing_v += 1
        if result < increasing_v:
            result = increasing_v
        else:
            result
    else:
        increasing_v = 1

for i in range(N-1):
    if num_list[i] >= num_list[i+1]:
        decreasing_v += 1
        if result < decreasing_v:
            result = decreasing_v
        else:
            result
    else:
        decreasing_v = 1

print(result)
