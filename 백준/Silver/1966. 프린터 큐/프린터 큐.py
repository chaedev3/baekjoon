from collections import deque 
import sys
input = sys.stdin.readline 

T = int(input()) 
for _ in range(T):
    N, M = map(int, input().split()) 
    priority_list = list(map(int, input().split())) 
    q = deque(priority_list)    
    index_list = deque([i for i in range(N)])
   
    result = 1  
 
    while q:  
        priority = q.popleft() 
        index = index_list.popleft() 
        
        if q and priority < max(q):
            q.append(priority) 
            index_list.append(index)

            
        else:
            if index == M:
                print(result) 
                break 
            else: 
                result += 1 
