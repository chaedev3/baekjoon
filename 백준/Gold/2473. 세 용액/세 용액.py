import sys
input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))

minV = sys.maxsize 
sorted_list = []
# 하나씩 돌면서
for i in range(N - 2):
    # 첫 번째 값은 뽑아줌
    firstV = arr[i]
    # 왼쪽 포인터는 arr[i + 1] 으로 해주고 오른쪽은 맨 끝값인 arr[N - 1]로 잡아줌
    a = i + 1
    b = N - 1
    while a < b:
        all_sum = firstV + arr[a] + arr[b]
        if abs(all_sum) <= minV:
            minV = abs(all_sum)
            sorted_list = [firstV, arr[a], arr[b]]
        if all_sum < 0:
            a += 1
        elif all_sum > 0:
            b -= 1
        else:
            break

print(*sorted_list)

