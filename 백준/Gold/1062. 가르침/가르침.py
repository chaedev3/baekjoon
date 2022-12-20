from itertools import combinations
import sys
input = sys.stdin.readline

# N : 단어의 개수, K : 가르치는 글자의 수
N, K = map(int, input().split())

# 'anti','tica' 는 필수로 알아야 하기 때문에 배워야하는 필수 문자들 정의
necessary_words = ['a', 'n', 't', 'i', 'c']
learned_words = [0] * N

# anta와 tica를 제외한 문자 뽑기
for i in range(N):
    words = list(input())[4:-5]
    for word in words:
        # 주어지는 알파벳은 모두 소문자기 때문에 이렇게 하게 되면 learned_words 에 들어있는 숫자들을 2진수로 바꾸게 되면
        # 알파벳 순서대로 포함된 숫자는 1, 포함되지 않은 숫자는 1로 표시되게 된다. (아직은 a , n , t, i, a 도 섞여진 상태)
        learned_words[i] |= (1 << (ord(word) - ord('a')))

# 이진수에서 combination을 사용하지 못하는 것 같아 a, n, t, i, c를 뺀 알파벳을 정의 해줌

result = 0
# K가 5보다 작다면 필수 단어(anta, tica)를 배우지도 못한다는 뜻이므로 배울 수 있는 단어는 없다.
if K < 5:
    pass
else:
    alphabet = 'bdefghjklmopqrsuvwxyz'
    combs = list(combinations(list(alphabet), K - 5))
    for comb in combs:
        # combination으로 나온 결과들을 이진수로 합쳐줌
        subset = 0
        for c in comb:
            subset |= 1 << (ord(c) - ord('a'))
        for n in necessary_words:
            subset |= 1 << (ord(n) - ord('a'))

        cnt = 0
        for word in learned_words:
            if word == word & subset:
                cnt += 1
        result = max(cnt, result)

print(result)














