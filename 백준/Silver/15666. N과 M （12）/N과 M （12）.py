'''
1. 아이디어
- 중복 가능, 비내림차순

2. 시간복잡도
- N^N : N = 8 까지 가능
'''

import sys
input = sys.stdin.readline

# input 받기
# num_list를 set으로 만들어서 중복을 제거한 뒤 -> 리스트로 바꾼 후 -> 오름차순 정렬해줌
N, M = map(int, input().split())
num_list = sorted(list(set(map(int, input().split()))))
# 결과를 저장할 빈 리스트 정의
result = []


def recursion(depth):
    # M개를 다 뽑았다면 print 
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    # set으로 만들었으니까 길이가 N 개가 아님 -> len(num_list) 이용 
    for i in range(len(num_list)):
        # 오름차순인 경우에만 담을 수 있기 때문에 조건 설정해줌 (prunning) 
        if depth == 0 or result[-1] <= num_list[i]:
            result.append(num_list[i])
            recursion(depth + 1)
            result.pop()


recursion(0)







