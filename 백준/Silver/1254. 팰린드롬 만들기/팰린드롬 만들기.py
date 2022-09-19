def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

words = input()
i_list = []
for i in range(len(words)):
    if is_palindrome(words[i:]):
        i_list.append(i)
result = 0
result = len(words) + i_list[0]
print(result)