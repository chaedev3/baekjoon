import sys 
input = sys.stdin.readline 

T = int(input())

for _ in range(T):
    N = int(input())
    mbti_list = list(map(str, input().split()))
    answer = 100 

    if N > 32:
        print(0)
    else: 
        distance_list = [[0] * N for _ in range(N)]
        pair_list = [] 
        for i in range(N):
            for j in range(i + 1, N):
                pair_list.append((i, j)) 
                result = 0 
                mbti_one = mbti_list[i]
                mbti_two = mbti_list[j] 
                if mbti_one[0] != mbti_two[0]:
                    result += 1
                if mbti_one[1] != mbti_two[1]:
                    result += 1 
                if mbti_one[2] != mbti_two[2]:
                    result += 1
                if mbti_one[3] != mbti_two[3]:
                    result += 1 
                distance_list[i][j] = result 


        for x, y in pair_list:
            for z in range(N):
                sum_distance = 0 
                if z != x and z != y:
                    a_list = [x, y, z]
                    sorted_list = sorted(a_list)
                    a, b, c = sorted_list
                    sum_distance = distance_list[a][b] + distance_list[b][c] + distance_list[a][c]
                    if sum_distance < answer: 
                        answer = sum_distance
                        if answer == 0:
                            break 
                    
        print(answer)