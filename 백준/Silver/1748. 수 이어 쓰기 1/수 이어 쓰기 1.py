import sys
input = sys.stdin.readline 

# 합을 담은 리스트 만들기
add_list = [0] 
for i in range(1, 10):
    if i == 1: 
        add_list.append(i * 9)
      
    else:
        num = add_list[i - 1] + (9 * 10 ** (i - 1)) * i 
        add_list.append(num) 

# N 
N = int(input()) 


num_len = len(str(N)) - 1
result = add_list[num_len]  
result += (N - 10 ** num_len + 1) * (num_len + 1) 

print(result) 