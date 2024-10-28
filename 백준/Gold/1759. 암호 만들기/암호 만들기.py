import sys, itertools
input = sys.stdin.readline
l, c = map(int, input().split())
alphabet_list = list(map(str, input().split()))
a_list = ['a', 'e', 'i', 'o', 'u'] 

result = [] 
for x in itertools.combinations(alphabet_list, l):
    a_cnt = 0 
    for a in a_list:
        if a in list(x):
            a_cnt += 1

    if 1 <= a_cnt <= l - 2: 
        result.append(''.join(sorted(list(x))))

result.sort()

for r in result:
    print(r) 