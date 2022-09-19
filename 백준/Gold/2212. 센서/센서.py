N = int(input())
# K는 집중국의 개수
K = int(input())
sensor_list = list(map(int, input().split()))
sensor_list.sort()

# 센서 리스트를 오름차순으로 정렬한 뒤에 gap_list에 센서들의 차를 더함
gap_list = []
for idx in range(0, N-1):
    gap_list.append(sensor_list[idx+1] - sensor_list[idx])
gap_list.sort()

# 여기서 만약 집중국의 개수가 2개라면 중간에 1번 나누는 것이고, 집중국의 개수가 5개라면 중간에 4번 나누는 것
# 즉, k-1 번을 나누기 때문에 gap_list를 오름차순 정렬해서 큰 순서대로 k-1개를 뺀 gap의 합을 구하면 된다
result = sum(gap_list[:N-K])
print(result)