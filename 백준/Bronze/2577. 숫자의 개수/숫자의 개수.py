def counting_sort(arr):
    result = [0] * 10
    for idx in range(len(arr)):
        result[arr[idx]] += 1
    return result


A = int(input())
B = int(input())
C = int(input())
a = str(A * B * C)
abc = list(map(int, a))
count_arr = counting_sort(abc)
for j in range(len(count_arr)):
    print(count_arr[j])