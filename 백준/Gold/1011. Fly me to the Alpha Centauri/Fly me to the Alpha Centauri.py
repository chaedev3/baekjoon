import sys, math 
input = sys.stdin.readline 

T = int(input())
for _ in range(T):
    x, y = map(int, input().split()) 
    gap = y - x 
    root = math.trunc(math.sqrt(gap))
    addTwo = (root ** 2 + (root + 1) ** 2) / 2      
    if gap == root ** 2:
        print(root * 2 - 1) 
    elif gap < addTwo:
        print(root * 2) 
    elif gap > addTwo:
        print(root * 2 + 1) 
