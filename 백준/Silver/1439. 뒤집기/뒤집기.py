number = input()
split_list = number.split('1')
cnt = 0
for s in split_list:
    if '0' in s:
        cnt += 1
zero = cnt


split_list2 = number.split('0')
cnt2 = 0
for p in split_list2:
    if '1' in p:
        cnt2 += 1
one = cnt2

if one <= zero:
    print(one)
else:
    print(zero)