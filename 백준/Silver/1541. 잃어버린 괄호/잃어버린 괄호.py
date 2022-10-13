# + 먼저 해주면 됨!

sentence_list = input().split('-')
total_list = []
for sentence in sentence_list:
    number = sentence.split('+')
    total = 0
    for num in number:
        total += int(num)
    total_list.append(total)

first_value = total_list.pop(0)

result = 0
if not total_list:
    result = first_value
else:
    for i in range(len(total_list)):
        result = first_value - total_list[i]
        first_value = result
print(result)












