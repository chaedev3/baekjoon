import sys
input = sys.stdin.readline 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    answer = 1 
    stack = set([(x, y, words[x][y])])
    while stack:
        x, y, alp = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C and words[nx][ny] not in alp:
                stack.add((nx, ny, alp + words[nx][ny]))
                answer = max(answer, len(alp) + 1)
    return answer


R, C = map(int, input().split())
words = [list(map(str, input())) for _ in range(R)]
print(dfs(0, 0))