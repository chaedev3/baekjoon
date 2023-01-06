import sys 
input = sys.stdin.readline 

A = input().strip()
B = input().strip() 

# LCS 정의, index를 1로 시작하기 위해 행열에 margin을 넣어줌 
LCS = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(0, len(A)): 
    for j in range(0, len(B)): 
        if A[i] == B[j]:
            LCS[i + 1][j + 1] = LCS[i][j] + 1
        else:
            LCS[i + 1][j + 1] = max(LCS[i][j + 1], LCS[i + 1][j]) 
      

print(LCS[-1][-1])    