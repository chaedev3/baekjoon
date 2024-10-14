import sys
input = sys.stdin.readline

N = int(input())
change_list = [500, 100, 50, 10, 5, 1]

change_num = 1000 - N

count = 0 
for change in change_list:
    count += change_num // change
    change_num = change_num % change

print(count)

