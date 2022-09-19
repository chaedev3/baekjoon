arr = list(map(int, input().split()))
idx_list = [0] * (len(arr) - 1)

for idx in range(len(arr)-1):
    if arr[idx] < arr[idx+1]:
        idx_list[idx] = 1
    elif arr[idx] > arr[idx+1]:
        idx_list[idx] = -1
    else:
        pass
result = 'mixed'
if idx_list == [1] * (len(arr) - 1):
    result = 'ascending'
elif idx_list == [-1] * (len(arr) - 1):
    result = 'descending'

print(result)