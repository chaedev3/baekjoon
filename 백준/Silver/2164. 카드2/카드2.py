from collections import deque

N = int(input())
card_list = list(range(1, N+1))
q = deque()
for card in card_list:
    q.append(card)

while len(q) > 1:
    q.popleft()
    q.rotate(-1)

print(q.popleft())