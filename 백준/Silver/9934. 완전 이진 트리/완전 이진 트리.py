from collections import deque

# 중위 순회 정의 
def inorder(n):
    global order_list
    if n > 0:
        inorder(ch1[n])
        order_list.append(n)
        inorder(ch2[n])


# 2의 x 제곱 정의 
def Power(a, x):
    if x == 0:
        return 1
    if x == 1:
        return a
    if x == 2:
        return a * a

    if x % 2 == 0:
        k = Power(a, x // 2)
        return k * k
    else:
        k = Power(a, (x - 1) // 2)
        return a * k * k

# input 받기 
K = int(input())
building_list = list(map(int, input().split()))

# 내가 완전 이진 트리 만들어줌 
a = len(building_list)
ch1 = [0] * (a + 1)
ch2 = [0] * (a + 1)

for i in range(2, a + 1):
    if i % 2 == 0:
        ch1[i // 2] = i
    else:
        ch2[i // 2] = i
# order_list에 내가 만든 이진 트리의 중위순회 순서 담아줌 
order_list = []
inorder(1)

# 두 개 합침 !! 
zip_list = list(zip(order_list, building_list))
# order_list를 기준으로 sort 해줌 
sorted_list = sorted(zip_list)
# popleft 하기 위해 deque로 .. 
q = deque(sorted_list)

# 몇 개씩 끊어서 출력할 건지 num_list에 담음 
num_list = []
for idx in range(K):
    num_list.append(Power(2, idx))

# 순서대로 popleft 해줌 
for num in num_list:
    for _ in range(num):
        print(q.popleft()[1], end=' ')
    print()