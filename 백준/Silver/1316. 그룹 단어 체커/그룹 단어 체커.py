N = int(input())
total = 0
for i in range(N):
    word = list(map(str, input()))
    result = []
    cnt = 0
    for idx in range(1, len(word)):
        result.append(word[0])
        if word[idx] not in result:
            result.append(word[idx])
        elif word[idx] in result:
            if word[idx] == word[idx - 1]:
                pass
            else:
                cnt += 1
    if cnt == 0:
        total += 1
print(total)