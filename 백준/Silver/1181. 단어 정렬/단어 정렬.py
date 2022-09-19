N = int(input())
words = []
for _ in range(N):
    words.append(input())
len_list = []
words = set(words)
words = list(words)
for word in words:
    len_list.append(len(word))


words_list = list(zip(len_list, words))
sorted_list = sorted(words_list, key=lambda x: (x[0], x[1]))
for char in sorted_list:
    print(char[1])
