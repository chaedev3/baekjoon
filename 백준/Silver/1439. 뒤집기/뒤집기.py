import sys
input = sys.stdin.readline 

str_list = str(input().strip())

str1 = str_list.split('0')
str2 = str_list.split('1')

count1 = 0 
for s in str1:
    if s != '':
        count1 += 1 

count2 = 0
for s in str2:
    if s != '':
        count2 += 1

print(min(count1, count2)) 