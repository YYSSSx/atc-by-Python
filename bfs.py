from collections import deque
h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
S = [input() for _ in range(h)]

d = [[100010]*w for _ in range(h)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1] 

def bfs(y, x):
    que = deque([[y, x]])
    d[y][x] = 0
    while que:
        yy, xx = que.popleft()

        if yy==gy-1 and xx==gx-1: break

        for i in range(4):
            ny, nx = yy + dy[i], xx + dx[i]

            if not (0<=ny<h and 0<=nx<w and S[ny][nx]!='#'): continue
            if d[ny][nx]==100010 and S[ny][nx]=='.':
                que.append([ny, nx])
                d[ny][nx] = d[yy][xx] + 1
            

    return d[gy-1][gx-1]

res = bfs(sy-1, sx-1)
print(res)