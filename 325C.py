import sys

sys.setrecursionlimit(10 ** 7)



h, w = map(int, input().split())

S = [input() for _ in range(h)]

ans = 0
visited = [[0]*w for _ in range(h)]

def dfs(row, col):
    
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (h>row+i>=0 and w>col+j>=0):
                continue
            if visited[row+i][col+j]==0 and S[row+i][col+j]=='#':
                visited[row][col] = 1
                dfs(row+i, col+j)
                

for k in range(h):
    for l in range(w):
        if S[k][l]=='#' and visited[k][l]==0:
            visited[k][l] = 1
            dfs(k, l)
            ans += 1

print(ans)