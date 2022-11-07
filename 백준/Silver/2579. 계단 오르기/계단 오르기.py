import sys
input = sys.stdin.readline

stairs_num = int(input())
stairs = [0] * 302
for idx in range(1, stairs_num + 1):
    stairs[idx] = int(input())

dp = [0] * 302
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[2] + stairs[3], stairs[1] + stairs[3])
for i in range(4, stairs_num + 2):
    dp[i] = max(stairs[i] + stairs[i - 1] + dp[i - 3], stairs[i] + dp[i - 2])

print(dp[stairs_num])

