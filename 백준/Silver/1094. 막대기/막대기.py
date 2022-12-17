import sys
input = sys.stdin.readline

# 처음에는 64cm 막대 하나 O
# 1. X 보다 막대 길이의 합이 크다면 가지고 있는 막대 중 가장 짧은 것을 절반으로 자름
# 2. 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같으면, 위에서 자른 막대의 절반 중
# 하나를 버림 / 그게 아니라면 버리지 말기
# 3. 남아 있는 모든 막대를 풀로 붙여서 Xcm 를 만든다.

# 64 의 경우 0b1000000
# 32 의 경우 0b100000
# 23 의 경우 0b10111
# 48 의 경우 0b110000

print(bin(int(input())).count('1'))


