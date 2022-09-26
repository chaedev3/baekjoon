from sys import stdin

# 테스트 케이스의 수
T = int(stdin.readline())
for _ in range(T):
    # input 받기
    N, M = map(int, stdin.readline().split())
    flight_list = [list(map(int, stdin.readline().split())) for _ in range(M)]
    # 간선의 수 = 노드의 수 - 1
    print(N - 1)