N = int(input())
# 기둥들의 위치와 높이가 저장된 리스트
pillar_list = [list(map(int, input().split())) for _ in range(N)]
# sort 하면 x 좌표를 기준으로 정렬이 됨
pillar_list.sort()
# y 좌표의 최대값과 최대값의 index 구하기(maxV) # 10, 3
maxV, max_index = 0, 0
p = [pillar[1] for pillar in pillar_list]
for idx in range(len(p)):
    if maxV < p[idx]:
        maxV, max_index = p[idx], idx

# 높이(height)와 결과를 저장할 total
total = 0
height = 0
# 먼저 왼편 먼저
for i in range(max_index):
    if height < pillar_list[i][1]:
        height = pillar_list[i][1]
    total += (pillar_list[i+1][0] - pillar_list[i][0]) * height

# 오른쪽 끝 부터~
height = 0
for j in range(N-1, max_index, -1):
    if height < pillar_list[j][1]:
        height = pillar_list[j][1]
    total += (pillar_list[j][0] - pillar_list[j-1][0]) * height

total += maxV
print(total)