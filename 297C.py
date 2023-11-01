h, w = map(int, input().split())

s = [input() for _ in range(h)]

for i in range(h):
    for j in range(w-1):
        if s[i][j]=='T' and s[i][j+1]=='T':
            s[i]= s[i][:j] + 'PC' + s[i][j+2:]

for k in range(h):
    print(s[k])