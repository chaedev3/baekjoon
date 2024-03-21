import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
score_list = [list(map(int, input().split())) for _ in range(N)]

result = 0 
# case1 일자로 이어진 애
for i in range(N):
    for j in range(M):
        if j + 3 < M:
            answer = sum(score_list[i][j:j+4])
            if answer > result:
                result = answer
        else:
            break

for j in range(M):
    for i in range(N):
        if i + 3 < N:
            answer = score_list[i][j] + score_list[i + 1][j] + score_list[i + 2][j] + score_list[i + 3][j]
            if answer > result:
                result = answer 
        else:
            break 


# case 2 네모
for i in range(N):
    for j in range(M):
        if j + 1 < M and i + 1 < N:
            answer = score_list[i][j] + score_list[i][j + 1] + score_list[i + 1][j] + score_list[i + 1][j + 1]
            if answer > result:
                result = answer 
        else:
            break 

# case 3 /4/ 5 
for i in range(N):
    for j in range(M):
        if j + 2 < M and i + 1 < N:
            # case 3 
            answer = score_list[i][j] + score_list[i][j + 1] + score_list[i][j + 2] + score_list[i + 1][j + 1]
            # case 4 
            answer_two = score_list[i][j] + score_list[i][j + 1] + score_list[i][j + 2] + score_list[i + 1][j]
            answer_three =  score_list[i][j] + score_list[i][j + 1] + score_list[i][j + 2] + score_list[i + 1][j + 2]
            # case 5
            answer_four = score_list[i][j + 1] + score_list[i][j + 2] + score_list[i + 1][j] + score_list[i + 1][j + 1]
            answer_five = score_list[i][j] + score_list[i][j + 1] + score_list[i + 1][j + 1] + score_list[i + 1][j + 2] 
            if max(answer, answer_two, answer_three, answer_four, answer_five) > result:
                result = max(answer, answer_two, answer_three, answer_four, answer_five)
        if j + 2 < M and i - 1 >= 0:
            answer = score_list[i][j] + score_list[i][j + 1] + score_list[i][j + 2] + score_list[i - 1][j + 1]
            answer_two = score_list[i][j] + score_list[i][j + 1] + score_list[i][j + 2] + score_list[i - 1][j]
            answer_three = score_list[i][j] + score_list[i][j + 1] + score_list[i][j + 2] + score_list[i - 1][j + 2]
            if max(answer, answer_two, answer_three) > result:
                result = max(answer, answer_two, answer_three)

for j in range(M):
    for i in range(N):
        if i + 2 < N and j + 1 < M:
            # case 3 
            answer = score_list[i][j] + score_list[i + 1][j] + score_list[i + 2][j] + score_list[i + 1][j + 1]
            # case 4 
            answer_two = score_list[i][j] + score_list[i + 1][j] + score_list[i + 2][j] + score_list[i][j + 1] 
            answer_three = score_list[i][j] + score_list[i + 1][j] + score_list[i + 2][j] + score_list[i + 2][j + 1] 
            # case 5
            answer_four = score_list[i + 1][j] + score_list[i + 2][j] + score_list[i][j + 1] + score_list[i + 1][j + 1] 
            answer_five = score_list[i][j] + score_list[i + 1][j] + score_list[i + 1][j + 1] + score_list[i + 2][j + 1] 
            if max(answer, answer_two, answer_three, answer_four, answer_five) > result:
                result = max(answer, answer_two, answer_three, answer_four, answer_five)
        if i + 2 < N and j - 1 >= 0:
            answer = score_list[i][j] + score_list[i + 1][j] + score_list[i + 2][j] + score_list[i + 1][j - 1]
            answer_two = score_list[i][j] + score_list[i + 1][j] + score_list[i + 2][j] + score_list[i][j - 1] 
            answer_three = score_list[i][j] + score_list[i + 1][j] + score_list[i + 2][j] + score_list[i + 2][j - 1]
            if max(answer, answer_two, answer_three) > result:
                result = max(answer, answer_two, answer_three)

print(result) 