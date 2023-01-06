import sys 
input = sys.stdin.readline 

# strip 해줘야 됨 
A = input().strip()
B = input().strip() 

# LCS 정의, index를 1로 시작하기 위해 행열에 margin을 넣어줌 
LCS = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
result = [] 

for i in range(0, len(A)): 
    for j in range(0, len(B)):
        # 같으면 LCS[i][j] = LCS[i-1][j-1] + 1 
        if A[i] == B[j]:
            LCS[i + 1][j + 1] = LCS[i][j] + 1
        # 다르면 LCS[i-1][j] 와 LCS[i][j-1] 중에 큰 값을 표시함 
        else:
            LCS[i + 1][j + 1] = max(LCS[i][j + 1], LCS[i + 1][j]) 
      

  

result = [] 

a = len(A)
b = len(B)

while a > 0 and b > 0:
    if LCS[a][b] == LCS[a - 1][b]: 
        a = a - 1 
        
    elif LCS[a][b] == LCS[a][b - 1]: 
        b = b - 1 
    else: 
        a = a - 1 
        b = b - 1
        result.append(A[a]) 
print(LCS[-1][-1])  
print(''.join(result[::-1]))  