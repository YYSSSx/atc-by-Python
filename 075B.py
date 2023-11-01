h, w = map(int, input().split())

s = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j]=='.':
            c = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k==0 and l==0: continue
                    elif i+k>=0 and j+l>=0 and i+k<h and j+l<w and s[i+k][j+l]=='#': c += 1

            s[i] = s[i][:j] + str(c) + s[i][j+1:w]

for i in range(h): 
    for j in range(w):
        print(s[i][j])
