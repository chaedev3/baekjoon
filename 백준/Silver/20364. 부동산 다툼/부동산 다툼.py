import sys
# input 받기
# N : 땅 개수  Q: 오리 수
N, Q = map(int, sys.stdin.readline().split())
duck_wanted_list = [int(sys.stdin.readline()) for _ in range(Q)]

# 실제 오리들이 점유한 땅 -> set로 만들어줌
ground_list = set()

# duck_wanted_list를 반복문 돌면서 트리에서 부모로 계속 이동 -> 1이 되면 끝
# 이동하면서 그 이동한 곳이 이미 점유된 땅이면 result를 계속 update 함 (제일 위 값이 출력되야 하기 때문) 
# 점유되지 않은 땅이면 0을 출력하도록 함 
for idx in range(Q):
    result = 0
    ground = duck_wanted_list[idx]
    while ground > 1:
        if ground in ground_list:
            result = ground
        ground = ground // 2
    ground_list.add(duck_wanted_list[idx])

    print(result)

