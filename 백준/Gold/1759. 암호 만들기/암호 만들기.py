from itertools import combinations
L, C = map(int, input().split())
# 알파벳 순으로 정렬하기
words = list(map(str, input().split()))
vowels = ['a', 'e', 'i', 'o', 'u']

word = list(combinations(words, L))
real_word = []
for w in word:
    cnt = 0
    for idx in range(L):
        if w[idx] in vowels:
            cnt += 1
    if 1 <= cnt <= (L - 2):
        real_word.append(sorted(w))

for ww in sorted(real_word):
    print(''.join(ww))


