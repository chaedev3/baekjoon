def pre_process(P):
    lps = [0] * len(P)
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = lps[j-1]
        if P[i] == P[j]:
            j += 1
            lps[i] = j
    return lps

# L: 광고의 크기
L = int(input())
# word: 광고판에 보이는 문자열
words = input()
print(L - pre_process(words)[-1])
