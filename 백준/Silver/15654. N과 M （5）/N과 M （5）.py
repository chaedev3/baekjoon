from itertools import permutations
# input 받기 
N, M = map(int, input().split())
number_list = list(map(int, input().split()))

# permutation으로 M개 뽑고 정렬하기  
result = sorted(list(permutations(number_list, M)))

# 하나씩 출력하기 
for r in result:
    print(*r)
