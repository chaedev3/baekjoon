import sys
input = sys.stdin.readline

# M : 수행해야 하는 연산의 수
M = int(input())
# 처음에는 비어있는 공집합 S
S = 0b0
all_S = 0b111111111111111111111
empty_S = 0b000000000000000000000

for _ in range(M):
    command = input().rstrip().split(" ")

    # add -> A | B
    if command[0] == 'add':
        S = S | (1 << int(command[-1]))

    # check (결과 출력)
    elif command[0] == 'check':
        if S & (1 << int(command[-1])):
            print(1)
        else:
            print(0)

    # remove -> A & ~B
    elif command[0] == 'remove':
        S = S & ~(1 << int(command[-1]))

    # toggle(있으면 삭제, 없으면 추가) -> A ^ B
    elif command[0] == 'toggle':
        S = S ^ (1 << int(command[-1]))

    elif command[0] == 'all':
        S = S | all_S

    elif command[0] == 'empty':
        S = S & empty_S



