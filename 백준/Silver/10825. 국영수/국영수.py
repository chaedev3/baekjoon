import sys
input = sys.stdin.readline

# 학생 수 n 
n = int(input())

arr = []
for _ in range(n):
    name, kor, eng, math = map(str, input().split())
    arr.append([name, int(kor), int(eng), int(math)])

# 이거는 말이죵 ~ 
# lambda로 풀면 됩니다앙~~
sorted_list = sorted(arr, key=lambda person: (-person[1], person[2], -person[3], person[0]))

for i in range(n):
    print(sorted_list[i][0])