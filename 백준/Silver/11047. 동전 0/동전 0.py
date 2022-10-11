# input 받기, list를 내림차순으로 정렬 
N, K = map(int, input().split())
coin_type_list = sorted([int(input()) for _ in range(N)], reverse=True)

# 동전의 개수를 셀 coin_cnt, 큰 동전부터 검사를 해봐야하니까 idx는 0부터 시작   
coin_cnt = 0
idx = 0
# 그리디 알고리즘 -> K 가 0이 되면 종료 
while K != 0:
    coin_cnt += (K // coin_type_list[idx]) 
    K -= (K // coin_type_list[idx]) * coin_type_list[idx]
    idx += 1

print(coin_cnt)
