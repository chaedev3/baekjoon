import sys 
input = sys.stdin.readline 

K, N = map(int, input().split())

lan = [int(input()) for _ in range(K)] 
 
start = 1 
end = max(lan)

while start <= end: 
    middle = (start + end) // 2
    result = 0 
    for l in lan:
        result += (l // middle) 
    
    if result >= N:
        start = middle + 1
        answer = middle   
    
    else: 
        end = middle - 1 
    
print(answer) 

