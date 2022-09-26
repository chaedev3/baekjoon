def is_not_diagonal(picked, i):
    for idx, num in enumerate(picked):
				# 기울기가 1 or -1 이면 같은 대각선에 있는 것임 
				# i 의 index는 len(picked) 와 같음! 
        if (num - i) == (idx - len(picked)) or (num - i) == -(idx - len(picked)):
            return False
    return True

# 순서가 있는 비복원 추출(permutation)을 이용함
# n은 범위, picked는 뽑은 걸 담는 리스트, to_pick은 추출할 개수임 
def pick(n, picked, to_pick):
    global cnt
    if to_pick == 0:
        cnt += 1
        return

    for i in range(1, n + 1):
				# 지금까지 안뽑혔고 같은 대각선 상에 없다면 추가해!! 
        if i not in picked:
            if is_not_diagonal(picked, i):
                picked.append(i)
                pick(n, picked, to_pick - 1)
								# 뽑을게 없으면 마지막 꺼 pop 하고 다시 진행하렴 .. 
                picked.pop()

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    cnt = 0
    pick(N, [], N)
    print(f'#{tc} {cnt}')