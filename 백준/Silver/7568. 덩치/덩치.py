# input 받기 - 사람의 수 N / weight, height 를 받아 wh_list에 저장 
N = int(input())
wh_list = []
for _ in range(N):
    weight, height = map(int, input().split())
    wh_list.append((weight, height))

# 반복문을 돌면서 i 보다 weight, height 가 둘 다 큰 j의 개수를 받음 
# cnt + 1 은 등수가 됨 
for i in range(N):
    cnt = 0
    for j in range(N):
        if wh_list[i][0] < wh_list[j][0] and wh_list[i][1] < wh_list[j][1]:
            cnt += 1
    print(cnt + 1, end=' ')





