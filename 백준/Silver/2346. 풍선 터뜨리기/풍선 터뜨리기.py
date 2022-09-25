from collections import deque

N = int(input())
balloon = list(map(int, input().split()))

bal_list = []
for idx, bal in enumerate(balloon, start=1):
    bal_list.append([idx, bal])
q = deque(bal_list)

a_list = []
while q:
    a_list.append(q[0])
    q.popleft()
    if a_list[-1][1] >= 0:
        q.rotate(-a_list[-1][1] + 1)
    else:
        q.rotate(-a_list[-1][1])

for i in range(len(a_list)):
    print(a_list[i][0], end=' ')

