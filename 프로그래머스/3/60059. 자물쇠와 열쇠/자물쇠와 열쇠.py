def check(expand_lock):
    l = len(expand_lock) // 3
    for i in range(l, 2 * l):
        for j in range(l, 2 * l):
            if expand_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    expand_lock = [[0] * (3 * n) for _ in range(3 * n)]
    
    # 3배 크기로 늘려서 중앙에 lock 위치시킴
    for i in range(n):
        for j in range(n):
            expand_lock[i + n][j + n] = lock[i][j] 
    
    # key 90도씩 회전해감
    for r in range(4):
        key = list(map(list, zip(*key[::-1])))
        
        for i in range(n * 2):
            for j in range(n * 2):
                
                for x in range(m):
                    for y in range(m):
                        expand_lock[i + x][j + y] += key[x][y]
                        
                if check(expand_lock) == True:
                    return True
                
                for x in range(m):
                    for y in range(m):
                        expand_lock[i + x][j + y] -= key[x][y]
    return False